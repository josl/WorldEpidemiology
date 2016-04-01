# Dockerizing MongoDB: Dockerfile for building MongoDB images
# Based on ubuntu:latest, installs MongoDB following the instructions from:
# http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/

# Set base image to NodeJS
FROM node:latest
# File Author / Maintainer
MAINTAINER Jose Luis Bellod Cisneros

RUN mkdir /root/.ssh/
RUN ssh-keyscan registry.npmjs.org >> /root/.ssh/known_hosts

RUN mkdir /code
WORKDIR /code
# Replace by a git clone
COPY . /code
WORKDIR /code/backend
RUN npm install
# RUN node /code/scripts/WDIexcelToMongo.js
# RUN grunt buildProduction
