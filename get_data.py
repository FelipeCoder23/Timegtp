import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_crypto_historical_data(crypto_id, vs_currency='usd', days=365):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart'
    params = {
        'vs_currency': vs_currency,
        'days': days
    }

    # Imprimir la URL completa para verificar
    print(f'URL de la solicitud: {url}?vs_currency={vs_currency}&days={days}')

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        prices = data['prices']
        return prices, vs_currency
    else:
        print(f"Error: {response.status_code}")
        print(f"Respuesta de la API: {response.text}")
        return None, vs_currency

def main():
    crypto_id = input('Ingrese el ID de la criptomoneda (por ejemplo, bitcoin, ethereum): ').lower()
    prices, vs_currency = get_crypto_historical_data(crypto_id)

    if prices:
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        # Mostrar las primeras filas del DataFrame
        print(df.head())

        # Crear una gráfica de los datos
        plt.figure(figsize=(10, 5))
        plt.plot(df['timestamp'], df['price'], label=crypto_id.capitalize())
        plt.xlabel('Fecha')
        plt.ylabel(f'Precio ({vs_currency.upper()})')
        plt.title(f'Precio de {crypto_id.capitalize()} a lo largo del tiempo')
        plt.legend()
        plt.show()
    else:
        print('No se pudo obtener los datos históricos.')

if __name__ == '__main__':
    main()
