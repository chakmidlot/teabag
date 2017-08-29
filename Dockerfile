FROM python:3.6

COPY . /opt/teabag/
RUN pip3 install -r /opt/teabag/requirements
EXPOSE 8080

CMD cd /opt/teabag/src/; gunicorn webapp:app --bind 0.0.0.0:8080 --worker-class aiohttp.GunicornWebWorker -w 3
