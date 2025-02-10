#!/usr/bin/env bash

WORK_DIR="module_1/terra_demo"

pushd $WORK_DIR
terraform plan --var-file=./deploy.tfvars
popd