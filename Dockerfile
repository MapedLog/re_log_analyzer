# Base container
FROM python:3.11

COPY src/requirements.txt /

RUN pip install -r requirements.txt

# Add requirements, code
COPY src/ /

VOLUME /data
# Declare entrypoint of that exposed service
ENTRYPOINT ["python3", "./main.py"]