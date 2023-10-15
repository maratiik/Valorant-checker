import pandas as pd
import time

old_valorant_table = pd.DataFrame()

while(True):
    tables = pd.read_html('https://docs.google.com/spreadsheets/d/1lmuMYYLpJENk6dho7-l0jmPsHoVVl2c9jpaQzRW0SiQ/htmlview#', header = 1, keep_default_na=False)
    # Finding only Valorant table
    for table in tables:
        if table.columns.values[1] == 'Valorant':
            valorant_table = table
            break

    # Filtering out useless columns
    valorant_table = valorant_table.filter(['Order ID', 'Service', 'Mode', 'Region', 'Price', 'Status'])

    # Making every value in 'Region' uppercase to filter only EU cases (later in code)
    for row in range(len(valorant_table['Region'])):
        valorant_table['Region'][row] = valorant_table['Region'][row].upper()

    # Filtering only EU cases
    valorant_table = valorant_table[valorant_table['Region'].str.contains('EU')]

    # Checking if the table somehow changed from the last time
    if old_valorant_table.equals(valorant_table):
        pass
    else:
        if valorant_table.empty:
            print('\n' * 30, 'No EU cases for now')
        else:
            print('\n' * 30, valorant_table)

    # Creating a deep copy of the table to compare them in the if statement
    old_valorant_table = valorant_table.copy(deep=True)

    time.sleep(5)