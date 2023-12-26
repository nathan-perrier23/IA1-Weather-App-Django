from decouple import config
import openai
from openai import OpenAI

client = OpenAI(api_key=config("OPENAI_API_KEY"))

#client.api_key = config("OPENAI_API_KEY")

GPT_MODEL = "gpt-3.5-turbo-1106"

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather of a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city or town e.g. New York. return city/town name only",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["metric", "imperial"],
                        "description": "The temperature unit to use. Defualt is metric. Infer this from the users location. only return either imperial or metric",
                    },
                    'fields': {
                        'type': 'string',
                        'properties': {  
                            'temperature': {'type': 'string', 'description': 'The temperature in Celcius (metric) or Fahrenheit (imperial)'},
                            'humidity': {'type': 'string', 'description': 'The humidity in %'},
                            'cloudCover': {'type': 'string', 'description': 'The fraction of the sky obscured by clouds when observed from a particular location, denoted by %'},
                            'dewPoint': {'type': 'string', 'description': 'The dew point in which The temperature to which air must be cooled to become saturated with water vapor in Celcius (metric) or Fahrenheit (imperial)'},
                            'epaHealthConcern': {'type': 'string', 'description': 'The epa health concern of the envirourmnt caused by pollutants in the air, from 0 (good) to 5 (hazardous)'},
                            'epaIndex': {'type': 'string', 'description': 'The epa index of how toxic the air quality is, from 0 (good) to 5 (hazardous)'},
                            'epaPrimaryPollutant': {'type': 'string', 'description': 'The epa primary pollutant (the primary air pollutant). PM2.5 (0), PM10 (1), O3 (2), NO2 (3), CO (4), SO2 (5)'},
                            'fireIndex': {'type': 'string', 'description': 'The fire index (FWI), the probability of a fire'},
                            'hailBinary': {'type': 'string', 'description': 'The hail binary prediction'},
                            'humidity': {'type': 'string', 'description': 'The humidity, which The concentration of water vapor present in the air, measured in %'},
                            'iceAccumilation': {'type': 'string', 'description': 'The ice accumilation in mm (metric) or in (imperial)'},
                            'moonPhase': {'type': 'string', 'description': 'The moon phase from 0 (new), 1 (waxing cresent), 2 (first quarter), 3 (waxing gibbous), 4 (full), 5 (waning gibbous), 6 (third quarter), to 7 (waning cresent)'},
                            'pollutantCO': {'type': 'string', 'description': 'The pollutant CO in ppb in the air'},
                            'pollutantNO2': {'type': 'string', 'description': 'The pollutant NO2 in ppb in the air'},
                            'pollutantO3': {'type': 'string', 'description': 'The pollutant O3 in ppb in the air'},
                            'pollutantSO2': {'type': 'string', 'description': 'The pollutant SO2 in ppb in the air'},
                            'precipitationIntensity': {'type': 'string', 'description': 'The precipitation intensity in which, The measure of the intensity of precipitation by calculating the amount of precipitation that would fall over a given interval of time if the precipitation intensity were constant over that time period., measured in mm/hr (metric) or in/hr (imperial)'},
                            'precipitationProbability': {'type': 'string', 'description': 'The precipitation probability, in which the Probability of precipitation represents the chance of >0.0254 cm (0.01 in.) of liquid equivalent precipitation at a radius surrounding a point location over a specific period of time. measured in %'},
                            'precipitationType': {'type': 'string', 'description': 'The various types of precipitation often include the character or phase of the precipitation which is falling to ground level (Schuur classification). Precipitation Type indicates what type the precipitation will be if something were to precipitate out. This will have a non-zero value regardless of the precipitation probability or intensity values. denoted by 0 (none), 1 (rain), 2 (snow), 3 (freezing rain), 4 (ice pellets)'},
                            'snowAccumulation': {'type': 'string', 'description': 'The accumulated amount of new snowfall that has or will accumulate for the past or future hour of the requested time, measured in mm (metric) or in (imperial)'},
                            'rainAccumulation': {'type': 'string', 'description': 'The accumulated amount of liquid rain that has or will accumulate for the past or future hour of the requested time, measured in mm (metric) or in (imperial)'},
                            'snowDepth': {'type': 'string', 'description': 'The depth of snow on the ground including both new and old snow, measured in cm (metric) or in (imperial)'},
                            'freezingRainIntensity': {'type': 'string', 'description': 'The measure of the intensity of freezing rain by calculating the amount of freezing rain that would fall over a given interval of time if the freezing rain intensity were constant over that time period, measured in mm/hr (metric) or in/hr (imperial)'},
                            'rainIntensity': {'type': 'string', 'description': 'The measure of the intensity of rainfall by calculating the amount of rain that would fall over a given interval of time if the rain intensity were constant over that time period, measured in mm/hr (metric) or in/hr (imperial)'},
                            'snowIntensity': {'type': 'string', 'description': 'The measure of the intensity of snowfall by calculating the amount of snow that would fall over a given interval of time if the snow intensity were constant over that time period, measured in mm/hr (metric) or in/hr (imperial)'},
                            'sleetIntensity': {'type': 'string', 'description': 'The measure of the intensity of sleet (ice pellets) by calculating the amount of sleet that would fall over a given interval of time if the sleet intensity were constant over that time period. measured in mm/hr (metric) or in/hr (imperial)'},
                            'sleetAccumulation': {'type': 'string', 'description': 'The accumulated amount of new sleet (ice pellets) that has or will accumulate for the past or future hour of the requested time, measured in mm (metric) or in (imperial)'},
                            'iceAccumulation': {'type': 'string', 'description': 'The accumulated amount of ice from freezing rain that has or will accumulate for the past or future hour of the requested time, measured in mm (metric) or in (imperial)'},
                            'temperature': {'type': 'string', 'description': 'The temperature in Celcius (metric) or Fahrenheit (imperial)'},
                            'temperatureApparent': {'type': 'string', 'description': 'The apparent temperature ("feels like" temperature). it is the temperature equivalent perceived by humans, caused by the combined effects of air temperature, relative humidity, and wind speed in Celcius (metric) or Fahrenheit (imperial)'},
                            'visibility': {'type': 'string', 'description': 'The measure of the distance at which an object or light can be clearly discerned, measured in km (metric) or mi (imperial)'},
                            'waveSignificantHeight': {'type': 'string', 'description': 'The wave significant height in m (metric) or ft (imperial)'},
                            'windDirection': {'type': 'string', 'description': 'The direction from which it originates, measured in degrees clockwise from due north'},
                            'windGust': {'type': 'string', 'description': 'The wind gust in which The maximum brief increase in the speed of the wind, usually less than 20 seconds, measured in m/s (metric) or mph (imperial)'},
                            'windSpeed': {'type': 'string', 'description': 'The fundamental atmospheric quantity caused by air moving from high to low pressure, usually due to changes in temperature in m/s (metric) or mph (imperial)'},
                            'sunriseTime': {'type': 'string', 'description': 'The daily appearance of the Sun on the horizon due to Earths rotation in UTC ISO-8601 format'},
                            'sunsetTime': {'type': 'string', 'description': 'The daily disappearance of the Sun below the horizon due to Earths rotation in UTC ISO-8601 format'},
                            'floodIndex': {'type': 'string', 'description': 'The flood index in which The Flood Index is a Standard measurement of the strength of flood producing rain at a particular place and time. The index is based on the following scale, 1 (least sereve) - Minor flash flooding possible: Rivers may go out of their banks briefly, 2 - Moderate flash flooding possible: Rivers experiencing flooding conditions with minor impacts to homes and businesses, 3 - Significant flash flooding possible: Could lead to disruptions with river flooding also significant enough to threaten homes and businesses, 4 - Major river and/or flash flooding possible: Major disruptions to transportation, along with significant impacts to homes/businesses, 5 (most servere) - Catastrophic or extreme river and/or flash flooding probable or likely: Extreme impacts along river networks and low-lying areas'},
                            'cloudBase': {'type': 'string', 'description': 'The cloud base in which The lowest altitude of the visible portion of the cloud in (km or null (metric)) or (mi or null (imperial))'},
                            'treeIndex': {'type': 'string', 'description': 'The tree index  is a Standard measurement of the strength of tree pollen at a particular place and time. Useful to identify alergines in the air. The index is based on the following scale, 0 (none), 1 (very low), 2 (low), 3 (medium), 4 (high), 5 (very high)'},
                            'grassIndex': {'type': 'string', 'description': 'The grass index  is a Standard measurement of the strength of grass pollen at a particular place and time. Useful to identify alergines in the air. The index is based on the following scale, 0 (none), 1 (very low), 2 (low), 3 (medium), 4 (high), 5 (very high)'},
                            'lightningFlashRateDensity': {'type': 'string', 'description': 'The lightning flash rate density in which The number of lightning flashes per unit area per unit time, measured in flashes per square kilometer per hour (metric) or flashes per square mile per hour (imperial)'},
                            'uvIndex': {'type': 'string', 'description': 'The uv index in which The UV Index is a Standard measurement of the strength of sunburn producing UV radiation at a particular place and time. The index is based on the following scale, 0-2 (low), 3-5 (moderate), 6-7 (high), 8-10 (very high), 11+ (extreme)'},
                            'uvHealthConcern': {'type': 'string', 'description': 'When the predicted UV index is within these numerical ranges, the recommended need for protection is indicated by the qualitative description of the values. The concern is based on the following scale, 0-2 (low), 3-5 (moderate), 6-7 (high), 8-10 (very high), 11+ (extreme)'},
                            'weatherCode': {'type': 'string', 'description': 'The text description that conveys the most prominent weather condition. 0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)'},
                            'weatherCodeFullDay': {'type': 'string', 'description': 'The text description that conveys the most prominent weather condition during the day (from sunrise till next sunrise). 0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)'},
                            'weatherCodeNight': {'type': 'string', 'description': 'The text description that conveys the most prominent weather condition during the night (from sunset till sunrise). 0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)'},
                        },
                        # 'enum': ['temperature', 'humidity', 'cloudCover', 'dewPoint', 'epaHealthConcern', 'epaIndex', 'epaPrimaryPollutant', 'fireIndex', 'hailBinary', 'humidity', 'iceAccumilation', 'moonPhase', 'pollutantCO', 'pollutantNO2', 'pollutantO3', 'pollutantSO2', 'precipitationIntensity', 'precipitationProbability', 'precipitationType', 'snowAccumulation', 'temperature', 'temperatureApparent', 'visibility', 'waveSignificantHeight', 'windDirection', 'windGust', 'windSpeed', 'weatherCode', 'weatherCodeFullDay'],
                        'description': 'The weather data fields that you can request. By Defualt the core weather fields are set. Based on the users request, add all and any relevent feilds to effectively answer the users prompt.',
                        #  optional parameters are cloudCover (%), dewPoint (Celcius:Fahrenheit), epaHealthConcern (0 (good)-5 (hazardous)), epaIndex (0 (good)-5 (hazardous)), epaPrimaryPollutant (PM2.5 (0), PM10 (1), O3 (2), NO2 (3), CO (4), SO2 (5)), fireIndex (FWI), hailBinary (Binary Prediction), humidity (%), iceAccumilation (mm:in), moonPhase (0 (new), 1 (waxing cresent), 2 (first quarter), 3 (waxing gibbous), 4 (full), 5 (waning gibbous), 6 (third quarter), 7 (waning cresent)), pollutantCO (ppb), pollutantNO2 (ppb), pollutantO3 (ppb), pollutantSO2 (ppb), precipitationIntensity (mm/hr:in/hr), precipitationProbability (%), precipitationType (0 (none), 1 (rain), 2 (snow), 3 (freezing rain), 4 (ice pellets)), snowAccumulation (mm:in), temperature (Celcius:Fahrenheit), temperatureApparent (Celcius:Fahrenheit), visibility (km:mi), waveSignificantHeight (m:ft), windDirection (degrees), windGust (m/s:mph), windSpeed (m/s:mph), weatherCode (0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)), weatherCodeFullDay (0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)). 
                    },
                },
                "required": [],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_daily_weather_forecast",
            "description": "Get the dialy weather forecast of a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city or town e.g. New York. return city/town name only",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["metric", "imperial"],
                        "description": "The temperature unit to use. Defualt is metric. Infer this from the users location. only return either imperial or metric",
                    },
                    'fields': {
                        'type': 'string',
                        'enum': ['temperature', 'humidity', 'cloudCover', 'dewPoint', 'epaHealthConcern', 'epaIndex', 'epaPrimaryPollutant', 'fireIndex', 'hailBinary', 'humidity', 'iceAccumilation', 'moonPhase', 'pollutantCO', 'pollutantNO2', 'pollutantO3', 'pollutantSO2', 'precipitationIntensity', 'precipitationProbability', 'precipitationType', 'snowAccumulation', 'temperature', 'temperatureApparent', 'visibility', 'waveSignificantHeight', 'windDirection', 'windGust', 'windSpeed', 'weatherCode', 'weatherCodeFullDay'],
                        'description': 'The weather data fields that you will recieve. Default: temperature, humidity, weatherCodeFullDay, precipitationIntensity, precipitationProbability, precipitationType, snowAccumulation, temperatureApparent (feels like), windSpeed. optional parameters are cloudCover (%), dewPoint (Celcius:Fahrenheit), epaHealthConcern (0 (good)-5 (hazardous)), epaIndex (0 (good)-5 (hazardous)), epaPrimaryPollutant (PM2.5 (0), PM10 (1), O3 (2), NO2 (3), CO (4), SO2 (5)), fireIndex (FWI), hailBinary (Binary Prediction), humidity (%), iceAccumilation (mm:in), moonPhase (0 (new), 1 (waxing cresent), 2 (first quarter), 3 (waxing gibbous), 4 (full), 5 (waning gibbous), 6 (third quarter), 7 (waning cresent)), pollutantCO (ppb), pollutantNO2 (ppb), pollutantO3 (ppb), pollutantSO2 (ppb), precipitationIntensity (mm/hr:in/hr), precipitationProbability (%), precipitationType (0 (none), 1 (rain), 2 (snow), 3 (freezing rain), 4 (ice pellets)), snowAccumulation (mm:in), temperature (Celcius:Fahrenheit), temperatureApparent (Celcius:Fahrenheit), visibility (km:mi), waveSignificantHeight (m:ft), windDirection (degrees), windGust (m/s:mph), windSpeed (m/s:mph), weatherCode (0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)), weatherCodeFullDay (0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)). add feilds from optional data when you see fit'
                    },
                },
                "required": []
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_hourly_weather_forecast",
            "description": "Get the hourly weather forecast for the current day of a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city or town e.g. New York. return city/town name only",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["metric", "imperial"],
                        "description": "The temperature unit to use. Defualt is metric. Infer this from the users location. only return either imperial or metric",
                    },
                    'fields': {
                        'type': 'string',
                        'enum': ['temperature', 'humidity', 'cloudCover', 'dewPoint', 'epaHealthConcern', 'epaIndex', 'epaPrimaryPollutant', 'fireIndex', 'hailBinary', 'humidity', 'iceAccumilation', 'moonPhase', 'pollutantCO', 'pollutantNO2', 'pollutantO3', 'pollutantSO2', 'precipitationIntensity', 'precipitationProbability', 'precipitationType', 'snowAccumulation', 'temperature', 'temperatureApparent', 'visibility', 'waveSignificantHeight', 'windDirection', 'windGust', 'windSpeed', 'weatherCode'],
                        'description': 'The weather data fields that you will recieve. Default: temperature, humidity, weatherCode, precipitationIntensity, precipitationProbability, precipitationType, snowAccumulation, temperatureApparent (feels like), windSpeed. optional parameters are cloudCover (%), dewPoint (Celcius:Fahrenheit), epaHealthConcern (0 (good)-5 (hazardous)), epaIndex (0 (good)-5 (hazardous)), epaPrimaryPollutant (PM2.5 (0), PM10 (1), O3 (2), NO2 (3), CO (4), SO2 (5)), fireIndex (FWI), hailBinary (Binary Prediction), humidity (%), iceAccumilation (mm:in), moonPhase (0 (new), 1 (waxing cresent), 2 (first quarter), 3 (waxing gibbous), 4 (full), 5 (waning gibbous), 6 (third quarter), 7 (waning cresent)), pollutantCO (ppb), pollutantNO2 (ppb), pollutantO3 (ppb), pollutantSO2 (ppb), precipitationIntensity (mm/hr:in/hr), precipitationProbability (%), precipitationType (0 (none), 1 (rain), 2 (snow), 3 (freezing rain), 4 (ice pellets)), snowAccumulation (mm:in), temperature (Celcius:Fahrenheit), temperatureApparent (Celcius:Fahrenheit), visibility (km:mi), waveSignificantHeight (m:ft), windDirection (degrees), windGust (m/s:mph), windSpeed (m/s:mph), weatherCode (0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)). add feilds from optional data when you see fit'
                    },
                },
                "required": []
            },
        }
    },
]