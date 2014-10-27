FROM python:2.7
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
ADD ./code /code
WORKDIR /code
CMD python app.py
