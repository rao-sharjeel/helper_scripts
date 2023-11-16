import requests
csrf_token_url='http://localhost:8000/csrf_token'

URL = 'http://localhost:8000/api-login' # login api 

client = requests.session()
client.get(csrf_token_url) # Get request to capture the csrf token 

if 'csrftoken' in client.cookies: # If token is under csrftoken
    csrftoken = client.cookies['csrftoken']
    print('Cookies from get are: ', client.cookies.get_dict())

else: # If token is under csrf
    csrftoken = client.cookies['csrf']
    print(csrftoken)

headers = {
    'Origin': 'http://localhost:8000',
    'X-CSRFToken': csrftoken, # Token added to the header of the second post request
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'Accept': 'application/json',
}

login_data = {
    'username':'admin', # username of the admin
    'password':'admin' # password of the admin
    } 
r = client.post(URL, json=login_data, headers=headers)

session_id = r.cookies['sessionid']
print('session_id')
print(session_id)

csrftoken = r.cookies['csrftoken']
print('csrftoken')
print(csrftoken)

print(r)
print(r.cookies.get_dict()) #Getting list of data in the cookies
print(r.status_code)
print(r.json()) # This should be a simple success message in json if successful, or 401 Unauthorized

headers = {
    'Origin': 'http://localhost:8000',
    # 'X-CSRFToken': csrftoken, # Token added to the header of the second post request
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Cookie': f"csrftoken={csrftoken}; sessionid={session_id}",
}

print("\n\nGetting Patients")
r = client.get('http://localhost:8000/api/patients', headers=headers)
print(r)
print(r.content)
