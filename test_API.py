from nixtla import NixtlaClient
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
