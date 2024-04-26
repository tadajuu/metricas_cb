import re
from datetime import datetime
import csv
import json
import os
import pandas as pd
from online_judge.CodebenchLog import CodebenchLog

__author__ = 'Flávio José Mendes Coelho'


# noinspection PyInterpreter
class LUT_ExercisesWithoutStartCode:

    def __init__(self, path: str, file_name: str):
        self._file_name: str = file_name
        self._path: str = path
        self._exercises_with_start_code: list = self._load_exercises_with_initial_code()

    def exercise_have_start_code(self, file_id: str) -> bool:
        # Remove MMMMM do file_id que tem formato MMMMM_NNNNN
        PATTERN_EXERCISE_ID = r'_\d+'
        exercise_id_lst = re.findall(PATTERN_EXERCISE_ID, file_id)

        # pega primeiro elemento da lista (que deveria ser unitária), e "remove" o underscore do elemento
        exercise_id = exercise_id_lst[0][1:]
        return exercise_id in self._exercises_with_start_code

    @staticmethod
    def extract_id(text: str) -> str:
        PATTERN_EXERCISE_ID = r'\d+'
        file_id = re.findall(PATTERN_EXERCISE_ID, text)
        return file_id[0]

    @staticmethod
    def extract_ids(exercises: list):
        exercise_ids: list = []
        for exercise in exercises:
            exercise_id = LUT_ExercisesWithoutStartCode.extract_id(exercise)
            exercise_ids.append(exercise_id)
        return exercise_ids

    def _load_exercises_with_initial_code(self) -> str:
        try:
            fr = open(self._path + self._file_name, 'r',encoding='utf-8')
            text = fr.read()
            fr.close()

            PATTERN_ALL_EXERCISES = ".*\#\%\#\%\#"
            all_exercises: list = re.findall(PATTERN_ALL_EXERCISES, text)
            all_exercise_ids: list = LUT_ExercisesWithoutStartCode.extract_ids(all_exercises)

            # Exercícios que não tem código inicial contém a string "#%#%##$#$#" ou "#%#%#NULL#$#$#".
            PATTERN_EXERCISES_DONT_HAVE_INITIAL_CODE = '.*\#\%\#\%\#\#\$\#\$\#\n|.*\#\%\#\%\#NULL\#\$\#\$\#\n'
            exercises_without_initial_code: list = re.findall(PATTERN_EXERCISES_DONT_HAVE_INITIAL_CODE, text)
            exercises_without_initial_code_ids: list = LUT_ExercisesWithoutStartCode.extract_ids(exercises_without_initial_code)

            exercises_with_initial_code_ids: list = list(set(all_exercise_ids) - set(exercises_without_initial_code_ids))

            # exercises_with_initial_code_ids = []
            # for exercise_id in all_exercise_ids:
            #     if exercise_id not in exercises_without_code_ids:
            #         exercises_with_initial_code_ids.append(exercise_id)
            return exercises_with_initial_code_ids

        except (OSError, FileNotFoundError, PermissionError):
            print(
                f"LUT_ExercisesHaveStartCode.load_text(): Erro ao manipular o arquivo '{self._path + self._file_name}'")


def extract_assessment_id(file_id: str) -> str:
    return file_id.split('_')[0]


def extract_exercise_id(file_id: str) -> str:
    return file_id.split('_')[1]


dummy_datetime = datetime.fromisoformat('2000-01-01 00:00:00.000')


def extract_datetime(line: str) -> datetime:
    date_str = extract_date(line)
    time_str = extract_time(line)
    datetime_str = date_str + " " + time_str
    _datetime = None
    try:
        if time_str[-1] == "#" or time_str[-1] == ")":
            # for debugging: print(datetime_str[:-1])       # debug
            _datetime = datetime.fromisoformat(datetime_str[:-1])
        else:
            # for debugging: print(datetime_str, " <<<<<<<< dummy_datetime") # debug
            _datetime = dummy_datetime
    except ValueError:
        print(f"Exceção em Helper.extract_datetime(): {ValueError}")
    return _datetime


def extract_date(line: str) -> str:
    PATTERN_DATE = r'\d+-\d+-\d+'
    date_lst = re.findall(PATTERN_DATE, line)
    if date_lst:
        date_str = date_lst[0]
        # O teste abaixo serve cobrir casos excepcionais quando date_str já vem
        # com mm e dd contendo zero à esquerda. Exemplo: 2020-01-2, 2021-4-09, 2022-03-05, etc.
        if len(date_str) < len("aaaa-mm-dd"):
            date_str = date_str + " "  # Espaço em branco ajuda em insert_zeros_in_date().
            date_str = insert_zeros_in_date(date_str)
    else:
        date_str = '2000-01-01'
    return date_str


def extract_time(line: str) -> str:
    PATTERN_TIME_KEYSTROKEFILE = r'\d+:\d+:\d+\.\d+#'
    PATTERN_TIME_EXECUTIONFILE = r'\d+:\d+:\d+\)'
    time_lst_1 = re.findall(PATTERN_TIME_KEYSTROKEFILE, line)
    time_lst_2 = re.findall(PATTERN_TIME_EXECUTIONFILE, line)
    if time_lst_1:
        time_str = time_lst_1[0]
    elif time_lst_2:
        time_str = time_lst_2[0][:-1] + '.000)'
    else:
        time_str = '00:00:00.000'
    return time_str


def insert_zeros_in_date(date_str: str) -> str:
    PATTERN_YEAR = r'\d+-'
    year_lst = re.findall(PATTERN_YEAR, date_str)
    year_str = year_lst[0][:-1]

    PATTERN_MONH = r'-\d+-'
    month_lst = re.findall(PATTERN_MONH, date_str)
    month_str = month_lst[0][1:-1]
    if int(month_str) < 10:
        month_str = "0" + month_str

    PATTERN_DAY = r'-\d+ '
    day_lst = re.findall(PATTERN_DAY, date_str)
    day_str = day_lst[0][1:-1]
    if int(day_str) < 10:
        day_str = "0" + day_str

    date_str = year_str + "-" + month_str + "-" + day_str
    return date_str


"""
Obtido de: https://pythonexamples.org/python-csv-to-json/
"""


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


def remove_tempfiles_from_reports(extension: str):
    extension = "." + extension
    reports_path = '../reports/'
    for f in os.listdir(reports_path):
        filename, fileext = os.path.splitext(f)
        if fileext == extension:
            os.remove(os.path.join(reports_path, f))


def convert_numericfields_to_numbers_in_dataframe(df: pd.DataFrame):
    """
    Converte os campos numéricos de um dataframe pandas no formato de string em números.
    Fonte: Douglas
    """
    for column in df.columns:
        df[column] = pd.to_numeric(df[column], errors='ignore')  # errors='ignore' mantém valores não numéricos


def IRBO_scale(metric: str, num_score: float) -> str:
    if metric in ["L", "S", "A", "X", "Y"]:
        if 9.0000 <= num_score <= 10.0000:
            grade = "O"
        elif 8.0000 <= num_score < 9.0000:
            grade = "B"
        elif 5.0000 <= num_score < 8.0000:
            grade = "R"
        elif 0.0000 <= num_score < 5.0000:
            grade = "I"
        else:
            grade = "-"  # valor inválido
    elif metric == "H":
        if 8.0000 <= num_score <= 10.0000:
            grade = "O"
        elif 6.0000 <= num_score < 8.0000:
            grade = "B"
        elif 4.0000 <= num_score < 6.0000:
            grade = "R"
        elif 0.0000 <= num_score < 4.0000:
            grade = "I"
        else:
            grade = "-"  # valor inválido
    elif metric == "P":
        if num_score >= 3.0000:
            grade = "O"
        elif 2.5000 <= num_score < 3.0000:
            grade = "B"
        elif 1.0000 <= num_score < 2.5000:
            grade = "R"
        elif 0.0000 <= num_score < 1.0000:
            grade = "I"
        else:
            grade = "-"  # valor inválido
    else:
        print("Parâmetro IRBO_scale(metric,...) inválido")
        grade = "-"  # valor inválido
    return grade






