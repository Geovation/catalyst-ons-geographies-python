'''Using a DuckDB database to get ONS Geography data from the ONS Postcode Directory'''

import os
import duckdb


def get_ons_from_postcodes(postcodes, db_path='/data/ons_postcodes.duckdb'):
    '''Get the ONS Geography data from the postcodes'''

    # The path is either data/ or /data/ depending on the environment
    if not os.path.exists(db_path):
        db_path = 'data/ons_postcodes.duckdb'

    conn = duckdb.connect(database=db_path, read_only=True)

    # For all postcodes in the postcode array, remove any whitespace
    postcodes = [postcode.replace(' ', '') for postcode in postcodes]

    postcode_list = ','.join(f'\'{p}\'' for p in postcodes)

    query = conn.execute(  # Not parameterised - fix this
        "select * from vw_postcodes where postcode IN (" + postcode_list + ")")

    descriptions = query.description

    postcode_data = query.fetchall()

    conn.close()
    if len(postcode_data) == 0:
        return None

    # Convert the data to a dictionary using the column names
    ons_data = []
    # Loop through each row returned
    for row in postcode_data:
        ons_data_object = {}
        # Loop through each column in the row
        for i, o in enumerate(row):
            if descriptions[i][0] not in ['longitude', 'latitude', 'geometry']:
                ons_data_object[descriptions[i][0]] = row[i]
        ons_data.append(ons_data_object)

    return ons_data
