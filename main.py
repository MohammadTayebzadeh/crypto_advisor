import streamlit as st
from urllib.parse import urljoin
from bitpin import bitpin
from crypto import crypto
from nobitex import nobitex
from eco import eco


st.title("ربات توصیه گر سرمایه گذاری در کریپتو")

symbol = st.text_input(
    'Enter Symbol like BTCUSD, ETHUSD, XRPUSD').upper().strip()
but = st.button('Lets go')

check_crypto_news = st.checkbox('بررسی اخبار فاندامنتال')
check_eco_news = st.checkbox('بررسی اخبار اقتصادی')
check_nobitex_news = st.checkbox('بررسی اخبار نوبیتکس')
check_bitpin_analysis = st.checkbox('بررسی تحلیل بیت پین')


# اجرای ماژول‌ها
if __name__ == "__main__":

    if symbol != '' and but and check_crypto_news:
        crypto(symbol)

    if check_nobitex_news:
        nobitex()

    if check_bitpin_analysis:
        bitpin()

    if check_eco_news:
        eco()
