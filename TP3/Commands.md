1.3 docker build -t flaskappv0 .
1.4 Docker-compose up
1.5 Go to http://127.0.0.1:5000/date et :80

2.1 cd /flask-api-user
    Create new Dockerfile
    from flaskappv0:latest
    RUN useradd -m newuser 
    RUN su - newuser 
2.2 Modifier Docker-compose    
     healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/date"] 
      interval: 3s       # Time between health checks
      timeout: 10s        # Time before a health check times out
      retries: 3          # Number of retries before marking as unhealthy
      start_period: 10s   # Initial delay before starting health checks
    
    . docker build -t newuserapp .
    . docker-compose up

3. Apres changement de docker file et docker compose on Répète 
    .docker build-t newuserapplocal . 
    . docker-compose up