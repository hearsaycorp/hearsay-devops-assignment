# Hearsay DevOps Assignment

## Introduction

Welcome to the DevOps assignment part of your Hearsay journey! In this repo we
present you with a small set of tasks that will help us assess your skill level
with various tools and technologies.

The assignment should take less than 2 hours to complete, please timebox yourself
to this timeframe.

We created some boilerplate for you which includes:

* a Python Flask API web application package with requirements
* `pytest` tests for the web application
* an Nginx configuration with its' corresponding `Dockerfile-nginx`
* two Github actions to run the tests and the linter
* a Github workflow file skeleton

Some of these might have issues which you should fix in order to have a working
solution.

## First steps

As a first step you should create a new **private repository** of your own from
this template. To do so click the green `Use this template` button and then
select `Create a new repository`, from then set yourself as `Owner` give a name
to the repo and **click the radio button next to `Private`** to make it private.

Once the repository is created make sure that Dependabot alerts are enabled under
Settings/Security/Code security. 

## Tasks

From here you can proceed with the following tasks:
* write two endpoints for the Flask app based on the tests and make sure it works 
  with the Nginx config
* write a `Dockerfile` which is able to run the Python application inside a Docker
  container
* minimize the size of the built Docker web app image
* write a `docker-compose.yml` to run and connect the two services and expose the
  web application through Nginx (use the provided `Dockerfile-nginx` to build the
  Nginx image)
* finish the `build` Github workflow job which should:
  - automatically start upon git pushes but can be started manually too 
  - build the web application image
  - print the size of the built image
  - start the two services using `docker-compose` 
  - print the responses and status codes from the two endpoins
* make sure that the tests pass and the liner reports no issues
* ensure that no temporary files can get pushed to git
* fix any other issues that you might encounter

## Wrap up

When you successfully finished the assignment or your time has ran out it's time
to submit the link to your repository while also sharing it with us. Go to
`Settings`, in the left panel click `Collaborators` and add the following
users:

* csizmaziakiki
* lopezm1
* renegillson
