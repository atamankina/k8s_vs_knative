#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
gunicorn --bind 0.0.0.0:5000 --workers=4 wsgi:app

docker build -t atamankina/reviews:latest .
docker push atamankina/reviews:latest

echo -n 'input' | openssl base64

kubectl apply -f namespace.yaml
kubectl apply -f postgres-credentials.yaml
kubectl apply -f postgres-deployment.yaml
kubectl apply -f postgres-service.yaml
kubectl apply -f app-deployment.yaml
kubectl apply -f app-service.yaml


export KOPS_CLUSTER_NAME=galina.k8s.local
export KOPS_STATE_STORE=s3://galina-kops-state

aws resourcegroupstaggingapi get-resources --tag-filters "Key=KubernetesCluster,Values=galina.k8s.local"