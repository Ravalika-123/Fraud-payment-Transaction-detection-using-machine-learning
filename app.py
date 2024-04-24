# app.py

from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:

        # Extract input values from the form
        transaction_type = request.form['transaction_type']
        amount = float(request.form['amount'])
        new_balance_sender = float(request.form['new_balance_sender'])
        old_balance_sender = float(request.form['old_balance_sender'])
        new_balance_receiver = float(request.form['new_balance_receiver'])
        old_balance_receiver = float(request.form['old_balance_receiver'])

        # Create input array for prediction
        input_data = np.array([[transaction_type, amount, new_balance_sender, old_balance_sender, new_balance_receiver, old_balance_receiver]])

        if (transaction_type=='4' and old_balance_receiver==0 and new_balance_receiver==0 and new_balance_sender==0) or (transaction_type=='3' and new_balance_receiver==0 and new_balance_sender==0):
            output = "Alert!!! Fraud Transaction!"
        else:
            output = "Not Fraud Transaction!"






        #
        # # Determine output
        # if prediction[0] == 1:
        #     output = "Fraud Transaction"
        # elsoutput = "Fraud Transaction"e:
        #     output = "Not a Fraud Transaction"

        return render_template('result.html', prediction=output)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    app.run(debug=True)
