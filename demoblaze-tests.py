import requests

# Base URL of the Demoblaze API
base_url = "https://www.demoblaze.com"

# User credentials for testing
username = "testuser"
password = "testpassword"

# Sign up API endpoint
signup_endpoint = "/signup"

# Login API endpoint
login_endpoint = "/login"

# Create a new user account
def signup(username, password):
    signup_url = base_url + signup_endpoint
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(signup_url, json=data)
    return response

# Log in with an existing user account
def login(username, password):
    login_url = base_url + login_endpoint
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(login_url, json=data)
    return response

# Test the Signup API
signup_response = signup(username, password)
if signup_response.status_code == 200:
    print("Signup successful")
else:
    print("Signup failed")

# Test the Login API
login_response = login(username, password)
if login_response.status_code == 200:
    print("Login successful")
else:
    print("Login failed")