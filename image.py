import streamlit as st
import pandas as pd

st.title('ランニング最適化プロジェクト')

df=pd.read_csv('rundiary.csv')

st.table(df)

#st.dataframe(df, 2000, 1000)