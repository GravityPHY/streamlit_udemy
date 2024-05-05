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

with st.expander("See full data table"):
    st.write(df)

# Selectbox

with st.form("population-form"):

    # columns

    col1, col2, col3 = st.columns(3)
    col1.write("Choose a starting date")
    col2.write("Choose an end date")
    col3.write("Choose a location")
    start_quarter = col1.selectbox("Quarter begin",
                        options=['Q1','Q2','Q3','Q4'],
                        index=0)
    start_year = col1.slider("Year", min_value=1991, max_value=2023, value=1991,
                            step=1, key="start_y")
    end_quarter = col2.selectbox("Quarter end",
                        options=['Q1','Q2','Q3','Q4'],
                        index=0)
    end_year = col2.slider("Year", min_value=1991, max_value=2023, value=1991,
                            step=1, key="end_y")

    target = col3.selectbox("Choose a location",
                        options=df.columns[1:],
                        index=0)
    analyze_btn = st.form_submit_button(label="Analyze", type="primary")



start_date = f"{start_quarter} {start_year}"
end_date = f"{end_quarter} {end_year}"

def format_date_for_comparison(date):
    if date[1]==2:
        return float(date[2:])+0.25
    elif date[2]==3:
        return float(date[2:])+0.50
    elif date[3]==4:
        return float(date[2:])+0.75
    else:
        return float(date[2:])

def end_before_start(start_date, end_date):
    num_start = format_date_for_comparison(start_date)
    num_end = format_date_for_comparison(end_date)
    if num_start>num_end:
        return True
    else:
        return False


def display_dashboard(start_date,end_date, target):
    tab1, tab2 = st.tabs(["Population change","Compare"])

    with tab1:
        st.subheader(f"Population change from {start_date} to {end_date}")
        col1,col2 = st.columns(2)
        
        with col1:
            initial = df.loc[df["Quarter"]==start_date,target].item()
            final = df.loc[df["Quarter"]==end_date,target].item()

            percentage_diff = round((final - initial) / initial *100,2)
            delta = f"{percentage_diff}%"
            st.metric(start_date, value=initial)
            st.metric(end_date, value=final, delta=delta)

        with col2:
            start_idx = df.loc[df['Quarter']==start_date].index.item()
            end_idx = df.loc[df['Quarter']==end_date].index.item()

            filtered_df = df.iloc[start_idx:end_idx+1]
            fig, ax = plt.subplots()
            ax.plot(filtered_df["Quarter"], filtered_df[target])
            ax.set_xlabel("Time")
            ax.set_ylabel("Population")
            ax.set_xticks([filtered_df['Quarter'].iloc[0],filtered_df['Quarter'].iloc[-1]])
            fig.autofmt_xdate()
            st.pyplot(fig)

    with tab2:
        st.subheader("Compare with other locations")
        all_targets = st.multiselect("Choose other locations",
                                    options=filtered_df.columns[1:],
                                    default=[target])
        fig, ax = plt.subplots()
        for each in all_targets:
            ax.plot(filtered_df['Quarter'], filtered_df[each])
        ax.set_xlabel("Time")
        ax.set_ylabel("Population")
        ax.set_xticks([filtered_df['Quarter'].iloc[0],
                       filtered_df['Quarter'].iloc[-1]])
        st.pyplot(fig)
        
        
if end_before_start(start_date,end_date):
    st.error("Start date must come before end date.")
elif start_date not in df['Quarter'].tolist() or end_date not in df['Quarter'].tolist():
    st.error("No data available.")
else:
    display_dashboard(start_date, end_date,target)
