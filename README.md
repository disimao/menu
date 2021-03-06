# menu

## docker

No mistery here:

    $ docker-compose up

## DRF

### Endpoints as requested in the code challenge

    /pedidos (GET, POST)
    /pedidos/:id (GET, PUT, DELETE)
    /clientes (GET, POST)
    /clientes/:id (GET, PUT, DELETE)

## Tests

### Unit Tests

    $ python manage.py test <app_name>

### End-to-end Tests

    $ python manage.py test tests

![e2e Demo](https://raw.githubusercontent.com/disimao/menu/master/data/gifs/Peek%202020-08-16%2015-52.gif)

## References

* [E2E] - [Selenium Tests in Django & Docker](https://marcgibbons.com/post/selenium-in-docker/)
* [Unit Tests] - [How To Add Unit Testing to Your Django Project](https://www.digitalocean.com/community/tutorials/how-to-add-unit-testing-to-your-django-project)
* [Docker] - [Quickstart: Compose and Django](https://docs.docker.com/compose/django/)
* [DRF Unit Tests] - [Testing](https://www.django-rest-framework.org/api-guide/testing/)

## ToDo:

Front-end work
