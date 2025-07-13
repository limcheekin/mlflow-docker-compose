FROM python:3.11-slim-buster
# Install python packages
COPY debug_mlflow_s3.py ./
COPY test_s3_connectivity.py ./
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
