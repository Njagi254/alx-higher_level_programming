# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Set environment variables to avoid user interaction prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package information, install MySQL server, and clean up to reduce image size
RUN apt-get update && \
    apt-get install -y wget lsb-release gnupg && \
    wget https://dev.mysql.com/get/mysql-apt-config_0.8.17-1_all.deb && \
    dpkg -i mysql-apt-config_0.8.17-1_all.deb && \
    apt-get update && \
    apt-get install -y mysql-server && \
    rm -rf /var/lib/apt/lists/*

# Expose MySQL port
EXPOSE 3306

# Start MySQL server
CMD ["mysqld"]
