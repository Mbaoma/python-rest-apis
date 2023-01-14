[Tutorial](https://realpython.com/flask-connexion-rest-api/)

## Aim
To:
- Build a base Flask project with a REST API
- Handle HTTP requests with Connexion
- Define API endpoints using the OpenAPI specification
- Interact with my API to manage data
- Build API documentation with Postman

## The REST API
Provides access to a collection of people and to the individuals within that collection.

### API Definition
| Action | HTTP Verb | URL Path | Description |
|------- | ----------| -------  |-----------  |
| Read   | GET    |  /api/people | Read information on people
| Create | POST  | /api/people | Create a new person's data
| Read   | GET  | /api/people/<lname> | Read information on a person
| Update | PUT | /api/people/<lname> | Update a person's information
| Delete | DELETE  | /api/people/<lname> | Delete a person's inforrmation

## Setting up CI/CD using GitHub Actions
- There is a branch protection rule set for the main branch - you cannot push directly to the main branch.

- In the  CI pipeline, unless all [tests](https://testdriven.io/blog/flask-pytest/) run successfully, you cannot merge code into the main branch.
**Resources**: [Test Routes](https://dev.to/po5i/how-to-add-basic-unit-test-to-a-python-flask-app-using-pytest-1m7a)

# Steps to run
- Activate virtual environment and install dependencies
```bash
$ source virtualenv/bin/activate
$ pip install requirements.txt
```

- Run project
```bash
python3 app.py
```

- Run tests
```bash
pytest tests
```

Failing Build -> cannot merge into main
<img width="915" alt="image" src="https://user-images.githubusercontent.com/49791498/210520306-81c5f381-27f2-4569-a198-a6dce7ff8c3b.png">

Passing Build -> can merge into main
<img width="915" alt="image" src="https://user-images.githubusercontent.com/49791498/210520789-e4d6931c-6506-4d98-92cd-3e98efd6838b.png">

### Routes
- -  ``` GET http://192.168.0.173:8000/```
<img width="1076" alt="image" src="https://user-images.githubusercontent.com/49791498/212395341-38ed8f55-79cd-4635-b3c0-f9c6c7f9ee9a.png">

- ```GET /api/people```
<img width="546" alt="image" src="https://user-images.githubusercontent.com/49791498/211180090-e6b105cf-57bb-498b-8998-3b08aea6826e.png">

- ```GET /api/ui```
<img width="1385" alt="image" src="https://user-images.githubusercontent.com/49791498/211180113-84ed10dd-b073-4114-9e12-dc07abfeba2c.png">

- ```GET http://192.168.0.173:8000/api/ui/#/People/people.read_all_people```
<img width="1376" alt="image" src="https://user-images.githubusercontent.com/49791498/212396243-e19f61c6-169a-46c5-a398-23aa4ba212cc.png">

- ```GET /api/home```
<img width="788" alt="image" src="https://user-images.githubusercontent.com/49791498/212398020-8f5e859e-d9fb-43cb-a80b-3ef081669775.png">

- ```POST /api/person```
<img width="826" alt="image" src="https://user-images.githubusercontent.com/49791498/212449224-047dbdac-1e21-4722-8cec-40f4ea50617e.png">

**expected response**
<img width="826" alt="image" src="https://user-images.githubusercontent.com/49791498/212449250-0b93ab28-1bed-41cc-bc95-3396ec84929e.png">

**error response**
<img width="712" alt="image" src="https://user-images.githubusercontent.com/49791498/212449812-143a852c-f901-4dbe-a7a0-45fab96ccab3.png">
