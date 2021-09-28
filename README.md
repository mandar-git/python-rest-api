# python-rest-api
A sample python flask rest API with docker



code()
### Build the docker image from Dockerfile ###
docker build -t flask-app . 

### Check Docker images on host ###
docker images
REPOSITORY   TAG        IMAGE ID       CREATED         SIZE
flask-app    latest     6204c64ac214   9 minutes ago   152MB
ubuntu       18.04      54919e10a95d   4 weeks ago     63.1MB


### Run docker image as a container ###

`docker run -p 5000:5000 flask-app`

```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
2021-09-28 15:26:54,557 WARNING werkzeug MainThread :  * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
2021-09-28 15:26:54,557 INFO werkzeug MainThread :  * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
```

`docker run -d -p 5000:5000 flask-app`

`docker ps`
```
CONTAINER ID   IMAGE       COMMAND             CREATED         STATUS         PORTS                                       NAMES
ea1efbaf9e2f   flask-app   "python ./app.py"   9 minutes ago   Up 9 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   suspicious_wescoff
```

`curl http://localhost:5000`
```
Welcome to my bookstore!`
```
`curl http://localhost:5000/v1/books/`
```
[{"book":"Kubernetes up and Running"},{"book":"Database Fundamentals"},{"book":"Let us C"},{"book":"docker up and running"}]
```
`curl http://localhost:5000/v1/books/hightower`
```
{"author":"hightower","title":"Kubernetes up and Running"}
```
`curl http://localhost:5000/v1/books/ritchie`
```
{"author":"ritchie","title":"Let us C"}
```
`curl http://localhost:5000/v1/books/navathe`
```
{"author":"navathe","title":"Database Fundamentals"}
```

`curl -H "Content-Type: application/json" -X POST -d '{"author":"sean","title":"docker up and running"}' http://localhost:5000/v1/books/`
```
{"author":"sean","book":"docker up and running","message":"Added book successfully"}
```
`docker logs ea1efbaf9e2f`
```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
2021-09-28 15:26:54,557 WARNING werkzeug MainThread :  * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
2021-09-28 15:26:54,557 INFO werkzeug MainThread :  * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
2021-09-28 15:26:59,038 INFO werkzeug Thread-1 : 172.17.0.1 - - [28/Sep/2021 15:26:59] "POST /v1/books/ HTTP/1.1" 200 -
2021-09-28 15:27:02,965 INFO flask.app Thread-2 : Getting book by Author
2021-09-28 15:27:02,966 INFO werkzeug Thread-2 : 172.17.0.1 - - [28/Sep/2021 15:27:02] "GET /v1/books/hightower HTTP/1.1" 200 -
2021-09-28 15:27:07,473 INFO flask.app Thread-3 : Getting book by Author
2021-09-28 15:27:07,473 INFO werkzeug Thread-3 : 172.17.0.1 - - [28/Sep/2021 15:27:07] "GET /v1/books/ritchie HTTP/1.1" 200 -
2021-09-28 15:27:10,892 INFO flask.app Thread-4 : Getting book by Author
2021-09-28 15:27:10,892 INFO werkzeug Thread-4 : 172.17.0.1 - - [28/Sep/2021 15:27:10] "GET /v1/books/navathe HTTP/1.1" 200 -
2021-09-28 15:27:19,704 INFO flask.app Thread-5 : Inside Welcome
2021-09-28 15:27:19,710 INFO werkzeug Thread-5 : 172.17.0.1 - - [28/Sep/2021 15:27:19] "GET /welcome HTTP/1.1" 200 -
2021-09-28 15:27:27,571 INFO flask.app Thread-6 : Retrieving list of all books
2021-09-28 15:27:27,571 INFO flask.app Thread-6 : list , iterating book list
2021-09-28 15:27:27,572 INFO werkzeug Thread-6 : 172.17.0.1 - - [28/Sep/2021 15:27:27] "GET /v1/books/ HTTP/1.1" 200 -
2021-09-28 15:27:31,847 INFO werkzeug Thread-7 : 172.17.0.1 - - [28/Sep/2021 15:27:31] "GET / HTTP/1.1" 200 
```

