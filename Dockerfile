FROM python:3.9.19 as base

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD python app.py

#FROM python:3.9.19-slim

#WORKDIR /app

#COPY --from=base /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

#COPY --from=base /app /app

#CMD python app.py
