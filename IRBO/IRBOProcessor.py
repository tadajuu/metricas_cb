import online_judge
from metrics.Assertiveness import Assertiveness
from online_judge.CodebenchLog import CodebenchLog
from datetime import datetime
import online_judge.Helper as Helper
import pandas as pd
import numpy as np
import csv
from collections import Counter

__author__ = 'Flávio José Mendes Coelho'


class IRBOProcessor:

    def __init__(self):
        self.DECIMAL_PLACES = 3

    def le_arquivo_csv_com_cabecalho(self, caminho_arquivo):
        linhas = []
        with open(caminho_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                linhas.append(linha)
        return linhas

    def escreve_em_arquivo_csv(self, dados_com_cabecalho, caminho_arquivo_saida):
        with open(caminho_arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo_saida:
            escritor_csv = csv.writer(arquivo_saida)

            # Escreve os cabeçalhos, se necessário
            # escritor_csv.writerow(['Coluna1', 'Coluna2', 'Coluna3'])  # Substitua pelos nomes reais das colunas

            # Escreve os dados
            for linha in dados_com_cabecalho:
                escritor_csv.writerow(linha)

    # Construção dos grupos HPX.LSAX.LSAY
    def process(self):
        # HPX.LSAX.LSAY

        # Lendo os arquivos
        caminho_arquivo_L = "../reports/LOGIC_ASSESSMENTS.csv"
        caminho_arquivo_S = "../reports/SINTAXE_ASSESSMENTS.csv"
        caminho_arquivo_A = "../reports/ASSERTIV_ASSESSMENTS.csv"
        caminho_arquivo_grades = "../aux_files/cache_notas_2023-2.csv"
        caminho_arquivo_trabalho_pesos = "../aux_files/trabalho_pesos.csv"
        # linhas_arquivo_L = self.le_arquivo_csv_com_cabecalho(caminho_arquivo_L)
        # linhas_arquivo_S = self.le_arquivo_csv_com_cabecalho(caminho_arquivo_S)
        # linhas_arquivo_A = self.le_arquivo_csv_com_cabecalho(caminho_arquivo_A)
        # linhas_arquivo_GRADES = self.le_arquivo_csv_com_cabecalho(caminho_arquivo_GRADES)
        # linhas_arquivo_trabalho_pesos = self.le_arquivo_csv_com_cabecalho(caminho_arquivo_trabalho_pesos)

        df_L = pd.read_csv(caminho_arquivo_L)
        # print(df_L)
        df_S = pd.read_csv(caminho_arquivo_S)
        df_A = pd.read_csv(caminho_arquivo_A)
        df_grades = pd.read_csv(caminho_arquivo_grades)
        df_trabalho_pesos = pd.read_csv(caminho_arquivo_trabalho_pesos)

        # Seleciona df com usuários sem repetição de valores
        df_users_distinct = df_L['USER_ID'].drop_duplicates()

        ESTADO_0 = 0
        ESTADO_1 = 1
        ESTADO_2 = 2
        ESTADO_3 = 3
        ESTADO_INICIAL = ESTADO_0

        contagem = {}
        report_linhas = []
        for user_id in df_users_distinct:

            user_id_int = int(user_id)
            linhas_df_L = df_L.query('USER_ID == @user_id_int', inplace=False)
            linhas_df_S = df_S.query('USER_ID == @user_id_int', inplace=False)
            linhas_df_A = df_A.query('USER_ID == @user_id_int', inplace=False)
            NUM_LINHAS_df_L = linhas_df_L.shape[0]
            EOF = NUM_LINHAS_df_L

            estado = ESTADO_INICIAL
            i: int = 0             # while i < NUM_LINHAS_df_L:
            while estado != ESTADO_3:

                date_start = linhas_df_L.iloc[i]['DATE_START']
                semester_id = linhas_df_L.iloc[i]['SEMESTER_ID']
                year, semester = semester_id[:3], semester_id[5]
                class_id_int = int(linhas_df_L.iloc[i]['CLASS_ID'])
                assessment_type = linhas_df_L.iloc[i]['ASSESSMENT_TYPE']
                assessments_id_int = int(linhas_df_L.iloc[i]['ASSESSMENTS_ID'])

                if assessment_type[:3] == "Lab":
                    tipo_de_trabalho = "homework"
                elif assessment_type[:2] == "TP":
                    tipo_de_trabalho = "exam"

                if estado == ESTADO_0 and tipo_de_trabalho == "exam" and i+1 < EOF:
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                  and ID_ASSESSMENT == @assessments_id_int \
                                                  and ID_CLASS == @class_id_int \
                                                  and ASSESSMENT_TYPE == 2',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i]['IRBO_GRADE']
                    Y = Helper.IRBO_scale("Y", grade)
                    ___LSAY = "----." + LSA + Y
                    report_linha = str(user_id_int) + " " + str(class_id_int) + " " + str(None) + " " + str("Lab ?") + " " + str(assessments_id_int) + " " + assessment_type + " " + ___LSAY
                    report_linhas.append(report_linha)
                    contagem.setdefault(___LSAY, 0)
                    contagem[___LSAY] += 1
                    estado = ESTADO_0

                elif estado == ESTADO_0 and tipo_de_trabalho == "homework" and i+1 < EOF:
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                  and ID_ASSESSMENT == @assessments_id_int \
                                                  and ID_CLASS == @class_id_int \
                                                  and ASSESSMENT_TYPE == 1',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i]['IRBO_GRADE']
                    X = Helper.IRBO_scale("X", grade)
                    LSAX = LSA + X     # a ser completado em um próximo estado
                    report_linha_0 = str(user_id_int) + " " + str(class_id_int) + " " + str(assessments_id_int) + " " + assessment_type + " "
                    estado = ESTADO_1

                # >>>>>> Estado de finalização <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                elif estado == ESTADO_0 and tipo_de_trabalho == "exam" and i+1 == EOF:
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                  and ID_ASSESSMENT == @assessments_id_int \
                                                  and ID_CLASS == @class_id_int \
                                                  and ASSESSMENT_TYPE == 2',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i]['IRBO_GRADE']
                    Y = Helper.IRBO_scale("Y", grade)
                    ___LSAY = "----." + LSA + Y
                    report_linha = str(user_id_int) + " " + str(class_id_int) + " " + str(None) + " " + str("Lab ?") + " " + str(assessments_id_int) + " " + assessment_type + " " + ___LSAY
                    report_linhas.append(report_linha)
                    contagem.setdefault(___LSAY, 0)
                    contagem[___LSAY] += 1
                    estado = ESTADO_3

                # >>>>>> Estado de finalização <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                elif estado == ESTADO_0 and tipo_de_trabalho == "homework" and i+1 == EOF:
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                  and ID_ASSESSMENT == @assessments_id_int \
                                                  and ID_CLASS == @class_id_int \
                                                  and ASSESSMENT_TYPE == 1',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i]['IRBO_GRADE']
                    X = Helper.IRBO_scale("X", grade)
                    LSAX = LSA + X
                    LSAX___ = LSAX + ".----"
                    report_linha = str(user_id_int) + " " + str(class_id_int) + " " + str(assessments_id_int) + " " + assessment_type + " " + str(None) + " " + "TP ?" + " " + LSAX___
                    report_linhas.append(report_linha)
                    contagem.setdefault(LSAX___, 0)
                    contagem[LSAX___] += 1
                    estado = ESTADO_3

                elif estado == ESTADO_1 and tipo_de_trabalho == "exam" and i+1 < EOF:
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                  and ID_ASSESSMENT == @assessments_id_int \
                                                  and ID_CLASS == @class_id_int \
                                                  and ASSESSMENT_TYPE == 2',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i]['IRBO_GRADE']
                    Y = Helper.IRBO_scale("Y", grade)
                    LSAY = LSA + Y
                    LSAX_LSAY = LSAX + "." + LSAY
                    report_linha_1 = report_linha_0 + str(assessments_id_int) + " " + assessment_type + " " + LSAX_LSAY
                    report_linhas.append(report_linha_1)
                    contagem.setdefault(LSAX_LSAY, 0)
                    contagem[LSAX_LSAY] += 1
                    estado = ESTADO_0

                elif estado == ESTADO_1 and tipo_de_trabalho == "homework" and i+1 < EOF:
                    # Processa LSAX do estado anterior
                    LSAX___ = LSAX + ".----"
                    report_linha_1 = report_linha_0 + str(None) + " " + "TP ?" + " " + LSAX___
                    report_linhas.append(report_linha_1)
                    contagem.setdefault(LSAX___, 0)
                    contagem[LSAX___] += 1

                    # Processa LSAX do estado atual
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                  and ID_ASSESSMENT == @assessments_id_int \
                                                  and ID_CLASS == @class_id_int \
                                                  and ASSESSMENT_TYPE == 1',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i]['IRBO_GRADE']
                    X = Helper.IRBO_scale("X", grade)
                    LSAX = LSA + X     # a ser completado em um próximo estado
                    report_linha_0 = str(user_id_int) + " " + str(class_id_int) + " " + str(assessments_id_int) + " " + assessment_type + " "
                    estado = ESTADO_2

                # >>>>>> Estado de finalização <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                elif estado == ESTADO_1 and tipo_de_trabalho == "homework" and i+1 == EOF:
                    # Processa LSAX do estado anterior
                    LSAX___ = LSAX + ".----"
                    report_linha_1 = report_linha_0 + str(None) + " " + "TP ?" + " " + LSAX___
                    report_linhas.append(report_linha_1)
                    contagem.setdefault(LSAX___, 0)
                    contagem[LSAX___] += 1

                    # Processa LSAX do estado atual
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                  and ID_ASSESSMENT == @assessments_id_int \
                                                  and ID_CLASS == @class_id_int \
                                                  and ASSESSMENT_TYPE == 1',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i]['IRBO_GRADE']
                    X = Helper.IRBO_scale("X", grade)
                    LSAX = LSA + X  # a ser completado em um próximo estado
                    LSAX___ = LSAX + ".----"
                    report_linha = str(user_id_int) + " " + str(class_id_int) + " " + str(assessments_id_int) + " " + assessment_type + " " + str(None) + " " + "TP ?" + " " + LSAX___
                    report_linhas.append(report_linha)
                    contagem.setdefault(LSAX___, 0)
                    contagem[LSAX___] += 1
                    estado = ESTADO_3

                # >>>>>> Estado de finalização <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                elif estado == ESTADO_1 and tipo_de_trabalho == "exam" and i+1 == EOF:
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                   and ID_ASSESSMENT == @assessments_id_int \
                                                   and ID_CLASS == @class_id_int \
                                                   and ASSESSMENT_TYPE == 2',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i][
                        'IRBO_GRADE']
                    Y = Helper.IRBO_scale("Y", grade)
                    LSAY = LSA + Y
                    LSAX_LSAY = LSAX + "." + LSAY
                    report_linha_1 = report_linha_0 + str(assessments_id_int) + " " + assessment_type + " " + LSAX_LSAY
                    report_linhas.append(report_linha_1)
                    contagem.setdefault(LSAX_LSAY, 0)
                    contagem[LSAX_LSAY] += 1
                    estado = ESTADO_3

                elif estado == ESTADO_2 and tipo_de_trabalho == "homework" and i+1 < EOF:
                    # Processa LSAX do estado anterior
                    LSAX___ = LSAX + ".----"
                    report_linha_1 = report_linha_0 + str(None) + " " + "TP ?" + " " + LSAX___
                    report_linhas.append(report_linha_1)
                    contagem.setdefault(LSAX___, 0)
                    contagem[LSAX___] += 1

                    # Processa LSAX do estado atual
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                  and ID_ASSESSMENT == @assessments_id_int \
                                                  and ID_CLASS == @class_id_int \
                                                  and ASSESSMENT_TYPE == 1',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i]['IRBO_GRADE']
                    X = Helper.IRBO_scale("X", grade)
                    LSAX = LSA + X     # a ser completado em um próximo estado
                    report_linha_0 = str(user_id_int) + " " + str(class_id_int) + " " + str(assessments_id_int) + " " + assessment_type + " "
                    estado = ESTADO_1

                elif estado == ESTADO_2 and tipo_de_trabalho == "exam" and i+1 < EOF:
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                   and ID_ASSESSMENT == @assessments_id_int \
                                                   and ID_CLASS == @class_id_int \
                                                   and ASSESSMENT_TYPE == 2',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i][
                        'IRBO_GRADE']
                    Y = Helper.IRBO_scale("Y", grade)
                    LSAY = LSA + Y
                    LSAX_LSAY = LSAX + "." + LSAY
                    report_linha_1 = report_linha_0 + str(assessments_id_int) + " " + assessment_type + " " + LSAX_LSAY
                    report_linhas.append(report_linha_1)
                    contagem.setdefault(LSAX_LSAY, 0)
                    contagem[LSAX_LSAY] += 1
                    estado = ESTADO_0

                # >>>>>> Estado de finalização <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                elif estado == ESTADO_2 and tipo_de_trabalho == "homework" and i+1 == EOF:
                    # Processa LSAX do estado anterior
                    LSAX___ = LSAX + ".----"
                    report_linha_1 = report_linha_0 + str(None) + " " + "TP ?" + " " + LSAX___
                    report_linhas.append(report_linha_1)
                    contagem.setdefault(LSAX___, 0)
                    contagem[LSAX___] += 1

                    # Processa LSAX do estado atual
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                      and ID_ASSESSMENT == @assessments_id_int \
                                                      and ID_CLASS == @class_id_int \
                                                      and ASSESSMENT_TYPE == 1',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i][
                        'IRBO_GRADE']
                    X = Helper.IRBO_scale("X", grade)
                    LSAX = LSA + X
                    LSAX___ = LSAX + ".----"
                    report_linha = str(user_id_int) + " " + str(class_id_int) + " " + str(
                        assessments_id_int) + " " + assessment_type + " " + str(None) + " " + "TP ?" + " " + LSAX___
                    report_linhas.append(report_linha)
                    contagem.setdefault(LSAX___, 0)
                    contagem[LSAX___] += 1
                    estado = ESTADO_3

                # >>>>>> Estado de finalização <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                elif estado == ESTADO_2 and tipo_de_trabalho == "exam" and i+1 == EOF:
                    data_grades = df_grades.query('ID_USER == @user_id_int \
                                                   and ID_ASSESSMENT == @assessments_id_int \
                                                   and ID_CLASS == @class_id_int \
                                                   and ASSESSMENT_TYPE == 2',
                                                  inplace=False)
                    grade = float(data_grades['GRADE'].values[0])
                    LSA = linhas_df_L.iloc[i]['IRBO_GRADE'] + linhas_df_S.iloc[i]['IRBO_GRADE'] + linhas_df_A.iloc[i][
                        'IRBO_GRADE']
                    Y = Helper.IRBO_scale("Y", grade)
                    LSAY = LSA + Y
                    LSAX_LSAY = LSAX + "." + LSAY
                    report_linha_1 = report_linha_0 + str(assessments_id_int) + " " + assessment_type + " " + LSAX_LSAY
                    report_linhas.append(report_linha_1)
                    contagem.setdefault(LSAX_LSAY, 0)
                    contagem[LSAX_LSAY] += 1
                    estado = ESTADO_3

                i += 1
                if i >= EOF:
                    estado = ESTADO_3

        print(len(report_linhas))
        for linha in report_linhas:
            print(linha)
        print()
        print("********************************************************************************")

        ordenado_por_valor = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
        print(len(ordenado_por_valor))
        for linha in ordenado_por_valor:
            grupo, valor = linha
            print(grupo, valor)
        # print(contagem)


    def process_ver0(self):
        # HPX.LSAX.LSAY

        # Lendo os arquivos
        caminho_arquivo_L = "../reports/LOGIC_ASSESSMENTS.csv"
        caminho_arquivo_S = "../reports/SINTAXE_ASSESSMENTS.csv"
        caminho_arquivo_A = "../reports/ASSERTIV_ASSESSMENTS.csv"
        caminho_arquivo_GRADES = "../aux_files/cache_notas_2023-2.csv"
        caminho_arquivo_trabalho_pesos = "../aux_files/trabalho_pesos.csv"
        linhas_arquivo_L = self.le_arquivo_csv_com_cabecalho(caminho_arquivo_L)
        linhas_arquivo_S = self.le_arquivo_csv_com_cabecalho(caminho_arquivo_S)
        linhas_arquivo_A = self.le_arquivo_csv_com_cabecalho(caminho_arquivo_A)
        linhas_arquivo_GRADES = self.le_arquivo_csv_com_cabecalho(caminho_arquivo_GRADES)
        linhas_arquivo_trabalho_pesos = self.le_arquivo_csv_com_cabecalho(caminho_arquivo_trabalho_pesos)

        df_grades = pd.read_csv(caminho_arquivo_GRADES)
        df_trabalho_pesos = pd.read_csv(caminho_arquivo_trabalho_pesos)

        # Itera sobre as linhas dos arquivos L, S e A
        i: int = 1
        for dict_linha_L, dict_linha_S, dict_linha_A in zip(linhas_arquivo_L, linhas_arquivo_S, linhas_arquivo_A):

            DATE_START = dict_linha_L['DATE_START']
            SEMESTER_ID = dict_linha_L['SEMESTER_ID']
            YEAR, SEMESTER = SEMESTER_ID[:3], SEMESTER_ID[5]
            CLASS_ID = dict_linha_L['CLASS_ID']
            ASSESSMENT_TYPE = dict_linha_L['ASSESSMENT_TYPE']
            ASSESSMENTS_ID = dict_linha_L['ASSESSMENTS_ID']
            USER_ID = dict_linha_L['USER_ID']
            IRBO = dict_linha_L['IRBO_GRADE'] + dict_linha_S['IRBO_GRADE'] + dict_linha_A['IRBO_GRADE']

            # COLUNAS trabalho_pesos: id_turma,id_trabalho,tipo,peso
            data_trabalho_pesos = df_trabalho_pesos.query('id_turma == @CLASS_ID_INT \
                                                          and id_trabalho == @ASSESSMENTS_ID_INT',
                                                          inplace=False)
            tipo_de_trabalho = "homework" if int(data_trabalho_pesos['tipo']) == 1 else "exam"
            # Um lab padrão é aquele que não é "extras", "desafios", etc.
            trabalho_eh_um_lab_padrao = True if int(data_trabalho_pesos['peso']) == 1 else False

            # Faça o mesmo para o segundo arquivo
            # linha2 = next(csvreader2, None)  # Lê a próxima linha do arquivo 2, se não houver, retorna None
            # if linha2 is not None:
            #     print('Linha do arquivo 2:', linha2)
            # else:
            #     print('Fim do arquivo 2 alcançado.')
            #     break

            # Cabeçalho do arquico grades
            # ID_USER, ID_ASSESSMENT, ID_CLASS, YEAR, SEMESTER, ASSESSMENT_DATE_START, ASSESSMENT_TITLE, ASSESSMENT_TYPE, GRADE
            # if ASSESSMENT_TYPE in ['Lab 1', 'Lab 01', 'Lab 2', 'Lab 02', 'Lab 3', 'Lab 03', 'Lab 4', 'Lab 04',
            #                     'Lab 5', 'Lab 05', 'Lab 6', 'Lab 06', 'Lab 7', 'Lab 07']:
            if tipo_de_trabalho == "homework" and trabalho_eh_um_lab_padrao:
                print(f"{DATE_START} {SEMESTER_ID} {CLASS_ID} {ASSESSMENTS_ID} {USER_ID} LSAX={IRBO}?", end="")
                # print(f"{DATE_START} {SEMESTER_ID} {CLASS_ID} {ASSESSMENTS_ID} {USER_ID} LSAX={IRBO}?", end="")

            if ASSESSMENT_TYPE in ['TP 1', 'TP 01', 'TP 2', 'TP 02', 'TP 3', 'TP 03', 'TP 4', 'TP 04', 'TP 5', 'TP 05',
                                   'TP 6', 'TP 06', 'TP 7', 'TP 07']:
                USER_ID_INT = int(USER_ID)
                ASSESSMENTS_ID_INT = int(ASSESSMENTS_ID)
                CLASS_ID_INT = int(CLASS_ID)
                data_grades = df_grades.query('ID_USER == @USER_ID_INT \
                                        and ID_ASSESSMENT == @ASSESSMENTS_ID_INT \
                                        and ID_CLASS == @CLASS_ID_INT \
                                        and ASSESSMENT_TYPE == 2',
                                              inplace=False)
                GRADE = float(data_grades['GRADE'])
                IRBO_Y = Helper.IRBO_scale("Y", GRADE)
                print(f".LSAY={IRBO}{IRBO_Y}")
                # print(f"{DATE_START} {SEMESTER_ID} {CLASS_ID} {ASSESSMENTS_ID} {USER_ID} {ASSESSMENT_TYPE} LSAY={IRBO}{IRBO_Y}")
                # print(data.to_string())
            # if i == 20:
            #     break
            i += 1

