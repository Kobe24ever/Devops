import requests

response = requests.post("http://127.0.0.1:5000/whatismyname")
# print(response.status_code)
# print(response.text)

expected = "saved new car"
actual = response.text

assert expected == actual
