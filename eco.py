import json
import requests
from bs4 import BeautifulSoup
from ai import ai


def eco():
    response = requests.get('https://www.tradingview.com/news/#top_stories')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # پیدا کردن تمام اخبار
        stories = soup.find('div', class_='grid-iTt_Zp4a')

        # لیستی برای ذخیره خبرها
        news_list = []

        for story in stories:
            # استخراج عنوان خبر
            title = story.find('div', class_='title-DmjQR0Aa')
            # استخراج اطلاعات اضافی (مثل توضیحات یا هدر)
            header = story.find('div', class_='header-DmjQR0Aa')

            if title:
                # ساختاردهی خبر
                news_item = {
                    "title": title.get_text(strip=True),
                    "header": header.get_text(strip=True) if header else None
                }
                news_list.append(news_item)

        if news_list:
            # آماده‌سازی برای ارسال به هوش مصنوعی
            prompt = f"""
            لطفاً خبرها را تحلیل کن و اطلاعات زیر را به من ارائه بده:

            1. هر خبر را تحلیل کن و مشخص کن که مثبت است یا منفی.
            2. اگر خبری در مورد آمریکا بود، تأثیر هر خبر را روی نرخ بهره بررسی کن و در جدول یادداشت کن.
            3. پس از تحلیل همه خبرها، یک بازه عددی از 0 تا 100 به من بده:
            - عدد 0 یعنی وضعیت اقتصادی به هیچ وجه برای ورود به بازار مناسب نیست.
            - عدد 100 یعنی بهترین فرصت برای ورود به بازار است.

            توجه کنید که جدول و تمام متن‌های ارائه‌شده باید با جهت نوشتار **راست به چپ (RTL)** نمایش داده شوند.

            در نهایت:
            - تمامی اطلاعات را **بصورت یک جدول نمایش بده** که شامل ستون‌های زیر باشد:
            - خبر انگلیسی
            - خبر ترجمه‌شده به فارسی
            - تأثیر خبر روی نرخ بهره
            - مثبت یا منفی بودن خبر

            خبرها:
            {json.dumps(news_list, ensure_ascii=False, indent=2)}
            """
            # ارسال داده به تابع هوش مصنوعی
            ai(prompt)

        else:
            print("هیچ خبری پیدا نشد.")
    else:
        print(f"خطای سرور: کد وضعیت {response.status_code}")
