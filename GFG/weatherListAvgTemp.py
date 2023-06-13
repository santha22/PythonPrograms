arr = []
with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(",")
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature. Ignore the row")

print(arr)
print(sum(arr[0:7]) / len(arr[0:7]))  # average temperature in first week of Jan

print(max(arr[0:10]))  # maximum temperature in first 10 days of Jan


