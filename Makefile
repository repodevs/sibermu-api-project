up:
	uvicorn main:app --port 8002 --reload

buildrun:
	docker build -t repodevs/sibermu-api-project:latest .
	docker rm -f apiapp
	docker run -d --name apiapp -p 8002:8002 repodevs/sibermu-api-project:latest

down:
	docker rm -f apiapp
