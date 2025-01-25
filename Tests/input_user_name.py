import requests
from Tests.Settings.File_Path_Excell import Excell_file_path


def input_user_name():
    # استفاده ازfunc اکسل و فراخوانی آن
    worksheet = Excell_file_path()
    payload = 'ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3D0D996589651C4235B7D40837E8C1DBC2F60410B2C9304298B568%26redirect_uri%3Dhttps%253A%252F%252Fwww.varzesh3.com%252Foidc%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520offline_access%2520videos.api%2520comments.api%2520profile.api%2520world-cup.prediction.api%2520engagement.api%2520notification.api%2520pishbini.api%26state%3Deb455dc7ec4b47f2a80ff1d4838d037a%26code_challenge%3DyR6G24eRAZ188PWV5POdgA48S6p6LJ2YJ-VwBYq67-g%26code_challenge_method%3DS256%26response_mode%3Dquery&PhoneNumber=09195099029&Username=989195099029&button=login&__RequestVerificationToken=CfDJ8G1n5SS8JqpNvWpZkn1Nt-7cuV2J5BaBxZKYLhTJITzRaXkMbc8FHguZ9PVSFLL2irSfqK3qW16ApaOCzu5ap83xrZx4WrytKYe6dJaXpnsvMhSNsXVb37mABwXrzgYer--CwyJGYSUWRVr11f7gUsA&Password=Gh%40123456'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; .raft=CfDJ8G1n5SS8JqpNvWpZkn1Nt-7xepZLbfDBRags7yGn2Pa-9yFpPbUYXEN8I-jmL9B8goPmq1Tnx6Sr7l2kif2Bht3SLFo31dUUGFuwlCdCsq4TOPz7fn1DhDm2abLgxZjCVIpa7mlWKdAp8Lk6AZGMtDU',
        'origin': 'https://sso.varzesh3.com',
        'priority': 'u=0, i',
        'referer': 'https://sso.varzesh3.com/account/login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3D0D996589651C4235B7D40837E8C1DBC2F60410B2C9304298B568%26redirect_uri%3Dhttps%253A%252F%252Fwww.varzesh3.com%252Foidc%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520offline_access%2520videos.api%2520comments.api%2520profile.api%2520world-cup.prediction.api%2520engagement.api%2520notification.api%2520pishbini.api%26state%3Deb455dc7ec4b47f2a80ff1d4838d037a%26code_challenge%3DyR6G24eRAZ188PWV5POdgA48S6p6LJ2YJ-VwBYq67-g%26code_challenge_method%3DS256%26response_mode%3Dquery',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Authorization': 'Bearer {{access_token}}'
    }

    response = requests.request("POST", worksheet.cell(row=2, column=1).value, headers=headers, data=payload)

    return response.status_code