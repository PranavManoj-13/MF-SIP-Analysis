import pandas as pd
from sqlalchemy import create_engine

# Edit Database Details
db_user = 'username'
db_password = 'password'
db_host = 'localhost'
db_port = '3306'
db_name = 'db_name'

engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Edit input file name
csv_file = 'file_name.csv'
df_nav = pd.read_csv(csv_file)

df_nav['date'] = pd.to_datetime(df_nav['date'], format='%d-%m-%Y')
df_nav['nav'] = df_nav['nav'].astype(float)
df_nav['scheme_code'] = df_nav['scheme_code'].astype(int)

# Edit table name
df_nav.to_sql('table_name', con=engine, if_exists='append', index=False)

print("Data imported successfully into MySQL database.")
