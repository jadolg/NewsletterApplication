DOCKER_TAG ?= $(shell git rev-parse HEAD)
DOCKER_IMAGE = newsletter-application:$(DOCKER_TAG)

.PHONY:
build:
	DOCKER_IMAGE=$(DOCKER_IMAGE) docker-compose build

test_docker: build
	docker run -e NEWSLETTER_DEBUG=True --rm -it $(DOCKER_IMAGE) python manage.py test
	docker run -e NEWSLETTER_DEBUG=True --rm -it $(DOCKER_IMAGE) python manage.py test test_pep8

test:
	NEWSLETTER_DEBUG=True python manage.py test
	NEWSLETTER_DEBUG=True python manage.py test test_pep8

run: build
	DOCKER_IMAGE=$(DOCKER_IMAGE) docker-compose up
