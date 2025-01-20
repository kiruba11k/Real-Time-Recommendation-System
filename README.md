
# Real-Time Recommendation System for E-commerce Platform

This project implements a **Real-Time Recommendation System** for an e-commerce platform using a **hybrid model** combining collaborative filtering and content-based filtering. It is designed to recommend products to users based on their browsing or purchase history.

### Table of Contents
1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [System Architecture](#system-architecture)
4. [Setup](#setup)
5. [Running the Project](#running-the-project)
6. [API Endpoints](#api-endpoints)
7. [Frontend](#frontend)
8. [Conclusion](#conclusion)

---

## Introduction

The real-time recommendation system suggests products to users based on their past interactions. The system uses two main approaches:

1. **Collaborative Filtering (CF)**: Recommends products based on the preferences of similar users.
2. **Content-Based Filtering (CBF)**: Recommends products similar to what the user has already interacted with, using product features like category, description, etc.

The combination of these models leads to a **Hybrid Recommendation System** that provides more accurate recommendations.

---

## Technologies Used

- **Backend**: 
  - **Flask**: Lightweight web framework for building the REST API.
  - **Pickle**: For saving and loading trained models.
  - **scikit-learn**: For implementing machine learning models, particularly for content-based filtering.
  - **Surprise**: For collaborative filtering.
  - **Pandas**: For data manipulation.
  - **SQLAlchemy** (optional): For database handling if you want to persist data.

- **Frontend**: 
  - **React.js**: JavaScript library for building user interfaces.
  - **Axios**: For making HTTP requests to the backend API.

- **Data**:
  - **CSV Files**: Simulated data for user interactions, products, and recommendations.

- **Deployment**: 
  - **Heroku** or **Docker** for cloud deployment (optional).

---

## System Architecture

The architecture follows a **client-server model**:

1. **Backend**: A Flask-based API serves the recommendation requests. It loads the hybrid recommendation model and returns product recommendations based on user history.
   
2. **Frontend**: A React.js web application where users can interact with the system and see personalized product recommendations.

3. **Database**: (Optional) A CSV file-based database or SQL database is used to store user interaction and product data.

---

## Setup

### Prerequisites
Before setting up the project, make sure you have the following installed:

- **Python 3.8+**
- **Node.js 12+**
- **pip** and **npm** for installing Python and Node packages.

---

### Backend Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Real-Time-Recommendation-System.git
   cd Real_Time_Recommendations/backend
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   This will install Flask, pandas, scikit-learn, surprise, and other required Python packages.

4. **Run the Flask server**:

   ```bash
   python app.py
   ```

   This will start the Flask application at `http://127.0.0.1:5000/`.

---

### Frontend Setup

1. **Navigate to the frontend directory**:

   ```bash
   cd ../frontend
   ```

2. **Install frontend dependencies**:

   ```bash
   npm install
   ```

3. **Start the React development server**:

   ```bash
   npm start
   ```

   This will start the React app at `http://localhost:3000/`.

---

## Running the Project

Once both the frontend and backend are up and running, navigate to `http://localhost:3000/` in your browser to interact with the recommendation system.

### API Endpoint

- **GET /recommend?user_id={user_id}**

  This endpoint returns product recommendations for a given user. The backend uses the hybrid recommendation system to provide suggestions based on the user's browsing or purchase history.

  **Example Request**:

  ```bash
  curl "http://127.0.0.1:5000/recommend?user_id=1"
  ```

  **Example Response**:

  ```json
  {
    "status": "success",
    "recommendations": [
      {
        "product_id": 1,
        "product_name": "Product 1",
        "category": "Electronics",
        "price": 99.99,
        "description": "A great product for tech enthusiasts."
      },
      ...
    ]
  }
  ```

---

## Frontend

The React frontend interacts with the Flask API to fetch product recommendations and display them to the user.

### Key Files:

- **src/App.js**: Main React component that displays the product recommendations.
- **src/api.js**: Contains functions for making HTTP requests to the backend API.

---

## Why We Used These Methods

1. **Hybrid Recommendation**: Combining collaborative and content-based filtering enhances recommendation accuracy. Collaborative filtering leverages the collective preferences of users, while content-based filtering focuses on the attributes of the products themselves.

2. **Flask**: A lightweight web framework that is easy to set up for small to medium-sized projects. It is perfect for serving machine learning models in production.

3. **React.js**: Offers a fast, interactive user interface. React allows us to build components that interact with the backend in real-time, providing a smooth user experience.

4. **Pickle**: Used to save and load machine learning models efficiently. This avoids retraining the models every time the app is restarted.

5. **Surprise**: An easy-to-use library for building collaborative filtering models, which can be integrated with content-based filtering methods.

---

## Conclusion

This project demonstrates a **real-time recommendation system** for e-commerce platforms, providing personalized product suggestions using a **hybrid model** combining collaborative and content-based filtering. The use of Flask and React.js makes it a scalable solution, and the hybrid approach ensures that recommendations are accurate and relevant for users.

---
