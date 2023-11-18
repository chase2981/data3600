from sqlalchemy import create_engine
import pandas as pd
from config import *

engine = create_engine('mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + ENDPOINT + ':' + str(PORT) + '/' + DBNAME)

df = pd.read_csv('county_level_ec_neighborhood.csv')

df.to_sql('ec', con = engine)

print('success')