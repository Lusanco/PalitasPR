# Sign Up API Endpoint Documentation

## Endpoint

`POST /signup`

### Parameters

The request body should be in JSON format and include the following fields:

- **first_name**: `string`  
  The first name of the user.

- **last_name**: `string`  
  The last name of the user.

- **email**: `string`  
  The email address of the user.

- **password**: `string`  
  The password for the user account.

### Example Request Body

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "password": "SecurePassword123"
}
```

#RETURNS depending on status
201:
{
"message": "Account created"
}
400:
{
"message": "Missing a required field"
}
400:
{
"message": "Invalid email format - {email validation error message}"
}
409:
{
"message": "Email already in use"
}
500:
{
"message": "Error in signup logic"
}
