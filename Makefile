
PHONY: build run stop

SERVER_API_IMAGE_NAME=server-api
SERVER_API_IMAGE_VERSION=1.0.0

IMAGE_NAME=$(SERVER_API_IMAGE_NAME):$(SERVER_API_IMAGE_VERSION)

CELERY_WORKER_IMAGE_NAME=celery-worker
CELERY_WORKER_IMAGE_VERSION=1.0.0

CELERY_IMAGE_NAME=$(CELERY_WORKER_IMAGE_NAME):$(CELERY_WORKER_IMAGE_VERSION)

build:
	@echo "Building api"
	docker build -t $(IMAGE_NAME) -f docker/server.dockerfile .
	@echo "Building celery worker"
	docker build -t $(CELERY_IMAGE_NAME) -f docker/worker.dockerfile .

run:
	@echo "Running api"
	minikube start
	eval $(minikube docker-env)
	kubectl apply -f k8s/deployment.yml
	kubectl apply -f k8s/service.yml
	minikube dashboard

stop:
	minikube stop

run-compose:
	docker-compose up -d
