FROM python:2.7

WORKDIR /app

# Fix Debian Buster EOL repositories
RUN sed -i 's|deb.debian.org|archive.debian.org|g' /etc/apt/sources.list && \
    sed -i 's|security.debian.org|archive.debian.org|g' /etc/apt/sources.list && \
    sed -i '/buster-updates/d' /etc/apt/sources.list

RUN apt-get -o Acquire::Check-Valid-Until=false update && \
    apt-get install -y git curl && \
    rm -rf /var/lib/apt/lists/*

RUN pip install six

RUN git clone https://github.com/tarunkant/Gopherus.git .

CMD ["bash"]
