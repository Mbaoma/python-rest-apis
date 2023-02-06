FROM python:alpine3.17

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN pip3 install "connexion[swagger-ui]"

COPY . .

CMD ["python3", "run.py"]