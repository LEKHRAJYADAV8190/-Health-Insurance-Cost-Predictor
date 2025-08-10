import pandas as pd
import joblib

# Load the trained models and scalers from the specified directory
model_young = joblib.load("model/model_young1.joblib")
model_rest = joblib.load("model/model_rest.joblib")
scaler_young = joblib.load("model/scaler_young1.joblib")
scaler_rest = joblib.load("model/scaler_rest.joblib")

def calculate_normalized_risk(medical_history):
    """
    Calculates a normalized risk score based on a user's medical history.
    """
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }
    # Split the medical history string (e.g., "diabetes & thyroid") into a list
    diseases = medical_history.lower().split(" & ")

    # Calculate the total risk by summing scores for each disease
    total_risk_score = sum(risk_scores.get(disease.strip(), 0) for disease in diseases)

    # Normalize the score to a 0-1 scale
    max_score = 14  # Max possible score (heart disease + diabetes/high blood pressure)
    min_score = 0
    normalized_risk_score = (total_risk_score - min_score) / (max_score - min_score)

    return normalized_risk_score

def preprocess_input(input_dict):
    """
    Converts the input dictionary from the web form into a DataFrame
    that matches the structure the model was trained on.
    """
    # Define all columns the model expects, including one-hot encoded and engineered features.
    # **FIX:** Added 'income_level' to this list to match the columns the scaler expects.
    expected_columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk',
        'normalized_risk_score', 'income_level', 'gender_Male', 'region_Northwest',
        'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight',
        'smoking_status_Occasional', 'smoking_status_Regular', 'employment_status_Salaried',
        'employment_status_Self-Employed'
    ]

    # Mapping for the insurance plan feature
    insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}

    # Create a single-row DataFrame initialized with zeros
    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    # Populate the DataFrame with values from the input dictionary
    for key, value in input_dict.items():
        if key == 'Gender' and value == 'Male':
            df['gender_Male'] = 1
        elif key == 'Region':
            if value == 'Northwest':
                df['region_Northwest'] = 1
            elif value == 'Southeast':
                df['region_Southeast'] = 1
            elif value == 'Southwest':
                df['region_Southwest'] = 1
        elif key == 'Marital Status' and value == 'Unmarried':
            df['marital_status_Unmarried'] = 1
        elif key == 'BMI Category':
            if value == 'Obesity':
                df['bmi_category_Obesity'] = 1
            elif value == 'Overweight':
                df['bmi_category_Overweight'] = 1
            elif value == 'Underweight':
                df['bmi_category_Underweight'] = 1
        elif key == 'Smoking Status':
            if value == 'Occasional':
                df['smoking_status_Occasional'] = 1
            elif value == 'Regular':
                df['smoking_status_Regular'] = 1
        elif key == 'Employment Status':
            if value == 'Salaried':
                df['employment_status_Salaried'] = 1
            elif value == 'Self-Employed':
                df['employment_status_Self-Employed'] = 1
        elif key == 'Insurance Plan':
            df['insurance_plan'] = insurance_plan_encoding.get(value, 1) # Default to Bronze
        elif key == 'Age':
            df['age'] = value
        elif key == 'Number of Dependants':
            df['number_of_dependants'] = value
        elif key == 'Income in Lakhs':
            df['income_lakhs'] = value
        elif key == "Genetical Risk":
            df['genetical_risk'] = value

    # Calculate and assign the normalized risk score
    df['normalized_risk_score'] = calculate_normalized_risk(input_dict['Medical History'])

    # Apply the correct scaling to the numerical features
    df = handle_scaling(input_dict['Age'], df)

    return df

def handle_scaling(age, df):
    """
    Applies the appropriate pre-trained scaler based on the user's age.
    """
    # Select scaler based on age group
    if age <= 25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_rest

    # Get the list of columns to scale and the scaler itself from the loaded object
    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']

    # Apply the scaler transformation to the specified columns
    # This now works because 'income_level' is already in the DataFrame 'df'
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])

    # **FIX:** The temporary 'income_level' column is no longer added and dropped here,
    # as it's now part of the main DataFrame from the start.

    return df

def predict(input_dict):
    """
    Main prediction function that orchestrates preprocessing and model inference.
    """
    # Preprocess the raw input dictionary into a model-ready DataFrame
    input_df = preprocess_input(input_dict)

    # Select the correct model based on age and make a prediction
    if input_dict['Age'] <= 25:
        prediction = model_young.predict(input_df)
    else:
        prediction = model_rest.predict(input_df)

    # Return the final prediction as an integer
    return int(prediction[0])
