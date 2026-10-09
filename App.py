
import streamlit as st

st.title("📚 Smart Study Buddy")
st.write("Your personal study planner!")

name = st.text_input("Enter your name")
hours = st.number_input("Study hours per day", 1, 12, 3)

subjects = st.multiselect(
    "Choose subjects",
    ["Python", "SQL", "AI Basics"]
)

if st.button("Create Study Plan"):
    if subjects:
        each = hours / len(subjects)
        st.subheader(name + "'s Study Plan")
        for subject in subjects:
            st.write(subject + ": " + str(round(each, 1)) + " hours")
    else:
        st.warning("Please select a subject.")

st.header("📝 Quick Quiz")

answer = st.radio(
    "What does AI stand for?",
    ["Artificial Intelligence", "Automatic Internet", "Advanced Input"],
    index=None
)

if st.button("Check Answer"):
    if answer == "Artificial Intelligence":
        st.success("Correct answer!")
    elif answer is None:
        st.warning("Please select an answer.")
    else:
        st.error("Wrong answer. Try again!")

