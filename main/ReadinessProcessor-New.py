import online_judge
from online_judge.CodebenchLog import CodebenchLog
import online_judge.Helper as Helper
from datetime import datetime
import os
import pandas as pd

__author__ = 'Flávio José Mendes Coelho'


import online_judge
from metrics.Assertiveness import Assertiveness
from online_judge.CodebenchLog import CodebenchLog
from datetime import datetime
import online_judge.Helper as Helper
import pandas as pd

__author__ = 'Flávio José Mendes Coelho'


class AssertivenessProcessor:

    def __init__(self):
        self.cb_log = online_judge.cb_log
        # self.dt_start = dt_start
        # self.dt_end = dt_end
        self.inconsistents: int = 0
        self.count_exercise_have_start_code = {}
        self.DECIMAL_PLACES = 3

    def process(self):
        df_assertiveness_by_student_exercise = self._process_report_assertiveness_by_student_exercise()
        self._process_report_assertiveness_by_student_assessments(df_assertiveness_by_student_exercise)

    def _process_report_assertiveness_by_student_exercise(self):

        i: int = 1  # conta registros
        self.inconsistents: int = 0

        # Listas para os dados do DataFrame
        id_list = []
        start_date_list = []
        semester_id_list = []
        class_id_list = []
        user_id_list = []
        consistency_list = []
        assessment_type_list = []
        assessments_id_list = []
        exercise_id_list = []
        strength_list = []
        assertiv_certifier_list = []
        assertiv_value_list = []
        cnt_chars_list = []
        cnt_keystrokes_list = []

        semesters = self.cb_log.semesters.values()
        for semester in semesters:
            classes = semester.classes.values()
            for cls in classes:
                users = cls.users.values()
                for user in users:

                    # if user.user_id in online_judge.LUT_tutors_monitors_professors:
                    #     # print("Pula tutores!")
                    #     continue
                    # for codefile in user.codefiles.values():
                    #     if codefile.exercise_have_start_code:
                    #         tmp_value = self.count_exercise_have_start_code.setdefault(
                    #             online_judge.Helper.extract_exercise_id(codefile.id))
                    #         if tmp_value:
                    #             self.count_exercise_have_start_code[
                    #                 online_judge.Helper.extract_exercise_id(codefile.id)] += 1
                    #         else:
                    #             self.count_exercise_have_start_code[
                    #                 online_judge.Helper.extract_exercise_id(codefile.id)] = 1
                    #     else:
                    #         # Salta os trabalhos extras e as provas finais
                    #         try:
                    #             assessment_id = online_judge.Helper.extract_assessment_id(codefile.id)
                    #             assessment_type = online_judge.LUT_class_id_assessment_type[cls.class_id][assessment_id]
                    #         except Exception:
                    #             continue
                    #         # Salta se o exercício = 0 (não existir ainda)
                    #         if online_judge.LUT_class_assessment_type_id[cls.class_id][assessment_type] == '0':
                    #             continue

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
                            # Se o trabalho/prova não estiver classificado, salta ele.
                            try:
                                assessment_type, assessment_title, start_date, end_date = \
                                    online_judge.LUT_assessments[cls.class_id][assessment_id]
                            except Exception:
                                print("Pulou!", assessment_id)
                                continue

                            keystrokesfile = user.keystrokesfiles[codefile.id]
                            executionsfile = user.executionsfiles[codefile.id]
                            assertiv = Assertiveness()
                            assertiv.calculate(codefile, keystrokesfile, executionsfile)

                            if not assertiv.has_files_consistents:
                                self.inconsistents += 1

                            if assertiv.strength:
                                id_list.append(i)
                                start_date_list.append(str(keystrokesfile.datetime_start.date()))
                                semester_id_list.append(semester.semester_id)
                                class_id_list.append(cls.class_id)
                                user_id_list.append(user.user_id)
                                consistency_list.append(bool(assertiv.has_files_consistents))
                                assessment_type_list.append(assessment_type)
                                assessments_id_list.append(online_judge.Helper.extract_assessment_id(keystrokesfile.id))
                                exercise_id_list.append(online_judge.Helper.extract_exercise_id(keystrokesfile.id))
                                strength_list.append("Strong")
                                assertiv_certifier_list.append(assertiv.certifier)
                                assertiv_value_list.append(assertiv.value)
                                cnt_chars_list.append(assertiv.cnt_chars)
                                cnt_keystrokes_list.append(assertiv.cnt_keystrokes)
                                i += 1

        df_assertiv = pd.DataFrame({'ID': id_list,
                                    'DATE_START': start_date_list,
                                    'SEMESTER_ID': semester_id_list,
                                    'CLASS_ID': class_id_list,
                                    'USER_ID': user_id_list,
                                    'CONSISTENCY': consistency_list,
                                    'ASSESSMENT_TYPE': assessment_type_list,
                                    'ASSESSMENTS_ID': assessments_id_list,
                                    'EXERCISE_ID': exercise_id_list,
                                    'STRENGTH': strength_list,
                                    'CERTIFIER': assertiv_certifier_list,
                                    'ASSERTIV_VALUE': assertiv_value_list,
                                    'CNT_CHARS': cnt_chars_list,
                                    'CNT_KEYSTROKES': cnt_keystrokes_list,
                                    })
        df_assertiv.to_csv('../reports/ASSERTIV_EXERCISES.csv', encoding='utf-8', index=False)
        return df_assertiv

    def _process_report_assertiveness_by_student_assessments(self, df_assertiv_exercise: pd.DataFrame):
        # fieldnames = ['ID', 'DATE_START', 'SEMESTER_ID', 'CLASS_ID', 'USER_ID', 'CONSISTENCY', 'ASSESSMENT_TYPE',
        #               'ASSESSMENTS_ID', 'EXERCISE_ID', 'STRENGTH', 'CERTIFIER', 'ASSERTIV_VALUE', 'CNT_CHARS',
        #               'CNT_KEYSTROKES']
        # header = ['ID', 'DATE_START', 'SEMESTER', 'CLASS', 'ASSESSMENT', 'ASSESSMENT_ID', 'USER', 'ASSERTIV_VALUE']

        # Listas-atributos para o DataFrame
        id_list = []
        start_date_list = []
        semester_id_list = []
        class_id_list = []
        assessment_type_list = []
        assessments_id_list = []
        user_id_list = []
        assertiv_value_list = []

        start_date_pred = None
        semester_pred = None
        class_pred = None
        user_pred = None
        assessment_pred = None
        assessment_id_pred = None
        first_time = True
        sum_cnt_chars = 0
        sum_cnt_keystrokes = 0
        i: int = 1  # conta registros
        for index, row in df_assertiv_exercise.iterrows():

            if not bool(row['CONSISTENCY']):
                continue

            # # PARA TESTES
            # if row['CLASS'] not in ["485"]:
            #     continue

            # # PARA TESTES
            # if row['ASSESSMENT_TYPE'] not in ["Lab 3", "TP 3"]:
            #     continue

            if first_time:
                start_date_pred = row['DATE_START']
                semester_pred = row['SEMESTER_ID']
                class_pred = row['CLASS_ID']
                user_pred = row['USER_ID']
                assessment_pred = row['ASSESSMENT_TYPE']
                assessment_id_pred = row['ASSESSMENTS_ID']
                first_time = False

            if user_pred == row['USER_ID'] and assessment_pred == row['ASSESSMENT_TYPE'] and assessment_id_pred == row[
                    'ASSESSMENTS_ID']:
                sum_cnt_chars += int(row['CNT_CHARS'])
                sum_cnt_keystrokes += int(row['CNT_KEYSTROKES'])
            else:
                if sum_cnt_keystrokes > 0.0:
                    assertiv_value = sum_cnt_chars / sum_cnt_keystrokes
                    if assertiv_value > 1.0:
                        # print("Overflow: ", assertiv_value)
                        assertiv_value = 1.0
                    # sum_cnt_chars = int(row['CNT_CHARS'])
                    # sum_cnt_keystrokes = int(row['CNT_KEYSTROKES'])
                    # user_pred = row['USER_ID']
                else:
                    assertiv_value = 0.0

                # Atualiza listas-atributos
                id_list.append(i)
                start_date_list.append(start_date_pred)
                semester_id_list.append(semester_pred)
                class_id_list.append(class_pred)
                assessment_type_list.append(assessment_pred)
                assessments_id_list.append(assessment_id_pred)
                user_id_list.append(user_pred)
                assertiv_value_list.append(round(assertiv_value, self.DECIMAL_PLACES))

                # Reinicia
                sum_cnt_chars = int(row['CNT_CHARS'])
                sum_cnt_keystrokes = int(row['CNT_KEYSTROKES'])
                start_date_pred = row['DATE_START']
                semester_pred = row['SEMESTER_ID']
                class_pred = row['CLASS_ID']
                user_pred = row['USER_ID']
                assessment_pred = row['ASSESSMENT_TYPE']
                assessment_id_pred = row['ASSESSMENTS_ID']
                i += 1

        # Processamento do último aluno do arquivo/relatório
        if sum_cnt_keystrokes > 0.0:
            assertiv_value = sum_cnt_chars / sum_cnt_keystrokes
            if assertiv_value > 1.0:
                # print("Overflow: ", assertiv_value)
                assertiv_value = 1.0
        else:
            assertiv_value = 0.0

        # Atualiza listas-atributos
        id_list.append(i)
        start_date_list.append(start_date_pred)
        semester_id_list.append(semester_pred)
        class_id_list.append(class_pred)
        assessment_type_list.append(assessment_pred)
        assessments_id_list.append(assessment_id_pred)
        user_id_list.append(user_pred)
        assertiv_value_list.append(round(assertiv_value, self.DECIMAL_PLACES))

        df = pd.DataFrame({'ID': id_list,
                           'DATE_START': start_date_list,
                           'SEMESTER_ID': semester_id_list,
                           'CLASS_ID': class_id_list,
                           'ASSESSMENT_TYPE': assessment_type_list,
                           'ASSESSMENTS_ID': assessments_id_list,
                           'USER_ID': user_id_list,
                           'ASSERTIV_VALUE': assertiv_value_list,
                           })

        Helper.convert_numericfields_to_numbers_in_dataframe(df)

        csvFilePath = '../reports/ASSERTIV_ASSESSMENTS.csv'
        df.to_csv(csvFilePath,
                  encoding='utf-8', index=False)
        json_file_path = '../reports/ASSERTIV_ASSESSMENTS.json'
        df.to_json(json_file_path, orient="records", indent=4)
