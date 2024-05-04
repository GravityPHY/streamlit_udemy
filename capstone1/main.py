import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

URL = "https://raw.githubusercontent.com/marcopeix/MachineLearningModelDeploymentwithStreamlit/master/12_dashboard_capstone/data/quarterly_canada_population.csv"

df = pd.read_csv(URL, dtype={'Quarter': str, 
                            'Canada': np.int32,
                            'Newfoundland and Labrador': np.int32,
                            'Prince Edward Island': np.int32,
                            'Nova Scotia': np.int32,
                            'New Brunswick': np.int32,
                            'Quebec': np.int32,
                            'Ontario': np.int32,
                            'Manitoba': np.int32,
                            'Saskatchewan': np.int32,
                            'Alberta': np.int32,
                            'British Columbia': np.int32,
                            'Yukon': np.int32,
                            'Northwest Territories': np.int32,
                            'Nunavut': np.int32})

# title
st.title("Population of Canada")

# markdown
st.markdown(f"Source table can be found [here]({URL})")


# Selectbox

select = st.selectbox("See full data table",
                        options=df.columns[1:],
                        index=0)

# columns

col1, col2, col3 = st.columns(3)
col1.write("Choose a starting date")
col2.write("Choose an end date")
col3.write("Choose a location")
select1 = col1.selectbox("Quarter begin",
                        options=df.columns[1:],
                        index=0)
start_year = col1.slider("Year", min_value=1991, max_value=2023, value=1991,
                            step=1, key="start_y")
select2 = col2.selectbox("Quarter end",
                        options=df.columns[1:],
                        index=0)
select3 = col3.selectbox("Choose a location",
                        options=df.columns[1:],
                        index=0)