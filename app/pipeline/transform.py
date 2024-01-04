import pandas as pd

"""
função para transformar uma lista de dataframes em um único dataframe.
"""


def contact_data_frames(data_frame_list):
    print("DataFrames na lista:")
    for df in data_frame_list:
        print(df)

    if not data_frame_list:
        raise ValueError("A lista de DataFrames está vazia")

    return pd.concat(data_frame_list, ignore_index=True)

#def contact_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
#    return pd.concat(data_frame_list, ignore_index=True)
