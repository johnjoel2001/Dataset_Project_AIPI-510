import pandas as pd
from scipy.stats import f_oneway

def load_dataset(file_path):
    """
    Load the dataset from an Excel file 

    Args:
        file_path (str): Path to the Excel file.

    Returns:
        pd.DataFrame: Loaded dataset with the Date column in datetime format.
    """
    data = pd.read_excel(file_path)
    data["Date"] = pd.to_datetime(data["Date"])
    return data

def perform_anova(column1, column2):
    """
    Perform a one-way ANOVA test between two columns.

    Args:
        column1 (pd.Series): First column for comparison.
        column2 (pd.Series): Second column for comparison.

    Returns:
        tuple: F-statistic and p-value from the ANOVA test.
    """
    result = f_oneway(column1.dropna(), column2.dropna())
    return result.statistic, result.pvalue

def display_anova_results(name, f_stat, p_value):
    """
    Display the results of the ANOVA test in a formatted manner.

    Args:
        name (str): Name of the comparison (e.g., "Orders").
        f_stat (float): F-statistic from the ANOVA test.
        p_value (float): p-value from the ANOVA test.
    """
    print(f"{name} ANOVA Results:")
    print(f"F-Statistic: {f_stat:.4f}")
    print(f"p-value: {p_value:.4f}\n")

# Main Script
if __name__ == "__main__":
    # Load the dataset
    file_path = 'Datset_Gloves.xlsx'  # Path to the dataset
    data = load_dataset(file_path)

    # Perform ANOVA for Orders (Grey vs Blue)
    f_stat_orders, p_value_orders = perform_anova(data["Gloves Ordered (Grey)"], data["Gloves Ordered (Blue)"])
    display_anova_results("Orders", f_stat_orders, p_value_orders)

    # Perform ANOVA for Production Efficiency (Grey vs Blue)
    f_stat_production, p_value_production = perform_anova(data["Production Efficiency (Grey)"], data["Production Efficiency (Blue)"])
    display_anova_results("Production Efficiency", f_stat_production, p_value_production)

    # Perform ANOVA for Dispatch Efficiency (Grey vs Blue)
    f_stat_dispatch, p_value_dispatch = perform_anova(data["Dispatch Efficiency (Grey)"], data["Dispatch Efficiency (Blue)"])
    display_anova_results("Dispatch Efficiency", f_stat_dispatch, p_value_dispatch)



