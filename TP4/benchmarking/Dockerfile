# Use the official Ubuntu base image
FROM ubuntu:latest

# Install necessary packages including unzip
RUN apt-get update && \
    apt-get install -y git build-essential libssl-dev wget unzip

# Clone the wrk repository
RUN git clone https://github.com/wg/wrk.git /opt/wrk

# Build wrk from source
RUN make -C /opt/wrk

# Add wrk to PATH
RUN ln -s /opt/wrk/wrk /usr/local/bin/wrk

# Set the working directory
WORKDIR /benchmarking

# Define the command that runs when the container starts
ENTRYPOINT ["wrk"]
