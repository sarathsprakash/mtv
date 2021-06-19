# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Copy just the requirements.txt
COPY ./requirements.txt /session/requirements.txt

# Set the working directory to /api
WORKDIR /session

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app 
ADD . /session

# run the command to start namekocommand
CMD ["nameko", "run", "--config", "config.yml", "session.service"]