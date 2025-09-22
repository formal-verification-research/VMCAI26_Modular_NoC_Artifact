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
    python3-pandas \
    wget \
    ca-certificates

RUN update-ca-certificates

# Set up dotnet runtime
RUN wget https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    rm packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get install -y dotnet-runtime-9.0

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