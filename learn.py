# Api is a set of commands, functions, protocols and objects that programmers can use to create software or interact with external systems
# it is an interface between you program and an external system
# API endpoint is the location of where our data is stored. It is just a url eg api.coinbase.com
# API request is similar to going to the bank and getting the money out.
# The teller in a bank is the api. 
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) #<Response [200]>

# response codes
# they tell us whether our requests succeeded or failed
# 1xx hold on 
# 2xx successful
# 3xx you don't have permission
# 4xx client error
# 5xx server error

print(response.status_code)

data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
print(longitude, latitude)