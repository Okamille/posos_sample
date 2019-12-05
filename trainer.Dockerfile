# Use the official docker image for python3.7
FROM tensorflow/tensorflow:latest-py3

RUN pip install --upgrade pip
RUN pip install --user sklearn
RUN pip install --user pandas
RUN pip install --user keras

CMD ["python", "${PWD}/training/neural_train.py"]