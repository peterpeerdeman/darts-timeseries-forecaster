FROM python:3.9.19 as base

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9.19-slim

WORKDIR /app

COPY --from=base /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

COPY --from=base /app /app

#RUN apt-get -y update  && apt-get install -y \
#  python3-dev \
#  apt-utils \
 # python-dev \
#  build-essential \
#&& rm -rf /var/lib/apt/lists/*

#RUN pip install coreforecast
#RUN pip install -r requirements.txt
#RUN pip install darts
#RUN pip install numpy

#RUN pip install --no-index --find-links=/svc/wheels -r requirements.txt

CMD python app.py
