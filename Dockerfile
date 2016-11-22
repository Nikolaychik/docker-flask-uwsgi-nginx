# specify image to build your container on
FROM python:3.5
# add needed files to container
ADD ./main.py /
ADD ./wsgi.py /
ADD ./requirements.txt /
ADD ./templates /
# we also need to install requirements for python
RUN pip install -r requirements.txt
