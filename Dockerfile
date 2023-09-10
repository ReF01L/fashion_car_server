FROM python:3.11

RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client && rm -rf /var/lib/apt/lists/*

ENV PATH="${PATH}:/"

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

RUN chown 0600 .pgpass

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]