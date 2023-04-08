## Project Aim

To:
- Build and deploy a container (Flask application) to an Azure Web App
- Build a Flask project with a REST API
- Handle HTTP requests with Connexion
- Define API endpoints using the OpenAPI specification
- Interact with my API to manage data
- Build API documentation with Swagger UI and Connexion
- Configure a SQLite database for my Flask project
- Use SQLAlchemy to save Python objects to my database
- Leverage the Marshmallow library to serialize data

[Tutorial](https://realpython.com/flask-connexion-rest-api/)

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

<!-- - Setup a Virtual machine and install [GitHub](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-20-04#setting-up-git).

- In the Azure CLI, create a service principal
```bash
$ az ad sp create-for-rbac --name "<name>" --role contributor --scopes <path to resource group> --sdk-auth 
```

Upon running the above command, a JSON response will be generated. Add this response to your GitHub secrets with the name ```AZURE_CREDENTIALS```.

- This [article](https://www.rosehosting.com/blog/how-to-deploy-flask-application-with-nginx-and-gunicorn-on-ubuntu-20-04/) provides a guide for  hosting this application on Nginx.

- Read [me](https://stackoverflow.com/questions/29679963/why-gunicorn-command-not-found-with-gunicorn-installed) fix gunicorn issues. -->

## Local setup
- Activate virtual environment and install dependencies
```bash
$ cd Part_1
$ source virtualenv/bin/activate
$ pip install requirements.txt
```

- Run project
```bash
$ python main.py
```

- Run tests
```bash
$ pytest tests
```

- Dockerizing the Application
```bash
$ docker image build -t <image-name> .
$ docker run -p port:port -d <image-name>
```

- To pull the container from Dockerhub
```bash
$ docker pull note_app
$ docker run -p port:port -d <image-name>
```

Failing Build -> cannot merge into main
<img width="915" alt="image" src="https://user-images.githubusercontent.com/49791498/210520306-81c5f381-27f2-4569-a198-a6dce7ff8c3b.png">

Passing Build -> can merge into main
<img width="915" alt="image" src="https://user-images.githubusercontent.com/49791498/210520789-e4d6931c-6506-4d98-92cd-3e98efd6838b.png">

### Routes
- ```GET /api/people```
- ```GET /api/ui```
- ```GET /api/home```
- ```POST /api/person```
- ```DELETE /api/person```

### Deploying the Application to Azure App Service
- [GitHub Actions Guide](https://learn.microsoft.com/en-us/azure/app-service/deploy-container-github-action?tabs=publish-profile)
- [Azure App Service Guide](https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal)
- Deployed application
<image>
<!-- <img width="1258" alt="image" src="https://user-images.githubusercontent.com/49791498/213863870-d04a9bbe-9169-428a-a61a-8431dd048d11.png"> -->

