FROM python:3.6

COPY . /opt/teabag/
RUN pip3 install -r /opt/teabag/requirements
EXPOSE 8080

CMD cd /opt/teabag/src/; python3 webapp.py
