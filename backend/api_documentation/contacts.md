# User Contacts API Endpoint Documentation

## Endpoint

`GET api/user/contacts`

### Responses

**200 OK**

```json
{
    "results": {
        "received": [
            {
                "created_at": "Wed, 19 Jun 2024 19:57:55 GMT",
                "id": "8a7de598-e423-4b65-995d-9e27f0cd7940",
                "promo_id": "5dd1f35e-b7ba-4f38-93bc-3fb727cc56d4",
                "read": true,
                "sender_email": "jane006@gmail.com",
                "sender_first_name": "Jane",
                "sender_id": "3db8d073-be9a-45cd-8181-40d556cb2b47",
                "sender_last_name": "Smith",
                "sent_task": true,
                "task": {
                    "created_at": "Wed, 19 Jun 2024 19:57:55 GMT",
                    "description": "TASK DESCRIPTION: Nightclubs and Weddings",
                    "id": "83b26321-25cf-451a-9d44-42e11caa52e7",
                    "initial_contact_id": "8a7de598-e423-4b65-995d-9e27f0cd7940",
                    "is_read": true,
                    "promo_id": "5dd1f35e-b7ba-4f38-93bc-3fb727cc56d4",
                    "provider_id": "74484047-244d-460b-94ab-ad8f3281561b",
                    "receiver_confirm": null,
                    "receiver_id": "3db8d073-be9a-45cd-8181-40d556cb2b47",
                    "service_id": 14,
                    "status": "closed",
                    "updated_at": "Wed, 19 Jun 2024 19:57:55 GMT"
                },
                "updated_at": "Wed, 19 Jun 2024 19:57:55 GMT"
            }
        ],
        "sent": [
            {
                "created_at": "Wed, 19 Jun 2024 19:57:55 GMT",
                "id": "5def65b5-3212-4bfd-854d-3dbdbe04d1ef",
                "promo_id": "51798b07-d16f-4b5a-9bc3-9d546d930b63",
                "read": true,
                "receiver_email": "hector.torres@gmail.com",
                "receiver_first_name": "Hector",
                "receiver_id": "48e90b1f-d522-49a8-8f41-1b492edce39f",
                "receiver_last_name": "Torres",
                "sent_task": true,
                "task": {
                    "created_at": "Wed, 19 Jun 2024 19:57:55 GMT",
                    "description": "TASK DESCRIPTION: Urban DJ",
                    "id": "2eadb090-8bcc-4cb7-832e-d88dad36209f",
                    "initial_contact_id": "5def65b5-3212-4bfd-854d-3dbdbe04d1ef",
                    "is_read": true,
                    "promo_id": "51798b07-d16f-4b5a-9bc3-9d546d930b63",
                    "provider_id": "48e90b1f-d522-49a8-8f41-1b492edce39f",
                    "receiver_confirm": null,
                    "receiver_id": "74484047-244d-460b-94ab-ad8f3281561b",
                    "service_id": 14,
                    "status": "closed",
                    "updated_at": "Wed, 19 Jun 2024 19:57:55 GMT"
                },
                "updated_at": "Wed, 19 Jun 2024 19:57:55 GMT"
            }
        ]
    }
}
