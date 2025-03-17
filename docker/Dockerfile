FROM python:3

WORKDIR /microservice-user
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY app/ app/
COPY main.py .

CMD ["python", "main.py"]