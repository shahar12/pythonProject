import requests
from requests.structures import CaseInsensitiveDict

url = "http://localhost:8000"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = """
{
  "Id": 78912,
  "Customer": "Jason Sweet",
}
"""

resp = requests.post(url, headers=headers, data=data)
print(resp.content)