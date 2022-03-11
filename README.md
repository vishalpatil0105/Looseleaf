# Looseleaf
Instructions To Run:

1.cd Looseleaf Assignments

2. PIP install -r requirements.txt

3. python manage.py makemigrations

4. python manage.py migrate

If Below Error Occurs at the time of API Call "Exception encountered while user signing up:no such table: SchoolAdminPortal_students"
Please Follow:
 python manage.py makemigrations SchoolAdminPortal
 python manage.py migrate SchoolAdminPortal
 

5.python manage.py createsuperuser

# Add super user credentials Eg Username etc
[ Optional step if you want to see models in django admin pannel ]

6. python manage.py runserver
Then Follow Api Provided in the postman collection fro the api.
