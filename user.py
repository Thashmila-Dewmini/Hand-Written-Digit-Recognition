import requests

url = "http://127.0.0.1:5000/predict"  # Flask API URL

# Open the file explicitly in binary mode
with open('Numbers/number-2.png', 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)  # Send POST request

print(response.json())  # Print response from server

