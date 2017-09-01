FROM python:3.6

COPY . /opt/teabag/
RUN pip3 install -r /opt/teabag/requirements

CMD cd /opt/teabag/src/; gunicorn webapp:app --bind 0.0.0.0:80 --worker-class aiohttp.GunicornWebWorker -w 3
