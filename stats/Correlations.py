# import online_judge.Helper as Helper
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg
import csv

__author__ = 'Flávio José Mendes Coelho'


class Correlations:

    def __init__(self):
        pass

    def create_SUMARY_METRICS_CSV(self):
        # Lendo os arquivos
        caminho_arquivo_L = "../reports/LOGIC_ASSESSMENTS.csv"
        caminho_arquivo_S = "../reports/SINTAXE_ASSESSMENTS.csv"
        caminho_arquivo_A = "../reports/ASSERTIV_ASSESSMENTS.csv"
        caminho_arquivo_grades = "../reports/MODULE_GRADES.csv"
        Summary_Metrics_filepath = "../reports/SUMMARY_METRICS.csv"
        df_L = pd.read_csv(caminho_arquivo_L)
        df_S = pd.read_csv(caminho_arquivo_S)
        df_A = pd.read_csv(caminho_arquivo_A)
        df_grades = pd.read_csv(caminho_arquivo_grades)

        # Cria df com usuários sem repetição de valores
        df_users_distinct = df_L['USER_ID'].drop_duplicates()

        ESTADO_0 = 0
        ESTADO_1 = 1
        ESTADO_2 = 2
        ESTADO_3 = 3
        ESTADO_INICIAL = ESTADO_0

        # Nome das colunas para o arquivo Summary
        columns = ['USER_ID', 'CLASS_ID', 'ASSESSMENT_TYPE_1', 'ASSESSMENT_ID_1', 'ASSESSMENT_TYPE_2', 'ASSESSMENT_ID_2',
                   'L_LAB', 'S_LAB', 'A_LAB', 'GRADE_LAB', 'L_TP', 'S_TP', 'A_TP', 'GRADE_TP']

        # Abrir o arquivo para escrita
        with open(Summary_Metrics_filepath, 'w', newline='') as summary_file:
            # Criar um escritor CSV para o arquivo summary_file
            writer = csv.writer(summary_file)

            # Escrever o cabeçalho no arquivo summary_file
            writer.writerow(columns)

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
                i: int = 0
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
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE']) + ","
                        Y = str(grade)
                        ___LSAY = "0.0,0.0,0.0,0.0," + LSA + Y
                        ___LSAY_lst = ___LSAY.split(',')
                        report_linha = str(user_id_int) + "," + str(class_id_int) + "," + str(None) + "," + str("Lab ?") + "," + str(assessments_id_int) + "," + assessment_type + "," + ___LSAY
                        # report_linha_lst = report_linha.split(',')
                        # df_Summary.loc[len(df_Summary)] = report_linha_lst
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
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE']) + ","
                        X = str(grade)
                        LSAX = LSA + X     # a ser completado em um próximo estado
                        report_linha_0 = str(user_id_int) + "," + str(class_id_int) + "," + str(assessments_id_int) + "," + assessment_type + ","
                        estado = ESTADO_1

                    # >>>>>> Estado de finalização <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    elif estado == ESTADO_0 and tipo_de_trabalho == "exam" and i+1 == EOF:
                        data_grades = df_grades.query('ID_USER == @user_id_int \
                                                      and ID_ASSESSMENT == @assessments_id_int \
                                                      and ID_CLASS == @class_id_int \
                                                      and ASSESSMENT_TYPE == 2',
                                                      inplace=False)
                        grade = float(data_grades['GRADE'].values[0])
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE']) + ","
                        Y = str(grade)
                        ___LSAY = "0.0,0.0,0.0,0.0," + LSA + Y
                        report_linha = str(user_id_int) + "," + str(class_id_int) + "," + str(None) + "," + str("Lab ?") + "," + str(assessments_id_int) + "," + assessment_type + "," + ___LSAY
                        # report_linha_lst = report_linha.split(',')
                        # df_Summary.loc[len(df_Summary)] = report_linha_lst
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
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE']) + ","
                        X = str(grade)
                        LSAX = LSA + X
                        # LSAX___ = LSAX + ".----"
                        LSAX___ = LSAX + "," + "0.0,0.0,0.0,0.0"
                        report_linha = str(user_id_int) + "," + str(class_id_int) + "," + str(assessments_id_int) + "," + assessment_type + "," + str(None) + "," + "TP ?" + "," + LSAX___
                        # report_linha_lst = report_linha.split(',')
                        # df_Summary.loc[len(df_Summary)] = report_linha_lst
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
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE']) + ","
                        Y = str(grade)
                        LSAY = LSA + Y
                        LSAX_LSAY = LSAX + "," + LSAY
                        report_linha_1 = report_linha_0 + str(assessments_id_int) + "," + assessment_type + "," + LSAX_LSAY
                        report_linha_lst = report_linha_1.split(',')
                        # new_line = dict(zip(columns, report_linha_lst))
                        # df_Summary = df_Summary.append(new_line, ignore_index=True)
                        # nova_linha_df = pd.DataFrame(report_linha_lst, columns=columns)
                        # df_Summary = pd.concat([df_Summary, nova_linha_df], ignore_index=True)
                        # Escrever as linhas encontradas no arquivo summary_file
                        writer.writerow(report_linha_lst)
                        report_linhas.append(report_linha_1)
                        contagem.setdefault(LSAX_LSAY, 0)
                        contagem[LSAX_LSAY] += 1
                        estado = ESTADO_0

                    elif estado == ESTADO_1 and tipo_de_trabalho == "homework" and i+1 < EOF:
                        # Processa LSAX do estado anterior
                        LSAX___ = LSA + "0.0,0.0,0.0,0.0"
                        report_linha_1 = report_linha_0 + str(None) + "," + "TP ?" + "," + LSAX___
                        # report_linha_lst = report_linha_1.split(',')
                        # df_Summary.loc[len(df_Summary)] = report_linha_lst
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
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE']) + ","
                        X = str(grade)
                        LSAX = LSA + X     # a ser completado em um próximo estado
                        report_linha_0 = str(user_id_int) + "," + str(class_id_int) + "," + str(assessments_id_int) + "," + assessment_type + ","
                        estado = ESTADO_2

                    # >>>>>> Estado de finalização <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    elif estado == ESTADO_1 and tipo_de_trabalho == "homework" and i+1 == EOF:
                        # Processa LSAX do estado anterior
                        # LSAX___ = LSAX + ".----"
                        LSAX___ = LSAX + "," + "0.0,0.0,0.0,0.0"
                        report_linha_1 = report_linha_0 + str(None) + "," + "TP ?" + "," + LSAX___
                        # report_linha_lst = report_linha_1.split(',')
                        # df_Summary.loc[len(df_Summary)] = report_linha_lst
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
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE']) + ","
                        X = str(grade)
                        LSAX = LSA + X  # a ser completado em um próximo estado
                        # LSAX___ = LSAX + ".----"
                        LSAX___ = LSAX + "," + "0.0,0.0,0.0,0.0"
                        report_linha = str(user_id_int) + "," + str(class_id_int) + "," + str(assessments_id_int) + "," + assessment_type + "," + str(None) + "," + "TP ?" + "," + LSAX___
                        # report_linha_lst = report_linha_1.split(',')
                        # df_Summary.loc[len(df_Summary)] = report_linha_lst
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
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE'])
                        Y = str(grade)
                        LSAY = LSA + "," + Y
                        LSAX_LSAY = LSAX + "," + LSAY
                        report_linha_1 = report_linha_0 + str(assessments_id_int) + "," + assessment_type + "," + LSAX_LSAY
                        report_linha_lst = report_linha_1.split(',')
                        # new_line = dict(zip(columns, report_linha_lst))
                        # df_Summary = df_Summary.append(new_line, ignore_index=True)
                        # nova_linha_df = pd.DataFrame(report_linha_lst, columns=columns)
                        # df_Summary = pd.concat([df_Summary, nova_linha_df], ignore_index=True)
                        # Escrever as linhas encontradas no arquivo summary_file
                        writer.writerow(report_linha_lst)
                        report_linhas.append(report_linha_1)
                        contagem.setdefault(LSAX_LSAY, 0)
                        contagem[LSAX_LSAY] += 1
                        estado = ESTADO_3

                    elif estado == ESTADO_2 and tipo_de_trabalho == "homework" and i+1 < EOF:
                        # Processa LSAX do estado anterior
                        # LSAX___ = LSAX + ".----"
                        LSAX___ = LSAX + "," + "0.0,0.0,0.0,0.0"
                        report_linha_1 = report_linha_0 + str(None) + "," + "TP ?" + "," + LSAX___
                        report_linha_lst = report_linha_1.split(',')
                        # new_line = dict(zip(columns, report_linha_lst))
                        # df_Summary = df_Summary.append(new_line, ignore_index=True)
                        # nova_linha_df = pd.DataFrame(report_linha_lst, columns=columns)
                        # df_Summary = pd.concat([df_Summary, nova_linha_df], ignore_index=True)
                        # Escrever as linhas encontradas no arquivo summary_file
                        # writer.writerow(report_linha_lst)
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
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE']) + ","
                        X = str(grade)
                        LSAX = LSA + X     # a ser completado em um próximo estado
                        report_linha_0 = str(user_id_int) + "," + str(class_id_int) + "," + str(assessments_id_int) + "," + assessment_type + ","
                        estado = ESTADO_1

                    elif estado == ESTADO_2 and tipo_de_trabalho == "exam" and i+1 < EOF:
                        data_grades = df_grades.query('ID_USER == @user_id_int \
                                                       and ID_ASSESSMENT == @assessments_id_int \
                                                       and ID_CLASS == @class_id_int \
                                                       and ASSESSMENT_TYPE == 2',
                                                      inplace=False)
                        grade = float(data_grades['GRADE'].values[0])
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE'])
                        Y = str(grade)
                        LSAY = LSA + "," + Y
                        LSAX_LSAY = LSAX + "," + LSAY
                        report_linha_1 = report_linha_0 + str(assessments_id_int) + "," + assessment_type + "," + LSAX_LSAY
                        report_linha_lst = report_linha_1.split(',')
                        # new_line = dict(zip(columns, report_linha_lst))
                        # df_Summary = df_Summary.append(new_line, ignore_index=True)
                        # nova_linha_df = pd.DataFrame(report_linha_lst, columns=columns)
                        # df_Summary = pd.concat([df_Summary, nova_linha_df], ignore_index=True)
                        # Escrever as linhas encontradas no arquivo summary_file
                        writer.writerow(report_linha_lst)
                        report_linhas.append(report_linha_1)
                        contagem.setdefault(LSAX_LSAY, 0)
                        contagem[LSAX_LSAY] += 1
                        estado = ESTADO_0

                    # >>>>>> Estado de finalização <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    elif estado == ESTADO_2 and tipo_de_trabalho == "homework" and i+1 == EOF:
                        # Processa LSAX do estado anterior
                        # LSAX___ = LSAX + ".----"
                        LSAX___ = LSAX + "," + "0.0,0.0,0.0,0.0"
                        report_linha_1 = report_linha_0 + str(None) + "," + "TP ?" + "," + LSAX___
                        report_linha_lst = report_linha_1.split(',')
                        # new_line = dict(zip(columns, report_linha_lst))
                        # df_Summary = df_Summary.append(new_line, ignore_index=True)
                        # nova_linha_df = pd.DataFrame(report_linha_lst, columns=columns)
                        # df_Summary = pd.concat([df_Summary, nova_linha_df], ignore_index=True)
                        # Escrever as linhas encontradas no arquivo summary_file
                        # writer.writerow(report_linha_lst)
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
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE'])
                        X = str(grade)
                        LSAX = LSA + "," + X
                        # LSAX___ = LSAX + ".----"
                        LSAX___ = LSAX + "," + "0.0,0.0,0.0,0.0"
                        report_linha = str(user_id_int) + "," + str(class_id_int) + "," + str(
                            assessments_id_int) + "," + assessment_type + "," + str(None) + "," + "TP ?" + "," + LSAX___
                        report_linha_lst = report_linha.split(',')
                        # new_line = dict(zip(columns, report_linha_lst))
                        # df_Summary = df_Summary.append(new_line, ignore_index=True)
                        # nova_linha_df = pd.DataFrame(report_linha_lst, columns=columns)
                        # df_Summary = pd.concat([df_Summary, nova_linha_df], ignore_index=True)
                        # Escrever as linhas encontradas no arquivo summary_file
                        # writer.writerow(report_linha_lst)

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
                        LSA = str(linhas_df_L.iloc[i]['MPL_VALUE']) + "," + str(linhas_df_S.iloc[i]['MLS_VALUE']) + "," + str(linhas_df_A.iloc[i]['ASSERTIV_VALUE'])
                        Y = str(grade)
                        LSAY = LSA + "," + Y
                        LSAX_LSAY = LSAX + "," + LSAY
                        report_linha_1 = report_linha_0 + str(assessments_id_int) + "," + assessment_type + "," + LSAX_LSAY
                        report_linha_lst = report_linha_1.split(',')
                        # Escrever as linhas encontradas no arquivo summary_file
                        writer.writerow(report_linha_lst)

                        report_linhas.append(report_linha_1)
                        contagem.setdefault(LSAX_LSAY, 0)
                        contagem[LSAX_LSAY] += 1
                        estado = ESTADO_3

                    i += 1
                    if i >= EOF:
                        estado = ESTADO_3
        # print(len(report_linhas))
        # for linha in report_linhas:
        #     print(linha)
        # print()

    def add_grade_TP_means_columns(self):
        Summary_Metrics_filepath = '../reports/SUMMARY_METRICS.csv'
        df_Summary_Metrics = pd.read_csv(Summary_Metrics_filepath)

        # Cria df com usuários sem repetição de valores
        df_users_distinct = df_Summary_Metrics['USER_ID'].drop_duplicates()

        grade_TP_mean_lst = []
        for user_id in df_users_distinct:
            user_id_int = int(user_id)
            rows_user = df_Summary_Metrics.query('USER_ID == @user_id_int', inplace=False)
            count: int = 0
            sum_grade_TPs: float = 0.0
            for grade in rows_user['GRADE_TP']:
                sum_grade_TPs += grade
                count += 1
            mean = sum_grade_TPs/count

            # Insere valores repetidas da média, um valor para cada TP k. É preciso isso para ajudar depois
            # no cálculo da correlação de Pearson que exige que as variáveis tenham o mesmo número de valores.
            grade_TP_mean_lst.extend([mean] * count)

        # Adiciona coluna
        df_Summary_Metrics['GRADE_TP_MEAN'] = grade_TP_mean_lst
        df_Summary_Metrics.to_csv(Summary_Metrics_filepath, encoding='utf-8', index=False)

    def process_Pearson_correlations_matplot(self):
        # Carregar o arquivo CSV em um DataFrame do pandas
        Summary_Metrics_filepath = '../reports/SUMMARY_METRICS.csv'
        df = pd.read_csv(Summary_Metrics_filepath)

        # Selecionar as colunas desejadas para calcular a correlação
        # colunas_selecionadas = ['L_LAB', 'S_LAB', 'A_LAB', 'GRADE_LAB', 'L_TP', 'S_TP', 'A_TP', 'GRADE_TP']  # Substitua com os nomes das colunas desejadas
        colunas_selecionadas = ['L_LAB', 'S_LAB', 'A_LAB', 'GRADE_LAB', 'L_TP', 'S_TP', 'A_TP', 'GRADE_TP_MEAN']  # Substitua com os nomes das colunas desejadas
        df_selecionado = df[colunas_selecionadas]

        # Calcular a matriz de correlação de Pearson entre as colunas selecionadas
        matriz_correlacao = df_selecionado.corr()
        # matriz_correlacao = df_selecionado.corr(method='kendall')

        # Plotar um gráfico de dispersão entre cada par de colunas selecionadas
        num_colunas = len(colunas_selecionadas)
        fig, axs = plt.subplots(num_colunas, num_colunas, figsize=(25, 25))

        for i, col1 in enumerate(colunas_selecionadas):
            for j, col2 in enumerate(colunas_selecionadas):
                axs[i, j].scatter(df_selecionado[col1], df_selecionado[col2], s=3)  # 's' define o tamanho dos pontos
                axs[i, j].set_xlabel(col1)
                axs[i, j].set_ylabel(col2)

        plt.tight_layout()
        plt.savefig('correlacoes_LSAX_LSAY.png')
        # plt.show()

        # Plotar o mapa de calor da matriz de correlação usando Matplotlib
        plt.figure(figsize=(10, 8))
        # plt.imshow(matriz_correlacao, cmap='coolwarm', interpolation='nearest')
        plt.imshow(matriz_correlacao, cmap='Blues', interpolation='nearest')
        # , annot = True, cmap = 'Blues', fmt = ".2f"

        # Adicionar os valores das correlações
        for i in range(len(matriz_correlacao.columns)):
            for j in range(len(matriz_correlacao.index)):
                plt.text(j, i, f'{matriz_correlacao.iloc[i, j]:.2f}', ha='center', va='center', color='black')

        plt.colorbar(label='Correlação')
        # plt.colorbar(label='Correlação', ticks=[-1.0, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0])
        plt.title('Mapa de Calor da Matriz de Correlação de Pearson')
        plt.xticks(np.arange(len(matriz_correlacao.columns)), matriz_correlacao.columns, rotation=45)
        plt.yticks(np.arange(len(matriz_correlacao.index)), matriz_correlacao.index)
        plt.tight_layout()
        plt.savefig('mapa_calor_correlacao_Pearson1.png')  # Salvar a figura como um arquivo de imagem
        plt.close()  # Fechar o plot para liberar memória
        # plt.show()

        # Exibir a matriz de correlação de Pearson
        print("Matriz de correlação de Pearson:")
        print(matriz_correlacao)

    def process_Pearson_correlations_matplot1(self):
        # Carregar o arquivo CSV em um DataFrame do pandas
        Summary_Metrics_filepath = '../reports/SUMMARY_METRICS.csv'
        df = pd.read_csv(Summary_Metrics_filepath)

        # Selecionar as colunas desejadas para calcular a correlação
        colunas_selecionadas = ['L_LAB', 'S_LAB', 'A_LAB', 'GRADE_LAB', 'L_TP', 'S_TP', 'A_TP', 'GRADE_TP']
        df_selecionado = df[colunas_selecionadas]

        # Calcular a matriz de correlação de Pearson entre as colunas selecionadas
        matriz_correlacao = df_selecionado.corr()
        # matriz_correlacao = df_selecionado.corr(method='kendall')

        # Convertendo a matriz de correlação em um array de triângulo superior sem diagonal
        num_colunas = len(colunas_selecionadas)
        fig, axs = plt.subplots(num_colunas, num_colunas, figsize=(25, 25))

        # Iterando sobre os subplots e plotando gráficos de dispersão com linha de regressão
        for i, col1 in enumerate(colunas_selecionadas):
            for j, col2 in enumerate(colunas_selecionadas):
                axs[i, j].scatter(df_selecionado[col1], df_selecionado[col2], s=2, color='black', alpha=0.5)
                slope, intercept = np.polyfit(df_selecionado[col1], df_selecionado[col2], 1)
                linha_regressao = slope * df_selecionado[col1] + intercept
                axs[i, j].plot(df_selecionado[col1], linha_regressao, color='red')
                axs[i, j].set_xlabel(col1)
                axs[i, j].set_ylabel(col2)
                # axs.set_title(f'Correlação: {correlacao:.2f}')
                # ax.set_xlabel(col1)
                # ax.set_ylabel(col2)

        # Ajustando layout e exibindo os subplots
        plt.tight_layout()
        plt.savefig('correlacoes_Pearson_LSAX_LSAY1.png')
        # plt.show()

        # Plotar o mapa de calor da matriz de correlação usando Matplotlib
        plt.figure(figsize=(10, 8))
        plt.imshow(matriz_correlacao, cmap='Greys', interpolation='nearest')
        # plt.imshow(matriz_correlacao, cmap='coolwarm', interpolation='nearest')
        # plt.imshow(matriz_correlacao, cmap='Blues', interpolation='nearest')

        # Adicionar os valores das correlações
        for i in range(len(matriz_correlacao.columns)):
            for j in range(len(matriz_correlacao.index)):
                if i != j:
                    plt.text(j, i, f'{matriz_correlacao.iloc[i, j]:.2f}', ha='center', va='center', color='black')
                else:
                    plt.text(i, i, f'{matriz_correlacao.iloc[i, j]:.2f}', ha='center', va='center', color='white')

        plt.colorbar(label='Correlação')
        # plt.colorbar(label='Correlação', ticks=[-1.0, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0])
        plt.title('Mapa de Calor da Matriz de Correlação de Pearson')
        plt.xticks(np.arange(len(matriz_correlacao.columns)), matriz_correlacao.columns, rotation=45)
        plt.yticks(np.arange(len(matriz_correlacao.index)), matriz_correlacao.index)
        plt.tight_layout()
        plt.savefig('mapa_calor_correlacao_Pearson1.png')  # Salvar a figura como um arquivo de imagem
        plt.close()  # Fechar o plot para liberar memória
        # plt.show()

        # Exibir a matriz de correlação de Pearson
        print("Matriz de correlação de Pearson:")
        # Definir para mostrar todas as colunas do DataFrame
        pd.set_option('display.max_columns', None)
        print(matriz_correlacao)

    def process_Pearson_correlations_matplot2(self):
        # Carregar o arquivo CSV em um DataFrame do pandas
        Summary_Metrics_filepath = '../reports/SUMMARY_METRICS.csv'
        df = pd.read_csv(Summary_Metrics_filepath)

        # Selecionar as colunas desejadas para calcular a correlação
        # colunas_selecionadas = ['L_LAB', 'S_LAB', 'A_LAB', 'GRADE_LAB', 'L_TP', 'S_TP', 'A_TP', 'GRADE_TP']
        colunas_selecionadas = ['L_LAB', 'S_LAB', 'A_LAB', 'GRADE_LAB', 'L_TP', 'S_TP', 'A_TP', 'GRADE_TP_MEAN']
        df_selecionado = df[colunas_selecionadas]

        # Calcular a matriz de correlação de Pearson entre as colunas selecionadas
        matriz_correlacao = df_selecionado.corr()
        # matriz_correlacao = df_selecionado.corr(method='kendall')

        # Convertendo a matriz de correlação em um array de triângulo superior sem diagonal
        # indices_superiores = np.triu_indices_from(matriz_correlacao, k=1)
        # valores_correlacao = matriz_correlacao.values[indices_superiores]
        num_colunas = len(colunas_selecionadas)
        fig, axs = plt.subplots(num_colunas, num_colunas, figsize=(25, 25))

        # Iterando sobre os subplots e plotando gráficos de dispersão com linha de regressão
        # for ax, (i, j), correlacao in zip(axs.flat, zip(*indices_superiores), valores_correlacao):
        for i, col1 in enumerate(colunas_selecionadas):
            for j, col2 in enumerate(colunas_selecionadas):
                # col1 = df.columns[i]
                # col2 = df.columns[j]
                # df_selecionado = df_selecionado[[col1, col2]]
                axs[i, j].scatter(df_selecionado[col1], df_selecionado[col2], s=2, color='blue', alpha=0.5)
                slope, intercept = np.polyfit(df_selecionado[col1], df_selecionado[col2], 1)
                linha_regressao = slope * df_selecionado[col1] + intercept
                axs[i, j].plot(df_selecionado[col1], linha_regressao, color='red')
                axs[i, j].set_xlabel(col1)
                axs[i, j].set_ylabel(col2)
                # axs.set_title(f'Correlação: {correlacao:.2f}')
                # ax.set_xlabel(col1)
                # ax.set_ylabel(col2)

        # Ajustando layout e exibindo os subplots
        plt.tight_layout()
        plt.savefig('correlacoes_Pearson_LSAX_LSAY2.png')
        # plt.show()

        # plt.figure(figsize=(10, 8))
        # plt.imshow(matriz_correlacao, cmap='coolwarm', interpolation='nearest')
        # plt.colorbar(label='Correlação')
        # plt.title('Mapa de Calor da Matriz de Correlação de Pearson')
        # plt.xticks(np.arange(len(matriz_correlacao.columns)), matriz_correlacao.columns, rotation=45)
        # plt.yticks(np.arange(len(matriz_correlacao.index)), matriz_correlacao.index)
        # plt.tight_layout()
        # plt.savefig('mapa_de_calor_correlacao_Pearson.png')  # Salvar a figura como um arquivo de imagem
        # plt.close()  # Fechar o plot para liberar memória

        # Plotar o mapa de calor da matriz de correlação usando Matplotlib
        plt.figure(figsize=(10, 8))
        # plt.imshow(matriz_correlacao, cmap='coolwarm', interpolation='nearest')
        plt.imshow(matriz_correlacao, cmap='Blues', interpolation='nearest')

        # Adicionar os valores das correlações
        for i in range(len(matriz_correlacao.columns)):
            for j in range(len(matriz_correlacao.index)):
                if i != j:
                    plt.text(j, i, f'{matriz_correlacao.iloc[i, j]:.2f}', ha='center', va='center', color='black')
                else:
                    plt.text(i, i, f'{matriz_correlacao.iloc[i, j]:.2f}', ha='center', va='center', color='white')

        plt.colorbar(label='Correlação')
        # plt.colorbar(label='Correlação', ticks=[-1.0, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0])
        plt.title('Mapa de Calor da Matriz de Correlação de Pearson')
        plt.xticks(np.arange(len(matriz_correlacao.columns)), matriz_correlacao.columns, rotation=45)
        plt.yticks(np.arange(len(matriz_correlacao.index)), matriz_correlacao.index)
        plt.tight_layout()
        plt.savefig('mapa_calor_correlacao_Pearson2.png')  # Salvar a figura como um arquivo de imagem
        plt.close()  # Fechar o plot para liberar memória
        # plt.show()

        # Exibir a matriz de correlação de Pearson
        print("Matriz de correlação de Pearson:")
        # Definir para mostrar todas as colunas do DataFrame
        pd.set_option('display.max_columns', None)
        print(matriz_correlacao)

    def process_Spearman_correlations_matplot(self):
        # Carregar o arquivo CSV em um DataFrame do pandas
        Summary_Metrics_filepath = '../reports/SUMMARY_METRICS.csv'
        df = pd.read_csv(Summary_Metrics_filepath)

        # Selecionar as colunas desejadas para calcular a correlação
        colunas_selecionadas = ['L_LAB', 'S_LAB', 'A_LAB', 'GRADE_LAB', 'L_TP', 'S_TP', 'A_TP', 'GRADE_TP']  # Substitua com os nomes das colunas desejadas
        df_selecionado = df[colunas_selecionadas]

        # Calcular a matriz de correlação de Spearman entre as colunas selecionadas
        matriz_correlacao = df_selecionado.corr(method='spearman')

        # Plotar um gráfico de dispersão entre cada par de colunas selecionadas
        num_colunas = len(colunas_selecionadas)
        fig, axs = plt.subplots(num_colunas, num_colunas, figsize=(25, 25))

        for i, col1 in enumerate(colunas_selecionadas):
            for j, col2 in enumerate(colunas_selecionadas):
                axs[i, j].scatter(df_selecionado[col1], df_selecionado[col2], s=3)  # 's' define o tamanho dos pontos
                axs[i, j].set_xlabel(col1)
                axs[i, j].set_ylabel(col2)

        plt.tight_layout()
        plt.savefig('correlacoes_LSAX_LSAY.png')
        # plt.show()

        # Exibir a matriz de correlação de Spearman
        print("Matriz de correlação de Spearman:")

        # Definir para mostrar todas as colunas do DataFrame
        pd.set_option('display.max_columns', None)
        print(matriz_correlacao)

    def process_Pearson_parcial_correlation_pingouin(self):

        # Carregar o arquivo CSV em um DataFrame do pandas
        Summary_Metrics_filepath = '../reports/SUMMARY_METRICS.csv'
        df = pd.read_csv(Summary_Metrics_filepath)

        # Calcular a correlação de Pearson parcial
        correlacao_parcial = pg.partial_corr(data=df, x='L_TP', y='S_TP', covar=['A_TP'])
        # correlacao_parcial = pg.partial_corr(data=df, x='L_TP', y='S_TP', covar=['A_TP', 'GRADE_TP'])

        # Mostrar a correlação parcial
        print("Correlação parcial entre L_TP e S_TP controlando A_TP:")
        # print("Correlação parcial entre L_TP e S_TP controlando A_TP e GRADE_TP:")
        print(correlacao_parcial)

        # Plotar gráfico de dispersão entre A e B controlando C e D
        sns.lmplot(x='L_TP', y='S_TP', data=df, hue='A_TP')
        # sns.lmplot(x='L_TP', y='S_TP', data=df, hue='A_TP', col='GRADE_TP', col_wrap=2)
        plt.savefig('correlacao_parcial.png')  # Salvar a figura como um arquivo de imagem
        plt.close()  # Fechar o plot para liberar memória
