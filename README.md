🗳️ Election Data Analysis
This project analyzes election voting data across different states/UTs in India using Python.
It includes basic data cleaning, statistical summaries, visualizations, and a T-Test to compare male and female voter counts.

📂 Project Structure
python project analysis.py — Main Python script that:

Loads and cleans the dataset (ElectionData.csv)

Performs basic statistical analysis

Visualizes the data with plots (bar graph, scatter plot, heatmap, boxplot, pie chart)

Conducts a T-test between male and female voter counts

📊 Features
Data Cleaning (handling missing values, removing duplicates)

Summary Statistics (mean, median, mode)

Data Visualizations:

Bar Plot

Scatter Plot

Heatmap

Boxplot

Pie Chart

Hypothesis Testing (T-Test)

🛠️ Libraries Used
pandas

numpy

matplotlib

seaborn

scipy

You can install them using:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn scipy
🚀 How to Run
Make sure you have Python installed.

Install required libraries (if not already installed).

Place the dataset ElectionData.csv in the same directory.

Run the script:

bash
Copy
Edit
python "python project analysis.py"
📌 Notes
The dataset file ElectionData.csv must be available in the same folder as the Python script.

The script shows visualizations and prints key analysis results to the terminal.

📷 Example Outputs
Bar chart showing total voters by state.

Scatter plot comparing male and female voters.

Heatmap of correlation between different gender counts.

Boxplots showing the distribution of voters.

Pie chart showing overall gender distribution.
