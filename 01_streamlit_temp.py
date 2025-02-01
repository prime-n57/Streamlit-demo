import streamlit as st
import pandas as pd

st.title("Pandas with Streamlit Demo")

# ファイルアップローダー
uploaded_file = st.file_uploader("CSVファイルをアップロード", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # データ表示
    st.subheader("データプレビュー")
    st.write(df.head())
    
    # 基本統計量
    st.subheader("データの基本統計量")
    st.write(df.describe())
    
    # カラム選択
    column = st.selectbox("カラムを選択", df.columns)
    
    # 選択したカラムのユニーク値表示
    st.subheader(f"{column} カラムのユニーク値")
    st.write(df[column].unique())
    
    # 選択したカラムのヒストグラム表示
    if df[column].dtype in ['int64', 'float64']:
        st.subheader(f"{column} カラムのヒストグラム")
        st.bar_chart(df[column])
