cat > README.md <<'EOF'
# To-Do List App (Dockerized)

## Requirements
- Docker
- Docker Compose
- Git

## Description
Simple To-Do app built with Flask + MySQL.  
- Add tasks
- Mark tasks as done
- Persistent storage with Docker volumes

## How to Run
```bash
./prepare-app.sh
./start-app.sh
# App available at http://localhost:5000
./stop-app.sh
./remove-app.sh
