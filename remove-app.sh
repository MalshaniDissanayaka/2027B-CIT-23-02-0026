#!/bin/bash
echo "Removing app..."
docker-compose down -v --rmi all --remove-orphans
