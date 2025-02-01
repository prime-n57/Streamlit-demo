import pandas as pd
import pygwalker as pyg
import streamlit as st

# ワイド表示
st.set_page_config(layout="wide")

# タイトル
st.title("Data Analysis with PyGWalker.")

# データフレームの用意
df = None

# サイドバーでファイル選択
with st.sidebar:
    uploaded_file = st.file_uploader("Choose a CSV file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

# ファイルがアップロードされている場合のみ pygwalker を表示
if df is not None:
    pyg.walk(df, env='Streamlit')
else:
    st.info("CSVファイルをアップロードしてください。")
