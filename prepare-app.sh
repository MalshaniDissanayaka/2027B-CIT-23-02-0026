#!/bin/bash
echo "Preparing app..."
docker network create todo-net || true
docker volume create todo-db-data || true
docker build -t todo-web ./app
