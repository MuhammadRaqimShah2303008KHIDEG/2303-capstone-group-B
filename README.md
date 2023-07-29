# Capstone_Emeritus
# 2303-capstone-group-B
# Our Task
- Online vs in-person appointments. PeaceOfMind would offer online appointments as
well. We'd use user's (both doctor's and patient's) location data, external APIs
(perhaps Google Maps API or similar, we'd need to research that a bit) and compare
how much time, money and greenhouse gases emissions they are saving by having
an online appointment instead of an in-person one.

### Table of Contents
- Team Members
- Getting Started
    - Prerequisites
    - Installation
    - Configuration
    - Usage

## Team Members
- Muhammad Talha
- Umaima Siddiqui
- Muhammad Hussam
- Syed Raqim Ali Shah
- Huzaifa Ali

## Getting Started
These instructions will help you set up the project on your local machine for development and testing purposes.

## Prerequisites
Before setting up the project, make sure you have the following installed:

- Docker [a installation guide](https://docs.docker.com/get-docker/)
- Docker Compose [a installation guide](https://docs.docker.com/compose/install/)

## Installation
To install the project, follow these steps:
- Clone the repository: `git clone https://github.com/talha660033/2303-capstone-group-B.git`
- Change to the project directory: `cd 2303-capstone-group-B`

## Configuration
The project requires some configuration files to run properly. Follow these steps to set up the configuration:
- Create a config.py file in the project src/fuel_service/ directory
- add the following code in it
```
FUEL_URL = "https://www.globalpetrolprices.com/"
REDIS_HOST ="redis"
REDIS_PORT = 6379

```
- Save the file
- Create one more config.py file in the project src/online_vs_inperson_comparison_service/ directory
- add the following code in it
```
PATIENT_URL="https://xloop-dummy.herokuapp.com/patient/"
COUNCILLOR_URL="https://xloop-dummy.herokuapp.com/councillor/"
ACCOUNT_URL="https://xloop-dummy.herokuapp.com/account/"
ROUTE_URL="https://api.tomtom.com/routing/1/calculateRoute/"
API_KEY = "HamdIRQ6ZeNJZj69Gy2Rru0VCqe04EoK"
PRICES_URL = "http://fuel-service:8001/fuel-price/"

```
- Save the file

## Usage

Add 

>src
 >fuel_service
  >config.py
  		FUEL_URL = "https://www.globalpetrolprices.com/"
		REDIS_HOST ="redis"
		REDIS_PORT = 6379
		
 >online_vs_inperson_comparison_service
  >config.py
   		PATIENT_URL="https://xloop-dummy.herokuapp.com/patient/"
		COUNCILLOR_URL="https://xloop-dummy.herokuapp.com/councillor/"
		ACCOUNT_URL="https://xloop-dummy.herokuapp.com/account/"
		ROUTE_URL="https://api.tomtom.com/routing/1/calculateRoute/"
		API_KEY = "HamdIRQ6ZeNJZj69Gy2Rru0VCqe04EoK"
		PRICES_URL = "http://fuel-service:8001/fuel-price/"



To start the project using Docker Compose, run the following command:

` docker-compose up --build `

## Disclaimer
This project is a collaborative effort of team Data Mavericks.
