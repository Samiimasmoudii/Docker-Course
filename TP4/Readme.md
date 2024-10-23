Flask-React App with Load Balancer
This project demonstrates a simple web application with a Flask backend and a React frontend, connected via an NGINX load balancer. The load balancer distributes traffic between two backend instances to ensure availability.

Project Structure
bash
Copy code
project/
├── backend/                # Flask backend code
│   ├── app.py              # Main backend application
│   ├── Dockerfile          # Dockerfile for backend
├── frontend/               # React frontend code
│   ├── src/
│   │   └── App.js          # Main frontend component
│   ├── Dockerfile          # Dockerfile for frontend
├── nginx.conf              # NGINX configuration file for load balancing
└── docker-compose.yml      # Docker Compose file for the whole setup
Prerequisites
Before running this project, ensure you have the following installed:

Docker
Docker Compose
Getting Started
1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/flask-react-load-balancer.git
cd flask-react-load-balancer
2. Build and Run the Project
To start the application, navigate to the project directory and run the following command:

bash
Copy code
docker build -t backend-image ./backend
docker build -t frontend-image ./frontend
docker-compose up --build
This command will:

Build and run two instances of the Flask backend in separate containers (backend1 and backend2).
Build and run the React frontend in a separate container.
Start the NGINX load balancer to route requests to the backend containers.
3. Access the Application
Once the containers are up, you can access the application in your browser:

Frontend: Open http://localhost:3000 to view the React frontend.
Backend API: The NGINX load balancer is available at http://localhost/api. It will route requests to either backend1 or backend2.
The frontend fetches a message from the backend and displays it on the page. If one backend instance goes down, the load balancer will automatically redirect traffic to the other instance.

Project Overview
Backend (Flask)
The Flask backend provides a simple API that returns a message.

File: backend/app.py
Running on: http://localhost:5000
Frontend (React)
The React frontend fetches the message from the Flask backend and displays it.

File: frontend/src/App.js
Running on: http://localhost:3000
Load Balancer (NGINX)
The NGINX load balancer distributes requests between two instances of the backend.

Config: nginx.conf
Running on: http://localhost/api
Stopping the Application
To stop the running containers, use the following command:

bash
Copy code
docker-compose down
This will stop and remove all the containers.

