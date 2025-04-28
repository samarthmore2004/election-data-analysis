import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load the dataset
file = pd.read_csv("ElectionData.csv")

# Basic Info
print("\n▶ First 5 Rows:")
print(file.head())

print("\n▶ Last 5 Rows:")
print(file.tail())

print("\n▶ Shape of Data:")
print(file.shape)

print("\n▶ Column Names:")
print(file.columns.tolist())  # Debugging support

print("\n▶ Dataset Info:")
print(file.info())

print("\n▶ Statistical Summary:")
print(file.describe())

print("\n▶ Missing Values:")
print(file.isnull().sum())

# Drop missing values
file = file.dropna()

print("\n▶ Missing Values After Drop:")
print(file.isnull().sum())

# Drop duplicates
file = file.drop_duplicates()
print("\n▶ Data After Dropping Duplicates:")
print(file.head())

# Mean, Median, Mode
print("\n▶ Mean Values:")
print(file[['Men', 'Women', 'Third Gender', 'Total']].mean())

print("\n▶ Median Values:")
print(file[['Men', 'Women', 'Third Gender', 'Total']].median())

print("\n▶ Mode Values:")
print(file[['Men', 'Women', 'Third Gender', 'Total']].mode().iloc[0])

# ---------------------------- #
# 📊 Data Visualizations
# ---------------------------- #

# 1. Bar Graph - Total voters by State/UT
plt.figure(figsize=(14, 6))
sns.barplot(x='State/UT & Code', y='Total', data=file.sort_values('Total', ascending=False))
plt.xticks(rotation=90)
plt.title("Total Voters by State/UT")
plt.xlabel("State/UT")
plt.ylabel("Total Voters")
plt.tight_layout()
plt.show()

# 2. Scatter Plot - Men vs Women
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Men', y='Women', data=file)
plt.title("Scatter Plot of Men vs Women Voters")
plt.xlabel("Men")
plt.ylabel("Women")
plt.tight_layout()
plt.show()

# 3. Heatmap - Correlation Matrix
plt.figure(figsize=(8, 6))
corr = file[['Men', 'Women', 'Third Gender', 'Total']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Heatmap of Correlation")
plt.tight_layout()
plt.show()

# 4. Boxplot - Distribution of Voters by Category
plt.figure(figsize=(10, 6))
sns.boxplot(data=file[['Men', 'Women', 'Third Gender', 'Total']])
plt.title("Boxplot of Voter Distribution")
plt.tight_layout()
plt.show()

# 5. Pie Chart - Gender Distribution (Summed over all States)
gender_totals = file[['Men', 'Women', 'Third Gender']].sum()
plt.figure(figsize=(7, 7))
plt.pie(gender_totals, labels=gender_totals.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Overall Gender Distribution")
plt.tight_layout()
plt.show()

# ---------------------------- #
# 📊 T-Test Between Men and Women Voter Counts
# ---------------------------- #
print("\n▶ T-Test Between Men and Women Voter Counts:")
t_stat, p_val = ttest_ind(file['Men'], file['Women'])
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_val:.4f}")

if p_val < 0.05:
    print("✅ There is a statistically significant difference between male and female voter counts.")
else:
    print("❌ There is no statistically significant difference between male and female voter counts.")
