# Rest_api_pizza


## Endpoint Authentication
I made Authentication Api using Token In Which first of all you need to Create user after that you can create Token for Authentication then using this token you can Authenticate after server started you can direct click on this to get url and i also provided urls
+ [Create User](http://127.0.0.1:8000/core/api/create/)
    http://127.0.0.1:8000/core/api/create/
+ [Token](http://127.0.0.1:8000/core/api/token/)
    http://127.0.0.1:8000/core/api/token/
+ [Edit or See Profile](http://127.0.0.1:8000/core/api/me/)
    http://127.0.0.1:8000/core/api/me/
    
## API endpoint to create regular pizza and a square pizza.
I don't used authentication in this api so you don't need to authenticate for using these api. you can directly use get or post on api based on  Pizza
For creating Pizza url is http://127.0.0.1:8000/core/api/pizza-create/
### Example for post data

  {
        "pizza_type": "Regular",
        "pizza_size": [
            "Small","Large"
        ],
        "pizza_toppings": [
            "Corn","Onion"
        ]
    }
## API endpoint which give list of the stored pizza 
the response of this contain the information about the toppings, size and type of Pizza

Url for this http://127.0.0.1:8000/core/api/pizza-list/

## Allow filtering the list of pizza returned by the API based on Size & Type of Pizza
Url for filter using size and type of pizza http://127.0.0.1:8000/core/api/pizza-filter/<str:key>=<str:value>

key = type,size

value for type = Regular, Square

value for size = Small, Large, Medium


## API endpoint that allows the user to edit or delete any pizza from the database.
Url for edit http://127.0.0.1:8000/core/api/pizza-update/<int:id>

Url for delete http://127.0.0.1:8000/core/api/pizza-delete/<int:id>

## Requirements
- Python3 
- mongodb
- pip
- you have create database using mongodb commands name "dbp"

## steps to run the project

+ Clone project 
+ Open Terminal go to ths dir of cloned project
+ Run Command "pip install -r requirerment.txt" or "pip3 install -r requirerment.txt"
+ Run command "python manage.py migrate" or "python3 manage.py migrate"
+ Run command "python manage.py runserver" or "python3 manage.py runserver"
+ Now use api
