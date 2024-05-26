# Explore API Endpoint Documentation

## Endpoint

`GET /explore`

### Parameters

- **model**: `string`  
  Specifies the type of data to retrieve.  
  Possible values: `'promotions'` or `'requests'`.

- **search**: `string`  
  The name of the service to search for.

- **town**: `string` or `null`  
  The name of the town to filter results by. This can be `null`.

### Example Request Body

```json
{
    "model": "Promotion",
    "search": "Cleaning Service",
    "town": "New York"
}

RETURNS:
If promotions:
200:
{
    "results": [
        {
            "promo_id": "12345",
            "service": "Cleaning Service",
            "title": "Spring Cleaning Discount",
            "description": "Get 20% off your first spring cleaning.",
            "price_min": 50,
            "price_max": 100,
            "first_name": "John",
            "last_name": "Doe",
            "towns": ["New York", "Brooklyn"],
            "created_at": "2023-05-01"
        },
        ...
    ]
}

If requests:
200:
{
    "results": [
        {
            "request_id": "54321",
            "service": "Gardening Service",
            "title": "Garden Maintenance Request",
            "description": "Looking for regular garden maintenance.",
            "first_name": "Jane",
            "last_name": "Smith",
            "towns": ["Queens", "Bronx"],
            "created_at": "2023-05-01"
        },
        ...
    ]
}

404:
{
    "message": "No Results"
}




```
