# Section 2: Coding Challenges 

# 4. Write a simple script in Python to automate the testing of a login API using POST requests. The API accepts a username and password and returns a token upon successful authentication. Include a test case for invalid credentials. 

import requests
import pytest


def test_valid_login():

# Tests successful login with valid credentials.

#Assuming the valid username is "Diana" and Password is "Kaks123"
  url = "http://your-api-endpoint.com/login" 
  data = {
      "username": "Diana",
      "password": "Kaks123"
  }
  response = requests.post(url, json=data) 

  assert response.status_code == 200
  assert "token" in response.json()

def test_invalid_login():
  
 # Tests login failure with invalid credentials.

  url = "http://your-api-endpoint.com/login" 
  data = {
      "username": "Diana",
      "password": "kaks123"  #NB: password here is in small letters which is contrary to what is correct
  }
  response = requests.post(url, json=data)
 

  assert response.status_code == 401 

if __name__ == "__main__":
  pytest.main()