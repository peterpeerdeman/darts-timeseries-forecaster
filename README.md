<h1 align="center">darts-timeseries-forecaster</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.0.1-blue.svg?cacheSeconds=2592000" />
  <img src="https://img.shields.io/badge/python-%3E%3D3.9.13-blue.svg" />
  <a href="https://github.com/peterpeerdeman/darts-timeseries-forecaster#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/peterpeerdeman/darts-timeseries-forecaster/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/peterpeerdeman/darts-timeseries-forecaster/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/peterpeerdeman/telegraf-pvoutput" />
  </a>
  <a href="https://twitter.com/peterpeerdeman" target="_blank">
    <img alt="Twitter: peterpeerdeman" src="https://img.shields.io/twitter/follow/peterpeerdeman.svg?style=social" />
  </a>
</p>

> a docker image that reads a timeseries csv file (queried from influxdb), and uses darts to create a forecast, writing it back to a csv or influx line protocol for processing

## environment variables configuration

PREDICTION_MODEL_EPOCHS=10
PREDICTION_MODEL=fft
PREDICTION_SPLIT=0.80
PREDICTION_COUNT=200

INPUT_FREQUENCY=h
INPUT_FILENAME=/volume/timeseries.csv
INPUT_TIMECOl=time
INPUT_VALUECOL=value
INPUT_MOVINGAVERAGE=30

OUTPUT_FORMAT=influx
OUTPUT_FILENAME=/volume/prediction.csv

## Prerequisites

- python >=3.9.13

## Standalone usage

```sh
cp .env.dist .env
# or ensure all environment variables listed in `.env.dist` are set before running node command
pip install -r requirements.txt
python3 app.py
```

## Docker development environment

mounts the current folder and runs with docker image
```
docker run --rm -v $PWD:/app -it peterpeerdeman/darts-timeseries-forecaster:1.0.0 python app.py
```

## Run tests

```sh
#TODO
```

## Author

👤 **Peter Peerdeman**

* Website: https://peterpeerdeman.nl
* Twitter: [@peterpeerdeman](https://twitter.com/peterpeerdeman)
* Github: [@peterpeerdeman](https://github.com/peterpeerdeman)
* LinkedIn: [@peterpeerdeman](https://linkedin.com/in/peterpeerdeman)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/peterpeerdeman/telegraf-pvoutput/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

This project is [MIT](https://github.com/peterpeerdeman/telegraf-pvoutput/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

