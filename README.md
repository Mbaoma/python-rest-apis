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

## Local setup
- Activate virtual environment and install dependencies
```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

- Run project
```bash
$ python run.py
```

- Dockerizing the Application
```bash
$ docker image build -t <image-name> .
$ docker push <repo>/<image-name> 
$ docker run -p port:port -d <image-name>
```

- To pull the container from Dockerhub
```bash
$ docker pull mbaoma/note-app
$ docker run -p port:port -d <image-name>
```

### Deploying the Application to Azure App Service

#### Manual Deployment
- Push your container to [Azure Registry](https://learn.microsoft.com/en-us/azure/app-service/tutorial-custom-container?tabs=azure-portal&pivots=container-linux)

- Create a web app under the Azure app services panel.

<img width="1157" alt="image" src="https://user-images.githubusercontent.com/49791498/230750952-23d617c4-b1d6-4597-a5ea-5e8f94c5aff0.png">

- Select what container registry your container is hosted in

<img width="1158" alt="image" src="https://user-images.githubusercontent.com/49791498/230754141-76389ddc-50fb-4b84-85b9-f497f7b98020.png">

- Create the web app and wait a while before checking the logs, to  determine the state of your container.

- Navigate to your app's URL to view the eployed application

https://brandnew7.azurewebsites.net/
<img width="1313" alt="image" src="https://user-images.githubusercontent.com/49791498/230754405-4cd12ea1-5371-4999-87c3-d7085eeac522.png">

-- ```/api/ui (swagger UI)```
https://brandnew7.azurewebsites.net/api/ui/
<img width="1313" alt="image" src="https://user-images.githubusercontent.com/49791498/230754246-5e796a2a-3254-4987-806d-16710c54447a.png"> 





