import os
import glob
from typing import List
import pandas as pd


directory_path = ("/Users/reginaldocunha/Documents/Luciano_Galvão_Filho/1º_Workshop_"
                  "-_Como_Estruturar_um_Projeto_de_Dados_do_Zero/estrutura_workshop/app/data/input")


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    função para ler os arquivos de uma pasta data/input
    e retornar uma lista de dataframes

    args: input/path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """

    all_files = glob.glob(os.path.join(directory_path + '/*.xlsx'))

    data_frame_list = []
    for file in all_files:
        data = pd.read_excel(file)
        data_frame_list.append(data)

    return data_frame_list


if __name__ == "__main__":
    data_frame_list = extract_from_excel(path="data/input")
    print(data_frame_list)
    print('Hello World')
