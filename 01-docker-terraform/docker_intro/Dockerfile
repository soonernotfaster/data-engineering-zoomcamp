FROM python:3.9

RUN pip install pandas

WORKDIR /app

COPY pipeline.py pipeline.py

CMD [ "python", "pipeline.py" ]