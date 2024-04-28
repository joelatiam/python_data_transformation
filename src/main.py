"""Transform excel files and store the result into a csv file"""

from pandas_helpers import load_and_transform_sheets, concat_data_frames

EXCEL_FILE_PATH = 'data/CPI_time_series_March_2024.xls'


print('***** Load And Transform Excel Data from', EXCEL_FILE_PATH)
[urban_df, rural_df, all_rwanda_df] = load_and_transform_sheets(
    EXCEL_FILE_PATH,
    ['Urban', 'Rural', 'All Rwanda'],
    3)

print('***** Combine Dataframes')
df_to_concat = [[urban_df, 'Urban'], [
    rural_df, 'Rural'], [all_rwanda_df, 'All Rwanda']]
cpi_df = concat_data_frames(df_to_concat).sort_values(
    by=['Date', 'Source', 'Products'])

CSV_FILE_PATH = 'data/CPI_time_series.csv'
print('***** Create CSV File', CSV_FILE_PATH)
cpi_df.to_csv(CSV_FILE_PATH, index=False)
