import streamlit as st

# Title
st.title("Student Grading System")

# Input fields
report = st.number_input("Enter Project Marks (0 - 100):", min_value=0, max_value=100, step=1)
local = st.number_input("Enter Internal Marks (0 - 100):", min_value=0, max_value=100, step=1)
global_marks = st.number_input("Enter External Marks (0 - 100):", min_value=0, max_value=100, step=1)

# Calculate total
total = report + local + global_marks

# Grade calculation functionu
def calculate_grade(total):
    # Example out of 300
    if total >= 240:
        return "A"
    elif total >= 200:
        return "B"
    elif total >= 160:
        return "C"
    elif total >= 120:
        return "D"
    elif total >= 50:
        return "E"
    else:
        return "F"

# Show results
if st.button("Calculate Grade"):
    grade = calculate_grade(total)
    st.success(f" Total Marks: {total} | Grade: {grade}")