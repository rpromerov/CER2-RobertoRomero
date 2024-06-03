# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY Certamen2 /code/

# Expose port 8000
EXPOSE 8000