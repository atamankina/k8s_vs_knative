#!/usr/bin/env bash

export FLASK_ENV=development
export DATABASE_URL=postgres://atamanki:@localhost:5432/restaurant_reviews
export SECRET_KEY=123

pip install -r requirements.txt
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
gunicorn --bind 0.0.0.0:5000 --workers=4 wsgi:app

docker build -t atamankina/reviews:latest .
docker push atamankina/reviews:latest

echo -n 'input' | openssl base64

kubectl apply -f namespace.yaml
kubectl apply -f app-deployment.yaml
kubectl apply -f app-service.yaml

kubectl get service -n k8s-test

kubectl autoscale deployment reviews-app-webserver -n k8s-test --cpu-percent=45 --min=2 --max=10

locust -f task_sets.py --no-web -c 1000 -r 100 --run-time 1h30m
locust -f task_sets.py SingleReadSlow