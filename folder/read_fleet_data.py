""" Have somethinig like this before using calliing this function

fleet_data = read_fleet_data("fleet_data.txt") """


def read_fleet_data(file_name):
    
    
    fleet_data = []
    with open(file_name, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            
            plane_model = data[0].strip()
            business_seats = int(data[1].strip())
            economy_seats = int(data[2].strip())
            total_seats = int(data[3].strip())
            gate = data[4].strip()
            destination = data[5].strip()
            arrival_status = data[6].strip()
            max_baggage_weight = int(data[7].strip())
            
            fleet_data.append([
                plane_model,
                business_seats,
                economy_seats,
                total_seats,
                gate,
                destination,
                arrival_status,
                max_baggage_weight
            ])
    return fleet_data
print(read_fleet_data("fleet_data.txt"))