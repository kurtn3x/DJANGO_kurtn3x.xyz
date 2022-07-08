- django installieren
- pip install django  dnspython djongo djoser django-cors-headers djangorestframework djangorestframework-simplejwt 
- pip install pymongo==3.12.3
- install mongodb
- mongoshell -> use admin
db.createUser(
  {
    user: "admin",
    pwd: "admin",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)

- go to mongo.conf, append or switch
security:
    authorization: "enable"


edit settings.py

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'kurtn3x',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
                'host': 'mongodb://admin:admin@localhost:27017/?authMechanism=DEFAULT&authSource=admin',
                'username': 'admin',
                'password': 'admin',
                'authSource': 'admin',
                'authMechanism': 'DEFAULT'
        }
    }
}

python manage.py createsuperuser
