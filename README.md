<h1 align="center">darts-timeseries-forecaster</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.2-blue.svg?cacheSeconds=2592000" />
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

|Variable|Type|Default|Description|
|---|----|----|----|
|PREDICTION_MODEL|string|fft|Timeseries model to use, either 'fft' or 'nbeats'|
|PREDICTION_MODEL_EPOCHS|int|30|Number of epochs to train when using nbeats model|
|PREDICTION_SPLIT|double|0.90|Percentage at which to split the data set into train and test data |
|PREDICTION_COUNT|int|a third of the number of inputs|Number of prediction timepoints to generate|
|INPUT_FREQUENCY|datefmt|h|Frequency of time points|
|INPUT_FILENAME|string|/volume/timeseries.csv|input csv filename to read from|
|INPUT_TIMECOl|string|time|name of the time column in the csv
|INPUT_VALUECOL|string|value|name of the value column in the csv|
|INPUT_MOVINGAVERAGE|int|false|if number is supplied, a moving average is taken to smooth the input |
|OUTPUT_FORMAT|string|csv|defaults to 'csv' but can be set to 'influx' to product line format txt for easy posting to influxdb with curl|
|OUTPUT_FILENAME|string|/volume/prediction.csv|location of the prediction output file|

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
docker run --rm -v $PWD:/app -it peterpeerdeman/darts-timeseries-forecaster:1.0.2 python app.py
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

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/peterpeerdeman/darts-timeseries-forecaster/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

This project is [MIT](https://github.com/peterpeerdeman/telegraf-pvoutput/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_

