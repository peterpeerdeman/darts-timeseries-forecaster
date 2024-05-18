import math
import os
import sys

from darts.metrics import mae
from darts.models.filtering.moving_average_filter import MovingAverageFilter
from darts.models.forecasting.fft import FFT
from darts.models.forecasting.nbeats import NBEATSModel
from darts.timeseries import TimeSeries
import pandas as pd

#import matplotlib.pyplot as plt

# parse environment variables
prediction_model = os.environ.get('PREDICTION_MODEL', 'fft')
prediction_fft_keepfreq = os.environ.get('PREDICTION_FFT_KEEPFREQ', 100)
prediction_model_epochs = os.environ.get('PREDICTION_MODEL_EPOCHS', 30)
prediction_split = float(os.environ.get('PREDICTION_SPLIT', 0.80))
prediction_count = os.environ.get('PREDICTION_COUNT')

# parse file info
input_frequency = os.environ.get('INPUT_FREQUENCY', '10m')
input_filename = os.environ.get('INPUT_FILENAME', '/volume/timeseries.csv')
input_timecol = os.environ.get('INPUT_TIMECOl', 'time')
input_valuecol = os.environ.get('INPUT_VALUECOL', 'value')
input_movingaverage = int(os.environ.get('INPUT_MOVINGAVERAGE', False))

output_filename = os.environ.get('OUTPUT_FILENAME', '/volume/prediction.csv')
output_format = os.environ.get('OUTPUT_FORMAT', 'csv')

print('reading from file:', input_filename)
print('timecol          :', input_timecol)
print('valuecol         :', input_valuecol)
print('frequency        :', input_frequency)

# retrieve and prepare data
df = pd.read_csv(input_filename);
df['time'] = df['time'].astype('datetime64[ns]')
df = df.set_index('time')
# remove tags (usually empty values)
df = df.drop(columns='tags')
# remove empty values
#df = df.dropna()

# apply 0shot machine learning
series =  TimeSeries.from_dataframe(df, value_cols='value' , fill_missing_dates=True, freq=input_frequency)
output_measurement_name = 'timeseries-prediction'
if 'name' in df.columns:
    measurement_name = df['name'].unique()[0] 
    output_measurement_name = measurement_name + '-prediction'

if input_movingaverage: 
    original = series
    ma = MovingAverageFilter(window=input_movingaverage)
    y_filtered = ma.filter(series)
    series = y_filtered

##TODO: extract to different file / functions
# predict with nbeats
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
    train, val = series.split_before(float(prediction_split))
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
    # predict with FFT
    train, val = series.split_before(float(prediction_split))

    model = FFT(required_matches={'hour'}, nr_freqs_to_keep=prediction_fft_keepfreq)
    model.fit(train)
    if prediction_count:
        pred_val = model.predict(n=int(prediction_count))
    else:
        pred_val = model.predict(len(val)*2)

print("MAE:", mae(pred_val, val))
if output_format == 'influx':
    lines = []
    for i in range(len(pred_val)):
        timestamp = pred_val.time_index[i].value
        value = pred_val.values()[i][0]
        line = f"{output_measurement_name} value={value} {timestamp}"
        lines.append(line)
    with open(output_filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
else:
    pred_val.to_csv(path_or_buf=output_filename, date_format='%s%f000')

#train.plot(label="train")
#val.plot(label="val")
#pred_val.plot(label="prediction")
#plt.show()
