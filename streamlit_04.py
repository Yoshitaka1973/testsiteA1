import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlitのレイアウト')

st.header('1. カラム')

st.subheader('カラムとは')
col = st.columns(3)
col[0].write('カラム１')
col[1].write('カラム２')
col[2].write('カラム３')


st.subheader('検索条件をカラムに分ける')
# col = st.columns(2)
col = st.columns([2, 1])
branch = col[0].multiselect('支店を選択してください（複数選択可）',
                            ['支店A', '支店B', '支店C', '支店D', '支店E'],key='m1')
year = col[1].number_input('年を指定してください', 
                           min_value=2020, 
                           max_value=2024, 
                           value=2020, 
                           step=1, 
                           key='n1')

df = pd.DataFrame(data=np.random.randint(0, 1000, (3, 6)),
                  index=['支店A', '支店B', '支店C'],
                  columns=['1月', '２月', '３月', '４月', '５月', '６月'])
st.dataframe(df, width=600, height=200)


st.subheader('検索条件と表示結果をカラムに分ける')
col2 = st.columns([1, 2])
branch = col2[0].multiselect('支店を選択してください（複数選択可）',
                             ['支店A', '支店B', '支店C', '支店D', '支店E'],
                             key='m2')
year = col2[0].number_input('年を指定してください', 
                            min_value=2020, 
                            max_value=2024, 
                            value=2020, 
                            step=1, 
                            key='n2')
col2[1].dataframe(df, width=600, height=200)


st.header('2. サイドバー')
with st.sidebar:
    branch = st.multiselect('支店を選択してください（複数選択可）',
                            ['支店A', '支店B', '支店C', '支店D', '支店E'],key='m3')
    year = st.number_input('年を指定してください', 
                           min_value=2020, 
                           max_value=2024, 
                           value=2020, 
                           step=1, 
                           key='n3')

st.dataframe(df, width=600, height=200)