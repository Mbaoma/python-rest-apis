[Tutorial](https://realpython.com/flask-connexion-rest-api/)

## Aim
To:
- Build a base Flask project with a REST API
- Handle HTTP requests with Connexion
- Define API endpoints using the OpenAPI specification
- Interact with my API to manage data
- Build API documentation with Swagger UI and Connexion
- Set up Continuous Integration and Continuous Deployment (CI/CD)
- Extensively test the API endpoints

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

- Setup a Virtual machine and install [GitHub](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-20-04#setting-up-git).

- In the Azure CLI, create a service principal
```bash
az ad sp create-for-rbac --name "<name>" --role contributor --scopes <path to resource group> --sdk-auth 
```bash```

Upon running the above command, a JSON response will be generated. Add this response to your GitHub secrets with the name ```AZURE_CREDENTIALS```.

- This [article](https://www.rosehosting.com/blog/how-to-deploy-flask-application-with-nginx-and-gunicorn-on-ubuntu-20-04/) provides a guide for  hosting this application on Nginx.

- Read [me](https://stackoverflow.com/questions/29679963/why-gunicorn-command-not-found-with-gunicorn-installed) fix gunicorn issues.

-- In the ``` /etc/systemd/system/flask.service```file, add
```bash
[Unit]
Description=Gunicorn to serve Flask App
After=network.target

[Service]
User=azureuser
Group=www-data
WorkingDirectory=/home/azureuser/python-rest-apis
Environment="PATH=/home/azureuser/python-rest-apis/Part_1/virtualenv/bin"
ExecStart=gunicorn --bind 0.0.0:80 wsgi:app

[Install]
WantedBy=multi-user.target
```

## Steps to run
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
- ```GET /api/people```
<img width="546" alt="image" src="https://user-images.githubusercontent.com/49791498/211180090-e6b105cf-57bb-498b-8998-3b08aea6826e.png">

- ```GET /api/ui```
<img width="1385" alt="image" src="https://user-images.githubusercontent.com/49791498/211180113-84ed10dd-b073-4114-9e12-dc07abfeba2c.png">

- ```GET /api/home```
<img width="788" alt="image" src="https://user-images.githubusercontent.com/49791498/212398020-8f5e859e-d9fb-43cb-a80b-3ef081669775.png">

- ```POST /api/person```
<img width="826" alt="image" src="https://user-images.githubusercontent.com/49791498/212449224-047dbdac-1e21-4722-8cec-40f4ea50617e.png">

**expected response**
<img width="826" alt="image" src="https://user-images.githubusercontent.com/49791498/212449250-0b93ab28-1bed-41cc-bc95-3396ec84929e.png">

**error response**
<img width="712" alt="image" src="https://user-images.githubusercontent.com/49791498/212449812-143a852c-f901-4dbe-a7a0-45fab96ccab3.png">

- ```PUT /api/person```
<img width="1358" alt="image" src="https://user-images.githubusercontent.com/49791498/212667394-d4f158cb-805a-4293-81ee-7478324ac714.png">

<img width="1323" alt="image" src="https://user-images.githubusercontent.com/49791498/212667500-18fc3ea2-500c-43ec-8d6f-24cf07d159db.png">

- ```DELETE /api/person```
<img width="1348" alt="image" src="https://user-images.githubusercontent.com/49791498/212667715-ef17261f-340c-44b0-9da8-da1cc884cc81.png">

<img width="1340" alt="image" src="https://user-images.githubusercontent.com/49791498/212667794-49645424-1563-4db4-9240-2798bdeb55d4.png">
