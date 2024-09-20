import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

ticker = 'AAPL'
data = yf.download(ticker, start= '2015-01-01', end= '2024-07-31')

data['50_MA'] = data['Close'].rolling(window=50).mean()
data['200_MA'] = data['Close'].rolling(window=200).mean()

print(data.columns)
print(data[['Close', '50_MA', '200_MA']].tail())

data.dropna(subset=['50_MA', '200_MA'], inplace=True)

fig = go.Figure()

fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode = 'lines', name='Close Price'))


fig.add_trace(go.Scatter(x=data.index, y=data['50_MA'], mode='lines', name='50-Day MA', line = dict(color = 'red')))
fig.add_trace(go.Scatter(x=data.index, y=data['200_MA'], mode='lines', name='200-Day MA', line = dict(color = 'green')))

fig.update_layout(title=f'{ticker} Stock Price and Moving Averages',
                  xaxis_title='Data',
                  yaxis_title = 'Stock Price (USD)')
fig.show()