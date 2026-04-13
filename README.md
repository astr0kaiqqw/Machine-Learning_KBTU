# ML FastAPI Docker Project

## Run locally
uvicorn main:app --reload

## Test API
http://localhost:8000/docs

## Docker
docker build -t ml-api .
docker run -p 8000:8000 ml-api