
# Health Insurance Cost Predictor

Health Insurance Cost Predictor is a Streamlit-based web application that estimates health insurance costs based on user-provided personal and health-related factors. The app uses interactive forms and visualizations (with Plotly) to help users understand the impact of various factors on their insurance premium and provides recommendations for risk mitigation.


## 🔹 Live Demo
[Click here to access the app](https://healthcare-premium-prediction-lekhraj.streamlit.app/)
## ✨ Features


- **Interactive User Input Form** 📋  
  Users can enter personal and health-related details such as age, income, BMI, smoking status, and medical history. The form is designed for ease of use with dropdowns and number inputs.

- **Real-time Insurance Cost Prediction** 💰  
  Instantly predicts health insurance costs based on user inputs using a trained algorithm.

- **Risk Factor Analysis & Recommendations** 🔎  
  - Identifies key risk factors affecting your insurance costs.  
  - Provides actionable recommendations to help reduce premiums.  

- **Visual Insights with Interactive Charts** 📊  
  - Displays risk impact analysis with bar charts and line graphs.  
  - Users can explore different factors contributing to cost variations.  

- **Insurance Cost Simulation** 🎛️  
  - Simulate insurance cost changes by adjusting the age slider.  
  - See how different age groups affect predicted premiums.  

- **Dark Theme & Modern UI** 🌙  
  - Clean and minimal dark-themed interface for a smooth experience.  
  - Uses custom CSS to enhance the visual appeal.  

- **Fast & Lightweight Web App** 🚀  
  - Runs on **Streamlit**, ensuring fast performance.  
  - No additional backend setup required – works directly in the browser.  

## 🛠️ Technologies Used

| Technology  | Purpose  |
|------------|---------|
| **Python** 🐍  | Core programming language  |
| **Streamlit** 🎨 | Web framework for interactive UI  |
| **Pandas** 🗂️ | Data processing and manipulation  |
| **Plotly** 📊 | Interactive data visualizations  |
| **NumPy** 🔢 | Numerical computations  |
| **Custom CSS** 🎨 | Enhances UI with a dark theme  |
| **prediction_helper.py** 🤖 | Insurance cost prediction logic  |

Here’s how you can integrate the **Prerequisites & Version Requirements** section into your README with the specific dependencies:


### 🔹 Prerequisites & Version Requirements
Before you begin, ensure you have the following installed:

| Dependency      | Required Version |
|----------------|-----------------|
| Python         | 3.7+             |
| pip           | Latest            |
| joblib        | 1.4.2             |
| pandas        | 2.2.3             |
| streamlit     | 1.42.0            |
| numpy         | 2.2.2             |
| scikit-learn  | 1.5.0             |
| xgboost       | 2.1.3             |
| plotly        | 6.0.0             |


## 📥 Installation Guide

This section provides step-by-step instructions on how users can install and run your project on their local machines.

---

```markdown
## 📥 Installation Guide  

Follow these steps to set up and run the **Health Insurance Cost Predictor** on your local machine.

### **Prerequisites**  
Before installing, ensure you have the following installed:  
- **Python 3.7+** 🐍  
- **pip (Python package manager)** 🛠️  

### **Step 1: Clone the Repository**  
First, download the project files by cloning the GitHub repository:  

```bash
git clone https://github.com/yourusername/health-insurance-cost-predictor.git
cd health-insurance-cost-predictor
```

---

### **Step 2: Create and Activate a Virtual Environment (Recommended)**
It's good practice to create a virtual environment before installing dependencies.  

#### **For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### **For Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

---

### **Step 3: Install Dependencies**  
Run the following command to install all required libraries:  

```bash
pip install -r requirements.txt
```

---

### **Step 4: Run the Application**
Start the Streamlit app by running:

```bash
streamlit run app.py
```

Once the server starts, you will see a link similar to:

```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
```

Click the link or open your browser and go to `http://localhost:8501` to use the application.

---

### **Step 5: Optional - Deactivate Virtual Environment**  
Once you're done using the app, you can deactivate the virtual environment:

```bash
deactivate
```

---

### **📌 Notes**  
- Ensure all dependencies are installed using `pip install -r requirements.txt`.  
- If you encounter issues with missing dependencies, try upgrading `pip` first:  
  ```bash
  pip install --upgrade pip
  ```
- If you wish to customize the CSS theme, modify the styles in `app.py`.

---
## 📊 Usage Instructions
### **📊 Usage Instructions**  

This section explains how to use your **Health Insurance Cost Predictor** after installation.

---

```markdown
## 📊 Usage Instructions  

Once you have installed all dependencies and launched the application using:

```bash
streamlit run app.py
```

follow these steps to use the application effectively:

---

### **Step 1: Open the Web Interface**  
After running the command, Streamlit will generate a local link such as:

```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
```

Click on the **Local URL** or open your web browser and navigate to **`http://localhost:8501`**.

---

### **Step 2: Fill in the Input Form (📝 Input Form Tab)**  
- Enter your **personal details** such as **age, income, dependents, employment status**.  
- Select **health-related factors** like **BMI category, smoking status, and medical history**.  
- Choose an **insurance plan** and **region**.  

🟢 **Tip:** Hover over any field to see additional guidance!

---

### **Step 3: View Risk Factors Summary**  
- The **Risk Summary Panel** on the right will analyze your inputs and display **potential risk factors**.  
- It highlights **high-risk factors** (e.g., smoking, obesity, or genetic predisposition).  
- If you have no major risks, a **"No major risk factors identified"** message appears.  

---

### **Step 4: Get Your Insurance Cost Prediction**  
- Click the **"Calculate Insurance Cost"** button.  
- The application will **process your inputs** and display the **predicted insurance cost** in **INR (₹)**.  
- Based on risk factors, the app will provide **personalized recommendations** to help you reduce costs.

---

### **Step 5: Explore the Risk Analysis Dashboard (📊 Risk Analysis Tab)**  
- Check **interactive bar charts** showing how different factors influence insurance costs.  
- Identify which elements contribute the most to premium calculations.

🟢 **Tip:** Hover over chart elements for detailed insights.

---

### **Step 6: Run Insurance Cost Simulations (📉 Simulation Tool)**  
- Use the **age slider** to see how insurance costs change based on different ages.  
- Run the simulation to explore **trends over time**.  
- Understand which age groups have **higher/lower premiums**.

---

### **Step 7: Learn More (ℹ️ Help Tab)**  
- Go to the **Help tab** for a quick tutorial on how to use the predictor.  
- Read **important notes** about predictions and data accuracy.  

---

### **🎯 Summary of Features You Can Use**
✅ **Fill out your details** → 📋 **View risk summary** → 📈 **Get a cost prediction**  
✅ **Check risk analysis** → 🏆 **Explore simulations** → ℹ️ **Read helpful tips**  

---


## 📈 Risk Analysis & Simulation  

The **Health Insurance Cost Predictor** includes a powerful **Risk Analysis Dashboard** and a **Simulation Tool** to help users understand how different factors impact insurance costs.

---

### **📊 Risk Analysis Dashboard**  
The **Risk Analysis** tab provides an **interactive data visualization** to show how various factors influence your insurance premium.  

🔹 **How to Use the Dashboard:**  
1. Navigate to the **📊 Risk Analysis** tab.  
2. View the **bar chart** that displays the relative impact of different risk factors such as **age, BMI, smoking, medical history, and genetic risk**.  
3. Hover over the bars to see detailed impact percentages.  
4. Identify which factors **contribute the most** to insurance cost increases.  

🔹 **Example Insights You Can Gain:**  
- **Smoking** may have a **higher impact** on premiums than BMI.  
- **Genetic Risk** could be a **moderate factor** but less significant than **age**.  
- **Having multiple medical conditions** may significantly raise insurance costs.  

🟢 **Tip:** Use these insights to adjust your lifestyle choices and potentially lower your premium.

---

### **🎛️ Insurance Cost Simulation**  
The **Simulation Tool** lets users **adjust their age** to see how predicted insurance costs change over time.

🔹 **How to Use the Simulation Tool:**  
1. Navigate to the **📊 Risk Analysis** tab.  
2. Scroll down to the **Simulation Tool** section.  
3. Use the **slider** to select a range of ages (e.g., 25-60).  
4. Click **"Run Simulation"** to generate a dynamic **line graph** showing insurance cost trends across the selected ages.  

🔹 **What You Can Learn:**  
✅ How insurance costs **increase with age** 📈  
✅ At what age insurance **becomes significantly more expensive**  
✅ The best time to **purchase health insurance** based on cost trends  

🟢 **Tip:** The simulation helps users make informed decisions about **when to buy or upgrade their insurance policy**.

---

### **📉 Example Simulation Output**  
If a user runs a simulation for ages **25 to 60**, they might see:

| Age  | Predicted Insurance Cost (₹) |
|------|-----------------------------|
| 25   | ₹10,500  |
| 30   | ₹12,200  |
| 35   | ₹15,300  |
| 40   | ₹18,900  |
| 45   | ₹23,500  |
| 50   | ₹28,800  |
| 55   | ₹35,200  |
| 60   | ₹42,000  |

📌 **Observation:**  
The cost gradually rises, but there is a significant jump **after 40 years**.  
Buying insurance **early** may help lock in lower rates!

---

### **🎯 Summary**
✅ **Check the Risk Analysis Dashboard** to identify high-impact factors.  
✅ **Use the Simulation Tool** to see how insurance costs change over time.  
✅ **Make data-driven decisions** on when to buy insurance.  

---


### **🤝 Contribution Guidelines**  

This section explains how others can contribute to your project and ensures they follow proper contribution etiquette.

---

```markdown
## 🤝 Contribution Guidelines  

We welcome contributions to improve the **Health Insurance Cost Predictor**! Whether it's fixing bugs, adding new features, or improving documentation, your help is greatly appreciated.  

---

### **📜 License Information**  
This project is licensed under the **Apache-2.0 License**. By contributing, you agree that your code will be distributed under this license.  
See the full license in the [LICENSE](LICENSE) file.

---

### **📌 How to Contribute**  

Follow these steps to contribute to the project:

1. **Fork the Repository**  
   - Click the "Fork" button on the top right of this repository.  
   - This creates a copy of the project under your GitHub account.  

2. **Clone Your Forked Repository**  
   Run the following command to download the code to your local machine:

   ```bash
   git clone https://github.com/yourusername/health-insurance-cost-predictor.git
   cd health-insurance-cost-predictor
   ```

3. **Create a New Branch**  
   Always create a separate branch for your contributions:  

   ```bash
   git checkout -b feature-name
   ```

4. **Make Your Changes & Commit**  
   - Edit the code, fix bugs, or add new features.  
   - After making changes, stage and commit them:  

   ```bash
   git add .
   git commit -m "Added feature: [describe your change]"
   ```

5. **Push Changes to GitHub**  
   Upload your changes to your forked repository:

   ```bash
   git push origin feature-name
   ```

6. **Create a Pull Request (PR)**  
   - Go to the original repository on GitHub.  
   - Click **"New Pull Request"** and select your branch.  
   - Describe the changes and submit your PR for review.  

---

### **✅ Contribution Rules**  
🔹 Ensure your code follows **PEP8 standards** for Python formatting.  
🔹 Use **meaningful commit messages** describing your changes.  
🔹 Test your changes before submitting a pull request.  
🔹 If adding a new feature, **update the README** if necessary.  
🔹 Be respectful and collaborate positively in discussions.  

---

### **💡 Need Help?**  
If you need help with your contributions, feel free to:  
- Open an **issue** describing your problem or feature request.  
- Ask questions in the **Discussions** section of this repository.  

---

### **🚀 Thank You for Contributing! 🎉**  
Your contributions make this project better for everyone. We appreciate your support!  
```

---
