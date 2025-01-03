import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title='데이터시각화',page_icon=💐)
st.sidebar.header('데이터 시각화')

st.header('💐시각화 개요',divider='rainbow')
st.markdown('''
            
            ''')
st.subheader('연관성 파악을 위한 시각화')
df=pd.read_csv('iris,csv')
t1,t2,t3,t4=st.tabs(['그래프1','그래프2','그래프3','그래프4'])
with t1:
    fig=plt.figure(figsize=(20,6))
    st.header('Sepal 히스토그램')
    sns.histplot(data=df, x='Sepal x열이름',hue='열이름')
    #막대그래프 sns.barplot(data=df, x='SepalLength', y='열이름')
    st.pyplot(fig)
with t2:
    st.header('Sepal 다른거 히스토그램')
    fig=plt.figure(figsize=(20,10))
    sns.histplot(data=df, x='Sepal x열이름',y='y열이름',hue='열이름')
    #sns.scatterplot(data=df, x='열이름',y='열이름')
    #sns.countplot(data=df, x='열이름',y='열이름',hue='비만도결과')
    st.pyplot(fig)
with t3:
with t4: