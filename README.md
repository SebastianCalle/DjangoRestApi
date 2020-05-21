# DJANGO API REST 

This is a API to manage CRUD operations between the entities Clients, Bills, Products.

The entire API was build with the `Django Rest Framework`.
## Prerequisites
The best practice to work with django projects is usign	virtual	enviroments, if	you don't have it,
yo need	to install it and pip3 component (this is for linux machine):
Install	pip3:
```
$ sudo apt-get install python3-pip
```
Install	virtual	enviroment:
```
$ sudo pip3 install virtualenv
```
in your	favorite path create a new folder called juanmontealegre:
```
$ mkdir	juanmontealegre
```
now change for juanmontealegre folder:
```
$ cd juanmontealegre
```
create a virtual enviroment called quickTestEnv
```
$ virtualenv quickTestEnv -p python3
```

activate the virtual enviroment:
```
$ source quickTestEnv/bin/activate
```
Install de requirements with the command 

    $ pip install -r requirements.txt   

## Run the app

    python manage.py runserver


# REST API

The REST API is described below.

##USER REGISTER
For user registration you need:

url: http://127.0.0.1:8000/register

usign a	POST method whit data(raw JSON):

Body:
```
{
	"email": "panchita@gomez.com"
        "password": "lameramera",
}
```
### Response:
```
{
        "email": "panchita@gomez.com",
        "username": "panchita@gomez.com"
}
```
## USER LOGIN
For user login you need the "username" response from USER REGISTER and:

url: http://127.0.0.1:8000/login
usign a POST method whit data(raw JSON):

Body:
```
{
        "username": "panchita@gomez.com"
        "password": "lameramera",
}
```
Response:
```
{
    "refresh": "token returned by the API",
    "access": "token returned by the API to access the CRUD api views"
}
```
All endpoints need to JWT for can access to the data, example:

    Autorizaton: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkwMDQxOTQyLCJqdGkiOiI5YTkyYzZkNGNhM2M0NDY3YWE5N2U0M2NiMWQyY2E2NiIsInVzZXJfaWQiOjR9.1W2kY2QOMduNGdp2irYFfImnPYwZbu0bCR53Cw9GtiE
## Get list of Clients or Products or Bills

All endpoints need to JWT for can access to the data, example:

    Autorizaton: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkwMDQxOTQyLCJqdGkiOiI5YTkyYzZkNGNhM2M0NDY3YWE5N2U0M2NiMWQyY2E2NiIsInVzZXJfaWQiOjR9.1W2kY2QOMduNGdp2irYFfImnPYwZbu0bCR53Cw9GtiE

### Request

`GET api/client`

`GET api/product`
    
`GET api/bill`

### Example Response of api/product

    [
        {
            "id": 1,
            "name": "Cup",
            "description": "Is a cup for cofe"
        },
        {
            "id": 3,
            "name": "Bet",
            "description": "The Best bet in the world"
        },
        {
            "id": 4,
            "name": "Tennis",
            "description": "Tennis Sport"
        },
        {
            "id": 5,
            "name": "Celphone",
            "description": "Celphone Motorola"
        }
    ] 

## Create a new Client, Product or Bill

### Request

`POST /api/client`

`POST /api/product`

`POST /api/bill`

Example POST for client:
```
{
    "document": 123098121233,
    "first_name": "Sebastian",
    "last_name": "Calle",
    "email": "jusemonca@gmail.com"
}
```
### Example Response of api/client
```
{
    "id": 7,
    "document": 123098121233,
    "first_name": "Sebastian",
    "last_name": "Calle",
    "email": "jusemonca@gmail.com"
}
```
## Update a Client, Product or Bill by id 

### Request

`PUT /api/client/{id}`

`PUT /api/product/{id}`

`PUT /api/bill/{id}`

Example PUT for client:


    {
        "document": 123098123,
        "first_name": "Juan",
        "last_name": "Calle",
        "email": "jusemonca@gmail.com"
    }

### Response
    {"success":"Client with id '1' updated successfully"}

## Delete Client, Product or Bill

### Request

`Delete api/client/{id}`

`Delete api/product/{id}`

`Delete api/bill/{id}`

## Get Bill by Client id

### Request
`Get api/bill-by-client/{id}`

### Response
    [
        {
            "id": 2,
            "company_name": "Holberton School",
            "nit": 102938210,
            "code": 10198,
            "client_id": 1
        },
        {
            "id": 6,
            "company_name": "Holberton",
            "nit": 102938210,
            "code": 10198,
            "client_id": 1
        }
    ]

## Get Product by Bill id

### Request
`Get api/products-by-bill/{id}`

### Response
    [
        [
            {
                "id": 1,
                "name": "Cup",
                "description": "Is a cup for cofe"
            }
        ],
        [
            {
                "id": 1,
                "name": "Cup",
                "description": "Is a cup for cofe"
            }
        ]
    ]
    
## Get Bill by Product id

### Request
`Get api/bills-by-product/{id}`

### Response
    [
        [
            {
                "id": 2,
                "company_name": "Holberton School",
                "nit": 102938210,
                "code": 10198,
                "client_id": 1
            }
        ],
        [
            {
                "id": 2,
                "company_name": "Holberton School",
                "nit": 102938210,
                "code": 10198,
                "client_id": 1
            }
        ]
    ]

## Create relationship between Bill and Product

### Request
`POST api/bills-product`

body:

    {
        "bill_id": 2,
        "product_id": 1
    }

### Response
    {
        "id": 8,
        "bill_id": 2,
        "product_id": 1
    }
    
## Get Bill and Product

### Request
`GET api/bills-product`

### Response
    [
        {
            "id": 1,
            "bill_id": 2,
            "product_id": 1
        },
        {
            "id": 7,
            "bill_id": 2,
            "product_id": 1
        },
        {
            "id": 8,
            "bill_id": 2,
            "product_id": 1
        }
    ]
    

## Get CSV wiht Document Full Name and Count of bills of the Client

### Request
`GET api/client-records`

### Response
    Document,Full Name,Count of Bill
    123098123,Juan Calle,2


