# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10.6-buster

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

EXPOSE 8080

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

# Install production dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install litestream
COPY litestream-v0.3.8-linux-amd64.deb litestream-v0.3.8-linux-amd64.deb
RUN dpkg -i litestream-v0.3.8-linux-amd64.deb
RUN litestream version
COPY litestream.yml /etc/litestream.yml
# RUN litestream restore -o example.db gcs://streamlit-widget-url-sync-bucket/example.db

# Copy local code to the container image.
COPY . ./

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
# Start it via litestream so that the database is automatically replicated while the app is running
#CMD litestream replicate -exec "streamlit run --server.port 8080 --server.enampleCORS false example_app.py"
CMD ./run_app.sh