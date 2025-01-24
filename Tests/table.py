import requests
from bs4 import BeautifulSoup


def table():
    url = "https://www.varzesh3.com/football/league/6/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86"

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'your_cookie_here',
        'referer': 'https://www.varzesh3.com/football/league/6/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # به عنوان مثال، استخراج عنوان صفحه
        title = soup.find('title').text
        print(f"عنوان صفحه: {title}")
        # استخراج تگ متا توضیحات
        description = soup.find('meta', attrs={'name': 'description'})
        if description:
            print(f"توضیحات: {description['content']}")
            print(response.status_code)
            print("تست با موفقیت پاشد")


    else:
        print(f"دریافت صفحه با شکست مواجه شد. کد وضعیت: {response.status_code}")

table()
