#!/usr/bin/env bash
docker-compose build

docker-compose up -d app nginx
docker-compose run repro
docker-compose stop app nginx
