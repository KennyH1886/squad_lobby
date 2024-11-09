#!/bin/bash

docker build -t squad-lobby:latest .
docker run -p 8501:8501 squad-lobby:latest