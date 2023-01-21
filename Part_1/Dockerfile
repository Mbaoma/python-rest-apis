# our base image
FROM python:3.8-slim-buster

WORKDIR /Part_1

# install Python modules needed by the Python app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy files required for the app to run
COPY . .

# run the application
CMD ["python3", "run.py"]