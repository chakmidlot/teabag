FROM python:3.6

COPY . /opt/teabag/src/
RUN pip3 install -r /opt/teabag/src/requirements.txt

CMD cd /opt/teabag/src/; gunicorn webapp:app --bind 0.0.0.0:5001 --worker-class aiohttp.GunicornWebWorker -w 3 --access-logfile /dev/null --error-logfile /dev/null
