import React, { useState } from 'react';
import axios from 'axios';

const TransactionForm = () => {
  const [formData, setFormData] = useState({
    Transaction_Amount: 0,
    Transaction_Type: 'POS',
    Account_Balance: 0,
    Avg_Transaction_Amount_7d: 0,
    Transaction_Distance: 0,
    Risk_Score: 0,
    Device_Type: 'Mobile',
    Location: 'New York',
    Merchant_Category: 'Electronics',
    Card_Type: 'Visa',
    Authentication_Method: 'Password',
    IP_Address_Flag: 0,
    Previous_Fraudulent_Activity: 0,
    Daily_Transaction_Count: 0,
    Failed_Transaction_Count_7d: 0,
    Card_Age: 0,
    Is_Weekend: 0,
  });

  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setPrediction(null);

    try {
      const response = await axios.post('http://localhost:8000/predict', formData);
      setPrediction(response.data.fraud_prediction);
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred');
    }
  };

  return (
    <div className="transaction-form">
      <form onSubmit={handleSubmit}>
        <label>
          Transaction Amount:
          <input
            type="number"
            name="Transaction_Amount"
            value={formData.Transaction_Amount}
            onChange={handleChange}
          />
        </label>
        <label>
          Transaction Type:
          <select
            name="Transaction_Type"
            value={formData.Transaction_Type}
            onChange={handleChange}
          >
            <option value="POS">POS</option>
            <option value="Bank Transfer">Bank Transfer</option>
            <option value="Online">Online</option>
            <option value="ATM Withdrawal">ATM Withdrawal</option>
          </select>
        </label>
        <label>
          Account Balance:
          <input
            type="number"
            name="Account_Balance"
            value={formData.Account_Balance}
            onChange={handleChange}
          />
        </label>
        <label>
          Average Transaction Amount (7d):
          <input
            type="number"
            name="Avg_Transaction_Amount_7d"
            value={formData.Avg_Transaction_Amount_7d}
            onChange={handleChange}
          />
        </label>
        <label>
          Transaction Distance:
          <input
            type="number"
            name="Transaction_Distance"
            value={formData.Transaction_Distance}
            onChange={handleChange}
          />
        </label>
        <label>
          Risk Score:
          <input
            type="number"
            name="Risk_Score"
            value={formData.Risk_Score}
            onChange={handleChange}
          />
        </label>
        <label>
          Device Type:
          <select
            name="Device_Type"
            value={formData.Device_Type}
            onChange={handleChange}
          >
            <option value="Laptop">Laptop</option>
            <option value="Mobile">Mobile</option>
            <option value="Tablet">Tablet</option>
          </select>
        </label>
        <label>
          Location:
          <select
            name="Location"
            value={formData.Location}
            onChange={handleChange}
          >
            <option value="Sydney">Sydney</option>
            <option value="New York">New York</option>
            <option value="Mumbai">Mumbai</option>
            <option value="Tokyo">Tokyo</option>
            <option value="London">London</option>
          </select>
        </label>
        <label>
          Merchant Category:
          <select
            name="Merchant_Category"
            value={formData.Merchant_Category}
            onChange={handleChange}
          >
            <option value="Travel">Travel</option>
            <option value="Clothing">Clothing</option>
            <option value="Restaurants">Restaurants</option>
            <option value="Electronics">Electronics</option>
            <option value="Groceries">Groceries</option>
          </select>
        </label>
        <label>
          Card Type:
          <select
            name="Card_Type"
            value={formData.Card_Type}
            onChange={handleChange}
          >
            <option value="Amex">Amex</option>
            <option value="Mastercard">Mastercard</option>
            <option value="Visa">Visa</option>
            <option value="Discover">Discover</option>
          </select>
        </label>
        <label>
          Authentication Method:
          <select
            name="Authentication_Method"
            value={formData.Authentication_Method}
            onChange={handleChange}
          >
            <option value="Biometric">Biometric</option>
            <option value="Password">Password</option>
            <option value="OTP">OTP</option>
            <option value="PIN">PIN</option>
          </select>
        </label>
        <label>
          IP Address Flag:
          <input
            type="number"
            name="IP_Address_Flag"
            value={formData.IP_Address_Flag}
            onChange={handleChange}
          />
        </label>
        <label>
          Previous Fraudulent Activity:
          <input
            type="number"
            name="Previous_Fraudulent_Activity"
            value={formData.Previous_Fraudulent_Activity}
            onChange={handleChange}
          />
        </label>
        <label>
          Daily Transaction Count:
          <input
            type="number"
            name="Daily_Transaction_Count"
            value={formData.Daily_Transaction_Count}
            onChange={handleChange}
          />
        </label>
        <label>
          Failed Transaction Count (7d):
          <input
            type="number"
            name="Failed_Transaction_Count_7d"
            value={formData.Failed_Transaction_Count_7d}
            onChange={handleChange}
          />
        </label>
        <label>
          Card Age:
          <input
            type="number"
            name="Card_Age"
            value={formData.Card_Age}
            onChange={handleChange}
          />
        </label>
        <label>
          Is Weekend:
          <input
            type="number"
            name="Is_Weekend"
            value={formData.Is_Weekend}
            onChange={handleChange}
          />
        </label>
        <button type="submit">Predict Fraud</button>
      </form>

      {prediction && (
        <div className="prediction-result">
          <h2>Prediction Result:</h2>
          <p>{prediction}</p>
        </div>
      )}

      {error && (
        <div className="error">
          <h2>Error:</h2>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
};

export default TransactionForm;