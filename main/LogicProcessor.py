import online_judge
from metrics.MasteryProgrammingLogic import MasteryProgrammingLogic as MPL
from online_judge.CodebenchLog import CodebenchLog
import online_judge.Helper as Helper
from datetime import datetime
import pandas as pd

__author__ = 'Flávio José Mendes Coelho'


class LogicProcessor:

    def __init__(self):
        self.cb_log = online_judge.cb_log
        # self.dt_start = dt_start
        # self.dt_end = dt_end
        self.inconsistents: int = 0
        self.count_exercise_have_start_code = {}
        self.DECIMAL_PLACES = 3

    def process(self):
        df = self._process_report_MPL_by_student_exercise()
        self._process_report_MPL_by_student_assessments(df)

    def _process_report_MPL_by_student_exercise(self):
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
        all_CTs_passed_list = []
        mpl_value_list = []  # average grade
        #sum_grades_list = []
        #count_grades_list = []
        produto_grade_taxa_list = []
        taxas_list = []
        print(online_judge.LUT_assessments)
        semesters = self.cb_log.semesters.values()
        for semester in semesters:
            classes = semester.classes.values()
            for cls in classes:
                # # PARA TESTES  # DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG
                # if cls.class_id not in ["485"]:
                #     continue
                total = cls.total_assessments
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

                        # print(user.user_id, assessment_id, exercise_id, user.is_consistent)
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
                            # if codefile.id == "4447_1366":
                            #     print("4447_1366 OK!", user.user_id)
                            # Se o trabalho/prova não estiver classificado, salta ele.
                            try:
                                _, _, assessment_type, assessment_title, start_date, end_date = online_judge.LUT_assessments[cls.class_id][assessment_id]
                            except Exception:
                                # if codefile.id == "4447_1366":
                                #     print(assessment_type, cls.class_id, assessment_id)
                                # print("Pulou!!!", cls.class_id, assessment_id)
                                continue

                        keystrokesfile = user.keystrokesfiles[codefile.id]
                        executionsfile = user.executionsfiles[codefile.id]
                        mpl = MPL()
                        _, _, block, total_sub, total_acertos = total[(total["assessmentId"] == assessment_id) & (total["programmingExerciseId"] == exercise_id)].iloc[0]
                        busca_todos_block = total[(total["assessmentId"] == assessment_id) & (total["block"] == block)]
                        total_acertos_block =  busca_todos_block['totalacertos'].sum()
                        total_sub_block = busca_todos_block['total'].sum()
                        taxa_acertos = total_acertos_block/ total_sub_block if total_sub_block > 0 else 0
                        #taxa_acertos = total_acertos/total_sub if total_sub > 0 else 0
                        mpl.calculate(executionsfile, taxa_acertos)

                        if not mpl.has_files_consistents:
                            self.inconsistents += 1

                        id_list.append(i)
                        date_start_list.append(str(keystrokesfile.datetime_start.date()))
                        semester_id_list.append(semester.semester_id)
                        class_id_list.append(cls.class_id)
                        user_id_list.append(user.user_id)
                        consistency_list.append(bool(mpl.has_files_consistents))
                        assessment_type_list.append(assessment_type)
                        assessments_id_list.append(assessment_id)
                        exercise_id_list.append(exercise_id)
                        # assessments_id_list.append(online_judge.Helper.extract_assessment_id(keystrokesfile.id))
                        # exercise_id_list.append(online_judge.Helper.extract_exercise_id(keystrokesfile.id))
                        produto_grade_taxa_list.append(mpl.value * taxa_acertos)
                        all_CTs_passed_list.append(bool(mpl.has_passed_all_CTs))
                        mpl_value_list.append(mpl.value)
                        #sum_grades_list.append(mpl.sum_grades)
                        #count_grades_list.append(mpl.count_grades)
                        taxas_list.append(taxa_acertos)
                        i += 1

        df_MPL = pd.DataFrame({'ID': id_list,
                               'DATE_START': date_start_list,
                               'SEMESTER_ID': semester_id_list,
                               'CLASS_ID': class_id_list,
                               'USER_ID': user_id_list,
                               'CONSISTENCY': consistency_list,
                               'ASSESSMENT_TYPE': assessment_type_list,
                               'ASSESSMENTS_ID': assessments_id_list,
                               'EXERCISE_ID': exercise_id_list,
                               'ALL_CTS_PASSED': all_CTs_passed_list,
                               'MPL_VALUE': mpl_value_list,
                               #'SUM_GRADES': sum_grades_list,
                               #'COUNT_GRADES': count_grades_list,
                               'PROD_GRADE_TAXA': produto_grade_taxa_list,
                               'TAXAS': taxas_list
                               })
        Helper.convert_numericfields_to_numbers_in_dataframe(df_MPL)
        csvFilePath = '../reports/LOGIC_EXERCISES.csv'
        df_MPL.to_csv(csvFilePath, encoding='utf-8', index=False)
        return df_MPL

    def _process_report_MPL_by_student_assessments(self, df_MPL_exercise: pd.DataFrame):

        # Listas-atributos para o DataFrame
        id_list = []
        date_start_list = []
        semester_id_list = []
        class_id_list = []
        assessment_type_list = []
        assessments_id_list = []
        user_id_list = []
        MPL_value_list = []
        MPL_IRBO_grade_list = []
        first_time = True
        user_pred = ''
        sum_taxas = 0.0
        sum_produtos_grade_taxa = 0.0
        #sum_grades = 0.0
        #count_grades = 0
        houve_processamento = False
        i: int = 1  # conta registros
        for index, row in df_MPL_exercise.iterrows():
            if not bool(row['CONSISTENCY']):
                continue
            # if not bool(row['CONSISTENCY']) or str(row['ASSESSMENT_TYPE'][:2]).upper() == "TP":
            #     continue

            # PARA TESTES
            # if row['CLASS_ID'] not in ["485"]:
            #     houve_processamento = False
            #     continue
            # else:
            #     houve_processamento = True

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

            mpl = 0.0
            # if user_pred == row['USER_ID'] and assessment_pred == row['ASSESSMENT_TYPE'] and assessment_id_pred == row[
            if user_pred == row['USER_ID'] and assessment_pred == row['ASSESSMENT_TYPE']:
                sum_taxas += float(row['TAXAS'])
                sum_produtos_grade_taxa += float(row['PROD_GRADE_TAXA'])
                #sum_grades += float(row['SUM_GRADES'])
                #count_grades += float(row['COUNT_GRADES'])
            else:
                if sum_taxas > 0.0:
                    #mpl = max(grades)*pow((1-0.001),pow(len(grades),1.5))
                    mpl = sum_produtos_grade_taxa/sum_taxas
                    #mpl = sum_grades / count_grades
                    if mpl > 1.0:
                        # print("Overflow MPL: ", mpl)
                        mpl = 1.0
                else:
                    mpl = 0.0

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
                num_score = round(mpl, self.DECIMAL_PLACES)
                MPL_value_list.append(num_score * 10) # *10 para num_score ficar entre 0.0 e 10.0

                # Obtém um conceito IRBO a partir do valor da assertividade, isto é, num_score.
                MPL_IRBO_grade_list.append(Helper.IRBO_scale("L", num_score * 10))  # *10 para num_score ficar entre 0.0 e 10.0

                #
                sum_taxas = float(row['TAXAS'])
                sum_produtos_grade_taxa = float(row['PROD_GRADE_TAXA'])
                #sum_grades = float(row['SUM_GRADES'])
                #count_grades = float(row['COUNT_GRADES'])
                date_start_pred = row['DATE_START']
                semester_pred = row['SEMESTER_ID']
                class_pred = row['CLASS_ID']
                user_pred = row['USER_ID']
                assessment_pred = row['ASSESSMENT_TYPE']
                assessment_id_pred = row['ASSESSMENTS_ID']
                i += 1

        # Processamento do último aluno do arquivo/relatório
        if sum_taxas > 0.0:
            mpl = sum_produtos_grade_taxa / sum_taxas
            #mpl = sum_grades / count_grades
            if mpl > 1.0:
                # print("Overflow MPL: ", mpl)
                mpl = 1.0
        else:
            mpl = 0.0

        # Atualiza listas-atributos
        if True:
            id_list.append(i)
            date_start_list.append(date_start_pred)
            semester_id_list.append(semester_pred)
            class_id_list.append(class_pred)
            assessment_type_list.append(assessment_pred)
            assessments_id_list.append(assessment_id_pred)
            user_id_list.append(user_pred)
            num_score = round(mpl, self.DECIMAL_PLACES)
            MPL_value_list.append(num_score)
            MPL_IRBO_grade_list.append(Helper.IRBO_scale("L", num_score * 10))  # *10 para num_score ficar entre 0.0 e 10.0

            df = pd.DataFrame({'ID': id_list,
                               'DATE_START': date_start_list,
                               'SEMESTER_ID': semester_id_list,
                               'CLASS_ID': class_id_list,
                               'ASSESSMENT_TYPE': assessment_type_list,
                               'ASSESSMENTS_ID': assessments_id_list,
                               'USER_ID': user_id_list,
                               'MPL_VALUE': MPL_value_list,
                               'IRBO_GRADE': MPL_IRBO_grade_list,
                               })

            Helper.convert_numericfields_to_numbers_in_dataframe(df)

            csvFilePath = '../reports/LOGIC_ASSESSMENTS.csv'
            df.to_csv(csvFilePath,
                      encoding='utf-8', index=False)
            json_file_path = '../reports/LOGIC_ASSESSMENTS.json'
            df.to_json(json_file_path, orient="records", indent=4)
