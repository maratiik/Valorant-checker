import pandas as pd
import time

while(True):
    tables = pd.read_html('<HTML table>', header = 1)

    # Finding only Valorant table

    for table in tables:
        if table.columns.values[1] == 'Valorant':
            valorant_table = table
            break
    
    # Filtering out useless columns

    valorant_table = valorant_table.filter(['Order ID', 'Service', 'Mode', 'Region', 'Price', 'Status'])

    # Making every value in 'Region' uppercase to filter only EU cases (later in code)

    for row in range(len(valorant_table['Region'])):
        if (type(valorant_table['Region'][row]) is str):
            valorant_table['Region'][row] = valorant_table['Region'][row].upper()

    # Dropping every NaN row in 'Region'

    valorant_table = valorant_table.dropna(subset='Region')

    # Show only EU cases

    valorant_table = valorant_table[valorant_table['Region'].str.contains('EU')]

    print('\n' * 30, valorant_table)

    time.sleep(6)