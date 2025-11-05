import requests
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------
# 1. Set Up: Enter Details
# ------------------------
API_KEY = '923e50ea946c9e1d584b90739345b5f0'  
CITY = 'Pune,in'          # Example: Pune, India
NUM_DAYS = 7              # How many days of history (max 5 for free accounts, use forecast for >5)

# ------------------------
# 2. Fetch Weather Data (Hourly or Daily)
# We'll use OpenWeatherMap's "One Call" API for free tier, or forecast endpoints
# But for most students, the free 'current' and 'forecast' endpoints suffice.
# ------------------------

# Get city geocoordinates
geo_url = f'http://api.openweathermap.org/geo/1.0/direct?q={CITY}&limit=1&appid={API_KEY}'
geo_resp = requests.get(geo_url)
geo_data = geo_resp.json()
if not geo_data:
    print("Couldn't find city coordinates. Check city name.")
    exit()
lat = geo_data[0]['lat']
lon = geo_data[0]['lon']

# Get 5 day/3 hour forecast data (Historical hourly data is paid on OWM)
url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
response = requests.get(url)
data = response.json()

# ------------------------
# 3. Extract Relevant Weather Attributes
# ------------------------
weather_records = []
for entry in data['list']:
    record = {
        'datetime': entry['dt_txt'],
        'temperature': entry['main']['temp'],
        'humidity': entry['main']['humidity'],
        'wind_speed': entry['wind']['speed'],
        'pressure': entry['main']['pressure'],
        'weather': entry['weather'][0]['main']
    }
    # Precipitation - might be missing; handle gracefully
    # Available sometimes under 'rain' or 'snow' key
    precip = 0.0
    if 'rain' in entry and '3h' in entry['rain']:
        precip = entry['rain']['3h']
    if 'snow' in entry and '3h' in entry['snow']:  # snow is rare in many Indian cities
        precip += entry['snow']['3h']
    record['precipitation'] = precip
    weather_records.append(record)

df = pd.DataFrame(weather_records)

# ------------------------
# 4. Clean and Preprocess Data
# ------------------------
df['datetime'] = pd.to_datetime(df['datetime'])
# Handle further missing values if needed
df = df.fillna(0)   # Simple fill for demo

# Derive day and hour
df['date'] = df['datetime'].dt.date
df['hour'] = df['datetime'].dt.hour

# ------------------------
# 5. Data Modeling and Aggregation
# ------------------------

# a) Average, max, min temps
print("Average temperature:", df['temperature'].mean())
print("Max temperature:", df['temperature'].max())
print("Min temperature:", df['temperature'].min())

# b) Daily statistics
daily_stats = df.groupby('date').agg({
    'temperature': ['mean', 'max', 'min'],
    'humidity': 'mean',
    'wind_speed': 'mean',
    'precipitation': 'sum'
}).reset_index()
print("\nDaily weather summary:\n", daily_stats)

# ------------------------
# 6. Visualizations
# ------------------------

# Line plot: temperature trend
plt.figure(figsize=(10,5))
plt.plot(df['datetime'], df['temperature'], marker='o', label='Temperature (°C)')
plt.title(f'Temperature Over Time in {CITY.title()}')
plt.xlabel('Date & Time')
plt.ylabel('Temperature (°C)')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

# Bar plot: daily total precipitation
plt.figure(figsize=(8,4))
plt.bar(daily_stats['date'].astype(str), daily_stats[('precipitation','sum')], color='royalblue')
plt.title(f'Daily Precipitation in {CITY.title()}')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.tight_layout()
plt.show()


# Plot: Humidity Trend Over Time (%)
plt.figure(figsize=(10,5))
plt.plot(df['datetime'], df['humidity'], color='green', marker='o')
plt.title(f'Humidity Trend in {CITY.title()}')
plt.xlabel('Date & Time')
plt.ylabel('Humidity (%)')
plt.grid()
plt.tight_layout()
plt.show()

# Plot: Wind Speed Trend Over Time (m/s)
plt.figure(figsize=(10,5))
plt.plot(df['datetime'], df['wind_speed'], color='blue', marker='s')
plt.title(f'Wind Speed Trend in {CITY.title()}')
plt.xlabel('Date & Time')
plt.ylabel('Wind Speed (m/s)')
plt.grid()
plt.tight_layout()
plt.show()


# Scatter plot: temp vs humidity
plt.figure(figsize=(6,5))
plt.scatter(df['temperature'], df['humidity'], c='purple')
plt.title('Temperature vs. Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.tight_layout()
plt.show()

# Heatmap: correlation between numerical columns
import seaborn as sns
corr = df[['temperature', 'humidity', 'wind_speed', 'precipitation', 'pressure']].corr()
plt.figure(figsize=(6,5))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# ------------------------
# 7. (Optional) - Geospatial Visualization
# ------------------------
print(f'City Latitude: {lat}, Longitude: {lon} ({CITY.title()})')
# For full map, would need folium/geopandas/etc., usually not needed for basic exam

# ------------------------
# 8. Data Sample
# ------------------------
print("\nWeather Data Sample:")
print(df.head())

