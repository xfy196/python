import requests
import execjs
import re
cookies = {
    'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1713970208',
    '.thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7': 'a987vqXgVqTaess3HF5e5YtoebJGXiVyku+y9mNaxoTTLAC1/78KNYLi54iPy8zvCzkwlqT77rx/7zyYjw5HZw%3D%3D',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lpvt_1db88642e346389874251b5a1eded6e3=1713970208; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=a987vqXgVqTaess3HF5e5YtoebJGXiVyku+y9mNaxoTTLAC1/78KNYLi54iPy8zvCzkwlqT77rx/7zyYjw5HZw%3D%3D',
    'Referer': 'https://xueqiu.com/today',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://xueqiu.com/today',
                        cookies=cookies, headers=headers)
# 用正则获取到返回的arg1的值 然后丢给js执行获取args2
content = response.text
arg1 = re.findall(r'arg1=\'(.*?)\'', content)[0]
with open('./index.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
    ctx = execjs.compile(js_code)
    arg2 = ctx.call('getAcwScV2', arg1)
    # cookies = {
    #     'acw_tc': '2760779617140602309807756edaa6d12e188d420ce327f619c9969b44516b',
    #     'acw_sc__v2': arg2,
    #     'xq_a_token': '5eeab96bfda3e05af7b6ef9e4626c2d12040b664',
    #     'xqat': '5eeab96bfda3e05af7b6ef9e4626c2d12040b664',
    #     'xq_r_token': '7548941cfe5a4311622757e10bf21aacf79c4843',
    #     'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxNjI1MjY4MCwiY3RtIjoxNzE0MDYwNjgzNDkyLCJjaWQiOiJkOWQwbjRBWnVwIn0.BWcKv4hXZgIc7iAYAHDNGa8sNsqcH4LjZc3-O36qfQ4n_es72sj5OU0eR-R02pB5El-8RQoBCC-bxjv1PkfwWQo23Zd-_YD0VRj7L4z6-ekskQcdw8iWqZCfDarqCFtPbQYX5VL3b3KwX6HtDQWn4RXZtGt8MYBbZ5wrv0-3C0hv1ePvSnxdguLwxOl-ho4-1N1Blp60O7gkIcMgcoWaIXZYmxee9ti3oRTcKwRC3EWkdhFUyIB-lAY14Wkg7pwN357Y-u4zOBRGL1S_XhEqOWlwulLB7eoRHpjioPFRe3L8j58kFV5V449LIBFOs5_08ayHnqMCv8J4P_udQ9w81g',
    #     'cookiesu': '251714060710231',
    #     'u': '251714060710231',
    #     'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1714060711',
    #     'smidV2': '2024042523583090b8c6461eab31669499d494b492989300894492b557dc7b0',
    #     'device_id': 'c200c199e8cd297859f7644d2df72dee',
    #     's': 'bu11p4vaey',
    #     'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1714060721',
    #     '.thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7': 'IO1o7nFA3foM2E71d+XcIfE6dQVBp2CiNlYs8ArVlkOG7qnP/oJpFuo4nOBt7jAEoRCA43Vwypquh4r/RcjH/Q%3D%3D',
    # }

    # headers = {
    #     'Host': 'xueqiu.com',
    #     'Cache-Control': 'max-age=0',
    #     'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'Sec-Fetch-Mode': 'navigate',
    #     'Sec-Fetch-User': '?1',
    #     'Sec-Fetch-Dest': 'document',
    #     'Referer': 'https://xueqiu.com/today',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # }

    # response = requests.get('https://xueqiu.com/today',
    #                         cookies=cookies, headers=headers)
    # print(response.text)
    # with open("./main.html", 'w', encoding='utf-8') as f:
    #     f.write(response.text)

    cookies = {
        'acw_tc': '2760779617140602309807756edaa6d12e188d420ce327f619c9969b44516b',
        'acw_sc__v2': arg2,
        'xq_a_token': '5eeab96bfda3e05af7b6ef9e4626c2d12040b664',
        'xqat': '5eeab96bfda3e05af7b6ef9e4626c2d12040b664',
        'xq_r_token': '7548941cfe5a4311622757e10bf21aacf79c4843',
        'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxNjI1MjY4MCwiY3RtIjoxNzE0MDYwNjgzNDkyLCJjaWQiOiJkOWQwbjRBWnVwIn0.BWcKv4hXZgIc7iAYAHDNGa8sNsqcH4LjZc3-O36qfQ4n_es72sj5OU0eR-R02pB5El-8RQoBCC-bxjv1PkfwWQo23Zd-_YD0VRj7L4z6-ekskQcdw8iWqZCfDarqCFtPbQYX5VL3b3KwX6HtDQWn4RXZtGt8MYBbZ5wrv0-3C0hv1ePvSnxdguLwxOl-ho4-1N1Blp60O7gkIcMgcoWaIXZYmxee9ti3oRTcKwRC3EWkdhFUyIB-lAY14Wkg7pwN357Y-u4zOBRGL1S_XhEqOWlwulLB7eoRHpjioPFRe3L8j58kFV5V449LIBFOs5_08ayHnqMCv8J4P_udQ9w81g',
        'cookiesu': '251714060710231',
        'u': '251714060710231',
        'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1714060711',
        'smidV2': '2024042523583090b8c6461eab31669499d494b492989300894492b557dc7b0',
        'device_id': 'c200c199e8cd297859f7644d2df72dee',
        's': 'bu11p4vaey',
        'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1714061438',
        '.thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7': 'ToGvdmCnrIpr4AHylSGrB8uT3ImOYybJL7ejAKweinqVNEQCtrQykyHA+zgEj1WYR3iWxCWRpWEvuQqGWiXOGw%3D%3D',
    }

    headers = {
        'Host': 'xueqiu.com',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'elastic-apm-traceparent': '00-053446e7b666ba1c7a795f8c8588965f-3970a69fadd83bc6-00',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://xueqiu.com/today',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = {
        'count': '10',
        'page': '1',
        'scope': 'day',
        'type': 'news',
    }

    response = requests.get('https://xueqiu.com/query/v1/status/hots.json',
                            params=params, cookies=cookies, headers=headers)
    print(response.json())
