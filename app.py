import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('a1.sav')  # Trained with 19 features

st.set_page_config(page_title="Life Expectancy Predictor", layout="centered")
st.title("🧬 Life Expectancy Prediction App")
st.write("Please enter the following health and economic indicators:")

# Option 1️⃣: Information Section
with st.expander("📘 Health Tips Based on WHO Guidelines"):
    st.markdown("""
    - 💧 Drink plenty of water (2–3 liters/day)
    - 🏃 Exercise at least 30 minutes daily
    - 🚭 Avoid smoking and excessive alcohol
    - 🥗 Eat a balanced diet: fruits, vegetables, protein, and whole grains
    - 💉 Stay up to date with vaccines (Hepatitis B, Polio, Diphtheria)
    - 🧘 Manage stress and maintain good mental health
    """)

# Input features
year = st.number_input("Year", min_value=2000, max_value=2025, value=2023)  # ✅ Add this missing feature
adult_mortality = st.number_input("Adult Mortality", min_value=0.0)
infant_deaths = st.number_input("Infant Deaths", min_value=0.0)
alcohol = st.number_input("Alcohol Consumption", min_value=0.0)
percentage_expenditure = st.number_input("Percentage Expenditure", min_value=0.0)
hepatitis_b = st.number_input("Hepatitis B (%)", min_value=0.0, max_value=100.0)
measles = st.number_input("Measles", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)
under_five_deaths = st.number_input("Under-five Deaths", min_value=0.0)
polio = st.number_input("Polio (%)", min_value=0.0, max_value=100.0)
total_expenditure = st.number_input("Total Expenditure", min_value=0.0)
diphtheria = st.number_input("Diphtheria (%)", min_value=0.0, max_value=100.0)
hiv_aids = st.number_input("HIV/AIDS", min_value=0.0)
gdp = st.number_input("GDP", min_value=0.0)
population = st.number_input("Population", min_value=0.0)
thinness_10_19 = st.number_input("Thinness 10–19 years", min_value=0.0)
thinness_5_9 = st.number_input("Thinness 5–9 years", min_value=0.0)
income_composition = st.number_input("Income Composition of Resources", min_value=0.0, max_value=1.0)
schooling = st.number_input("Schooling (years)", min_value=0.0)

# Prepare input (🛠️ Fixed to match model’s 19 features)
input_features = np.array([[year, adult_mortality, infant_deaths, alcohol, percentage_expenditure,
                            hepatitis_b, measles, bmi, under_five_deaths, polio, total_expenditure,
                            diphtheria, hiv_aids, gdp, population, thinness_10_19, thinness_5_9,
                            income_composition, schooling]])

# Prediction
if st.button("🔮 Predict Life Expectancy"):
    prediction = model.predict(input_features)
    st.success(f"🧓 Predicted Life Expectancy: {prediction[0]:.2f} years")

    # Option 4️⃣: Simple Analysis
    with st.expander("📊 Analysis Based on Prediction"):
        if prediction[0] < 60:
            st.warning("⚠️ Life expectancy is quite low. Consider improving healthcare access, nutrition, and education.")
        elif prediction[0] < 75:
            st.info("ℹ️ Moderate life expectancy. Some risk factors still exist, such as low vaccination or high mortality.")
        else:
            st.success("✅ Great! The predicted life expectancy indicates a healthy and stable environment.")
