#------------------------------------------------
# Djoser API available
#------------------------------------------------
# /users/
# /users/me/
# /users/confirm/
# /users/resend_activation/
# /users/set_password/
# /users/reset_password/
# /users/reset_password_confirm/
# /users/set_username/
# /users/reset_username/
# /users/reset_username_confirm/

# Using Djoser allows us to use all above API endpoints, we implement below methods by default

# /api/users     - No role required                          - POST - Creates a new user with name, email and password
# /api/users/me/ - Anyone with a valid user token            - GET  - Displays only the current user
# /token/login/  - Anyone with a valid username and password - POST - Generates access tokens that can be used in other API calls in this project
# http://127.0.0.1:8000/api/api-token-auth

# http:/127.0.0.1:8000/api