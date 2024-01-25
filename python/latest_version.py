import requests

packages = [
    "Flask", "MarkupSafe", "Werkzeug", "itsdangerous", 
    "psutil", "plotly", "tenacity", "boto3", "kubernetes"
]

for package in packages:
    response = requests.get(f"https://pypi.org/pypi/{package}/json")
    if response.status_code == 200:
        data = response.json()
        print(f"The latest version of {package} is: {data['info']['version']}")
    else:
        print(f"Could not fetch data for {package}")

## this is branch 5