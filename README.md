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

```
python manage.py migrate # init the db.sqlite3
python manage.py runserver
```