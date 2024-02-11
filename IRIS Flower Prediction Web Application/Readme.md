# Simple Iris Flower Prediction App

## Overview
This is a simple Streamlit web application for predicting the type of Iris flower based on user-input parameters. The app utilizes a RandomForestClassifier from scikit-learn to make predictions.

## Dependencies
- [Streamlit](https://www.streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)

## Usage
1. Install the required dependencies:
2. Run the app:
3. Adjust the sliders in the sidebar to set the input parameters for Sepal length, Sepal width, Petal length, and Petal width.

4. The app will display the user input parameters, the class labels and their corresponding index numbers, the predicted class label, and the prediction probability.

## Code Structure
- `app.py`: The main script containing the Streamlit application code.
- `README.md`: This file providing information about the app and instructions for use.

## Additional Notes
- The app uses the Iris dataset from scikit-learn for training the RandomForestClassifier.
- The trained model predicts the class label and probability based on user-input parameters.
- Feel free to customize and extend the app for other machine learning models or datasets.

Happy predicting!

