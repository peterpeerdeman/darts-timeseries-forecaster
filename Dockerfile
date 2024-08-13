FROM python:3.9.19 as base

RUN mkdir /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD python app.py

#FROM python:3.9.19-slim

#WORKDIR /app

#COPY --from=base /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

#COPY --from=base /app /app

#CMD python app.py
