# ML FastAPI Docker Project

## Project structure
- train.py
- main.py
- model.joblib
- requirements.txt
- Dockerfile
- README.md

## Run locally
uvicorn main:app --reload

## API docs
http://127.0.0.1:8000/docs

## Docker
docker build -t ml-api .
docker run -p 8000:8000 ml-api