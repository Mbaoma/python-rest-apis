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

## Setting up CI/CD using  GitHub Actions
- There is a branch protection rule set for the main branch. 
- In the  CI pipeline, unless all [tests](https://testdriven.io/blog/flask-pytest/) run successfully, a pull request (PR) cannot be made to the  main branch.
**Resources**: [Test Routes](https://medium.com/analytics-vidhya/how-to-test-flask-applications-aef12ae5181c)
# Steps to run
- Activate virtual environment and install dependencies
```bash
$ source virtualenv/bin/activate
$ pip install requirements.txt
```