import streamlit as st # type: ignore

st.title("Simple Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
    st.success(f"Result: {result}")