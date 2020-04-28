DOCKER_TAG ?= $(shell git rev-parse HEAD)
DOCKER_IMAGE = newsletter-application:$(DOCKER_TAG)

.PHONY:
build:
	docker build -t $(DOCKER_IMAGE) .

test_docker: build
	docker run -e NEWSLETTER_DEBUG=True --rm -it $(DOCKER_IMAGE) python manage.py test
	docker run -e NEWSLETTER_DEBUG=True --rm -it $(DOCKER_IMAGE) python manage.py test test_pep8

test:
	NEWSLETTER_DEBUG=True python manage.py test
	NEWSLETTER_DEBUG=True python manage.py test test_pep8
