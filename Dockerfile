FROM python

RUN apt-get update -y
RUN apt-get install -y build-essential
RUN pip install --upgrade pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/app/starter.py"]