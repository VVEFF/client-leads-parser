** Client Leads Parser
Python script for processing client leads from CSV files.
  ##Features
Reads leads from CSV
Validates required fields
Removes duplicates
Separates valid and invalid leads
Counts leads by source
Exports results to CSV and JSON
  ##Technologies
Python
Pandas
JSON
  ##How to run
pip install pandas
python script.py
  ##CRM Integration
To integrate with a CRM, add:
requests library
CRM API URL in CRM_URL
Authentication headers in HEADERS
POST request for each client
 #Example:
import requests

for client in clients:
    response = requests.post(
        CRM_URL,
        headers=HEADERS,
        json=client
    )
    print(response.status_code)

