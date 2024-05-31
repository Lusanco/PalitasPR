# API Endpoint Documentation

## Create New Promotion or Request and Upload Picture

### Endpoint

`POST /api/promotion-request/<user_id>`

### Description

This route allows frontend to create a new promotion or request and upload a picture for it.

### Request Body

The request body sent by the frontend should include the following parameters:

- **model**: `string`  
  Specifies the type of model to create.  
  Possible values: `'promotion'` or `'request'`.
- **title**: `string`  
  The title of the promotion or request.
- **description**: `string`  
  The description of the promotion or request.
- **price_min**: `number` (optional)  
  The minimum price for the promotion or request.
- **price_max**: `number` (optional)  
  The maximum price for the promotion or request.
- **service**: `string` (optional)  
  The type of service associated with the promotion or request.
- **image**: `file`  
  The image file to be uploaded.

### Example Request Body 'GET'

url: /api/promotion-request/<user_id>
user will be verified with flask login

### Example Request Body 'POST'

```json
Create Promotion:
{
    "model": "Promotion",
    "title": "Spring Cleaning Discount",
    "description": "Get 20% off your first spring cleaning.",
    "service_id": "Cleaning Service",
    "price_min": 50(optional),
    "price_max": 100(optional),
}
multipart file format: image(optional)

Create Request:
{
    "model": "Request",
    "title": "In need of a plumber",
    "description": "Kitchen sink needs a major work, it is leaking constantly",
    "service_id": "Plumbing",
}
multipart file format: image(optional)
```
