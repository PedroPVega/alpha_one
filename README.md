# Alpha One
---
Authentification service built with Python, FastAPI, pydantic and bcrypt.

## Table of contents
- [Requirements](#requirements)
- [Status](#project-status)
- [Stack](#tech-stack)
- [Use cases](#current-use-cases)
- [**Setup**](#installation--setup)
- [**Containerization**](#containerization)

## Requirements
| Asset | version |
| --- | --- |
| uv | latest |
| python | v3.13 |

## Project status
Free time project I made to showcase some of my skill in using Python's FastAPI.<br>
Here I showcase my ease with handling pydantic classes, fastapi's routers and restful API's.<br>
The service at it's current state isn't without it's limits. Here are a few of them:
- At each new implementation every endpoint must be retested
- The database are currently just lists that reset at every app restart. 
- Bare minimum endpoints currently in place.
- OpenAPI documentation could be better

So these are the solutions that must be made:
- CI/CD workflow file with test pipeline
- Unit tests with pytest
- Create real db connection with a sqllite or postgres container
- Some endpoints ideas : User preferences customization, password change, admin actions in DB

## Tech stack
- UV
- Python 3.13
- bcrypt v5.0.0
- fastapi
- pydantic
- pyjwt

## Current use cases
- User creation on signin
- Session start at signin and login
- Access token refreshment with session token
- Session token invalidity at client logout
- List of users registered consultation 

## Installation / Setup
Clone this repo and running by executing:
``` bash
git clone https://github.com/PedroPVega/alpha_one.git
cd alpha_one
uv sync
source .venv/bin/activate
cp .env.example .env 
uv run uvicorn src.app:app --port 8080
```
**WARNING** : Server will crash if env variables missing and/or your jwt key is not long enough

## Containerization
In order to build the image: open docker, open the terminal and travel to /alpha_one.<br>
Then execute:
```bash
docker build -t alpha-one:1.0 .
```
---
In order to create and run a container containing this image, execute:
```bash
docker run -e JWT_ALG=HS256 -e JWT_KEY=your-key -p 8080:8080 alpha-one:1.0
```
**WARNING** : container will fail to run if your jwt key is not long enough

---
**To access the swagger UI**, type in your browser:
http://127.0.0.1:8080/docs