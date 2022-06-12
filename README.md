# Pokemon Crawler

## Design

The pokemon crawler is implemented as a Django admin command which can be run to create or update pokemon. The pokemon and their characteristics are displayed on the Django admin site.

The crawler queries the pokemon API with limit of 20 (the API's default) within a loop that will continue querying the API with an updated offset until all the pokemon have been caught. A generator is yielded from the while loop; this is iterated through to process each pokemon. I considered an asynchronous implementation (e.g. using asyncio to query multiple URLs starting with different offsets) but since there were no explicit time requirements for pokemon-catching I decided to prioritize simplicity.

I implemented some simple unit tests for the crawler, but with more time would have finished the unit test coverage, included unit tests for the models, and possibly added an integration test.

To make the crawler more robust I would add validation for the pokemon API response, retries for HTTP requests, the ability to pause/resume the crawler (e.g. by storing the current offset), and improve the error handling.

## Running the app

#### Start the application

```
docker-compose up
```

#### Run migrations

```
docker-compose exec web python manage.py migrate
```

#### Create an admin user

```
docker-compose exec web python manage.py createsuperuser
```

#### Catch pokemon

```
docker-compose exec web python manage.py catchpokemon
```

You can view your pokemon at http://0.0.0.0:8000/admin/.

## Running tests

```
docker-compose exec web python manage.py test
```
