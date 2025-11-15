import online_judge
from metrics.ActiveCodingTime import ActiveCodingTime
from online_judge.CodebenchLog import CodebenchLog
from datetime import datetime
import pandas as pd
import numpy as np
import online_judge.Helper as Helper

__author__ = 'Flávio José Mendes Coelho'


class WeeklyCodingHoursProcessor:

    # def __init__(self, cb_log: CodebenchLog, dt_start: datetime, dt_end: datetime):
    def __init__(self):
        self.cb_log = online_judge.cb_log
        # self.dt_start = dt_start
        # self.dt_end = dt_end
        self.inconsistents: int = 0
        self.count_exercise_have_start_code = {}
        self.max_sum_active_coding_time = 0.0
        self.DECIMAL_PLACES = 3

    def process(self):
        df = self._process_report_ACT_by_student_exercise()
        self._process_report_WCH_by_student_assessments(df)

    def _process_report_ACT_by_student_exercise(self):

        self.inconsistents: int = 0
        i: int = 1  # conta registros

        # Listas para os dados do DataFrame
        id_list = []
        semester_id_list = []
        class_id_list = []
        user_id_list = []
        consistency_list = []
        assessment_type_list = []
        assessment_title_list = []
        assessments_id_list = []
        start_date_list = []
        end_date_list = []
        exercise_id_list = []
        active_coding_time_list = []

        semesters = self.cb_log.semesters.values()
        for semester in semesters:
            classes = semester.classes.values()
            for cls in classes:
                users = cls.users.values()
                for user in users:
                    if user.user_id in online_judge.LUT_tutors_monitors_professors:
                        # print("Pula tutores!")
                        continue
                    for codefile in user.codefiles.values():

                        exercise_id = int(online_judge.Helper.extract_exercise_id(codefile.id))
                        assessment_id = int(online_judge.Helper.extract_assessment_id(codefile.id))

                        # Salta o Simulado 2: retirar quando for processar o período 2023/2
                        if assessment_id == 4527:
                            continue

                        if codefile.exercise_have_start_code:
                            tmp_value = self.count_exercise_have_start_code.setdefault(exercise_id)
                            if tmp_value:
                                self.count_exercise_have_start_code[exercise_id] += 1
                            else:
                                self.count_exercise_have_start_code[exercise_id] = 1
                            continue
                        else:
                            # # Se o trabalho/prova não estiver classificado, salta ele.
                            # try:
                            #     assessment_type, assessment_title, start_date, end_date = online_judge.LUT_assessments[cls.class_id][assessment_id]
                            # except Exception:
                            try:
                                _, _, assessment_type, assessment_title, start_date, end_date = online_judge.LUT_assessments[cls.class_id][assessment_id]
                            except Exception:
                                #print("WCHProcessor::_process_report_ACT_by_student_exercise: Pulou assessment_id: ", assessment_id)
                                continue

                            keystrokesfile = user.keystrokesfiles[codefile.id]
                            act = ActiveCodingTime()
                            act.calculate(keystrokesfile)

                            if not act.has_files_consistents:
                                self.inconsistents += 1

                            id_list.append(i)
                            semester_id_list.append(semester.semester_id)
                            class_id_list.append(cls.class_id)
                            user_id_list.append(user.user_id)
                            consistency_list.append(bool(act.has_files_consistents))
                            assessment_type_list.append(assessment_type)
                            assessment_title_list.append(assessment_title)
                            assessments_id_list.append(assessment_id)
                            start_date_list.append(start_date)  # Data do início do assessment
                            end_date_list.append(end_date)
                            exercise_id_list.append(exercise_id)
                            active_coding_time_list.append(act.value)
                            i += 1

        active_coding_time_list = np.round(active_coding_time_list, self.DECIMAL_PLACES)
        df = pd.DataFrame({'ID': id_list,
                           'SEMESTER_ID': semester_id_list,
                           'CLASS_ID': class_id_list,
                           'USER_ID': user_id_list,
                           'CONSISTENCY': consistency_list,
                           'ASSESSMENT_TYPE': assessment_type_list,
                           'ASSESSMENT_TITLE': assessment_title_list,
                           'ASSESSMENTS_ID': assessments_id_list,
                           'DATE_START': start_date_list,
                           'DATE_END': end_date_list,
                           'EXERCISE_ID': exercise_id_list,
                           'ACTIVE_CODING_TIME': active_coding_time_list,
                           })

        Helper.convert_numericfields_to_numbers_in_dataframe(df)

        csv_file_path = '../reports/ACT_EXERCISES.csv'
        df.to_csv(csv_file_path, encoding='utf-8', index=False)

        json_file_path = '../reports/ACT_EXERCISES.json'
        df.to_json(json_file_path, orient="records", indent=4)
        return df

    def _extract_dates_from_strdate_pairs(self, set_strdate_pairs: set):
        strdate_pairs = list(set_strdate_pairs)
        dates = []
        for strdate_pair in strdate_pairs:
            str_startdate = strdate_pair[:16]
            str_startdate += ":00.000"
            startdate = datetime.fromisoformat(str_startdate)
            dates.append(startdate)

            str_enddate = strdate_pair[17:]
            str_enddate += ":00.000"
            enddate = datetime.fromisoformat(str_enddate)
            dates.append(enddate)

        return dates

    def _get_startdate(self, set_strdate_pairs: set) -> datetime:
        dates = self._extract_dates_from_strdate_pairs(set_strdate_pairs)
        oldest_datetime = min(dates)
        return oldest_datetime

    def _get_enddate(self, set_strdate_pairs: set) -> datetime:
        dates = self._extract_dates_from_strdate_pairs(set_strdate_pairs)
        newest_datetime = max(dates)
        return newest_datetime

    def _get_total_days_assessments(self, set_strdate_pairs: set, df: pd.DataFrame, j: int) -> float:
        strdate_pairs = list(set_strdate_pairs)
        SECONDS_PER_DAY = 24 * 60 * 60  # 86.400 segundos
        sum_days_in_decimal = 0.0
        for strdate_pair in strdate_pairs:
            # Quebra em data inicial e final
            str_startdate = strdate_pair[:16]
            str_startdate += ":00.000"
            startdate = datetime.fromisoformat(str_startdate)

            str_enddate = strdate_pair[17:]
            str_enddate += ":00.000"
            enddate = datetime.fromisoformat(str_enddate)

            # Diferença entre datas em dias em formato decimal.
            days_in_decimal = (enddate - startdate).total_seconds() / SECONDS_PER_DAY
            ## DEBUG
            # if df['USER_ID'].iloc[j] == 1242:
            #     print(f"days_in_decimal = {days_in_decimal}")
            sum_days_in_decimal += days_in_decimal
        return sum_days_in_decimal

    def converts_decimal_hours_to_hhmm_format(self, tempo_decimal: float):
        # Extrai as horas (parte inteira) e os minutos (parte decimal * 60)
        horas = int(tempo_decimal)
        minutos = int((tempo_decimal - horas) * 60)
        # Formata para HH:MM
        formato_HH_MM = '{:02d}:{:02d}'.format(horas, minutos)
        return formato_HH_MM

    def _process_report_WCH_by_student_assessments(self, df_in: pd.DataFrame):
        # df_in fieldnames:
        # ID, SEMESTER_ID, CLASS_ID, USER_ID, CONSISTENCY, ASSESSMENT_TYPE, ASSESSMENT_TITLE, ASSESSMENTS_ID,
        # DATE_START, DATE_END, EXERCISE_ID, ACTIVE_CODING_TIME

        # Listas-atributos para o DataFrame
        id_list = []
        startdate_list = []
        enddate_list = []
        semester_id_list = []
        class_id_list = []
        assessment_type_list = []
        assessments_id_list = []
        user_id_list = []
        wch_assessment_list = []
        wch_hhmm_assessment_list = []
        wch_IRBO_grade_list = []

        semester_id_pred = None
        class_id_pred = None
        user_id_pred = None
        assessment_id_pred = None

        DAYS_PER_WEEK = 7.0
        line: int = 1
        EOF = False
        i: int = 0
        while i < len(df_in):

            # while i < len(df_in) and not bool(df_in['CONSISTENCY'].iloc[i]):
            # while not bool(df_in['CONSISTENCY'].iloc[i]):
            #     print(f"while CONSISTENCY: {i}")
            #     i += 1
            #     if i >= len(df_in):
            #         EOF = True
            #         break

            # PARA TESTES
            # while i < len(df_in) and int(df_in['CLASS_ID'].iloc[i]) != 494 and int(df_in['USER_ID'].iloc[i]) != 4190:
            # while int(df_in['CLASS_ID'].iloc[i]) != 494 and int(df_in['USER_ID'].iloc[i]) != 4190:
            #     print(f"while CLASS_ID: {i}")
            #     i += 1
            #     if i >= len(df_in):
            #         EOF = True
            #         break

            while not bool(df_in['CONSISTENCY'].iloc[i]) or str(
                    df_in['ASSESSMENT_TYPE'].iloc[i][:2]).upper() == "TP":
                i += 1
                if i >= len(df_in):
                    EOF = True
                    break

            if EOF:
                continue

            if not bool(df_in['CONSISTENCY'].iloc[i]):
                continue

            assessment_type_pred = str(df_in['ASSESSMENT_TYPE'].iloc[i])
            assessment_user_id_pred = df_in['USER_ID'].iloc[i]

            sum_active_coding_time = 0.0
            set_assessments_ids = set()
            set_strdate_pairs = set()
            j = i
            while i < len(df_in) and str(df_in['ASSESSMENT_TYPE'].iloc[i]).upper() == assessment_type_pred.upper() and df_in['USER_ID'].iloc[i] == assessment_user_id_pred:
                if bool(df_in['CONSISTENCY'].iloc[i]):
                    sum_active_coding_time += float(df_in['ACTIVE_CODING_TIME'].iloc[i])
                    strdates_pair = df_in['DATE_START'].iloc[i] + "|" + df_in['DATE_END'].iloc[i]
                    set_strdate_pairs.add(strdates_pair)
                    set_assessments_ids.add(int(df_in['ASSESSMENTS_ID'].iloc[i]))
                i += 1

            # if not bool(df_in['CONSISTENCY'].iloc[i]):
            #     continue

            assessment_user_id_pred = assessment_user_id_pred

            id_list.append(line)
            semester_id_list.append(df_in['SEMESTER_ID'].iloc[j])
            class_id_list.append(df_in['CLASS_ID'].iloc[j])
            user_id_list.append(df_in['USER_ID'].iloc[j])
            assessment_type_list.append(df_in['ASSESSMENT_TYPE'].iloc[j])
            sorted_set_assessments_ids_lst = sorted(set_assessments_ids)
            sorted_set_assessments_ids = sorted_set_assessments_ids_lst[0]
            # sorted_set_assessments_ids = [-1] # O Douglas pediu para não receber a lista de assessments. Acho que passou a gerar no código que ele me passou.
            assessments_id_list.append(sorted_set_assessments_ids)
            startdate = self._get_startdate(set_strdate_pairs)
            startdate_list.append(startdate.strftime('%Y-%m-%d %H:%M'))
            enddate = self._get_enddate(set_strdate_pairs)
            enddate_list.append(enddate.strftime('%Y-%m-%d %H:%M'))

            total_days_assessment = self._get_total_days_assessments(set_strdate_pairs, df_in, j)
            sum_active_coding_time_hours = sum_active_coding_time / 3600  # converte para horas
            if(total_days_assessment == 0):
                wch_assessment = 0
            else:
                wch_assessment = sum_active_coding_time_hours / total_days_assessment * DAYS_PER_WEEK
            # wch_assessment_list.append(round(wch_assessment, self.DECIMAL_PLACES))
            wch_hhmm_assessment_list.append(self.converts_decimal_hours_to_hhmm_format(wch_assessment))

            # num_score é o próprio valor da métrica. Esse valor corresponde a um conceito I, R, B ou O. Esse conceitos são
            # chamados de grade.
            num_score = round(wch_assessment, self.DECIMAL_PLACES)
            wch_assessment_list.append(num_score * 10)

            # Obtém um conceito IRBO a partir do valor da assertividade, isto é, num_score.
            wch_IRBO_grade_list.append(
                Helper.IRBO_scale("H", num_score * 10))  # *10 para num_score ficar entre 0.0 e 10.0

            line += 1

        df = pd.DataFrame({'ID': id_list,
                           'SEMESTER_ID': semester_id_list,
                           'CLASS_ID': class_id_list,
                           'USER_ID': user_id_list,
                           'ASSESSMENT_TYPE': assessment_type_list,
                           'ASSESSMENTS_ID': assessments_id_list,
                           'DATE_START': startdate_list,
                           'DATE_END': enddate_list,
                           'WEEKLY_CODING_HOURS_DEC': wch_assessment_list,
                           'WCH': wch_assessment_list,
                           'WCH_IRBO_GRADE': wch_IRBO_grade_list,
                           })

        Helper.convert_numericfields_to_numbers_in_dataframe(df)

        csv_file_path = '../reports/WCH_ASSESSMENTS.csv'
        df.to_csv(csv_file_path,
                  encoding='utf-8', index=False)
        json_file_path = '../reports/WCH_ASSESSMENTS.json'
        df.to_json(json_file_path, orient="records", indent=4)

        return df
