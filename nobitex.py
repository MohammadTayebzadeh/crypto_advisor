import requests
from bs4 import BeautifulSoup
from ai import ai


def nobitex():

    response = requests.get('https://nobitex.ir/mag/category/news/')

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        news_links = soup.find_all('li', class_='news-item')

        for link in news_links:

            news_title = link.find('a').text.strip()
            news_url = link.find('a')['href']

            news_response = requests.get(news_url)

            if news_response.status_code == 200:
                news_soup = BeautifulSoup(news_response.text, 'html.parser')
                news_content = news_soup.find_all('p')

                if news_content:
                    news_text = ' '.join([content.get_text().strip()for content in news_content])
                else:
                    news_text = "محتوای خبر یافت نشد"

            prompt = f"""
            لطفاً خبرهای زیر را تحلیل کن و اطلاعات خواسته‌شده را ارائه بده:

            1. عنوان هر خبر را بخوان.
            2. وارد لینک هر خبر شو و متن کامل آن را تحلیل کن.
            3. برای هر خبر موارد زیر را در جدول یادداشت کن:
                - خلاصه‌ای از تحلیل خبر.
                - تأثیر هر خبر.
           

            در نهایت، نتیجه را در قالب یک جدول با فرمت زیر نمایش بده:
            - تیتر خبر
            - خلاصه تحلیل خبر
            - تأثیر هر خبر

            خبرها:
            {news_title}

            {news_text}
            """

            ai(prompt)
