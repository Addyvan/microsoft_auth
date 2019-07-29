# microsoft_auth
Basic django app for demonstrating authenticating with Microsoft Graph

# Install dependencies

```
pip install Django
pip install requests_oauthlib==1.2.0
pip install pyyaml==5.1
pip install python-dateutil==2.8.0
```

# To run the app

Replace `oauth_settings.example.yml` with `oauth_settings.yml` along with the proper settings. To get this app going you need to specify the client id, client secret and the correct redirect uri (defaulted to http://localhost:8000/microsoft_auth/callback).

```
python manage.py migrate # init the db.sqlite3
python manage.py runserver
```