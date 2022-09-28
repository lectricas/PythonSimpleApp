# PythonSimpleApp

### Run the project

In order to run the project, clone it and then create venv with inside your root directory:

```sh
python3 -m venv venv
source venv/bin/activate
```

After that, you need to load dependencies with:

```sh
pip install -r requirements.txt
```

Finally, migrate the database and start the project:

```sh
python manage.py migrate
python manage.py runserver
```

### Tests

To run the tests, simply execute 

```sh
python manage.py test my_module
```

where my_module is the module for testing.

As for now, this project has only one module, so you can simply execute

```sh
python manage.py test bank
```

to run the tests.