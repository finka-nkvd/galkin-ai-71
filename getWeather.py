import requests

def get_weather_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=05466f10640b17226797cfa8537cf71f'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        forecast_list = data['list']
        forecast_data = []
        for forecast in forecast_list:
            timestamp = forecast['dt_txt']
            weather_description = forecast['weather'][0]['description']
            temperature = forecast['main']['temp'] - 273.15  # Кельвины в Цельсии
            forecast_data.append(f'{timestamp}: {weather_description}, температура: {temperature:.1f}°C')
        return forecast_data
    else:
        return [f'Ошибка при получении данных: {data["message"]}']

city = input('Введите город для получения прогноза погоды: ')
forecast = get_weather_forecast(city)

if forecast:
    print(f'Прогноз погоды на 5 дней для города {city}:\n', '-'*60)
    a = 0
    for entry in forecast:
        a+=1
        print(entry)
        if a % 5 == 0:
            print("-"*60)
