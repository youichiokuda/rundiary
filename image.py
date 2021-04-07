import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

st.title('ランニング最適化プロジェクト')

df=pd.read_csv('rundiary.csv')

st.table(df)


st.write(
    px.bar(df, x='day', y='condition' ,title="コンディション")
)

st.write(
    px.bar(df, x='day', y='distance' ,title="距離")
)

st.write(
    px.bar(df, x='day', y='span' ,title="スパン")
)



st.title('グラフテスト')
st.line_chart(df)

df_corr = df.corr(method='pearson')
df_corr

sns.heatmap(df_corr, cmap= sns.color_palette('coolwarm', 10), annot=True,fmt='.2f', vmin = -1, vmax = 1)


