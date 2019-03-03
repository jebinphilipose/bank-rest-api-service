# Bank REST API Service ([Live Version](https://bank-rest-api-service.herokuapp.com/))

## Project Overview

Create a REST service that can:
1. Given a bank branch IFSC code, get branch details
2. Given a bank name and city, gets details of all branches of the bank in the city

Note: Data available in this [repository](https://github.com/snarayanank2/indian_banks) is used in the backend database

## Getting Started

### Prerequisites

* Python 3.0
* pip
* virtualenv
* Git

### Project Setup

1. Create a virtual environment: `python3 -m venv myvenv && cd myvenv`
2. Activate virtualenv: `source bin/activate`
3. Clone this repo: `git clone https://github.com/jebinphilipose/bank-rest-api-service.git && cd bank-rest-api-service`
4. Upgrade pip and install dependencies: `pip install --upgrade pip && pip install -r requirements.txt`
5. Change **DBNAME**, **DBUSER** & **DBPASS** accordingly in `database_setup.sh`
6. Setup database and create initial records: `bash database_setup.sh`
7. Create a `.env` file and set **SECRET_KEY**, **ALLOWED_HOSTS**, **DEBUG**, **DB_NAME**, **DB_USER** & **DB_PASS**. See this [article](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html) for more details
8. Run the server: `python manage.py runserver`
9. Access webpage at [http://localhost:8000/](http://localhost:8000/)


## API Endpoints

* `GET /api/v1/branch/<ifsc>/` --> Returns JSON of a particular branch given its IFSC code
* `GET /api/v1/bank/<bank-name>/city/<city>/` --> Returns JSON of all the branches given a bank name and a city