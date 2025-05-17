# Fraud Detection System

A machine learning-powered fraud detection system with a React frontend and FastAPI backend, containerized using Docker.

![image](https://github.com/user-attachments/assets/0e4708ea-7a03-4a5f-bb5e-2f6db1cd865d)

![image](https://github.com/user-attachments/assets/6b7bb604-a0e4-4725-b7f4-894e18a338dd)

## Features

- **Machine Learning Model**: Pre-trained decision tree model for fraud detection
- **REST API**: FastAPI backend with proper type validation
- **Web Interface**: React-based form for submitting transaction details
- **Containerized**: Ready-to-run with Docker Compose
- **Input Validation**: Comprehensive schema validation for all transaction fields

## Tech Stack

**Frontend**:
- React.js
- Axios (for API calls)
- CSS (vanilla)

**Backend**:
- FastAPI
- Pydantic (for data validation)
- Scikit-learn (model serving)
- Pandas (data preprocessing)

**Infrastructure**:
- Docker
- Docker Compose

## Prerequisites

- Docker (v20.10+)
- Docker Compose (v1.29+)
- Node.js (v16+) *[only for frontend development]*
- Python (3.9+) *[only for backend development]*

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FAHAD4132/Fraud_Detection_System.git
   cd fraud_detection_system

2. Build and run with Docker:
   ```bash
   docker-compose up --build
   ```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Project Structure

```
fraud-detection-system/
├── backend/
│   ├── app/
│   │   ├── models.py        # ML model loading and prediction
│   │   ├── schemas.py       # Pydantic models
│   │   └── data/            # Model files (not in repo)
│   ├── main.py              # FastAPI application
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── public/
|   │   ├── index.html
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── App.jsx          # Main application
│   │   ├── index.js
│   │   └── styles.css       # Global styles
│   ├── Dockerfile
│   └── package.json
└── docker-compose.yml       # Orchestration
```

## Development

### Backend Development

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac)
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Development

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm start
   ```

## API Documentation

The FastAPI backend automatically generates OpenAPI documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Contact

Fahad Abdullah Al-Otaibi - fahadalotaibi730@gmail.com

Project Link: [here](https://github.com/FAHAD4132/Fraud_Detection_System)
