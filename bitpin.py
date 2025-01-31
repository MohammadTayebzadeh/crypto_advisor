import requests
import streamlit as st
from bs4 import BeautifulSoup
from ai import ai


def bitpin():

    # درخواست به صفحه اصلی اخبار
    response = requests.get('https://bitpin.ir/academy/analysis/')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # یافتن تمام لینک‌های خبری
        news_links = soup.find_all('a', class_='title')

        if news_links:
            for link in news_links:
                # استخراج عنوان و لینک هر خبر
                news_title = link.text.strip()
                news_url = link['href']

                # درخواست به صفحه خبر
                news_response = requests.get(news_url)
                if news_response.status_code == 200:
                    news_soup = BeautifulSoup(
                        news_response.text, 'html.parser')

                    # یافتن محتوای خبر
                    news_content = news_soup.find_all('p')
                    if news_content:
                        news_text = ' '.join(
                            [content.get_text().strip() for content in news_content])
                    else:
                        news_text = "محتوای خبر یافت نشد."

                    # ایجاد پرامپت برای AI
                    prompt = f"""
                    لطفاً تحلیل‌های زیر را بررسی کرده و نکات کلیدی آن‌ها را استخراج کنید. در هنگام ارائه نتیجه، تمام متن‌ها و جدول‌ها باید با جهت 

                    برای هر تحلیل، موارد زیر را انجام دهید:

                    1. **استخراج نکات کلیدی:**  
                    نکات و اطلاعات مهم تحلیل را به‌صورت مختصر و دقیق بیان کنید.

                    2. **تأثیرات بر بازار و روندهای اقتصادی:**  
                    توضیح دهید که تحلیل چه تأثیری بر بازارهای مختلف و روندهای اقتصادی دارد.

                    3. **تأثیر خبر بر نرخ بهره آمریکا:**  
                    مشخص کنید که خبر چه تأثیری بر نرخ بهره آمریکا دارد. اگر تاثیری ندارد، بنویسید "تأثیری ندارد".

                    4. **نتیجه‌گیری:**  
                    یک نتیجه‌گیری کلی و جامع از تحلیل‌ها ارائه دهید.

                    در پایان، **لینک خبر** را به‌طور جداگانه ذکر کنید.

                    اطلاعات تحلیل‌ها:  
                    **عنوان:** {news_title}  
                    **متن تحلیل:** {news_text}  
                    **لینک:** {news_url}
                    """


                    # ارسال پرامپت به مدل AI (در صورتی که تابع ai() برای شما در نظر گرفته شده باشد)
                    ai(prompt)

        else:
            print("هیچ لینکی پیدا نشد.")
    else:
        print(f"Failed to fetch the main page. Status code: {
            response.status_code}")
