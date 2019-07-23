#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
gunicorn --bind 0.0.0.0:5000 --workers=4 wsgi:app

docker build -t atamankina/reviews:latest .
docker push atamankina/reviews:latest

docker build -t atamankina/reviews-knative:latest .
docker push atamankina/reviews-knative:latest

docker build -t atamankina/reviews-k8s:latest .
docker push atamankina/reviews-k8s:latest

echo -n 'input' | openssl base64

kubectl apply -f namespace.yaml
kubectl apply -f postgres-credentials.yaml
kubectl apply -f postgres-deployment.yaml
kubectl apply -f postgres-service.yaml
kubectl apply -f app-deployment.yaml
kubectl apply -f app-service.yaml

locust -f task_sets.py --no-web -c 1000 -r 100 --run-time 1h30m
locust -f task_sets.py SingleReadSlow