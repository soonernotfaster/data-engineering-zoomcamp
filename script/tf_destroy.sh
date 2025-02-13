#!/usr/bin/env bash

WORK_DIR="01-docker-terraform/terra_demo"

pushd $WORK_DIR
terraform destroy --var-file=./deploy.tfvars --state=tf_state/terraform.tf_state
popd