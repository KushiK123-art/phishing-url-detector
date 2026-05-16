import requests

API_KEY = "YOUR_API_KEY"

def check_url_virustotal(url):

    endpoint = "https://www.virustotal.com/api/v3/urls"

    headers = {
        "x-apikey": API_KEY
    }

    data = {
        "url": url
    }

    response = requests.post(endpoint, headers=headers, data=data)

    if response.status_code == 200:
        return "Suspicious"
    else:
        return "Safe"
        