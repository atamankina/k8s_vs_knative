#!/usr/bin/env bash

ssh -i .ssh/gal_ec2_keypair.pem ec2-user@ec2-3-86-67-102.compute-1.amazonaws.com

export KOPS_CLUSTER_NAME=galina.k8s.local
export KOPS_STATE_STORE=s3://galina-kops-state

aws resourcegroupstaggingapi get-resources --tag-filters "Key=KubernetesCluster,Values=galina.k8s.local"
