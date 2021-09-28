# start from base
FROM python:3.8-slim
LABEL maintainer="Mandar Dindorkar"
# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./code /app
EXPOSE 5000
CMD [ "python", "./app.py" ]
