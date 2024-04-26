import online_judge
from metrics.MasteryProgrammingLanguageSintaxe import MasteryProgrammingLanguageSintaxe as MLS
from online_judge.CodebenchLog import CodebenchLog
import online_judge.Helper as Helper
from datetime import datetime
import pandas as pd
import numpy as np
import csv

__author__ = 'Flávio José Mendes Coelho'


class GradeProcessor:

    def __init__(self):
        self.cb_log = online_judge.cb_log
        # self.dt_start = dt_start
        # self.dt_end = dt_end
        self.inconsistents: int = 0
        self.count_exercise_have_start_code = {}
        self.DECIMAL_PLACES = 3

    def process(self):
        arq1 = "../aux_files/USER-IDS-2023-2.txt"
        arq2 = "../aux_files/cache_notas_2023-2.csv"
        arq3 = "../reports/MODULE_GRADES.csv"
        self.buscar_linhas_e_copiar(arq1, arq2, arq3)

    def buscar_linhas_e_copiar(self, arq1, arq2, arq3):
        # Lendo os arquivos
        caminho_arquivo_L = "../reports/LOGIC_ASSESSMENTS.csv"
        df_L = pd.read_csv(caminho_arquivo_L)

        # Cria df com usuários sem repetição de valores
        df_users_distinct = df_L['USER_ID'].drop_duplicates()

        # Lista para armazenar as linhas encontradas
        linhas_encontradas = []

        for user_id in df_users_distinct:
            # Remover caracteres de quebra de linha
            # s = user_id.strip()
            user_id = str(user_id)

            # Abrir o arquivo arq2 para leitura
            with open(arq2, 'r') as file2:
                # Criar um leitor CSV para o arquivo arq2
                reader = csv.DictReader(file2)

                # Procurar por linhas que contenham a string s
                for linha_arq2 in reader:
                    if user_id in str(linha_arq2.values()):
                        # Remover a primeira coluna
                        primeira_coluna = list(linha_arq2.keys())[0]
                        linha_arq2.pop(primeira_coluna)
                        linhas_encontradas.append(linha_arq2)

        # Nome das colunas para o arquivo arq3
        colunas_arq3 = ['ID_USER', 'ID_ASSESSMENT', 'ID_CLASS', 'YEAR', 'SEMESTER',
                        'ASSESSMENT_DATE_START', 'ASSESSMENT_TITLE', 'ASSESSMENT_TYPE', 'GRADE']

        # Abrir o arquivo arq3 para escrita
        with open(arq3, 'w', newline='') as file3:
            # Criar um escritor CSV para o arquivo arq3
            writer = csv.DictWriter(file3, fieldnames=colunas_arq3)

            # Escrever o cabeçalho no arquivo arq3
            writer.writeheader()

            # Escrever as linhas encontradas no arquivo arq3
            writer.writerows(linhas_encontradas)

    # def buscar_linhas_e_copiar(self, arq1, arq2, arq3):
    #     # Lista para armazenar as linhas encontradas
    #     linhas_encontradas = []
    #
    #     # Abrir o arquivo arq1 para leitura
    #     with open(arq1, 'r') as file1:
    #         # Ler cada linha do arquivo arq1
    #         for linha_arq1 in file1:
    #             # Remover caracteres de quebra de linha
    #             s = linha_arq1.strip()
    #
    #             # Abrir o arquivo arq2 para leitura
    #             with open(arq2, 'r') as file2:
    #                 # Criar um leitor CSV para o arquivo arq2
    #                 reader = csv.DictReader(file2)
    #
    #                 # Procurar por linhas que contenham a string s
    #                 for linha_arq2 in reader:
    #                     if s in str(linha_arq2.values()):
    #                         # Remover a primeira coluna
    #                         primeira_coluna = list(linha_arq2.keys())[0]
    #                         linha_arq2.pop(primeira_coluna)
    #
    #                         linhas_encontradas.append(linha_arq2)
    #
    #     # Nome das colunas para o arquivo arq3
    #     colunas_arq3 = ['ID_USER', 'ID_ASSESSMENT', 'ID_CLASS', 'YEAR', 'SEMESTER',
    #                     'ASSESSMENT_DATE_START', 'ASSESSMENT_TITLE', 'ASSESSMENT_TYPE', 'GRADE']
    #
    #     # Abrir o arquivo arq3 para escrita
    #     with open(arq3, 'w', newline='') as file3:
    #         # Criar um escritor CSV para o arquivo arq3
    #         writer = csv.DictWriter(file3, fieldnames=colunas_arq3)
    #
    #         # Escrever o cabeçalho no arquivo arq3
    #         writer.writeheader()
    #
    #         # Escrever as linhas encontradas no arquivo arq3
    #         writer.writerows(linhas_encontradas)
    #
