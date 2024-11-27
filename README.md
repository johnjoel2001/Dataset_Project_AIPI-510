# Steps to run the repository

### 1. Set Up a Virtual Environment
To avoid dependency conflicts, create a virtual environment:
```bash
# Create a virtual environment
python -m venv glove_env

# Activate the virtual environment

# On Windows:
glove_env\Scripts\activate

```
### 2. Install Dependencies
Install the required libraries using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Place the Dataset
Ensure the dataset file (`Datset_Gloves.xlsx`) is in the same directory as the script.

---

## 4. Run the Script

### Step 1: Run the Python Script
Execute the script using the following command:
```bash
python eda.py
python power_analysis_result.py
```
### Step 2: View Results
- The scripts will display:
  - **Visualizations**: Trends, efficiencies, and correlations.
  - **Outliers**: Identified for dispatch efficiency.
  - **Unit Tests**: Validation of the dataset structure.
  - **Power Analysis Results**: Statistical Analysis
- Printed outputs will summarize the outlier data and statistical analysis.
