import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("My App")

st.header("Product by HY")

st.subheader("2024")


st.markdown("**Under construction**")

st.markdown("```python3```")

st.code("python3 main.py")

st.text("some text")
st.write("Some text")

df = pd.read_csv('data/sample.csv',dtype="int")
st.dataframe(df)
#st.table(df)
st.metric(label="Population", value=900, delta=20, delta_color="inverse")

st.line_chart(df, x="year",y=["col1","col2",'col3'])

#st.area_chart(df, x="year",y=["col1","col2",'col3'])

st.bar_chart(df,x="year",y=["col1","col2",'col3'])

geo_df=pd.read_csv("data/sample_map.csv")

st.map(geo_df)


# Matplotlib

fig, ax = plt.subplots()
ax.plot(df.year, df.col1)
ax.set_title("My figure title")
ax.set_xlabel("x label")
ax.set_ylabel("y label")
fig.autofmt_xdate()

st.pyplot(fig)