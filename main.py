import requests
import csv
import time

from requests.api import head

url = "https://random-data-api.com/api/users/random_user?size=10"

headers = {
    'Accept': 'application/json',
    'COntent-type' : 'application/json'
}

response = requests.request("GET", url, headers=headers,data=())

myjson = response.json()
ourdata = []
csvheader = ["ID", "Name", "Last Name", "Email", "Gender", "DOB"]

for x in myjson:
    listing = [x['id'],x['first_name'],x['last_name'], x['email'], x['gender'], x['date_of_birth']]
    
    ourdata.append(listing)
with open("users.csv", 'w', encoding = 'UTF8', newline='')as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)
print(ourdata)