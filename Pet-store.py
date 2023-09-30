import requests

base_url = "https://petstore.swagger.io/v2"

# create a pet
def test_create_pet():
    endpoint = "/pet"
    url = base_url + endpoint
    payload = {
        "id": 1,
        "name": "Fluffy",
        "status": "available"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200 or response.status_code == 201:
        print("POST API - Create Pet - Test Passed")
    else:
        print("POST API - Create Pet - Test Failed")

# get a pet
def test_get_pet():
    pet_id = 1
    endpoint = f"/pet/{pet_id}"
    url = base_url + endpoint
    response = requests.get(url)

    if response.status_code == 200 and response.json()["name"] == "Fluffy":
        print("GET API - Get Pet - Test Passed")
    else:
        print("GET API - Get Pet - Test Failed")

# update a pet
def test_update_pet():
    pet_id = 1
    endpoint = "/pet"
    url = base_url + endpoint
    payload = {
        "id": pet_id,
        "name": "Updated Fluffy",
        "status": "sold"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 200 and response.json()["name"] == "Updated Fluffy" and response.json()["status"] == "sold":
        print("PUT API - Update Pet - Test Passed")
    else:
        print("PUT API - Update Pet - Test Failed")

# delete a pet
def test_delete_pet():
    pet_id = 1
    endpoint = f"/pet/{pet_id}"
    url = base_url + endpoint
    response = requests.delete(url)

    if response.status_code == 200:
        print("DELETE API - Delete Pet - Test Passed")
    else:
        print("DELETE API - Delete Pet - Test Failed")

# Execute the test suite
test_create_pet()
test_get_pet()
test_update_pet()
test_delete_pet()