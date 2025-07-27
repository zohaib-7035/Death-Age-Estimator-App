

# 📊 Life Expectancy Prediction App

## 📝 Overview

This is a **Streamlit web application** that predicts life expectancy based on **19 health and economic indicators** using a **pre-trained machine learning model** (`a1.sav`). The app provides:

* An interactive form to input indicators
* Health tips based on WHO guidelines
* Analysis of predicted results

---

## 🚀 Features

* **User Input**: Collects 19 health and economic indicators, including **Year (2000–2025)**
* **Health Tips**: Expandable section with WHO-based health tips
* **Model**: Uses a **pre-trained `.sav` model** via `joblib`
* **Prediction Analysis**: Feedback based on predicted life expectancy:

  * Low: < 60 years
  * Moderate: 60–75 years
  * High: > 75 years
* **Output**: Predicted life expectancy displayed in years

---

## 📦 Requirements

* **Python 3.7+**
* `streamlit` → `pip install streamlit`
* `joblib` → `pip install joblib`
* `numpy` → `pip install numpy`
* A pre-trained model file named **`a1.sav`** (must be in the same directory)

---

## ⚙️ Installation

1. **Clone/download** this repository to your local machine.

2. **Install required packages**:

   ```bash
   pip install streamlit joblib numpy
   ```

3. Ensure `a1.sav` (the trained model) is in the **same directory** as `app.py`.

---

## ▶️ Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open the URL (e.g., `http://localhost:8501`) in your browser.

3. Expand the **"Health Tips Based on WHO Guidelines"** section.

4. **Enter values** for the following 19 features:

| Feature                             | Description                                  |
| ----------------------------------- | -------------------------------------------- |
| **Year**                            | Between 2000–2025                            |
| **Adult Mortality**                 | Probability of dying (age 15–60) per 1000    |
| **Infant Deaths**                   | Infant deaths per 1000 live births           |
| **Alcohol Consumption**             | Liters per capita                            |
| **Percentage Expenditure**          | Health expenditure as % of GDP               |
| **Hepatitis B (%)**                 | Immunization coverage (%)                    |
| **Measles**                         | Measles cases per 1000                       |
| **BMI**                             | Body Mass Index                              |
| **Under-five Deaths**               | Deaths per 1000 children under 5             |
| **Polio (%)**                       | Immunization coverage (%)                    |
| **Total Expenditure**               | Health expenditure as % of government budget |
| **Diphtheria (%)**                  | Immunization coverage (%)                    |
| **HIV/AIDS**                        | Deaths per 1000                              |
| **GDP**                             | Per capita (USD)                             |
| **Population**                      | Total country population                     |
| **Thinness 10–19 years**            | % prevalence                                 |
| **Thinness 5–9 years**              | % prevalence                                 |
| **Income Composition of Resources** | HDI income index (0 to 1)                    |
| **Schooling**                       | Average years of schooling                   |

5. Click **"🔮 Predict Life Expectancy"** to view results and analysis.

---

## 📁 File Structure

```bash
├── app.py           # Streamlit app script
├── a1.sav           # Pre-trained ML model
└── README.md        # This documentation
```

---

## ☁️ Deployment

To deploy the app (e.g., Streamlit Cloud):

1. Upload `app.py` and `a1.sav` to the platform.

2. Create `requirements.txt` with:

   ```txt
   streamlit
   joblib
   numpy
   ```

3. Follow the platform's deployment instructions.

---

## ⚠️ Notes

* `a1.sav` **must** be trained with **19 features**, including **Year**.
* Input values must be **realistic and within range**.
* The **health analysis** is general and not personalized:

  * **< 60 years** → 🚨 Suggests need for better healthcare, education, and nutrition.
  * **60–75 years** → ⚠️ Moderate risks remain.
  * **> 75 years** → ✅ Indicates a healthy environment.

---

## 🚫 Limitations

* Model accuracy depends on the **training dataset quality**.
* No cross-validation of input combinations.
* Model file must exist for the app to run.
* Health tips are **not personalized**.

---

## 🤝 Contributing

Contributions are welcome!
You can:

* Improve input validation
* Add data visualizations
* Support multiple model versions or add feature selection

Fork the repo → Create a branch → Submit a pull request!

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 📬 Contact

For questions or support, contact the developer or visit the [Streamlit Community](https://discuss.streamlit.io/) forums.

---

