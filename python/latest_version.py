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

<<<<<<< HEAD
## this is branch 5
        
## this is branch 6
=======
## this is branch 5
>>>>>>> b28037b (This is commit 0005 this will be merged)
