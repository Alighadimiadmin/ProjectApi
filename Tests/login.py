import requests

from Tests.Settings.File_Path_Excell import Excell_file_path


def login():
    # استفاده ازfunc اکسل و فراخوانی آن
    worksheet = Excell_file_path()

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'analytics_campaign={%22source%22:%22google%22%2C%22medium%22:%22organic%22}; .raft=CfDJ8G1n5SS8JqpNvWpZkn1Nt-7xepZLbfDBRags7yGn2Pa-9yFpPbUYXEN8I-jmL9B8goPmq1Tnx6Sr7l2kif2Bht3SLFo31dUUGFuwlCdCsq4TOPz7fn1DhDm2abLgxZjCVIpa7mlWKdAp8Lk6AZGMtDU',
        'priority': 'u=0, i',
        'referer': 'https://www.varzesh3.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Authorization': 'Bearer {{access_token}}'
    }

    response = requests.request("GET", worksheet.cell(row=4, column=1).value, headers=headers, data=payload)

    return response.status_code
