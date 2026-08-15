import requests

url = "https://mf.azeriqaz.az/dashboard/gas-pipelines/devices-list/datatable?draw=4&columns[0][data]=id&columns[0][name]=&columns[0][searchable]=false&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=title&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=destination.title&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=actions&columns[3][name]=&columns[3][searchable]=false&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&order[0][column]=0&order[0][dir]=desc&start=0&length=100&search[value]=&search[regex]=false&_token=3IchPVB1uVeb3NWsHK8kY7bZGw47kwS01pjILs3L&title=&designation=31&_=1785329250846"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Response:")
print(response.text[:1000])  # Print the first 1000 characters

# Only parse JSON if it is actually JSON
if "application/json" in response.headers.get("Content-Type", ""):
    data = response.json()
    print(data)
else:
    print("Response is not JSON.")