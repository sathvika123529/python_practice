import streamlit as st
num1=st.number_input("enter the first value(0-100):",min_value=0,max_value=100,step=1)
num2=st.number_input("enter the second value(0-100):",min_value=0,max_value=100,step=1)
st.write("The Addition of two numbers is:",num1+num2)