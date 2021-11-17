# Developing in local environment

You can develop xxx on your local machine. First you need to set up a Python 3
virtual environment and install the required dependency: 

```
$ mkdir build
$ python3 -m venv build
$ pip3 install -r requirements.txt
```

You can start the web server using the following command:

```
export DJANGO_SETTINGS_MODULE=xxx.settings.development
export DJANGO_SECRET_KEY=<some secret key>
python manage.py runserver
```

You should be able to see the applications at http://localhost:8000.

# Basic guidelines for development

The implementation is expected to pass the pylint test.
