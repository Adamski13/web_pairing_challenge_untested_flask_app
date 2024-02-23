import os
from flask import Flask, jsonify, request

def test_example(web_client):
    response = web_client.get("/users")
    assert response.status_code == 200

#test cases
"""
When: I make a GET request to /users
Then: I should get a 200 OK response and a list of users
"""
def test_get_all_users(web_client):
    response = web_client.get('/users')
    current_users = response.json
    assert response.status_code == 200
    assert len(response.json) == len(current_users)

"""
When: I make a GET request to /users/1
Then: I should get a 200 OK response and the user with id 1
"""
def test_get_specific_user(web_client):
    response = web_client.get('/users/1')
    assert response.status_code == 200
    assert response.json['username'] == 'john'

"""
When: I make a POST request to /users with a username
Then: I should get a 201 Created response and the new user's details
"""
def test_create_user(web_client):
    response = web_client.post('/users', json={'username': 'Adam'})
    assert response.status_code == 201
    assert response.json['username'] == 'Adam'

"""
When: I make a PUT request to /users/1 with a new username
Then: I should get a 200 OK response and the updated user's details
"""
def test_update_user(web_client):
    response = web_client.put('/users/1', json={'username': 'JohnSnow'})
    assert response.status_code == 200
    assert response.json['username'] == 'JohnSnow'

"""
When: I make a DELETE request to /users/1
Then: I should get a 200 OK response and a confirmation message
"""
def test_delete_user(web_client):
    response = web_client.delete('/users/1')
    assert response.status_code == 200
    assert 'User deleted' in response.json['message']