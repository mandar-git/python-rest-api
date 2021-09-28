FROM python:3.8-slim as builder
COPY . /src
RUN pip install --user boto3 flask

FROM python:3.8-slim as app
COPY --from=builder /src /app
COPY /code /app
WORKDIR /app
EXPOSE 5000
CMD ["python3", "app.py"]
