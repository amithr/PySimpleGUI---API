import PySimpleGUI as sg
import weather_api

sg.change_look_and_feel('GreenTan')

layout = [[sg.Text("Enter Location", size=(20, 1)), sg.Input(key='-LOCATION-', do_not_clear=True, size=(20, 1))],
          [sg.Text('Current Condition: ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='-CURRENT_CONDITION-')],
          [sg.Text('Feels Like (C): ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='-FEELS_LIKE-')],
          [sg.Text('Temperature (C): ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='-TEMPERATURE-')],
          [sg.Text('Wind Speed (kph): ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='-WIND_SPEED-')],
          [sg.Text('Precipitation (mm): ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='-PRECIPITATION-')],
          [sg.Text('Humidity (%): ', size=(20, 1), ), sg.Text(size=(20, 1), justification='left', key='-HUMIDITY-')],
          [sg.Text('UV Index: ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='-UV_INDEX-')],
          [sg.Text('Visibility (km): ', size=(20, 1)), sg.Text(size=(20, 1), justification='left', key='-VISIBILITY-')],
          [sg.Button('Get Weather Data', size=(20, 1)), sg.Button('Quit')]
]

window = sg.Window('Weather API Application', layout)

while True:
    event, values = window.read()
    if event in (None, 'Quit'):
        break
    if event == "Get Weather Data":
        weather_information = weather_api.request_weather_information(values['-LOCATION-'])
        window['-CURRENT_CONDITION-'].Update(weather_information['conditions'])
        window['-FEELS_LIKE-'].Update(weather_information['feels_like'])
        window['-TEMPERATURE-'].Update(weather_information['temperature'])
        window['-WIND_SPEED-'].Update(weather_information['wind_speed'])
        window['-HUMIDITY-'].Update(weather_information['humidity'])
        window['-PRECIPITATION-'].Update(weather_information['precipitation'])
        window['-VISIBILITY-'].Update(weather_information['visibility'])
        window['-UV_INDEX-'].Update(weather_information['uv_index'])

window.close()