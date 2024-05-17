FROM python:3.9.19

#RUN apt-get -y update  && apt-get install -y \
#  python3-dev \
#  apt-utils \
 # python-dev \
#  build-essential \
#&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

#RUN pip install --upgrade pip setuptools wheel

#RUN pip install coreforecast
RUN pip install -r requirements.txt
#RUN pip install darts
#RUN pip install numpy

CMD python app.py
