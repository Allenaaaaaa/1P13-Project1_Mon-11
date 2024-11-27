def passenger_data():
    file = open("passenger_data_v2.txt", "r")
    passenger_data = []
    for line in file:
        line = line.split(",")
        print(line)
        line[-1] = line[-1].strip()
        line[6] = float(line[6])
        passenger_data.append(line)
    file.close()
    return passenger_data

print(passenger_data())