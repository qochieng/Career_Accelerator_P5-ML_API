FROM python:3.10.11

# Create a working directory in the container
WORKDIR /app

# Copy the contents of the requirements.txt into a temporary folder
COPY ./requirements.txt /tmp/requirements.txt

# Install packages in the requirements.txt file
RUN python -m pip install --timeout 300000 -r /tmp/requirements.txt

# Copy all files into containers working directory
COPY . /app 

# Expose port 80 outside the container
EXPOSE 80 

# Run the fastapi application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

