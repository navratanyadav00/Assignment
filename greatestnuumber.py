import streamlit as st

def largest_num(num1, num2, num3):
    """
    A function that takes in three numbers and returns the largest one.
    """
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest

# Define the Streamlit app
def app():
    st.title("Find the largest number among three")
    st.write("Enter three numbers below to find the largest one:")
    
    # Get user inputs
    num1 = st.number_input("Enter number 1:", value=0, step=1)
    num2 = st.number_input("Enter number 2:", value=0, step=1)
    num3 = st.number_input("Enter number 3:", value=0, step=1)
    
    # Compute and display the result
    if st.button("Find the largest number"):
        result = largest_num(num1, num2, num3)
        st.write("The largest number is:", result)

# Run the app
if _name_ == '_main_':
    app()
