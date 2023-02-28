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
        .run(capture_stdout=True)
    )

    base64_data = base64.b64encode(output[0]).decode("utf-8")

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
    print(response_json)
    print(response_json["err_no"])

    # response_json = response.content.decode("utf-8")
    # print(response_json)
