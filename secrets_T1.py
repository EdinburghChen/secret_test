import streamlit as st
#Google sheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB userid:", st.secrets["db_userid"])
st.write("DB password:", st.secrets["db_password"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)
st.write( st.secrets["cjson"])


# 前置作業
scopes = ["https://spreadsheets.google.com/feeds"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["cjson"], scopes)
gss_client = gspread.authorize(credentials)

#開啟 Google Sheet 資料表
spreadsheet_key = '1b6OiZ8USWq94vvf-0jg3WSnP8RVggRFpt2_qn_5fcKM' 
sheet = gss_client.open_by_key(spreadsheet_key).sheet1

# Google Sheet 資料表
#sheet.clear() # 清除 Google Sheet 資料表內容
sheet.batch_clear(['A1:A','B1:B','C1:C','D1:D','E1:E','F1:F'])
 # 增加標題
wstitle=["姓名Online","姓名代號","員工證卡號","單位名稱","單位代號","職位名稱"]
sheet.append_row(wstitle) 
