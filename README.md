# Newsletter Application for job interview

This is a sample django project written as answer for a job interview code challenge.

[![Build Status](https://travis-ci.org/jadolg/NewsletterApplication.svg?branch=master)](https://travis-ci.org/jadolg/NewsletterApplication) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/102ff10966d14df589aa1a5e2f70ef92)](https://www.codacy.com/manual/jadolg/NewsletterApplication?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jadolg/NewsletterApplication&amp;utm_campaign=Badge_Grade) [![codecov](https://codecov.io/gh/jadolg/NewsletterApplication/branch/master/graph/badge.svg)](https://codecov.io/gh/jadolg/NewsletterApplication)

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)
- [Make](https://www.gnu.org/software/make/manual/html_node/index.html)

## How to test

Executing `make test_docker` will execute all the tests inside a docker container.

## How to run

1. Make a copy of `.env.example` named `.env`
2. Write proper values on `.env` 
3. Execute `make run`

## How to run in development

1. Create a new virtual environment `python3 -m virtualenv newsletter` and activate it `source newsletter/bin/activate`
2. Install the requirements `pip install -r requirements.txt`
3. Run the migrations `python manage.py migrate`
4. Start the server `python manage.py runserver`

*note:* Default configuration will use `DEBUG=True` and sqlite database to avoid the hassles of starting postgres. No environment variable is needed in development.

## How to use the API

### Creating a subscription

First the user must subscribe to the newsletter sending the name and email.
The system should send and email containing the frontend URLs for confirming and deleting the subscription.
These URLs should contain the subscription secret ID which is used by the service to confirm and delete subscriptions.

curl request
```bash
curl -H "Content-Type: application/json" http://localhost:8000/v1/subscriptions/ -d '{"name":"Matt Verne", "email":"matt@hello.io"}'
```

response
201 Created
```json
{
   "email" : "matt@hello.io",
   "is_active" : false,
   "name" : "Matt Verne"   
}
```
*note:* If DEBUG is set to True the secret ID of the subscription is also coming in the json as no email is going to be sent. 

### Confirming a subscription

Once the user has created a subscription it's time to activate it.
The frontend should send a call to the activation endpoint with the token provided on the email.

curl request
```bash
curl -X POST http://localhost:8000/v1/subscriptions/9241a4a6-26ab-4fc6-8ad2-abbb44354198/confirm
```

response
200 OK
```json
{
   "email" : "matt@hello.io",
   "is_active" : true,
   "name" : "Matt Verne"
}
```

### Deleting a subscription

curl request
```bash
curl -X DELETE http://localhost:8000/v1/subscriptions/9241a4a6-26ab-4fc6-8ad2-abbb44354198
```

response
200 OK
```json
{
   "email" : "matt@hello.io",
   "is_active" : false,
   "name" : "Matt Verne"
}
```

### Metrics

Using [django-prometheus](https://pypi.org/project/django-prometheus/) you can access application relevant metrics under `/metrics`

### Healthcheck

A healthcheck for the service is available on API under `/health`
