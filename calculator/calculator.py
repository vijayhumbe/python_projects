import streamlit as st

st.title("Calculator")
st.header("Enter Two Numbers")

# Inputs
a = st.number_input("Enter first number")
b = st.number_input("Enter second number", value=0.0)

st.subheader("Select Operation")
option = st.selectbox("Choose operation", ["+", "-", "*", "/", "%"])

# Button
if st.button("Calculate"):

    if option == "+":
        st.success(f"Result: {a + b}")

    elif option == "-":
        st.success(f"Result: {a - b}")

    elif option == "*":
        st.success(f"Result: {a * b}")

    elif option == "/":
        if b == 0:
            st.error("Division by zero is not allowed")
        else:
            st.success(f"Result: {a / b}")

    elif option == "%":
        st.success(f"Result: {a % b}")
