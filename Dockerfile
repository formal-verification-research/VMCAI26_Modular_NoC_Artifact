# Debian base
FROM debian:stable

# Set noninteractive for apt
ENV DEBIAN_FRONTEND=noninteractive

# Intsall essential tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3 \
    unzip \
    python3-matplotlib \
    python3-pandas

# Copy modest to the container
COPY modest.zip /tmp/modest.zip 

# Create a directory for Modest
RUN mkdir -p /opt/modest

# Unzip the archive
RUN unzip /tmp/modest.zip -d /opt/modest && rm /tmp/modest.zip

# Add modest to the path
ENV PATH="/opt/modest:$PATH"

# Create the base directory for working from
RUN mkdir -p /home && mkdir -p /home/python && mkdir -p /home/models

# Copy the code into the image
COPY README.md /home/README.md
COPY LICENSE /home/LICENSE
COPY python/ /home/python
COPY models/ /home/models

# Set the working directory
WORKDIR /home