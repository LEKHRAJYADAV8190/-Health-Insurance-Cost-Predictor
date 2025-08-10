import pandas as pd
import joblib

# Load the models and scalers
# It's assumed these .joblib files contain the raw scaler/model objects
model_young = joblib.load("model/model_young1.joblib")
model_rest = joblib.load("model/model_rest.joblib")
scaler_young = joblib.load("model/scaler_young1.joblib")
scaler_rest = joblib.load("model/scaler_rest.joblib")

def calculate_normalized_risk(medical_history):
    """Calculates a normalized risk score based on medical history."""
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }
    # Split the medical history into potential two parts and convert to lowercase
    diseases = medical_history.lower().split(" & ")

    # Calculate the total risk score by summing the risk scores for each part
    total_risk_score = sum(risk_scores.get(disease, 0) for disease in diseases)

    # Max score assumes the two highest non-exclusive conditions
    max_score = 14  # heart disease (8) + diabetes/high blood pressure (6)
    min_score = 0

    # Normalize the total risk score to a 0-1 range
    normalized_risk_score = (total_risk_score - min_score) / (max_score - min_score)

    return normalized_risk_score

def preprocess_input(input_dict):
    """Converts the input dictionary from the frontend into a DataFrame for prediction."""
    # Define the full set of columns the model was trained on
    expected_columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk', 'normalized_risk_score',
        'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
        'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
    ]
    
    # Create a DataFrame initialized with zeros
    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    # --- Populate DataFrame from input_dict ---
    df['age'] = input_dict.get('Age', 0)
    df['number_of_dependants'] = input_dict.get('Number of Dependants', 0)
    df['income_lakhs'] = input_dict.get('Income in Lakhs', 0)
    df['genetical_risk'] = input_dict.get('Genetical Risk', 0)

    # Encode categorical features
    insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}
    df['insurance_plan'] = insurance_plan_encoding.get(input_dict.get('Insurance Plan'), 1)

    if input_dict.get('Gender') == 'Male':
        df['gender_Male'] = 1
    
    region = input_dict.get('Region')
    if region == 'Northwest':
        df['region_Northwest'] = 1
    elif region == 'Southeast':
        df['region_Southeast'] = 1
    elif region == 'Southwest':
        df['region_Southwest'] = 1

    if input_dict.get('Marital Status') == 'Unmarried':
        df['marital_status_Unmarried'] = 1

    bmi_cat = input_dict.get('BMI Category')
    if bmi_cat == 'Obesity':
        df['bmi_category_Obesity'] = 1
    elif bmi_cat == 'Overweight':
        df['bmi_category_Overweight'] = 1
    elif bmi_cat == 'Underweight':
        df['bmi_category_Underweight'] = 1

    smoking = input_dict.get('Smoking Status')
    if smoking == 'Occasional':
        df['smoking_status_Occasional'] = 1
    elif smoking == 'Regular':
        df['smoking_status_Regular'] = 1

    employment = input_dict.get('Employment Status')
    if employment == 'Salaried':
        df['employment_status_Salaried'] = 1
    elif employment == 'Self-Employed':
        df['employment_status_Self-Employed'] = 1

    # Calculate and add the normalized risk score
    df['normalized_risk_score'] = calculate_normalized_risk(input_dict.get('Medical History', 'none'))
    
    # Apply the correct scaling
    df = handle_scaling(input_dict['Age'], df)

    return df

def handle_scaling(age, df):
    """
    Applies the correct scaler to the numerical columns.
    The column names are now defined here directly.
    """
    # Define the columns that need to be scaled. This should match your training script.
    cols_to_scale = ['age', 'income_lakhs'] 
    
    # Choose the correct scaler based on age
    if age <= 25:
        scaler = scaler_young
    else:
        scaler = scaler_rest

    # Apply the scaler to the specified columns
    # The scaler expects a DataFrame, so we pass df[cols_to_scale]
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])

    return df

def predict(input_dict):
    """Performs the final prediction based on the preprocessed input."""
    input_df = preprocess_input(input_dict)

    # Ensure the order of columns matches the model's training data
    # This list should be identical to 'expected_columns' in preprocess_input
    final_columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk', 'normalized_risk_score',
        'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
        'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
    ]
    
    # Reorder DataFrame to be certain
    input_df = input_df[final_columns]

    # Use the appropriate model based on age
    if input_dict['Age'] <= 25:
        prediction = model_young.predict(input_df)
    else:
        prediction = model_rest.predict(input_df)

    return int(prediction[0])
