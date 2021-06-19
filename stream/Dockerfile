# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Copy just the requirements.txt
COPY ./requirements.txt /stream/requirements.txt

# Set the working directory to /stream
WORKDIR /stream

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /stream 
ADD . /stream

# run the command to start namekocommand
CMD ["nameko", "run", "--config", "config.yml", "stream.service"]