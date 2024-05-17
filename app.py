import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
from darts.timeseries import TimeSeries
from darts.models.forecasting.fft import FFT
from darts.models.forecasting.nbeats import NBEATSModel
from darts.utils.missing_values import fill_missing_values
from darts.metrics import mae
from darts.models.filtering.moving_average_filter import MovingAverageFilter
import math

# parse environment variables
prediction_model = os.environ.get('PREDICTION_MODEL', 'fft')
prediction_model_epochs = os.environ.get('PREDICTION_MODEL_EPOCHS', 30)
prediction_split = os.environ.get('PREDICTION_SPLIT')
prediction_metric_name = os.environ.get('PREDICTION_METRIC_NAME', 'prediction')
prediction_count = os.environ.get('PREDICTION_COUNT')

# parse file info
input_frequency = os.environ.get('INPUT_FREQUENCY', 'h')
input_filename = os.environ.get('INPUT_FILENAME', '/volume/timeseries.csv')
input_timecol = os.environ.get('INPUT_TIMECOl', 'time')
input_valuecol = os.environ.get('INPUT_VALUECOL', 'value')
input_movingaverage = int(os.environ.get('INPUT_MOVINGAVERAGE', False))

output_filename = os.environ.get('OUTPUT_FILENAME', '/volume/prediction.csv')

print('reading from file:', input_filename)
print('timecol          :', input_timecol)
print('valuecol         :', input_valuecol)
print('frequency        :', input_frequency)

# retrieve and prepare data
df = pd.read_csv (input_filename);
df['time'] = df['time'].astype('datetime64[ns]')
df = df.set_index('time')
#df.drop(df.tail(1).index,inplace=True) # drop last row, to avoid issues with frequency

#alt
#series = TimeSeries.from_csv(input_filename, time_col='time', value_cols=['value'])#, freq=input_frequency)

# apply 0shot machine learning
series =  TimeSeries.from_dataframe(df, value_cols='value')
output_measurement_name = 'timeseries-prediction'
if 'name' in df.columns:
    measurement_name = df['name'].unique()[0] 
    output_measurement_name = measurement_name + '-prediction'

if input_movingaverage: 
    original = series
    ma = MovingAverageFilter(window=input_movingaverage)
    y_filtered = ma.filter(series)
    y_filtered.plot(label="filter")
    series = y_filtered


#series = fill_missing_values(series)

##TODO: extract to different file / functions
if prediction_model == 'nbeats':
    model = NBEATSModel(
        input_chunk_length=30,
        output_chunk_length=30,
        generic_architecture=True,
        num_stacks=10,
        num_blocks=1,
        num_layers=4,
        layer_widths=512,
        n_epochs=int(prediction_model_epochs),
        nr_epochs_val_period=1,
        batch_size=800,
        model_name="nbeats_run",
    )
    if prediction_split:
        train, val = series.split_before(float(prediction_split))
    else:
        train, val = series.split_before(0.90)
    try:
        model.fit(train, val_series=val, verbose=False)
    except BaseException: 
        print(BaseException)
        print("error fitting model, try inputting more data", file=sys.stderr)
        quit()
    if prediction_count:
        pred_val = model.predict(n=int(prediction_count))
    else:
        pred_val = model.predict(n=math.floor(len(series)/3))
else:
    if prediction_split:
        train, val = series.split_before(float(prediction_split))
    else:
        train, val = series.split_before(0.80)
        model = FFT(nr_freqs_to_keep=200)
        model.fit(train)
    if prediction_count:
        pred_val = model.predict(n=int(prediction_count))
    else:
        pred_val = model.predict(len(val)*2)


print("MAE:", mae(pred_val, val))
pred_val.to_csv(path_or_buf=output_filename, date_format='%s%f000')

#train.plot(label="train")
#val.plot(label="val")
#pred_val.plot(label="prediction")
#plt.show()
