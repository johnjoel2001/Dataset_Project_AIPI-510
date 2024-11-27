import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import unittest

# Load the dataset
file_path = 'Datset_Gloves.xlsx'  # Path to the dataset
data = pd.read_excel(file_path)

# Ensuring that the Date column is in datetime format
data["Date"] = pd.to_datetime(data["Date"])


# Unit testing class
class TestDataset(unittest.TestCase):

    def test_columns_exist(self):
        """Test that all necessary columns exist in the dataset."""
        expected_columns = [
            "Date", "Gloves Ordered (Grey)", "Gloves Ordered (Blue)",
            "Gloves Produced (Grey)", "Gloves Produced (Blue)",
            "Gloves Delivered (Grey)", "Gloves Delivered (Blue)",
            "Dispatch Efficiency (Grey)", "Dispatch Efficiency (Blue)",
            "Production Efficiency (Grey)", "Production Efficiency (Blue)"
        ]
        for col in expected_columns:
            self.assertIn(col, data.columns, f"Column '{col}' is missing!")


# Visualization code

# 1. Daily Orders Trend
"""
This plot shows the daily trend of orders received for grey and blue gloves.
It highlights how demand varies over time for each type of glove.
"""
plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data["Gloves Ordered (Grey)"], label='Grey Gloves Ordered', marker='o', linestyle='-', alpha=0.7)
plt.plot(data["Date"], data["Gloves Ordered (Blue)"], label='Blue Gloves Ordered', marker='x', linestyle='--', alpha=0.7)
plt.title('Daily Orders Trend')
plt.xlabel('Date')
plt.ylabel('Number of Gloves Ordered')
plt.legend()
plt.grid(alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Daily Production Trend
"""
This plot shows the daily production levels of grey and blue gloves.
It helps to identify consistency or variability in glove production.
"""
plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data["Gloves Produced (Grey)"], label='Grey Gloves Produced', marker='o', linestyle='-', alpha=0.7)
plt.plot(data["Date"], data["Gloves Produced (Blue)"], label='Blue Gloves Produced', marker='x', linestyle='--', alpha=0.7)
plt.title('Daily Production Trend')
plt.xlabel('Date')
plt.ylabel('Number of Gloves Produced')
plt.legend()
plt.grid(alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Daily Delivered Gloves Trend
"""
This plot tracks the daily deliveries of grey and blue gloves.
It helps analyze delivery patterns and any potential inconsistencies.
"""
plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data["Gloves Delivered (Grey)"], label='Grey Gloves Delivered', marker='o', linestyle='-', alpha=0.7)
plt.plot(data["Date"], data["Gloves Delivered (Blue)"], label='Blue Gloves Delivered', marker='x', linestyle='--', alpha=0.7)
plt.title('Daily Delivered Gloves Trend')
plt.xlabel('Date')
plt.ylabel('Number of Gloves Delivered')
plt.legend()
plt.grid(alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Scatterplot for Dispatch Efficiency
"""
This scatterplot compares dispatch efficiency between grey and blue gloves.
It helps identify patterns or relationships between the two efficiencies.
"""
plt.figure(figsize=(10, 6))
plt.scatter(data["Dispatch Efficiency (Grey)"], data["Dispatch Efficiency (Blue)"], alpha=0.7, color='purple')
plt.title('Dispatch Efficiency: Grey vs. Blue')
plt.xlabel('Dispatch Efficiency (Grey) (%)')
plt.ylabel('Dispatch Efficiency (Blue) (%)')
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

# 5. Scatterplot for Production Efficiency
"""
This scatterplot compares production efficiency between grey and blue gloves.
It visualizes operational differences or correlations in production processes.
"""
plt.figure(figsize=(10, 6))
plt.scatter(data["Production Efficiency (Grey)"], data["Production Efficiency (Blue)"], alpha=0.7, color='purple')
plt.title('Production Efficiency: Grey vs. Blue Gloves')
plt.xlabel('Production Efficiency (Grey) (%)')
plt.ylabel('Production Efficiency (Blue) (%)')
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

# 6. Correlation Analysis
"""
This heatmap shows correlations between key variables, such as orders, production, and deliveries.
It helps identify relationships between these metrics for grey and blue gloves.
"""
correlation_matrix = data[["Gloves Ordered (Grey)", "Gloves Ordered (Blue)",
                           "Gloves Produced (Grey)", "Gloves Produced (Blue)",
                           "Gloves Delivered (Grey)", "Gloves Delivered (Blue)"]].corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Between Key Variables')
plt.show()

# 7. Monthly Trends: Aggregate Data
"""
This plot visualizes monthly averages for orders and dispatch efficiency.
It highlights seasonal trends or consistent differences between grey and blue gloves.
"""
data['Month'] = data['Date'].dt.to_period('M')
monthly_summary = data.groupby('Month').mean()

# Monthly Average Orders
plt.figure(figsize=(12, 6))
monthly_summary[['Gloves Ordered (Grey)', 'Gloves Ordered (Blue)']].plot(marker='o')
plt.title('Monthly Average Orders')
plt.ylabel('Average Number of Gloves')
plt.xlabel('Month')
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

# Monthly Average Dispatch Efficiency
plt.figure(figsize=(12, 6))
monthly_summary[['Dispatch Efficiency (Grey)', 'Dispatch Efficiency (Blue)']].plot(marker='x')
plt.title('Monthly Average Dispatch Efficiency')
plt.ylabel('Efficiency (%)')
plt.xlabel('Month')
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

# 8. Outlier Detection for Dispatch Efficiency
"""
Identifies and prints outliers in dispatch efficiency for grey and blue gloves.
Outliers are determined based on 2 standard deviations above the mean.
"""
grey_dispatch_threshold = data["Dispatch Efficiency (Grey)"].mean() + 2 * data["Dispatch Efficiency (Grey)"].std()
blue_dispatch_threshold = data["Dispatch Efficiency (Blue)"].mean() + 2 * data["Dispatch Efficiency (Blue)"].std()

grey_outliers = data[data["Dispatch Efficiency (Grey)"] > grey_dispatch_threshold]
blue_outliers = data[data["Dispatch Efficiency (Blue)"] > blue_dispatch_threshold]

print("Grey Dispatch Efficiency Outliers:")
print(grey_outliers[["Date", "Dispatch Efficiency (Grey)"]])

print("\nBlue Dispatch Efficiency Outliers:")
print(blue_outliers[["Date", "Dispatch Efficiency (Blue)"]])

# 9. Delivery Gap Analysis
"""
This plot visualizes the difference between gloves ordered and delivered for both grey and blue gloves.
It helps identify supply chain issues or fulfillment delays.
"""
data['Delivery Gap (Grey)'] = data['Gloves Ordered (Grey)'] - data['Gloves Delivered (Grey)']
data['Delivery Gap (Blue)'] = data['Gloves Ordered (Blue)'] - data['Gloves Delivered (Blue)']

plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data["Delivery Gap (Grey)"], label='Grey Gloves Gap', marker='o', linestyle='-', alpha=0.7)
plt.plot(data["Date"], data["Delivery Gap (Blue)"], label='Blue Gloves Gap', marker='x', linestyle='--', alpha=0.7)
plt.axhline(0, color='red', linestyle='--', label='No Gap')
plt.title('Delivery Gap Over Time')
plt.xlabel('Date')
plt.ylabel('Delivery Gap (Ordered - Delivered)')
plt.legend()
plt.grid(alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 10. Comparison of Dispatch and Production Efficiencies
"""
This scatterplot compares dispatch efficiency and production efficiency for both grey and blue gloves.
It visualizes their relationship and helps identify areas for operational improvement.
"""
plt.figure(figsize=(12, 6))
plt.scatter(data["Dispatch Efficiency (Grey)"], data["Production Efficiency (Grey)"], alpha=0.7, label="Grey Gloves", color='gray')
plt.scatter(data["Dispatch Efficiency (Blue)"], data["Production Efficiency (Blue)"], alpha=0.7, label="Blue Gloves", color='blue')
plt.title('Dispatch Efficiency vs Production Efficiency')
plt.xlabel('Dispatch Efficiency (%)')
plt.ylabel('Production Efficiency (%)')
plt.legend()
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

# 11. Distribution of Dispatch Efficiency
"""
This plot visualizes the distribution of dispatch efficiency for grey and blue gloves.
It helps understand the range and frequency of efficiency values, highlighting any patterns or anomalies.
"""
plt.figure(figsize=(12, 6))
sns.histplot(data["Dispatch Efficiency (Grey)"], kde=True, color='black', label="Grey Dispatch Efficiency", bins=20, alpha=0.7)
sns.histplot(data["Dispatch Efficiency (Blue)"], kde=True, color='blue', label="Blue Dispatch Efficiency", bins=20, alpha=0.6)
plt.title('Distribution of Dispatch Efficiency')
plt.xlabel('Dispatch Efficiency (%)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

# 12. Distribution of Production Efficiency
"""
This plot visualizes the distribution of production efficiency for grey and blue gloves.
It highlights the efficiency levels and identifies trends or outliers in production processes.
"""
plt.figure(figsize=(12, 6))
sns.histplot(data["Production Efficiency (Grey)"], kde=True, color='green', label="Grey Production Efficiency", bins=20, alpha=0.6)
sns.histplot(data["Production Efficiency (Blue)"], kde=True, color='orange', label="Blue Production Efficiency", bins=20, alpha=0.6)
plt.title('Distribution of Production Efficiency')
plt.xlabel('Production Efficiency (%)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

# 13. Comparison of Dispatch and Production Efficiencies
"""
This scatterplot compares dispatch efficiency and production efficiency for grey and blue gloves.
It shows the relationship between these two metrics, helping identify correlations or areas for improvement.
"""
plt.figure(figsize=(12, 6))
plt.scatter(data["Dispatch Efficiency (Grey)"], data["Production Efficiency (Grey)"], alpha=0.7, label="Grey Gloves", color='gray')
plt.scatter(data["Dispatch Efficiency (Blue)"], data["Production Efficiency (Blue)"], alpha=0.7, label="Blue Gloves", color='blue')
plt.title('Dispatch Efficiency vs Production Efficiency')
plt.xlabel('Dispatch Efficiency (%)')
plt.ylabel('Production Efficiency (%)')
plt.legend()
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

# Run the unit tests
if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestDataset))

