# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY truth_or_dare.py /app

# No additional dependencies are needed
# So no RUN pip install commands

# Command to run the Python app
CMD ["python", "truth_or_dare.py"]
