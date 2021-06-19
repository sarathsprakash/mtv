# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Copy just the requirements.txt
COPY ./requirements.txt /frontend/requirements.txt

# Set the working directory to /api
WORKDIR /frontend

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app 
ADD . /frontend

# run the command to start namekocommand
CMD ["uwsgi", "app.ini"]