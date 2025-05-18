from pydantic import BaseModel, Field
from enum import Enum

# Define enums for categorical fields
class TransactionType(str, Enum):
    POS = "POS"
    BANK_TRANSFER = "Bank Transfer"
    ONLINE = "Online"
    ATM_WITHDRAWAL = "ATM Withdrawal"


class DeviceType(str, Enum):
    LAPTOP = "Laptop"
    MOBILE = "Mobile"
    TABLET = "Tablet"

class location(str, Enum):
    SYDNEY = "Sydney"
    NEW_YORK = "New York"
    MUMBAI = "Mumbai"
    TOKYO = "Tokyo"
    LONDON = "London"

class MerchantCategory(str, Enum):
    TRAVEL = "Travel"
    CLOTHING = "Clothing"
    RESTAURANTS = "Restaurants"
    ELECTRONICS = "Electronics"
    GROCERIES = "Groceries"

class CardType(str, Enum):
    AMEX = "Amex"
    MASTERCARD = "Mastercard"
    VISA = "Visa"
    DISCOVER = "Discover"

class AuthenticationMethod(str, Enum):
    BIOMETRIC = "Biometric"
    PASSWORD = "Password"
    OTP = "OTP"
    PIN = "PIN"

# Define the input schema for the prediction API
class PredictionInput(BaseModel):
    """
    Schema for the input data required to make a prediction.
    """
    Transaction_Amount: float = Field(..., ge=0, description="The amount of money involved in the transaction.")
    Account_Balance: float = Field(..., description="User's account balance before the transaction.")
    Avg_Transaction_Amount_7d: float = Field(..., ge=0, description="User's average transaction amount in the past 7 days.")
    Transaction_Distance: float = Field(..., ge=0, description="Distance between the user's usual location and transaction location.")
    Risk_Score: float = Field(..., description="Fraud risk score computed for the transaction (from 0 to 1).")


    Transaction_Type: TransactionType = Field(..., description="Type of transaction ('POS', 'Bank Transfer', 'Online', 'ATM Withdrawal').")
    Device_Type: DeviceType = Field(..., description="Type of device used ('Laptop', 'Mobile', 'Tablet').")
    Location: location = Field(..., description="Geographical location of the transaction ('Sydney', 'New York', 'Mumbai', 'Tokyo', 'London').")
    Merchant_Category: MerchantCategory = Field(..., description="Type of merchant ('Travel', 'Clothing', 'Restaurants', 'Electronics', 'Groceries').")
    Card_Type: CardType = Field(..., description="Type of payment card used ('Amex', 'Mastercard', 'Visa', 'Discover').")
    Authentication_Method: AuthenticationMethod = Field(..., description="How the user authenticated ('Biometric', 'Password', 'OTP', 'PIN').")


    IP_Address_Flag: int = Field(..., ge=0, le=1, description="Whether the IP address was flagged as suspicious (0 or 1).")
    Previous_Fraudulent_Activity: int = Field(..., ge=0, le=1, description="Number of past fraudulent activities by the user (0 or 1).")
    Daily_Transaction_Count: int = Field(..., ge=0, description="Number of transactions made by the user that day")
    Failed_Transaction_Count_7d: int = Field(..., ge=0, description="Count of failed transactions in the past 7 days")
    Card_Age: int = Field(..., description="Age of the card in months")
    Is_Weekend: int = Field(..., ge=0, le=1, description="Whether the transaction occurred on a weekend (0 or 1).")


# Define the output schema for the prediction API
class PredictionOutput(BaseModel):
    """
    Schema for the output data returned by the prediction API.
    """
    fraud_prediction: str = Field(..., description="Predicted fraud status ('Fraud' or 'Not Fraud').")