#!/bin/bash
docker build -t retirement-planner .
docker run --rm -p 8080:8080 --env-file .env.example retirement-planner
