#!/bin/bash

docker build -t gcr.io/rajdphd-prep/squad-lobby:latest .
docker push  gcr.io/rajdphd-prep/squad-lobby:latest 

gcloud run deploy squad-lobby-app   --image gcr.io/rajdphd-prep/squad-lobby:latest   --platform managed   --region us-central1   --port 8501 --project rajdphd-prep --allow-unauthenticated