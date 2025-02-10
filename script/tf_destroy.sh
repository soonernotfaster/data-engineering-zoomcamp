#!/usr/bin/env bash

WORK_DIR="module_1/terra_demo"

pushd $WORK_DIR
terraform destroy --var-file=./deploy.tfvars --state=tf_state/terraform.tf_state
popd