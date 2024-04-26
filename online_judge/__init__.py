import re
import json
import os
import online_judge
from online_judge.CodebenchLog import CodebenchLog
from online_judge.Helper import LUT_ExercisesWithoutStartCode

"""
Aqui são instaciados/gerados dicionários e tabelas de consulta (lookup tables) de utilidade geral,
com acesso global.
Também é instanciado CodebenchLog, objeto de navegação pelo dataset do Condebench. 
"""


def load_LUT_tutors_monitors_professors(path: str, filename: str) -> list:
    try:
        fr = open(path + filename, 'r')
        text = fr.read()
        fr.close()
        return text.splitlines()
    except (OSError, FileNotFoundError, PermissionError):
        print(
            f"load_LUT_tutors_monitors_professors(): Erro ao manipular o arquivo '{path + filename}'")


# def load_LUT_tutors_monitors_professors(path: str, filename: str) -> str:
#     try:
#         fr = open(path + filename, 'r')
#         text = fr.read()
#         fr.close()
#         return text.splitlines()
#     except (OSError, FileNotFoundError, PermissionError):
#         print(
#             f"load_LUT_tutors_monitors_professors(): Erro ao manipular o arquivo '{path + filename}'")


def assessments_type_list():
    keys = list(online_judge.LUT_class_id_assessment_type.keys())
    max_len_keys = len(keys)
    for i in range(0, online_judge.LUT_class_id_assessment_type.__len__()):
        keys = list(online_judge.LUT_class_id_assessment_type.keys())
        if max_len_keys < len(keys):
            max_len_keys = len(keys)
    assessments = list(online_judge.LUT_class_id_assessment_type[keys[max_len_keys - 1]].values())
    return assessments


# def load_LUT_assessment_types(path_classes: str):
#     class_ids: list = os.listdir(path_classes)
#     class_ids.sort()
#     LUT_assessmentid_typeid = {}
#     for class_id in class_ids:
#         if class_id == '.DS_Store':
#             continue
#         path_assessment = path_classes + class_id + "/assessments"
#         assessment_filenames: list = os.listdir(path_assessment)
#         assessment_filenames.sort()
#         LUT_assessmentid_typeid[class_id] = {}
#         homework_number = 1  # trabalho prático (lab)
#         exam_number = 1  # prova
#         for assessment_filename in assessment_filenames:
#             if assessment_filename == '.DS_Store':
#                 continue
#             assessment_file = open(path_assessment + '/' + assessment_filename, 'r')
#             assessment_data = assessment_file.readlines()
#             assessment_id = int(assessment_filename.replace(".data", ""))
#             got_assessment_type = False
#             got_date_start = False
#             got_date_end = False
#             assessment_title = None
#             assessment_type = None
#             date_start = None
#             date_end = None
#             for data in assessment_data:
#
#                 if "---- assessment title: " in data:
#                     assessment_title = data.replace("---- assessment title: ", "")
#                     continue
#
#                 if "---- type: homework" in data:
#                     assessment_type = "Lab " + str(homework_number)
#                     got_assessment_type = True
#                     continue
#
#                 if "---- type: exam" in data:
#                     assessment_type = "TP " + str(exam_number)
#                     if assessment_title[:2] == "TP" and not assessment_title[3].isnumeric():   # TP Substitutivo
#                         assessment_type = "TP-Especial"
#                     elif assessment_title[:5].upper() == "PROVA":  # Prova Final
#                         assessment_type = "PF"
#                     got_assessment_type = True
#                     continue
#
#                 if "---- start: " in data:
#                     title = data.replace("---- start: ", "")
#                     PATTERN = '\d+-\d+-\d+ \d+:\d+'
#                     results: list = re.findall(PATTERN, title)
#                     if results:
#                         date_start = results[0]
#                         got_date_start = True
#                         continue
#
#                 if "---- end: " in data:
#                     title = data.replace("---- end: ", "")
#                     PATTERN = '\d+-\d+-\d+ \d+:\d+'
#                     results: list = re.findall(PATTERN, title)
#                     if results:
#                         date_end = results[0]
#                         got_date_end = True
#
#                 if got_assessment_type and got_date_start and got_date_end:
#                     break
#
#             if got_assessment_type and got_date_start and got_date_end:
#                 LUT_assessmentid_typeid[class_id][assessment_id] = (assessment_type, assessment_title, date_start, date_end)
#
#             if got_assessment_type:
#                 if assessment_type[:2] in ["TP", "PF"]:
#                     exam_number += 1
#                     homework_number += 1
#
#     return LUT_assessmentid_typeid


# Funciona agrupando Lab K, e trbalhos pós Lab K sob o nome "Lab K". O Lab 0 ainda está separado do Lab 1.
# def load_LUT_assessment_types(path_classes: str):
#     class_ids: list = os.listdir(path_classes)
#     class_ids.sort()
#     LUT_assessmentid_typeid = {}
#     for class_id in class_ids:
#         if class_id == '.DS_Store':
#             continue
#         path_assessment = path_classes + class_id + "/assessments"
#         assessment_filenames: list = os.listdir(path_assessment)
#         assessment_filenames.sort()
#         LUT_assessmentid_typeid[class_id] = {}
#         lab_number = 1
#         TP_number = 1
#         for assessment_filename in assessment_filenames:
#             if assessment_filename == '.DS_Store':
#                 continue
#             assessment_file = open(path_assessment + '/' + assessment_filename, 'r')
#             assessment_data = assessment_file.readlines()
#             assessment_id = int(assessment_filename.replace(".data", ""))
#             got_assessment_type = False
#             got_date_start = False
#             got_date_end = False
#             assessment_title = None
#             assessment_type = None
#             date_start = None
#             date_end = None
#             for data in assessment_data:
#                 if "---- assessment title: " in data:
#                     title = data.replace("---- assessment title: ", "")
#                     assessment_title = title
#                     PATTERN = 'TP \d+:|TP \d+ '
#                     results: list = re.findall(PATTERN, title)
#                     if results:
#                         assessment_type = "TP " + str(TP_number)
#                         got_assessment_type = True
#                         continue
#                     else:
#                         if title[:2] == "TP" or title[:5] == "Prova":   # TP Substitutivo ou Prova Final
#                             break
#                         else:   # É um Lab ou Extra, Simulado, etc
#                             assessment_type = "Lab " + str(lab_number)
#                             got_assessment_type = True
#                             continue
#
#                 if "---- start: " in data:
#                     title = data.replace("---- start: ", "")
#                     PATTERN = '\d+-\d+-\d+ \d+:\d+'
#                     results: list = re.findall(PATTERN, title)
#                     if results:
#                         date_start = results[0]
#                         got_date_start = True
#                         continue
#
#                 if "---- end: " in data:
#                     title = data.replace("---- end: ", "")
#                     PATTERN = '\d+-\d+-\d+ \d+:\d+'
#                     results: list = re.findall(PATTERN, title)
#                     if results:
#                         date_end = results[0]
#                         got_date_end = True
#
#                 if got_assessment_type and got_date_start and got_date_end:
#                     break
#
#             if got_assessment_type and got_date_start and got_date_end:
#                 LUT_assessmentid_typeid[class_id][assessment_id] = (assessment_type, assessment_title, date_start, date_end)
#             if got_assessment_type:
#                 # if assessment_type[:5] == "Lab 0":
#                 #     lab_number += 1
#                 if assessment_type[:2] == "TP":
#                     TP_number += 1
#                     lab_number += 1
#     return LUT_assessmentid_typeid


# *******************************************************************************************************
# Essa versão volta a desunificar as variações de trabalhos (variações: extras, desafios, etc) e considera
# somente os Labs padrão, ou seja, Lab 1, Lab 2, etc (salta o Lab 0).
# O TP, se for uma variação (ex.: TP substitutivo) passa a se chamar "TP_Especial".
# *******************************************************************************************************
def load_LUT_assessment_types(path_classes: str):
    class_ids: list = os.listdir(path_classes)
    class_ids.sort()
    LUT_assessmentid_typeid = {}
    for class_id in class_ids:
        if class_id == '.DS_Store':
            continue
        path_assessment = path_classes + class_id + "/assessments"
        assessment_filenames: list = os.listdir(path_assessment)
        assessment_filenames.sort()
        LUT_assessmentid_typeid[class_id] = {}
        homework_number = 1
        exam_number = 1
        for assessment_filename in assessment_filenames:
            if assessment_filename == '.DS_Store':
                continue
            assessment_file = open(path_assessment + '/' + assessment_filename, 'r')
            assessment_data = assessment_file.readlines()
            assessments_id = int(assessment_filename.replace(".data", ""))
            got_assessment_type = False
            got_date_start = False
            got_date_end = False
            # got_weight = False
            jump_assessment = False
            assessment_title = None
            assessment_type = None
            date_start = None
            date_end = None
            for data in assessment_data:
                # Desconsidera Extras, Desafios, Simulados, TP Substitutivo, etc.
                if "---- weight: 0" in data:
                    jump_assessment = True
                    break

                elif "---- assessment title: " in data:
                    assessment_title = data.replace("---- assessment title: ", "")
                    assessment_title = assessment_title.strip()
                    L = ["Lab 0", "extra", "desafio", "simulado", "ajud", "chamada", "chance", "substitutiv", "test", "prova"]
                    # Encontrar as strings de L na string assessment_title (independente de caixa)
                    PATTERN = '|'.join(map(re.escape, L))
                    results = re.findall(PATTERN, assessment_title, flags=re.IGNORECASE)                    # if assessment_title[:5] == "Lab 0":
                    # if assessments_id == 4629:
                    #     print("assessments_id = ", assessments_id)
                    #     print("assessment_title = ", assessment_title)
                    #     print("results", results)
                    if results:
                        # if assessments_id == 4629:
                        #     print("jump=True + break")
                        jump_assessment = True
                        break
                    else:
                        # if assessments_id == 4629:
                        #     print("continue")
                        continue

                elif "---- type: homework" in data:
                    assessment_type = "Lab " + str(homework_number)
                    got_assessment_type = True
                    continue

                elif "---- type: exam" in data:
                    if (assessment_title[:2] == "TP" and not assessment_title[3].isnumeric()) or assessment_title[:5].upper() == "PROVA":  # TP Substitutivo ou Prova Final
                        jump_assessment = True
                        break
                    else:
                        assessment_type = "TP " + str(exam_number)
                        got_assessment_type = True
                        continue

                elif "---- start: " in data:
                    title = data.replace("---- start: ", "")
                    PATTERN = '\d+-\d+-\d+ \d+:\d+'
                    results: list = re.findall(PATTERN, title)
                    if results:
                        date_start = results[0]
                        got_date_start = True
                        continue
                    # else:
                    #     print(">", end="")

                elif "---- end: " in data:
                    title = data.replace("---- end: ", "")
                    PATTERN = '\d+-\d+-\d+ \d+:\d+'
                    results: list = re.findall(PATTERN, title)
                    if results:
                        date_end = results[0]
                        got_date_end = True
                    # else:
                    #     print("<", end="")

                if jump_assessment or (got_assessment_type and got_date_start and got_date_end):
                    break

            if jump_assessment:
                # Despreza assessment atual (porque é desafio, extras, etc) e busca o próximo
                # print("jump ", end="")
                continue
            else:
                if got_assessment_type and got_date_start and got_date_end:
                    LUT_assessmentid_typeid[class_id][assessments_id] = (class_id, assessments_id, assessment_type, assessment_title, date_start, date_end)
                    # if assessments_id == 4629:
                    #     print("Lab registrado!")
                    # print("=>", class_id, assessments_id, assessment_type, assessment_title, date_start, date_end)

                if got_assessment_type:
                    if assessment_type[:3] == "Lab":
                        homework_number += 1
                    if assessment_type[:2] == "TP":
                        exam_number += 1

                    # if assessment_type[:5] == "Lab 0":
                    #     homework_number += 1
                    # elif assessment_type[:2] == "TP":
                    #     exam_number += 1
                    #     homework_number += 1

                    # Old code
                    # if assessment_type[:5] == "Lab 0":
                    #     homework_number += 1
                    # if assessment_type[:2] == "TP":
                    #     exam_number += 1
                    #     homework_number += 1
                    # if assessment_type[:2] in ["TP", "PF"]:
                    #     exam_number += 1
                    #     homework_number += 1
    return LUT_assessmentid_typeid

# *******************************************************************************************************
# Essa versão funciona unificando as variações de trabalhos em Lab k (variações: extras, desafios, etc).
# O TP, se for também uma variação (ex.: TP substitutivo) passa a se chamar "TP_Especial".
# *******************************************************************************************************
# def load_LUT_assessment_types(path_classes: str):
#     class_ids: list = os.listdir(path_classes)
#     class_ids.sort()
#     LUT_assessmentid_typeid = {}
#     for class_id in class_ids:
#         if class_id == '.DS_Store':
#             continue
#         path_assessment = path_classes + class_id + "/assessments"
#         assessment_filenames: list = os.listdir(path_assessment)
#         assessment_filenames.sort()
#         LUT_assessmentid_typeid[class_id] = {}
#         homework_number = 1
#         exam_number = 1
#         for assessment_filename in assessment_filenames:
#             if assessment_filename == '.DS_Store':
#                 continue
#             assessment_file = open(path_assessment + '/' + assessment_filename, 'r')
#             assessment_data = assessment_file.readlines()
#             assessments_id = int(assessment_filename.replace(".data", ""))
#             got_assessment_type = False
#             got_date_start = False
#             got_date_end = False
#             assessment_title = None
#             assessment_type = None
#             date_start = None
#             date_end = None
#             for data in assessment_data:
#                 # if "---- assessment title: " in data:
#                 #     title = data.replace("---- assessment title: ", "")
#                 #     assessment_title = title
#                 #     PATTERN = 'TP \d+:|TP \d+ '
#                 #     results: list = re.findall(PATTERN, title)
#                 #     if results:
#                 #         assessment_type = "TP " + str(TP_number)
#                 #         got_assessment_type = True
#                 #         # continue
#                 #     else:
#                 #         if title[:2] == "TP" or title[:5] == "Prova":   # TP Substitutivo ou Prova Final
#                 #             break
#                 #         else:   # É um Lab ou Extra, Simulado, etc
#                 #             assessment_type = "Lab " + str(lab_number)
#                 #             got_assessment_type = True
#                 #             continue
#
#                 if "---- assessment title: " in data:
#                     assessment_title = data.replace("---- assessment title: ", "")
#                     assessment_title = assessment_title.strip()
#                     continue
#
#                 if "---- type: homework" in data:
#                     assessment_type = "Lab " + str(homework_number)
#                     got_assessment_type = True
#                     continue
#
#                 if "---- type: exam" in data:
#                     assessment_type = "TP " + str(exam_number)
#                     if (assessment_title[:2] == "TP" and not assessment_title[3].isnumeric()) or \
#                             assessment_title[:5].upper() == "PROVA":  # TP Substitutivo ou Prova Final
#                         assessment_type = "TP-Especial"
#                     got_assessment_type = True
#                     continue
#
#                 if "---- start: " in data:
#                     title = data.replace("---- start: ", "")
#                     PATTERN = '\d+-\d+-\d+ \d+:\d+'
#                     results: list = re.findall(PATTERN, title)
#                     if results:
#                         date_start = results[0]
#                         got_date_start = True
#                         continue
#
#                 if "---- end: " in data:
#                     title = data.replace("---- end: ", "")
#                     PATTERN = '\d+-\d+-\d+ \d+:\d+'
#                     results: list = re.findall(PATTERN, title)
#                     if results:
#                         date_end = results[0]
#                         got_date_end = True
#
#                 if got_assessment_type and got_date_start and got_date_end:
#                     break
#
#             if got_assessment_type and got_date_start and got_date_end:
#                 LUT_assessmentid_typeid[class_id][assessments_id] = (assessment_type, assessment_title, date_start, date_end)
#
#             if got_assessment_type:
#                 # if assessment_type[:5] == "Lab 0":
#                 #     lab_number += 1
#                 # if assessment_type[:2] == "TP":
#                 #     TP_number += 1
#                 #     lab_number += 1
#                 if assessment_type[:2] in ["TP", "PF"]:
#                     exam_number += 1
#                     homework_number += 1
#     return LUT_assessmentid_typeid


# Estou trabalhando nesse código aqui <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def load_all_assessments() -> dict:
#     df = pd.DataFrame({
#         'ASSESSMENT_ID': [],
#         'TYPE': [],
#         'SUBTYPE': [],
#         'ASSESSMENT_TITLE': [],
#         'CLASS_NAME': [],
#         'CLASS_NUMBER': [],
#         'START': [],
#         'END': [],
#         'LANGUAGE': [],
#         'CODEMIRROR_MODE': [],
#         'WEIGHT': [],
#         'TOTAL_EXERCISES': [],
#     })
#     semesters = cb_log.semesters.values()
#     for semester in semesters:
#         classes = semester.classes.values()
#         for cls in classes:
#             load_assessments_per_class(df, cls.class_path_assessments)
#     return df
#
#
# def load_assessments_per_class(df: pd.DataFrame, class_path_assessments: str) -> list:
#     # Pega as turmas
#     assessments_filenames: list = os.listdir(class_path_assessments)
#     assessments_filenames.sort()
#     for filename in assessments_filenames:
#         if filename == '.DS_Store':
#             continue
#         file = open(class_path_assessments + '/' + filename, 'r')
#         assessment_data = file.readlines()
#         assessment_id = filename.replace(".data", "")
#
#         for data in assessment_data:
#
#             if "---- assessment title: " in data:
#                 assessment_title = data.replace("---- assessment title: ", "")
#                 assessment_title = assessment_title.strip()
#
#             if "---- class name: " in data:
#                 class_name = data.replace("---- class name: ", "")
#                 class_name = class_name.strip()
#
#             if "---- class number: " in data:
#                 class_number = data.replace("---- class number: ", "")
#                 class_number = class_number.strip()
#
#             if "---- start: " in data:
#                 start = data.replace("---- start: ", "")
#                 start = start[:-1]
#                 start = start.strip()
#                 # start = start + ":00.000"
#                 start = datetime.fromisoformat(start)
#
#             if "---- end: " in data:
#                 end = data.replace("---- end: ", "")
#                 end = end[:-1]
#                 end = end.strip()
#                 # end = end + ":00.000"
#                 end = datetime.fromisoformat(end)
#
#             if "---- language: " in data:
#                 language = data.replace("---- language: ", "")
#                 language = language.strip()
#
#             if "---- codemirror mode: " in data:
#                 codemirror_mode = data.replace("---- codemirror mode: ", "")
#                 codemirror_mode = codemirror_mode.strip()
#
#             if "---- type: " in data:
#                 assessment_type = data.replace("---- type: ", "")
#                 assessment_type = assessment_type.strip()
#
#             if "---- weight: " in data:
#                 weight_str = data.replace("---- weight: ", "")
#                 weight = int(weight_str)
#
#             if "---- total_exercises: " in data:
#                 total_exercises_str = data.replace("---- total_exercises: ", "")
#                 total_exercises = int(total_exercises_str)
#
#             if "---- exercise " in data:
#                 break
#             # if "---- exercise " in data:
#             #     assessments[assessment_id]['exercises'].append(data.strip())
#
#         subtype = ''
#         new_row = [assessment_id, assessment_type, subtype, assessment_title, class_name, class_number, start, end, language,
#                    codemirror_mode, weight, total_exercises, ]
#         df.loc[len(df)] = new_row

# Main
print("Limpa relatórios antigos...")
# reports_path = '../reports/*.csv'
# for f in os.listdir(reports_path):
#     os.remove(os.path.join(reports_path, f))
# reports_path = '../reports/*.json'
# for f in os.listdir(reports_path):
#     os.remove(os.path.join(reports_path, f))
online_judge.Helper.remove_tempfiles_from_reports("csv")
online_judge.Helper.remove_tempfiles_from_reports("json")


print("Carregando LUTs...")
path = "../online_judge/"

filename1 = "LUT_ExercisesWithInitialCode.csv"
LUT_EWSC = LUT_ExercisesWithoutStartCode(path, filename1)

filename2 = "LUT_TutorsMonitorsProfessors.csv"
LUT_tutors_monitors_professors = load_LUT_tutors_monitors_professors(path, filename2)

print("Carregando CodeBenchLog...")
cb_log = CodebenchLog()

print("Carregando LUT_assessment_types...")
#classes_path = "/Users/fcoelho/dataset-cb/2022-2/"
classes_path = "/SUPER/dataset-cb/2022-2/"
LUT_assessments = load_LUT_assessment_types(classes_path)



# print("Gerando RELATION_ID_TYPE.json...")
# print("Null")
# json_formatado = json.dumps(online_judge.LUT_assessments, ensure_ascii=False, indent=4)
# path = "/Users/fcoelho/Documents/Dev/doutorado/cb-metrics/reports/"
# with open(path + 'RELATION_ID_TYPE.json', 'w', encoding='utf-8') as arquivo:
#     arquivo.write(json_formatado)


# print(LUT_assessments)
# df = LUT_assessments
# df = df.sort_values(['CLASS_NUMBER', 'ASSESSMENT_ID'], ascending=[True, True])
# # df = df.sort_values(['CLASS_NUMBER', 'START'], ascending=[True, True])
# # print(df.to_string())
# csv_file_path = '../reports/LUT_ASSESSMENTS.csv'
# df.to_csv(csv_file_path,
#           encoding='utf-8', index=False)

# i: int = 0
# for row in LUT_assessments.iterrows():
#     print(row)
#     if i == 200:
#         break
#     i += 1

# LUT_assessments = sorted(LUT_assessments.items(), key=lambda x: x[1]["end"])

# class_path_assessments = "/Users/fcoelho/dataset-cb/2022-2/"
# LUT_assessmentid_typeid = load_LUT_assessment_types(class_path_assessments)


# def load_assessments_per_class(class_path_assessments: str) -> dict:
# def load_assessments(class_path_assessments: str) -> dict:
#     # Pega as turmas
#     assessments_filenames: list = os.listdir(class_path_assessments)
#     assessments_filenames.sort()
#     assessments = {}
#     for filename in assessments_filenames:
#
#         if filename == '.DS_Store':
#             continue
#
#         file = open(class_path_assessments + '/' + filename, 'r')
#         assessment_data = file.readlines()
#         assessment_id = filename.replace(".data", "")
#
#         assessments[assessment_id] = {
#             'assessment_title': '',
#             'class_name': '',
#             'class_number': '',
#             'start': '',
#             'end': '',
#             'language': '',
#             'codemirror_mode': '',
#             'type': '',
#             'subtype': '',
#             'weight': '',
#             'total_exercises': '',
#             'exercises': [],
#         }
#         for data in assessment_data:
#
#             if "---- assessment title: " in data:
#                 assessment_title = data.replace("---- assessment title: ", "")
#                 assessments[assessment_id]['assessment_title'] = assessment_title
#
#             if "---- class name: " in data:
#                 class_name = data.replace("---- class name: ", "")
#                 class_name = class_name.strip()
#                 assessments[assessment_id]['class_name'] = class_name
#
#             if "---- class number: " in data:
#                 class_number = data.replace("---- class number: ", "")
#                 class_number = class_number.strip()
#                 assessments[assessment_id]['class_number'] = int(class_number)
#
#             if "---- start: " in data:
#                 start = data.replace("---- start: ", "")
#                 start = start[:-1]
#                 start = start.strip()
#                 # start = start + ":00.000"
#                 # start = datetime.fromisoformat(start)
#                 assessments[assessment_id]['start'] = start
#
#             if "---- end: " in data:
#                 end = data.replace("---- end: ", "")
#                 end = end[:-1]
#                 end = end.strip()
#                 # end = end + ":00.000"
#                 # end = datetime.fromisoformat(end)
#                 assessments[assessment_id]['end'] = end
#
#             if "---- language: " in data:
#                 language = data.replace("---- language: ", "")
#                 language = language.strip()
#                 assessments[assessment_id]['language'] = language
#
#             if "---- codemirror mode: " in data:
#                 codemirror_mode = data.replace("---- codemirror mode: ", "")
#                 codemirror_mode = codemirror_mode.strip()
#                 assessments[assessment_id]['codemirror_mode'] = codemirror_mode
#
#             if "---- type: " in data:
#                 type = data.replace("---- type: ", "")
#                 type = type.strip()
#                 assessments[assessment_id]['type'] = type
#
#             assessments[assessment_id]['subtype'] = ''
#
#             if "---- weight: " in data:
#                 weight_str = data.replace("---- weight: ", "")
#                 weight = int(weight_str)
#                 assessments[assessment_id]['weight'] = weight
#
#             if "---- total_exercises: " in data:
#                 total_exercises_str = data.replace("---- total_exercises: ", "")
#                 total_exercises = int(total_exercises_str)
#                 assessments[assessment_id]['total_exercises'] = int(total_exercises)
#
#             # if "---- exercise " in data:
#             #     assessments[assessment_id]['exercises'].append(data.strip())
#     return assessments
