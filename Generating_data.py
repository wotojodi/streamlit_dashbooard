import csv
import random
from faker import Faker

# Initialize Faker for generating realistic data
fake = Faker()

# Sample data
countries = ['USA', 'Canada', 'UK', 'Germany', 'France', 'Australia', 'India', 'Brazil','Spain','Japan','Portugal','Zimbabwe','Zambia','Russia','Netherlands','China','Jamaica']
job_types = ['AI Solutions Architect','Data Scientist','Software Engineer','User  Experience (UX) Designer','Product Manager','Business Analyst','AI Research Scientist','Technical Support Specialist','Digital Transformation Consultant','Marketing Specialist']
demo_requests = ['Scheduled Demo', 'Promotional Event', 'AI-Powered Virtual Assistant']
payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer', 'Debit Card']

# Number of records to generate
num_records = 10000

# Generate realistic data
data = []
for _ in range(num_records):
    timestamp = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")  # Random timestamp
    ip_address = fake.ipv4()  # Random IP address
    country = random.choice(countries)
    jobs_placed = random.randint(1, 10)  # Random number of jobs placed
    job_requested = random.choice(job_types)  # Random job type requested
    demo_request = random.choice(demo_requests) if random.random() < 0.5 else None  # 50% chance of demo request
    response_code = random.choice([200, 304, 404])  # Random response code
    page_accessed = random.choice(['/index.html', '/images/events.jpg', '/event.php', '/scheduledemo.php', '/prototype.php'])
    user_agent = fake.user_agent()  # Random user agent
    session_id = fake.uuid4()  # Random session ID
    sales_revenue = round(random.uniform(1000, 10000), 2)  # Random sales revenue
    payment_method = random.choice(payment_methods)  # Random payment method
    satisfaction_rating = random.randint(1, 5)  # Random satisfaction rating (1 to 5)

    data.append({
        'Timestamp': timestamp,
        'IP Address': ip_address,
        'Country': country,
        'Jobs Placed': jobs_placed,
        'Job Requested': job_requested,
        'Demo Request': demo_request,
        'Response Code': response_code,
        'Page Accessed': page_accessed,
        'User  Agent': user_agent,
        'Session ID': session_id,
        'Sales Revenue': sales_revenue,
        'Payment Method': payment_method,
        'Satisfaction Rating': satisfaction_rating
    })

# Specify the CSV file name
csv_file = 'web_server_logs.csv'

# Write to CSV
with open(csv_file, mode='w', newline='') as file:
    fieldnames = ['Timestamp', 'IP Address', 'Country', 'Jobs Placed', 'Job Requested', 'Demo Request', 'Response Code', 'Page Accessed', 'User  Agent', 'Session ID', 'Sales Revenue', 'Payment Method', 'Satisfaction Rating']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data)

print(f"Data generated and saved to {csv_file}")

