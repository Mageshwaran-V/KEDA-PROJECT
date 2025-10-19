# prophet_predictor.py
from flask import Flask, jsonify
import pandas as pd
from prophet import Prophet
import requests
import datetime

PROMETHEUS_URL = "http://prometheus:9090/api/v1/query"

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    now = int(time.time())
    query = 'workload_intensity'
    step = '15s'

    r = requests.get(PROMETHEUS_URL, params={
        'query': f'{query}[30m]'
    })

    results = r.json()['data']['result']
    if not results:
        return jsonify({"predicted_load": 0})

    ts_data = results[0]['values']
    df = pd.DataFrame(ts_data, columns=['ds', 'y'])
    df['ds'] = pd.to_datetime(df['ds'], unit='s')
    df['y'] = df['y'].astype(float)

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=1, freq='min')
    forecast = model.predict(future)
    yhat = forecast.iloc[-1]['yhat']
    return jsonify({"predicted_load": yhat})

