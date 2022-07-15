## DJANGO Rest api für https://kurtn3x.xyz - erreichbar über https://api.kurtn3x.xyz

### ( bzw. als developement API unter https://test2.kurtn3x.xyz )
### Notes zu Apache und Plugins: 
- apache strippt sämtliche cors header und authorization headers, führt zu menge an problemen \
`WSGIPassAuthorization On` in apache2.conf -> Authorization header wird nicht entfernt wichtig für Tokens

- django-defender 0.9.5 wirft [non-type errors](https://github.com/jazzband/django-defender/issues/219)

api-website einstellungen:

```
	# Pfad zum static folder von django (python manage.py collectstatic)
        Alias /static /var/www/kurtn3x.xyz/kurtn3x-django/static
        <Directory /var/www/kurtn3x.xyz/kurtn3x-django/static>
                Header set Access-Control-Allow-Origin "*"
                Header add Access-Control-Allow-Methods "GET, POST, OPTIONS"
                Header add Access-Control-Allow-Headers "authorization, content-type"
                Require all granted
        </Directory>
        <Directory /var/www/kurtn3x.xyz/kurtn3x-django/kurtn3x>
                Header set Access-Control-Allow-Origin "*"
                Header add Access-Control-Allow-Methods "GET, POST, OPTIONS"
                Header add Access-Control-Allow-Headers "authorization, content-type"
                Require all granted
        </Directory>
        WSGIDaemonProcess djangoapi python-path=/var/www/kurtn3x.xyz/kurtn3x-django python-home=/var/www/kurtn3x.xyz/kurtn3x-django/venv
        WSGIProcessGroup djangoapi
        WSGIScriptAlias / /var/www/kurtn3x.xyz/kurtn3x-django/kurtn3x/wsgi.py
```
____________________________________________________________________________________________________________________________________

### Notes zur Django API 

- static root setzen
```
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
```
