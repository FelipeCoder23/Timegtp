from nixtla import NixtlaClient
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Asegúrate de que tu API key sea correcta
nixtla_client = NixtlaClient(
    api_key='nixtla-tok-ltLeWIWTCxxTpIdEMPBE6fCtJNTEoaqvzGwNmR6LceJTdFhbnAVT50fdxJ02yZTCvAqzsCmx0vaYBoYx'
)

# Cargar los datos
df = pd.read_csv('https://raw.githubusercontent.com/Nixtla/transfer-learning-time-series/main/datasets/air_passengers.csv')

# Mostrar las primeras filas del DataFrame
print(df.head())

# Crear un gráfico usando NixtlaClient
nixtla_client.plot(df, time_col='timestamp', target_col='value')

timegpt_fcst_df = nixtla_client.forecast(df=df, h=12, freq='MS', time_col='timestamp', target_col='value')
timegpt_fcst_df.head()




# obtener datos de coingecko
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
params = {
    'vs_currency': 'usd',
    'days': 'max'  # Puedes cambiar 'max' por el número de días que necesitas
}

# Hacer la solicitud a la API
response = requests.get(url, params=params)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
else:
    print("Error:", response.status_code)
    data = None

# Convertir los datos a un DataFrame de pandas
if data:
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Mostrar las primeras filas del DataFrame
    print(df.head())

    # Crear una gráfica de los datos
    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['price'])
    plt.xlabel('Fecha')
    plt.ylabel('Precio (USD)')
    plt.title('Precio de Bitcoin')
    plt.show()
