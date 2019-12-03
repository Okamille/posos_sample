# Use the official docker image for python3.7
FROM python:3.7

# Installing packages

RUN pip3 install --user sklearn
RUN pip3 install --user numpy