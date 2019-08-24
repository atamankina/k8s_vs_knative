#*** before all
gcloud auth login
gcloud config set project rosy-sunspot-246115
gcloud config set project eighth-study-243122
gcloud config set compute/zone europe-west6-c
gcloud config get-value project
gcloud config get-value core/account
gcloud config get-value compute/zone

#*** finally
gcloud container clusters delete $CLUSTER_NAME

#*** 0
export CLUSTER_NAME=knative-thesis
export CLUSTER_NAME=k8s-thesis
export CLUSTER_ZONE=europe-west6-c
export PROJECT=rosy-sunspot-246115
export PROJECT=eighth-study-243122
gcloud config set core/project $PROJECT

#*** 1
gcloud beta container clusters create $CLUSTER_NAME \
  --addons=HorizontalPodAutoscaling,HttpLoadBalancing,Istio \
  --machine-type=n1-standard-2 \
  --cluster-version=latest --zone=$CLUSTER_ZONE \
  --enable-stackdriver-kubernetes --enable-ip-alias \
  --enable-autoscaling --min-nodes=1 --max-nodes=3 \
  --enable-autorepair \
  --scopes cloud-platform

kubectl create clusterrolebinding cluster-admin-binding \
     --clusterrole=cluster-admin \
     --user=$(gcloud config get-value core/account)

#*** 2
kubectl apply --selector knative.dev/crd-install=true \
   --filename https://github.com/knative/serving/releases/download/v0.6.0/serving.yaml \
   --filename https://github.com/knative/build/releases/download/v0.6.0/build.yaml \
   --filename https://github.com/knative/eventing/releases/download/v0.6.0/release.yaml \
   --filename https://github.com/knative/eventing-sources/releases/download/v0.6.0/eventing-sources.yaml \
   --filename https://github.com/knative/serving/releases/download/v0.6.0/monitoring.yaml \
   --filename https://raw.githubusercontent.com/knative/serving/v0.6.0/third_party/config/build/clusterrole.yaml

kubectl apply --filename https://github.com/knative/serving/releases/download/v0.6.0/serving.yaml \
   --filename https://github.com/knative/build/releases/download/v0.6.0/build.yaml \
   --filename https://github.com/knative/eventing/releases/download/v0.6.0/release.yaml \
   --filename https://github.com/knative/eventing-sources/releases/download/v0.6.0/eventing-sources.yaml \
   --filename https://github.com/knative/serving/releases/download/v0.6.0/monitoring.yaml \
   --filename https://raw.githubusercontent.com/knative/serving/v0.6.0/third_party/config/build/clusterrole.yaml

#*** 3
kubectl get svc istio-ingressgateway --namespace istio-system


#*** other
gcloud beta container --project "rosy-sunspot-246115"
clusters create "standard-cluster-1"
--zone "europe-west6-c"
--no-enable-basic-auth --cluster-version "1.12.8-gke.10"
--machine-type "n1-standard-1" --image-type "COS"
--disk-type "pd-standard" --disk-size "100"
--scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append"
--num-nodes "3"
--enable-cloud-logging --enable-cloud-monitoring
--no-enable-ip-alias
--network "projects/rosy-sunspot-246115/global/networks/default"
--subnetwork "projects/rosy-sunspot-246115/regions/europe-west6/subnetworks/default"
--addons HorizontalPodAutoscaling,HttpLoadBalancing
--enable-autoupgrade
--enable-autorepair
