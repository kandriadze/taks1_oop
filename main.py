import pandas as pd
from datetime import datetime

class Dataframereader:
    def __init__(self , df):
        self.df = df.iloc[1000:2000 , :].astype(object)


def from_csv(cls , file_path):
    file_path = '/home/kote/Downloads/nyc_tlc_yellow_trips_2018_subset_1.csv'
    df = pd.read_csv(file_path)
    return cls(df)


def transformdate(self):
    self.df = self.df["pickup_datetime"].apply(lambda x: datetime.strptime(x.split('T')[0], '%y-%m-%d').date())
    self.df = self.df["dropoff_datetime"].apply(lambda x: datetime.strptime(x.split('T')[0], '%y-%m-%d').date())

def leaving2rows(self):
    self.df = self.df[['pickup_datetime' , 'dropoff_datetime']]

def is_two_or_more_days_ride(self):
    self.df['is_two_or_more_days'] = (self.df['pickup_datetime'] != self.df['dropoff_datetime'] , 1 , 0)
