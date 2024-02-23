
## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# List all users
GET /users

# Get a single user by ID
GET /users/<int:user_id>

# Create a new user
POST /users
  username: string

# Update an existing user
PUT /users/<int:user_id>
  username: string

# Delete a user
DELETE /users/<int:user_id>

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._
_Remember to try out different parameter values._
_Include the status code and the response body._

```python

#note: In the Flask application, routes are defined with paths and associated with view functions. The view function names (get_user, create_user, etc.) are used within the Flask application to map URLs to Python functions. However, when documenting or testing these routes, we refer to them by their HTTP method and path, not by the function names. See bellow


#1 GET /users
#  Expected response (200 OK):
"""
[
  {"id": 1, "username": "john"},
  {"id": 2, "username": "jane"},
  {"id": 3, "username": "alice"}
]
"""


#2 GET /users/1
#  Expected response (200 OK):
"""
{"id": 1, "username": "john"}
"""
#2 Error scenarios
#  GET /users/999
#  Expected response (404 Not Found):
"""
{"error": "User not found"}
"""


#3 POST /users
#  Parameters:
#   username: Adam
#  Expected response (201 Created):
"""
{"id": 4, "username": "Adam"}
"""
#3 POST /users
#  Parameters: none
#  Expected response (400 Bad Request):
"""
{"error": "Username is required"}
"""


#4 PUT /users/1
#  Parameters:
#   username: JohnSnow
#  Expected response (200 OK):
"""
{"id": 1, "username": "JohnSnow"}
"""
#4 Error scenarios
#  PUT /users/999
#  Expected response (404 Not Found):
"""
{"error": "User not found"}
"""
#4 Error scenarios
#  PUT /users
#  Parameters: none
#  Expected response (400 Bad Request):
"""
{"error": "Username is required"}
"""


#5 DELETE /users/1
#  Expected response (200 OK):
"""
{"message": "User deleted"}
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

See the test_app.py file.
```

