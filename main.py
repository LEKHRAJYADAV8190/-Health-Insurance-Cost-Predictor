import streamlit as st
import pandas as pd
import plotly.express as px
from prediction_helper import predict


def main():
    # Set page config
    st.set_page_config(
        page_title="Health Insurance Cost Predictor",
        page_icon="🏥",
        layout="wide"
    )

    # Custom CSS for dark theme
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
            background-color: #0E1117;
            color: #FAFAFA;
        }
        .stButton>button {
            width: 100%;
            margin-top: 1rem;
        }
        .info-box {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #1E1E1E;
            margin-bottom: 1rem;
            color: #FAFAFA;
        }
        [data-testid="stHeader"] {
            background-color: #0E1117;
        }
        .css-1d391kg {
            background-color: #1E1E1E;
        }
        .stTabs [data-baseweb="tab-list"] {
            background-color: #1E1E1E;
        }
        .stTabs [data-baseweb="tab"] {
            color: #FAFAFA;
        }
        div[data-testid="stMarkdownContainer"] {
            color: #FAFAFA;
        }
        .st-emotion-cache-j5r0tf {
            background-color: #1E1E1E;
        }
        </style>
    """, unsafe_allow_html=True)

    # Rest of the code remains the same as before
    st.title('🏥 Health Insurance Cost Predictor')
    st.markdown("""
        <div class="info-box">
        This application helps predict health insurance costs based on various personal and health-related factors.
        Please fill in all the fields below to get an accurate prediction.
        </div>
    """, unsafe_allow_html=True)

    # Define options for categorical variables
    categorical_options = {
        'Gender': ['Male', 'Female'],
        'Marital Status': ['Unmarried', 'Married'],
        'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
        'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
        'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
        'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
        'Medical History': [
            'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
            'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
            'Diabetes & Heart disease'
        ],
        'Insurance Plan': ['Bronze', 'Silver', 'Gold']
    }

    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["📝 Input Form", "📊 Risk Analysis", "ℹ️ Help"])

    with tab1:
        # Create columns for form layout
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("Personal Information")

            # Create four rows of three columns each
            row1 = st.columns(3)
            row2 = st.columns(3)
            row3 = st.columns(3)
            row4 = st.columns(3)

            # First row inputs
            with row1[0]:
                age = st.number_input('Age',
                                      min_value=18,
                                      max_value=100,
                                      step=1,
                                      help="Enter age between 18 and 100")
            with row1[1]:
                number_of_dependants = st.number_input('Number of Dependants',
                                                       min_value=0,
                                                       max_value=20,
                                                       step=1)
            with row1[2]:
                income_lakhs = st.number_input('Income in Lakhs',
                                               min_value=0,
                                               max_value=200,
                                               step=1)

            # Second row inputs
            with row2[0]:
                genetical_risk = st.number_input('Genetical Risk',
                                                 min_value=0,
                                                 max_value=5,
                                                 step=1,
                                                 help="Scale of 0-5, where 5 indicates highest risk")
            with row2[1]:
                insurance_plan = st.selectbox('Insurance Plan',
                                              categorical_options['Insurance Plan'],
                                              help="Select your preferred insurance plan")
            with row2[2]:
                employment_status = st.selectbox('Employment Status',
                                                 categorical_options['Employment Status'])

            # Third row inputs
            with row3[0]:
                gender = st.selectbox('Gender',
                                      categorical_options['Gender'])
            with row3[1]:
                marital_status = st.selectbox('Marital Status',
                                              categorical_options['Marital Status'])
            with row3[2]:
                bmi_category = st.selectbox('BMI Category',
                                            categorical_options['BMI Category'],
                                            help="Select your BMI category")

            # Fourth row inputs
            with row4[0]:
                smoking_status = st.selectbox('Smoking Status',
                                              categorical_options['Smoking Status'])
            with row4[1]:
                region = st.selectbox('Region',
                                      categorical_options['Region'])
            with row4[2]:
                medical_history = st.selectbox('Medical History',
                                               categorical_options['Medical History'])

        with col2:
            st.subheader("Risk Factors Summary")

            # Calculate risk score
            risk_factors = []
            if smoking_status != 'No Smoking':
                risk_factors.append('Smoking')
            if genetical_risk > 3:
                risk_factors.append('High Genetic Risk')
            if bmi_category in ['Obesity', 'Underweight']:
                risk_factors.append('BMI Risk')
            if medical_history != 'No Disease':
                risk_factors.append('Medical History')

            # Display risk factors
            st.warning(f"Number of Risk Factors: {len(risk_factors)}")
            if risk_factors:
                st.markdown("**Identified Risk Factors:**")
                for factor in risk_factors:
                    st.markdown(f"- {factor}")
            else:
                st.success("No major risk factors identified")

        # Create input dictionary
        input_dict = {
            'Age': age,
            'Number of Dependants': number_of_dependants,
            'Income in Lakhs': income_lakhs,
            'Genetical Risk': genetical_risk,
            'Insurance Plan': insurance_plan,
            'Employment Status': employment_status,
            'Gender': gender,
            'Marital Status': marital_status,
            'BMI Category': bmi_category,
            'Smoking Status': smoking_status,
            'Region': region,
            'Medical History': medical_history
        }

        # Prediction button
        if st.button('Calculate Insurance Cost'):
            with st.spinner('Calculating...'):
                prediction = predict(input_dict)
                st.success(f'Predicted Health Insurance Cost: ₹{prediction:,.2f}')

                # Show recommendation based on prediction
                st.subheader("Recommendations")
                recommendations = []
                if smoking_status != 'No Smoking':
                    recommendations.append("Consider quitting smoking to potentially reduce your insurance costs.")
                if bmi_category in ['Obesity', 'Underweight']:
                    recommendations.append("Working towards a normal BMI range could help lower your insurance costs.")
                if len(recommendations) > 0:
                    for rec in recommendations:
                        st.info(rec)

    with tab2:
        st.subheader("Risk Analysis Dashboard")

        # Sample data for visualization
        risk_data = pd.DataFrame({
            'Factor': ['Age', 'BMI', 'Smoking', 'Medical History', 'Genetic Risk'],
            'Impact': [0.3, 0.25, 0.2, 0.15, 0.1]
        })

        # Create impact visualization with dark theme
        fig = px.bar(risk_data,
                     x='Factor',
                     y='Impact',
                     title='Relative Impact of Different Factors on Insurance Cost',
                     color='Impact',
                     template="plotly_dark")  # Using dark template for the plot
        st.plotly_chart(fig)

    with tab3:
        st.subheader("How to Use This Predictor")
        st.markdown("""
        1. **Fill in all fields** in the Input Form tab
        2. **Review the Risk Factors Summary** on the right side
        3. **Click 'Calculate Insurance Cost'** to get your prediction
        4. **Check the Risk Analysis** tab for more insights

        **Important Notes:**
        - All fields are required for accurate prediction
        - The prediction is an estimate based on historical data
        - Actual insurance costs may vary
        """)


if __name__ == "__main__":
    main()