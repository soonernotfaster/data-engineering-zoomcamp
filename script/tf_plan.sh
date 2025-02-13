#!/usr/bin/env bash

WORK_DIR="01-docker-terraform/terra_demo"

pushd $WORK_DIR
terraform plan --var-file=./deploy.tfvars
popd