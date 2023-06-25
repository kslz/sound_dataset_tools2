# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/24/024 13:38
    @Author : 李子
    @Url : https://github.com/kslz
"""
import json

import ffmpeg
import requests
import base64

from utils.log import requsetlogger


def get_biaobei_token(client_id, client_secret):
    url = 'https://openapi.data-baker.com/oauth/2.0/token'

    payload = {
        'grant_type': 'client_credentials',
        'client_secret': client_secret,
        'client_id': client_id
    }

    response = requests.post(url, data=payload)

    if response.ok:
        response_json = response.json()
        access_token = response_json.get('access_token')
        return access_token
    else:
        return False


def pingce_biaobei(file_path, text, access_token, start_time, end_time):
    """
    通过标贝接口进行音频评测，并将返回的json文件保存到本地，需自行填入鉴权信息
    注意：只支持采样率16k、位长16bit、单声道的pcm音频。
    标贝语音评测只支持3秒以上的音频，建议使用wav2pcm2()函数进行转换
    文档：https://www.data-baker.com/specs/file/eva_api_restful

    :param file_path: 音频文件路径
    :param text: 音频对应文本
    :param access_token: 鉴权信息（请参考文档获取）
    :parap start_time: 开始时间（毫秒）
    :parap end_time: 结束时间（毫秒）
    """

    duration = (end_time - start_time) / 1000
    start_time = start_time / 1000

    # 从长音频文件中提取指定时间段的音频
    output = (
        ffmpeg
        .input(file_path, ss=start_time, t=duration)
        .output('pipe:', format='s16le', acodec='pcm_s16le', ac=1, ar=16000)
        .run(capture_stdout=True, quiet=True)
    )
    output = output[0]

    if duration < 3.1:
        # 因为标贝要求音频不能短于3s 所以如果不足3.1s就会生成静音段将音频补到3.1s
        # 这段写了一个小时，我现在已经完全了解一切
        silence_duration = 3.1 - duration

        silence = (
            ffmpeg
            .input('anullsrc', f='lavfi', t=silence_duration)
            .output('pipe:', format='s16le', acodec='pcm_s16le', ac=1, ar=16000)
            .run(capture_stdout=True, quiet=True)
        )

        output = output + silence[0]

    base64_data = base64.b64encode(output).decode("utf-8")

    headers = {
        'Content-Type': 'application/json',
        'Host': 'openapi.data-baker.com'
    }

    json_data = {
        'access_token': access_token,
        'format': 'pcm',
        'txt': text,
        'lan': 'cn',
        'audio': base64_data,
    }

    response = requests.post('https://openapi.data-baker.com/cap/getCapScore', headers=headers, json=json_data)

    response_json = response.json()
    if response_json["err_no"] == 90000:
        return response_json
    requsetlogger.error(f"标贝评测请求失败，错误码: {response_json['err_no']} 错误信息： {response_json['err_msg']}")
    return False

    # response_json = response.content.decode("utf-8")
    # print(response_json)


def test_biaobei_pingce(access_token):
    text = "你好世界，"
    silence = (
        ffmpeg
        .input('anullsrc', f='lavfi', t=3.1)
        .output('pipe:', format='s16le', acodec='pcm_s16le', ac=1, ar=16000)
        .run(capture_stdout=True, quiet=True)
    )
    # with open("test.wav", "wb") as f:
    #     f.write(silence[0])
    base64_data = base64.b64encode(silence[0]).decode("utf-8")

    headers = {
        'Content-Type': 'application/json',
        'Host': 'openapi.data-baker.com'
    }

    json_data = {
        'access_token': access_token,
        'format': 'pcm',
        'txt': text,
        'lan': 'cn',
        'audio': base64_data,
    }

    response = requests.post('https://openapi.data-baker.com/cap/getCapScore', headers=headers, json=json_data)

    response_json = response.json()
    if response_json["err_no"] == 50001 or response_json["err_no"] == 50002:
        return False
    return True
