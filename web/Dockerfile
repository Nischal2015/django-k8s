FROM python:3.10-slim

COPY . /app
WORKDIR /app

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt && \  
    chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]