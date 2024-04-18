# Pull base image
FROM python:3.11.5-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install required dependencies for django geo
RUN apt-get update && apt-get install --yes libgdal-dev

# Set work directory
WORKDIR /REST-example

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .
