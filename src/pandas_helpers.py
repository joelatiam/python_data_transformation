from typing import List, Tuple

import pandas as pd

def load_and_transform_sheets(
    file_path: str,
    sheets_list: list,
    header_from_row: int = 0
)  -> List[pd.DataFrame]:
    """
    Loads and transforms multiple sheets from an Excel file

    Args:
        file_path (str): Path to the Excel file to be loaded.
        sheets_list (list): List of sheet names to be loaded from the file.
        header_from_row (int, optional): Row index containing headers. Defaults to 0.

    Returns:
        list: List of pandas DataFrames, one for each loaded and transformed sheet.

    Raises:
        ValueError: If an empty list of sheets is provided.
    """
    if not sheets_list:
        raise ValueError('sheets_list cannot be empty.')

    df_list = []
    for sheet in sheets_list:
        df = pd.read_excel(file_path , sheet_name=sheet, header=header_from_row)

        # Set up custom headers: first three from row 1, and 'Products' for the fourth.
        header_row = df.iloc[0, :3].tolist() + ['Products']
        df.columns = header_row + df.columns[4:].tolist()

        # Drop unnecessary rows
        df = df.drop([0, len(df)-1])

        # Clean the 'Products' column
        df['Products'] = df['Products'].apply(clean_product_column)


        # Unpivot Date Related Columns
        id_vars_columns = ['Province', 'U_R', 'COICOP', 'Products', 'Weights']

        melted_df = pd.melt(df,
                          id_vars=id_vars_columns,
                          var_name='Date',
                          value_name='Index')

        melted_df['Date'] = pd.to_datetime(melted_df['Date']).dt.date

        df_list.append(melted_df)

    return df_list


def clean_product_column(product_name: str) -> str:
    # Trim whitespace and remove the initial 'v'
    cleaned_name = product_name.strip().lstrip('v').strip()
    return cleaned_name


def concat_data_frames(data_frames: List[Tuple[pd.DataFrame, str]]) -> pd.DataFrame:
    """
    Concate multiple DataFrames into a single DF, adding a 'Source' column to differentiate data sources.

    Args:
        data_frames (List[pd.DataFrame]): The list of DataFrames to combine.
        sources (List[str]): The list of sources corresponding to each DataFrame.

    Returns:
        pd.DataFrame: The combined DataFrame with a new 'Source' column.
    Raises:
        ValueError: If an empty list of dataFrames is provided.
    """
   
    if not len(data_frames):
        raise ValueError('Provide Data Frames to Concat')
    
    df_to_concat = []

    for [df, source] in data_frames:
        df['Source'] = source
        df_to_concat.append(df)
    
    # Concatenate all DataFrames into one
    combined_df = pd.concat(df_to_concat, ignore_index=True)
    
    return combined_df
