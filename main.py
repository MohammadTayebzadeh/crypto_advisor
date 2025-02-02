import streamlit as st
from urllib.parse import urljoin
from crypto import crypto
from eco import eco
import os


st.title("📈ربات توصیه گر سرمایه گذاری در کریپتو")


symbol = st.text_input('Enter Symbol like BTCUSD, ETHUSD, XRPUSD').upper().strip()
but = st.button('بررسی')

check_crypto_news = st.checkbox('بررسی اخبار فاندامنتال هر ارز')
check_eco_news = st.checkbox('بررسی اخبار اقتصاد کلان')

# اجرای ماژول‌ها
if __name__ == "__main__":

    if symbol != '' and but and check_crypto_news:
        crypto(symbol)

    if check_eco_news:
        eco()
