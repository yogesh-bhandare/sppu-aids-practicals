# Weather data
weather_data = [
    ["2006-01-01", 10.5],
    ["2006-01-02", 12.3],
    ["2006-01-03", 11.2],
    ["2007-01-01", 22.1],
    ["2007-01-02", 23.4],
    ["2007-01-03", 21.5],
    ["2008-01-01", 5.2],
    ["2008-01-02", 4.8],
    ["2008-01-03", 6.1],
]

# ===== MAPPER =====
mapper_output = []

for row in weather_data:
    year = row[0][:4]
    temp = row[1]

    mapper_output.append((year, temp))

# ===== REDUCER =====
year_data = {}

for year, temp in mapper_output:
    if year not in year_data:
        year_data[year] = []

    year_data[year].append(temp)

# Find hottest and coolest year
hottest_year = ""
coolest_year = ""

hottest_temp = -999
coolest_temp = 999

for year in year_data:
    avg_temp = sum(year_data[year]) / len(year_data[year])

    print(f"{year}: Average = {avg_temp:.2f}°C")

    if avg_temp > hottest_temp:
        hottest_temp = avg_temp
        hottest_year = year

    if avg_temp < coolest_temp:
        coolest_temp = avg_temp
        coolest_year = year

# ===== FINAL OUTPUT =====
print("\n" + "=" * 50)

print(f"Hottest Year: {hottest_year} with average temperature {hottest_temp:.2f}°C")
print(f"Coolest Year: {coolest_year} with average temperature {coolest_temp:.2f}°C")
