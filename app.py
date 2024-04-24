import streamlit as st
import numpy as np

def main():
    st.title("Fraud Payment Transaction Detection")

    transaction_type = st.selectbox("Transaction Type", ["Credit", "Debit"])
    amount = st.number_input("Amount")
    new_balance_sender = st.number_input("New Balance Sender")
    old_balance_sender = st.number_input("Old Balance Sender")
    new_balance_receiver = st.number_input("New Balance Receiver")
    old_balance_receiver = st.number_input("Old Balance Receiver")

    if st.button("Predict"):
        if (transaction_type == "Debit" and old_balance_receiver == 0 and new_balance_receiver == 0 and new_balance_sender == 0) or (transaction_type == "Credit" and new_balance_receiver == 0 and new_balance_sender == 0):
            output = "Alert!!! Fraud Transaction!"
        else:
            output = "Not a Fraud Transaction!"

        st.write(output)

if __name__ == "__main__":
    main()
