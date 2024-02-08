import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import streamlit as st



#제목
st.title("한투 개인 매매 실적 대시보드")


#데이터 업로드(한투에서 받은 csv파일 업로드 or 깃허브에 있는 디폴트값)
st.write("파일 업로드.")


#디폴트 데이터 설정
default_data = pd.read_csv('solution_data.csv')


#파일 업로드 설정/올리지 않으면 디폴트 데이터, 올리면 데이터가 올린것으로 변경됨
uploaded_file = st.file_uploader("파일을 업로드하세요", type=['csv', 'xlsx'])

if uploaded_file is None: 
    data = default_data
    st.write(data)
else:
    data = pd.read_csv(uploaded_file)
    st.write(data)







# menu = ["Home", "About"]
# choice = st.sidebar.selectbox("메뉴를 선택하세요", menu)

    




