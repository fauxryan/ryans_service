# ryans_service

My new project

## Setting up the environment

This project depends on [Python](https://www.python.org/) 2.7+ or 3.4+
and the [CherryPy](http://cherrypy.org/) web framework.

Once you have installed Python for your environment, you
should also setup a [virtual environment](https://virtualenv.pypa.io/en/stable/)
with [pip](https://pip.pypa.io/en/stable/installing/).

Then, you should install the dependencies required by
the project as follows:

```
$ pip install -r requirements.txt
```

## Getting started

Before you can run the application, the package must be found
in your `PYTHONPATH`. To do so, run the next command once:

```
$ python setup.py develop
```

Run the application as follows:

```
$ python -m ryans_service
```

then point your client at `http://localhost:8080/`.

## Develop your application

### Run tests

Tests are part of the project and should be continuously. Those
tests are implemented using the [nosetest](http://nose.readthedocs.io/en/latest/)
framework and located in the `tests` directory.

To execute them, run the following command:

```
$ nosetests -s -v tests
```

## Package & distribute your application

The project provides a recipe to build a Docker
image of the application and its dependencies to
simply its distribution. You can build the image
as follows:

```
$ docker build -t ryans_service .
```

To run the application inside a container, execute then
the following commands:

```
$ docker run -d -p 8080:8080 ryans_service
```
