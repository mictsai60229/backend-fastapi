# Backend-Fastapi: Python Pure Backend Built in Fastapi


## Installation
---
## Prerequisites
Before starting the project, you should install `python3.7`. Other python 3.x versions are not tested but it should work by changing python version in `Pipfile`.


## Pyenv
Pyenv lets you control different version of python in your computer.
Try [pyenv](https://github.com/pyenv/pyenv) to install `python3.7`.

## Pipenv
Pipenv equals to `pip` + `virtualenv`. Install with Python and pip.
```sh
$ pip install pipenv
```
Install dependency
```sh
$ pipenv install
```
Open virtaul enviroment shell
```sh
$ pipenv shell
```

## Run server with uvicorn
```sh
$ uvicorn main:app --reload
```

## Run multiprocess server with gunicorn uvicorn
```sh
$ export prometheus_multiproc_dir={{your_log_dir}}
$ gunicorn -w {{number_of_processes}} -k uvicorn.workers.UvicornWorker main:app {{host}}:{{port}}
```




