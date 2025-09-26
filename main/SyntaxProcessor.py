import online_judge
from metrics.MasteryProgrammingLanguageSintaxe import MasteryProgrammingLanguageSintaxe as MLS
from online_judge.CodebenchLog import CodebenchLog
import online_judge.Helper as Helper
from datetime import datetime
import pandas as pd
import numpy as np

__author__ = 'Flávio José Mendes Coelho'


class SyntaxProcessor:

    def __init__(self):
        self.cb_log = online_judge.cb_log
        # self.dt_start = dt_start
        # self.dt_end = dt_end
        self.inconsistents: int = 0
        self.count_exercise_have_start_code = {}
        self.DECIMAL_PLACES = 3

    def process(self):
        df = self._process_report_MLS_by_student_exercise()
        self._process_report_MLS_by_student_assessments(df)

    def _process_report_MLS_by_student_exercise(self):

        i: int = 1  # conta registros
        self.inconsistents: int = 0

        # Listas para os dados do DataFrame
        id_list = []
        date_start_list = []
        semester_id_list = []
        class_id_list = []
        user_id_list = []
        consistency_list = []
        assessment_type_list = []
        assessments_id_list = []
        exercise_id_list = []
        mls_value_list = []
        scores_normalized_list = []
        total_pairs_list = []
        lista_seq = []

        semesters = self.cb_log.semesters.values()
        for semester in semesters:
            classes = semester.classes.values()
            for cls in classes:

                # # # PARA TESTES  # DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG
                # if cls.class_id not in ["485"]:
                #     continue

                users = cls.users.values()
                for user in users:

                    # if user.user_id != '7675': # DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG
                    # if user.user_id != '7104': # DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG
                    #     continue

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
                                _, _, assessment_type, assessment_title, start_date, end_date = online_judge.LUT_assessments[cls.class_id][assessment_id]
                            except Exception:
                                # print("Pulou!!!", cls.class_id, assessment_id)
                                continue

                            keystrokesfile = user.keystrokesfiles[codefile.id]
                            executionsfile = user.executionsfiles[codefile.id]

                            mls = MLS()
                            mls.calculate(executionsfile)

                            if not mls.has_files_consistents:
                                self.inconsistents += 1

                            id_list.append(i)
                            date_start_list.append(str(keystrokesfile.datetime_start.date()))
                            semester_id_list.append(semester.semester_id)
                            class_id_list.append(cls.class_id)
                            user_id_list.append(user.user_id)
                            consistency_list.append(bool(mls.has_files_consistents))
                            assessment_type_list.append(assessment_type)
                            assessments_id_list.append(online_judge.Helper.extract_assessment_id(keystrokesfile.id))
                            exercise_id_list.append(online_judge.Helper.extract_exercise_id(keystrokesfile.id))
                            mls_value_list.append(mls.value)
                            scores_normalized_list.append(mls.scores_normalized)
                            total_pairs_list.append(mls.total_pairs)
                            lista_seq.append(mls.lista_seq)
                            i += 1

        self.max_mls_value = np.max(mls_value_list)
        mls_value_normalized_list = np.divide(mls_value_list, self.max_mls_value)
        df_MLS = pd.DataFrame({'ID': id_list,
                               'DATE_START': date_start_list,
                               'SEMESTER_ID': semester_id_list,
                               'CLASS_ID': class_id_list,
                               'USER_ID': user_id_list,
                               'CONSISTENCY': consistency_list,
                               'ASSESSMENT_TYPE': assessment_type_list,
                               'ASSESSMENTS_ID': assessments_id_list,
                               'EXERCISE_ID': exercise_id_list,
                               'MLS_VALUE': mls_value_normalized_list,
                               'SCORES_NORMALIZED': scores_normalized_list,
                               'TOTAL_PAIRS': total_pairs_list,
                               'LISTA_SEQ': lista_seq
                               })
        # df_MLS.to_csv('../reports/REPORT_MLS_BY_STUDENT_EXERCISE.csv', encoding='utf-8', index=False)
        return df_MLS

    def _process_report_MLS_by_student_assessments(self, df_MLS_exercise: pd.DataFrame):
        # fieldnames = ['ID', 'DATE_START', 'SEMESTER_ID', 'CLASS_ID', 'USER_ID', 'CONSISTENCY', 'ASSESSMENT_TYPE',
        #               'ASSESSMENTS_ID', 'EXERCISE_ID', 'MLS_VALUE', 'SCORES_NORMALIZED', 'TOTAL_PAIRS']
        # header = ['ID', 'DATE_START', 'SEMESTER', 'CLASS', 'ASSESSMENT', 'ASSESSMENT_ID', 'USER', 'MLS']

        # Listas-atributos para o DataFrame
        id_list = []
        date_start_list = []
        semester_id_list = []
        class_id_list = []
        assessment_type_list = []
        assessments_id_list = []
        user_id_list = []
        MLS_value_list = []
        MLS_IRBO_grade_list = []
        max_mls_value = np.max(df_MLS_exercise['MLS_VALUE'])
        first_time = True
        user_pred = ''
        sum_scores_normalized = 0.0
        sum_total_pairs = 0
        total_lista_seq = []
        i: int = 1  # conta registros
        for index, row in df_MLS_exercise.iterrows():
            if not bool(row['CONSISTENCY']):
                continue

            # # PARA TESTES
            # if row['CLASS'] not in ["485"]:
            #     continue

            # # PARA TESTES
            # if row['ASSESSMENT_TYPE'] not in ["Lab 3", "TP 3"]:
            #     continue

            if first_time:
                date_start_pred = row['DATE_START']
                semester_pred = row['SEMESTER_ID']
                class_pred = row['CLASS_ID']
                user_pred = row['USER_ID']
                assessment_pred = row['ASSESSMENT_TYPE']
                assessment_id_pred = row['ASSESSMENTS_ID']
                first_time = False

            mls = 0.0
            # if user_pred == row['USER_ID'] and assessment_pred == row['ASSESSMENT_TYPE']:
            if user_pred == row['USER_ID'] and assessment_pred == row['ASSESSMENT_TYPE']:
                sum_scores_normalized += float(row['SCORES_NORMALIZED'])
                sum_total_pairs += float(row['TOTAL_PAIRS'])
                for num in (row['LISTA_SEQ']):
                    total_lista_seq.append(float(num))
            else:
                if sum_total_pairs > 0.0:
                    #calcular mean_p_i:
                    conjuntos = []
                    l_soma = 0
                    mean_p_i = 0
                    size_conjunto = 0
                    iniciou = False
                    for num in total_lista_seq:
                        if num == 11:
                            if iniciou:
                                size_conjunto += 1
                            else:
                                iniciou = True
                                size_conjunto += 1
                        else:
                            if iniciou:
                                if size_conjunto > 1:
                                    conjuntos.append(size_conjunto)
                                size_conjunto = 0
                                iniciou = False
                    for seq in conjuntos:
                        l_soma += seq
                    mean_p_i = (l_soma + len(conjuntos)) / (2 * sum_total_pairs)
                    #print(f"sum_scores = {sum_scores_normalized} pairs = {sum_total_pairs} mean_p_i = {mean_p_i}")
                    mls = (1.0 - pow((sum_scores_normalized / sum_total_pairs),1 - mean_p_i)) / max_mls_value
                    if mls > 1.0:
                        mls = 1.0
                else:
                    mls = 0.0

                # Atualiza listas-atributos
                id_list.append(i)
                date_start_list.append(date_start_pred)
                semester_id_list.append(semester_pred)
                class_id_list.append(class_pred)
                assessment_type_list.append(assessment_pred)
                assessments_id_list.append(assessment_id_pred)
                user_id_list.append(user_pred)

                # num_score é o próprio valor da métrica. Esse valor corresponde a um conceito I, R, B ou O. Esse conceitos são
                # chamados de grade.
                num_score = round(mls, self.DECIMAL_PLACES)
                MLS_value_list.append(num_score * 10) # *10 para num_score ficar entre 0.0 e 10.0
                # Obtém um conceito IRBO a partir do valor da assertividade, isto é, num_score.
                MLS_IRBO_grade_list.append(Helper.IRBO_scale("S", num_score * 10))  # *10 para num_score ficar entre 0.0 e 10.0

                # Reinicia
                sum_scores_normalized = float(row['SCORES_NORMALIZED'])
                total_lista_seq = row['LISTA_SEQ']
                sum_total_pairs = float(row['TOTAL_PAIRS'])
                date_start_pred = row['DATE_START']
                semester_pred = row['SEMESTER_ID']
                class_pred = row['CLASS_ID']
                user_pred = row['USER_ID']
                assessment_pred = row['ASSESSMENT_TYPE']
                assessment_id_pred = row['ASSESSMENTS_ID']
                i += 1

        # Processamento do último aluno do arquivo/relatório
        if sum_total_pairs > 0.0:
            conjuntos = []
            l_soma = 0
            mean_p_i = 0
            iniciou = False
            size_conjunto = 0
            for num in total_lista_seq:
                if num == 11:
                    if iniciou:
                        size_conjunto += 1
                    else:
                        iniciou = True
                        size_conjunto += 1
                else:
                    if iniciou:
                        if size_conjunto > 1:
                            conjuntos.append(size_conjunto)
                        size_conjunto = 0
                        iniciou = False
            for seq in conjuntos:
                l_soma += seq
            mean_p_i = (l_soma + len(conjuntos)) / (2 * sum_total_pairs)
            mls = (1.0 - pow((sum_scores_normalized / sum_total_pairs), 1 - mean_p_i)) / max_mls_value
            if mls > 1.0:
                # print("Overflow MSL:", mls)
                mls = 1.0
        else:
            mls = 0.0

        # Atualiza listas-atributos
        id_list.append(i)
        date_start_list.append(date_start_pred)
        semester_id_list.append(semester_pred)
        class_id_list.append(class_pred)
        assessment_type_list.append(assessment_pred)
        assessments_id_list.append(assessment_id_pred)
        user_id_list.append(user_pred)
        num_score = round(mls, self.DECIMAL_PLACES)
        MLS_value_list.append(num_score *10)
        MLS_IRBO_grade_list.append(Helper.IRBO_scale("S", num_score * 10))  # *10 para num_score ficar entre 0.0 e 10.0

        df = pd.DataFrame({'ID': id_list,
                           'DATE_START': date_start_list,
                           'SEMESTER_ID': semester_id_list,
                           'CLASS_ID': class_id_list,
                           'ASSESSMENT_TYPE': assessment_type_list,
                           'ASSESSMENTS_ID': assessments_id_list,
                           'USER_ID': user_id_list,
                           'MLS_VALUE': MLS_value_list,
                           'IRBO_GRADE': MLS_IRBO_grade_list,
                           })

        Helper.convert_numericfields_to_numbers_in_dataframe(df)

        csvFilePath = '../reports/SINTAXE_ASSESSMENTS.csv'
        df.to_csv(csvFilePath,
                  encoding='utf-8', index=False)
        json_file_path = '../reports/SINTAXE_ASSESSMENTS.json'
        df.to_json(json_file_path, orient="records", indent=4)
