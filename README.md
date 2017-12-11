# django-intranet

## Install python 3

https://www.python.org/downloads/

## Clone this repo

https://help.github.com/articles/cloning-a-repository/

```
git clone <url> ~/django-intranet
```

## Setup virtualenv and install required packages
```
pip install virtualenv
virtualenv -p python3.6 ~/django-venv
. ~/django-venv/bin/activate
cd ~/django-intranet
pip install -r requirements.txt
```

## Start up the server

If the virtualenv is not active, run this:
```
. ~/django-venv/bin/activate
```

Start up the server
```
cd ~/django-intranet/intranet
python manage.py runserver
```

## Connect to the server

http://127.0.0.1:8000/account/

Log in with the default admin credentials: (admin/password123)


