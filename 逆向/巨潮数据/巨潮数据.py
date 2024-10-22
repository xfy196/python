import requests
import execjs
import execjs



def getEncKey():
    # 读取 crypto-js.min.js 文件内容
    with open("crypto-js.min.js", "r", encoding="utf-8") as f:
        crypto_js = f.read()

    # 读取 script.js 文件内容
    with open("script.js", "r", encoding="utf-8") as f:
        script_js = f.read()

    crypto_js = (
        "var CryptoJS = (function(){var module={};"
        + crypto_js
        + "; return module.exports;})();"
    )
    # 合并两个脚本的内容
    combined_script = crypto_js + "\n" + script_js

    # 使用 execjs 执行合并后的脚本
    context = execjs.compile(combined_script)

    # 调用你想执行的函数或代码
    encKey = context.call("getResCode")
    return encKey

cookies = {
    "routeId": ".uc1",
    "Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b": "1729568671",
    "HMACCOUNT": "62C289311C24B817",
    "MALLSSID": "733664326845765A576559776E502F6C7058473147766C36305A37653652443939787253586E68434866764C5741326E31756F74504D462B6D4854796C2F507A",
    "Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b": "1729568742",
}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-EncKey": getEncKey(),
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    # 'Content-Length': '0',
    # 'Cookie': 'routeId=.uc1; Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1729568671; HMACCOUNT=62C289311C24B817; MALLSSID=733664326845765A576559776E502F6C7058473147766C36305A37653652443939787253586E68434866764C5741326E31756F74504D462B6D4854796C2F507A; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1729568742',
    "Origin": "https://webapi.cninfo.com.cn",
    "Referer": "https://webapi.cninfo.com.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}

params = {
    "market": "012001",
    "sdate": "20230217",
}

response = requests.post(
    "https://webapi.cninfo.com.cn/api/stock/p_stock2247",
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.json())
