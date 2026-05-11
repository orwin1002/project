print("Hello World")
print("Updated Code")





























git --version
mkdir project
cd project
git init
nano demo.py
print("Hello World")
git status
git add demo.py
git status
git commit -m "first commit"
git log
nano demo.py
print("Hello World")
print("Updated Code")
git diff
git add demo.py
git diff --staged
git commit -m "updated code"
git remote -v
git remote add origin https://github.com/yourusername/project.git
git remote -v
git push -u origin master
git config --global user.name "Your Name"
git config --global user.email "yourmail@gmail.com"




mkdir monitoring
cd monitoring
nano prometheus.yml

global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

nano docker-compose.yml
version: '3'

services:

  prometheus:
    image: prom/prometheus
    container_name: prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana
    container_name: grafana
    ports:
      - "3000:3000"

sudo docker compose up -d
sudo docker ps

http://localhost:9090
http://localhost:3000

up
prometheus_http_requests_total
process_resident_memory_bytes
process_cpu_seconds_total
sudo docker compose down





kubectl run my-pod --image=nginx --restart=Never
kubectl get pods
kubectl get pod my-pod -o wide
kubectl expose pod my-pod --type=NodePort --port=80 --name=my-service
kubectl get services
minikube service my-service --url
kubectl delete service my-service
kubectl delete pod my-pod
kubectl create deployment my-deployment --image=nginx --replicas=2
kubectl get pods
kubectl get deployment
kubectl expose deployment my-deployment --type=NodePort --port=80
minikube service my-deployment
minikube service my-deployment --url
kubectl scale deployment my-deployment --replicas=5
kubectl get pods
kubectl get pods
kubectl get pods
kubectl delete pod my-deployment-5f8fc99b79-5tpl4
kubectl delete pod my-deployment-5f8fc99b79-b87vt
kubectl delete pod my-deployment-5f8fc99b79-mvn66
kubectl get pods
kubectl delete deployment my-deployment
kubectl get pods
minikube stop




sudo su -

docker images

docker run hello-world

docker pull nginx

docker run -d -p 8000:80 nginx

docker ps

docker ps -a

docker stop <container_id>

docker start <container_id>

docker restart <container_id>

docker run -d -p 7000:80 --name my-nginx nginx

docker exec -it my-nginx bash

cd /usr/share/nginx/html/

ls

nano index.html

<h1>Hello World!</h1>
<h2>My Name is Raweena</h2>

exit

docker stop my-nginx

docker rm my-nginx

docker rmi nginx

sudo su -

cd Documents

mkdir pythonproj

cd pythonproj

mkdir templates

nano app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Flask App"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

cd templates

nano index.html

<h1>Welcome to My Flask App</h1>
<p>This is the home page</p>

cd ..

python3 app.py

http://localhost:5000

nano DockerfileFROM python:3-alpine3.15

WORKDIR /app

COPY . /app

RUN pip install flask

CMD ["python3", "app.py"]

sudo docker build -t myimage:1 .

sudo docker images

sudo docker run -p 8000:5000 myimage:1

http://localhost:8000

sudo docker images

sudo docker tag myimage:1 raweena/dockerimage

sudo docker login -u raweena

sudo docker push raweena/dockerimage

docker logout




PART 1 — Start Jenkins (Terminal Commands)

These are the only important commands you should know.

Update system
sudo apt update

Start Jenkins
sudo systemctl start jenkins
Enable Jenkins
sudo systemctl enable jenkins
Check status
sudo systemctl status jenkins
PART 2 — Open Jenkins in Browser

Open:

http://localhost:8080

Then:

Enter admin password
Install suggested plugins

Suggested Plugins
Build Pipeline Plugin

Open Jenkins dashboard
PART 3 — Integrate Jenkins with Git

This is MOST IMPORTANT for your portion.

Create Job1
Steps:
Click New Item
Give name:
git_job1
Select:
Freestyle Project
Click OK
Configure Git

Inside job configuration:

Source Code Management

Select:

Git

Paste GitHub repo URL:

https://github.com/username/repository.git

(Use your own repo)

Build Step

Add:

Execute Shell

Example command:

echo "Hello Jenkins"

Save.

Build Job

Click:

Build Now

If success → green tick.

PART 4 — Create Job2

This is from your teacher’s file.

Create another freestyle job

Name:

job2
Build Trigger

Select:

Build after other projects are built

Choose:

git_job1
Execute Shell

Add:

date

or

echo "Current date and time"
date

Save.

PART 5 — Install Pipeline View Plugin

This is the browser/plugin part.

Go to:
Manage Jenkins → Plugins

Search:

Build Pipeline

Install plugin.

PART 6 — Create Pipeline View
Steps
Click +
Enter view name
Select:
Build Pipeline View
Create
Configure Pipeline

Set:

Initial Job = git_job1

Save.

PART 7 — Connect Job1 → Job2

Open:

git_job1 → Configure
Add Post Build Action

Select:

Build other projects

Enter:

job2

Save.

PART 8 — Run Pipeline

Now click:

Build Now

Result:

Job1 runs
Automatically Job2 runs
Pipeline becomes green

This is the final output your examiner wants.

