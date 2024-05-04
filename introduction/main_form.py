import streamlit as st

with st.form("form_key"):
    appetizer = st.selectbox("Appetizers",
                        options=["choice1","choice2"],
                        index=0)
    main = st.selectbox("Main course",
                    options=["choice1","choice2"],
                    index=0)
    dessert = st.selectbox("Dessert",
                    options=["choice1","choice2"],
                    index=0)
    wine = st.checkbox("Are you bringing your own wine?")

    visit_date=st.date_input("When are you coming")
    visit_time=st.time_input("At what time are you coming?")
    allergies=st.text_area("Any allergies",height=500,
                        placeholder="Leave us a note for allergies")
    submit_btn = st.form_submit_button(label="Submit")
st.write(f"""Your order summary:\\
    Appetizer: {appetizer}\\
    Main course: {main}\\
    Dessert: {dessert}\\
    Are you bringing your won wine: {"yes" if wine else "no"}\\
    Data of visit: {visit_date}\\
    Time of visit: {visit_time}\\
    Allergies: {allergies}\\

""")
