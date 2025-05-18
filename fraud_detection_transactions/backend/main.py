from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import PredictionInput, PredictionOutput
from app.models import preprocessing, prediction
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    try:
        # Convirt the input data to pandas data frame
        input_df = pd.DataFrame([{  'Transaction_Amount': input_data.Transaction_Amount, 
                                    'Transaction_Type': input_data.Transaction_Type,
                                    'Account_Balance': input_data.Account_Balance, 
                                    'Device_Type': input_data.Device_Type, 
                                    'Location': input_data.Location,
                                    'Merchant_Category': input_data.Merchant_Category, 
                                    'IP_Address_Flag': input_data.IP_Address_Flag, 
                                    'Previous_Fraudulent_Activity': input_data.Previous_Fraudulent_Activity,
                                    'Daily_Transaction_Count': input_data.Daily_Transaction_Count, 
                                    'Avg_Transaction_Amount_7d': input_data.Avg_Transaction_Amount_7d,
                                    'Failed_Transaction_Count_7d': input_data.Failed_Transaction_Count_7d, 
                                    'Card_Type': input_data.Card_Type, 
                                    'Card_Age': input_data.Card_Age,
                                    'Transaction_Distance': input_data.Transaction_Distance, 
                                    'Authentication_Method': input_data.Authentication_Method, 
                                    'Risk_Score': input_data.Risk_Score,
                                    'Is_Weekend': input_data.Is_Weekend
                                }])
        
        # Preprocess the input data
        processed_data = preprocessing(input_df)

        # Make prediction
        fraud_detection_prediction = prediction(processed_data)

        # Return the prediction as a dictionary
        prediction_result = "Fraud" if fraud_detection_prediction[0] == 1 else "Not Fraud"
        return {"fraud_prediction": prediction_result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    