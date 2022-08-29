# openfaas-model-microservice
Use openfaas to do the model microservice system

# How to use?

## Step 1: Login DockerHub
```bash
docker login -u <docker-username> -p <docker-password>
```

## Step 2: openfaas-service project
```bash
$ cd openfaas-service
$ faas-cli build -f application-service.yml
$ faas-cli push -f application-service.yml
$ faas-cli deploy -f application-service.yml
```

## Step 3: openfaas-service-image project
```bash
$ cd openfaas-service-image
$ faas-cli build -f application-service-image.yml
$ faas-cli push -f application-service-image.yml
$ faas-cli deploy -f application-service-image.yml
```