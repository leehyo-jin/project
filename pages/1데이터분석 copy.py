import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='page1',page_icon='🎈')

st.sidebar.header('🎈데이터 분석')

st.header('갑상선 데이터 분석',divider='rainbow')

st.markdown('''
            
- sepal length :꽃받침 길이
            ''')
df=pd.read_csv('iris.csv')
t1,t2,t3,t4=st.tabs(['상위데이터','데이터통계','컬럼데이터','조건데이터'])
with t1:
    dh=df.head(10)
    st.write(dh)
with t2:
    dd=df.describe()
    st.write(dd)
with t3:
    col=df.columns.tolist()
    col=col[0: ]
    se_col=st.multiselect('select col',col)
    new_df = df.loc[:, se_col]
    st.write(new_df)
with t4:
    c=st.selectbox('select species',('setosa','b','c'))
    cl=df['Species']==c
    c_df=df.loc[cl]
    st.write(c_df)