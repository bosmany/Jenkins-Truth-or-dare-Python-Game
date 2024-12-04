# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY truth_or_dare.py /app

# Install any necessary dependencies (if needed)
RUN pip install --no-cache-dir random

# Command to run the app
CMD ["python", "truth_or_dare.py"]
