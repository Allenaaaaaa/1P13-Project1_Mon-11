
def oversold(f_data, d_data):
    """
    Passenger data is omitted because daily data is derived from passenger data
    :param list f_data: flight data
    :param list d_data: daily data
    """
    os_business_seats = []
    os_economy_seats = []

    for f in f_data:
        model = f[0]
        b_seats = f[1]
        e_seats = f[2]
        gate = f[4]

        # Filter data for gate only, convert the filtered data to a list
        filter_d_data = list(filter(lambda x: x[0] == gate, d_data))
        # make sure the filtered data actually has an item
        if len(filter_d_data) != 0:
            # Grab the element
            d = filter_d_data[0]
            sold_bs = d[1]
            sold_es = d[2]

            # compute oversold ct (if < 0, it means there is actually a surplus of seats)
            oversold_b = max(0, sold_bs - b_seats )
            oversold_e = max(0, sold_es - e_seats)

            # Add data to the results
            os_business_seats.append([model, oversold_b])
            os_economy_seats.append([model, oversold_e])

        else:
            # Data does not line up, one of the flights isnt in departures
            raise ValueError("Departure data does not match flight data!")


    return os_business_seats, os_economy_seats