import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('web_server_logs.csv')

# Display the first few rows of the dataset
print(data.head())
 
# Display basic statistics
print(data.describe(include='all'))

# Count unique job requests
job_counts = data['Job Requested'].value_counts()
print("Job Requests Frequency:\n", job_counts)

# Visualize job requests
plt.figure(figsize=(10, 6))
sns.barplot(x=job_counts.index, y=job_counts.values, palette='viridis')
plt.title('Job Requests Frequency')
plt.xlabel('Job Types')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

# Analyze demo requests
demo_counts = data['Demo Request'].value_counts()
print("Demo Requests:\n", demo_counts)

# Visualize demo requests
plt.figure(figsize=(6, 4))
sns.countplot(x='Demo Request', data=data, palette='pastel')
plt.title('Demo Requests Count')
plt.xlabel('Demo Request')
plt.ylabel('Count')
plt.show()

# Analyze promotional event requests
promo_counts = data['Promotional Event Request'].value_counts()
print("Promotional Event Requests:\n", promo_counts)

# Visualize promotional event requests
plt.figure(figsize=(6, 4))
sns.countplot(x='Promotional Event Request', data=data, palette='pastel')
plt.title('Promotional Event Requests Count')
plt.xlabel('Promotional Event Request')
plt.ylabel('Count')
plt.show()

# Analyze jobs placed by country
country_job_counts = data.groupby('Country')['Jobs Placed'].sum().sort_values(ascending=False)
print("Total Jobs Placed by Country:\n", country_job_counts)

# Visualize jobs placed by country
plt.figure(figsize=(10, 6))
country_job_counts.plot(kind='bar', color='skyblue')
plt.title('Total Jobs Placed by Country')
plt.xlabel('Country')
plt.ylabel('Total Jobs Placed')
plt.xticks(rotation=45)
plt.show()

# Analyze AI-powered virtual assistant requests
ai_counts = data['AI-Powered Virtual Assistant Request'].value_counts()
print("AI-Powered Virtual Assistant Requests:\n", ai_counts)

# Visualize AI-powered virtual assistant requests
plt.figure(figsize=(6, 4))
sns.countplot(x='AI-Powered Virtual Assistant Request', data=data, palette='pastel')
plt.title('AI-Powered Virtual Assistant Requests Count')
plt.xlabel('AI-Powered Virtual Assistant Request')
plt.ylabel('Count')
plt.show()


# Aggregate data
aggregated_data = {
    'Total Jobs Placed': data['Jobs Placed'].sum(),
    'Average Jobs Placed': data['Jobs Placed'].mean(),
    'Total Sales Revenue': data['Sales Revenue'].sum(),
    'Average Sales Revenue': data['Sales Revenue'].mean(),
    'Average Satisfaction Rating': data['Satisfaction Rating'].mean(),
    'Total Demo Requests': data['Demo Request'].notnull().sum(),
    'Job Type Distribution': data['Job Requested'].value_counts(),
    'Payment Method Usage': data['Payment Method'].value_counts()
}

# Convert job type distribution and payment method usage to DataFrames for easier visualization
job_type_distribution = data['Job Requested'].value_counts().reset_index()
job_type_distribution.columns = ['Job Type', 'Count']

payment_method_usage = data['Payment Method'].value_counts().reset_index()
payment_method_usage.columns = ['Payment Method', 'Count']

# Display aggregated results
print("Aggregated Data:")
print(aggregated_data)

print("\nJob Type Distribution:")
print(job_type_distribution)

print("\nPayment Method Usage:")
print(payment_method_usage)