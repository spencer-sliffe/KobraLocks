import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Specify the dtypes for columns with mixed types and handle missing values
dtype_dict = {
    'date': 'str',
    'day_night': 'str',
    'park_id': 'str',
    'v_line_score': 'str',
    'h_line_score': 'str',
    'hp_umpire_id': 'str',
    'hp_umpire_name': 'str',
    '1b_umpire_id': 'str',
    '1b_umpire_name': 'str',
    '2b_umpire_id': 'str',
    '2b_umpire_name': 'str',
    '3b_umpire_id': 'str',
    '3b_umpire_name': 'str',
    'lf_umpire_id': 'str',
    'lf_umpire_name': 'str',
    'rf_umpire_id': 'str',
    'rf_umpire_name': 'str',
    'v_manager_id': 'str',
    'v_manager_name': 'str',
    'h_manager_id': 'str',
    'h_manager_name': 'str',
    'winning_pitcher_id': 'str',
    'winning_pitcher_name': 'str',
    'losing_pitcher_id': 'str',
    'losing_pitcher_name': 'str',
    'saving_pitcher_id': 'str',
    'saving_pitcher_name': 'str',
    'winning_rbi_batter_id': 'str',
    'winning_rbi_batter_id_name': 'str',
    'v_starting_pitcher_id': 'str',
    'v_starting_pitcher_name': 'str',
    'h_starting_pitcher_id': 'str',
    'h_starting_pitcher_name': 'str',
    'v_player_1_id': 'str',
    'v_player_1_name': 'str',
    'v_player_2_id': 'str',
    'v_player_2_name': 'str',
    'v_player_3_id': 'str',
    'v_player_3_name': 'str',
    'v_player_4_id': 'str',
    'v_player_4_name': 'str',
    'v_player_5_id': 'str',
    'v_player_5_name': 'str',
    'v_player_6_id': 'str',
    'v_player_6_name': 'str',
    'v_player_7_id': 'str',
    'v_player_7_name': 'str',
    'v_player_8_id': 'str',
    'v_player_8_name': 'str',
    'v_player_9_id': 'str',
    'v_player_9_name': 'str',
    'h_player_1_id': 'str',
    'h_player_1_name': 'str',
    'h_player_2_id': 'str',
    'h_player_2_name': 'str',
    'h_player_3_id': 'str',
    'h_player_3_name': 'str',
    'h_player_4_id': 'str',
    'h_player_4_name': 'str',
    'h_player_5_id': 'str',
    'h_player_5_name': 'str',
    'h_player_6_id': 'str',
    'h_player_6_name': 'str',
    'h_player_7_id': 'str',
    'h_player_7_name': 'str',
    'h_player_8_id': 'str',
    'h_player_8_name': 'str',
    'h_player_9_id': 'str',
    'h_player_9_name': 'str',
    'additional_info': 'str',
    'acquisition_info': 'str'
}

# Create a connection to the SQL Server database
server = 'kobralocks-sql.database.windows.net'
database = 'KobraLocksDevDB'
username = 'KL-ADMIN-1'
password = 'zuhdym-8gijwo-dydHah'
driver = 'ODBC Driver 17 for SQL Server'

connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
engine = create_engine(connection_string)

# Determine the row to start from
start_row = 156833

# Read the CSV file with specified dtypes and handle missing values, starting from the specified row
chunksize = 1000
try:
    for i, chunk in enumerate(pd.read_csv('../game_logs.csv', dtype=dtype_dict, na_values=['', ' ', 'null', 'NaN', 'None'], chunksize=chunksize, skiprows=range(1, start_row + 1))):
        chunk.to_sql('api_1871through2016MlbGameData', engine, if_exists='append', index=False)
        logging.info(f'Chunk {i + 1 + start_row // chunksize} inserted successfully')
except SQLAlchemyError as e:
    logging.error(f'Error occurred: {e}')

