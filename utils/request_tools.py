# -*- coding: utf-8 -*-
"""
    @Time : 2023/2/24/024 13:38
    @Author : 李子
    @Url : https://github.com/kslz
"""

import requests

def get_biaobei_token(client_id,client_secret):
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
