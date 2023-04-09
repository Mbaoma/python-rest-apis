FROM python:alpine3.17

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install swagger-ui-bundle

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"]