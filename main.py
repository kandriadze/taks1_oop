import pandas as pd
from datetime import datetime

DATE_FORMAT = '%y-%m-%d'


class DataframeReader:
    def __init__(self, file_path, start_index, number_of_rows):
        self.df = pd.read_csv(filepath_or_buffer=file_path,
                              skiprows=start_index, nrows=number_of_rows)

    def transform_date(self, column_name='pickup_datetime'):
        self.df = self.df[column_name].apply(
            lambda x: datetime.strptime(x.split('T')[0], DATE_FORMAT).date())

    def shrink_df_to_particular_columns(self, columns):
        self.df = self.df[columns]

    def is_two_or_more_days_ride(self, new_column_name, date_column1,
                                 date_column2):
        self.df[new_column_name] = (
            self.df[date_column1] != self.df[date_column2], 1, 0)
