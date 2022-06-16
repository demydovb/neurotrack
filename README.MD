# neurotrack test assignment
Flask application for simulation vending machine.

## How to start application:

* Clone repository.
* Change directory to repo's directory.
* Create virtualenv ([instructions](https://docs.python.org/3/library/venv.html)).
* Install dependencies `pip install -r requirements`
* Start application `flask run`
* Visit web page http://127.0.0.1:5000/

## Remark:

* Tested with Python 3.9.5.

## Things to improve:

To simplify the app, there are a lot of shortcuts. What I would change if I had more time:

* Add unittests.
* Add CSS.
* Instead of using url parameters for storing data, use JS and AJAX to send to
backend inserted coin ( instead of url parameter), create record in DB for every order or 
  store total amount of inserted coins and item in session.
* Instead of hardcoded items, create table in DB for available items.
* Store secret key as OS variable.
* Wrap application inside Docker container.