import online_judge
from online_judge.CodebenchLog import CodebenchLog
import online_judge.Helper as Helper
from datetime import datetime
import os
import pandas as pd

__author__ = 'Flávio José Mendes Coelho'


class ReadinessProcessor:
    def __init__(self):
        self.cb_log = online_judge.cb_log
        # self.dt_start = dt_start
        # self.dt_end = dt_end
        self.inconsistents: int = 0
        self.count_exercise_have_start_code = {}
        self.DECIMAL_PLACES = 3
        self.i: int = 1  # conta registros impressos
        self.total_files_no_submissions = 0

        # Listas para os dados do DataFrame
        self.id_list = []
        self.semester_id_list = []
        self.class_id_list = []
        self.user_id_list = []
        self.consistency_list = []
        self.assessment_type_list = []
        self.date_start_list = []
        self.date_end_list = []
        self.assessments_id_list = []
        self.readiness_value_list = []
        self.readiness_IRBO_grade_list = []
        self.sum_procrastination_list = []
        self.sum_count_submissions_list = []

    def load_assessments_per_class(self, class_path_assessments: str) -> dict:
        # Pegando dados sobre os trabalhos da turma
        assessment_filenames: list = os.listdir(class_path_assessments)
        assessment_filenames.sort()
        assessments = {}
        for assessment_filename in assessment_filenames:

            if assessment_filename == '.DS_Store':
                continue

            assessment_file = open(class_path_assessments + '/' + assessment_filename, 'r')
            assessment_data = assessment_file.readlines()
            assessment_id = assessment_filename.replace(".data", "")

            assessments[assessment_id] = {
                'show': True,
                'title': '',
                'type': '',
                'start': '',
                'end': '',
                'amount_exercises': 0,
                'sum_procrastination': 0,
                'total_submissions': 0,
                'procrastination': 0,
                'readiness': 0,
            }

            for data in assessment_data:

                if "---- assessment title: " in data:
                    title = data.replace("---- assessment title: ", "")
                    title = title[:-1]
                    assessments[assessment_id]['title'] = title

                if "---- type: " in data:
                    assessment_type = data.replace("---- type: ", "")
                    assessment_type = assessment_type.strip()
                    assessments[assessment_id]['type'] = assessment_type

                if "---- start: " in data:
                    start = data.replace("---- start: ", "")
                    start = start.strip()
                    # start = start + ":00.000"
                    # start = datetime.fromisoformat(start)
                    assessments[assessment_id]['start'] = start

                if "---- end: " in data:
                    end = data.replace("---- end: ", "")
                    end = end.strip()
                    # end = end + ":00.000"
                    # end = datetime.fromisoformat(end)
                    assessments[assessment_id]['end'] = end

                if "---- exercise " in data:
                    assessments[assessment_id]['amount_exercises'] += 1
        return assessments

    def process(self):
        N: int = 0
        self.i = 1  # conta registros impressos
        self.inconsistents = 0

        semesters = self.cb_log.semesters.values()
        assessments_class = {}

        for semester in semesters:
            semester_id = semester.semester_id

            classes = semester.classes.values()
            for cls in classes:

                class_id = cls.class_id
                assessments = self.load_assessments_per_class(cls.class_path_assessments)
                assessments_class = {class_id: assessments}

                users = cls.users.values()
                for user in users:

                    user_id = user.user_id

                    if user_id in online_judge.LUT_tutors_monitors_professors:
                        # print("Pula tutores!")
                        continue

                    assessment_user = {user_id: assessments_class}

                    assessment_id = ''
                    assessment_id_ant = ''
                    first_time = True
                    for codefile in user.codefiles.values():

                        keystrokesfile = user.keystrokesfiles[codefile.id]
                        executionsfile = user.executionsfiles[codefile.id]

                        assessment_id = online_judge.Helper.extract_assessment_id(executionsfile.id)

                        # # Chiclete com arame: Salta os assessments extras e as provas finais
                        # try:
                        #     new_assessment_id = online_judge.Helper.extract_assessment_id(executionsfile.id)
                        #     title = assessment_user[user_id][class_id][new_assessment_id]['title']
                        #     if "TP" in title.upper() or "EXTRA" in title.upper() or "SIMULADO" in title.upper():
                        #         assessment_user[user_id][class_id][new_assessment_id]['show'] = False
                        #         if assessment_id == '':
                        #             assessment_user[user_id][class_id][new_assessment_id]['procrastination'] = -1
                        #             assessment_id = new_assessment_id
                        #         continue
                        #
                        #     # Salta se o exercício = 0 (não existir ainda)
                        #     assessment_type = online_judge.LUT_class_id_assessment_type[cls.class_id][new_assessment_id]
                        #     if online_judge.LUT_class_assessment_type_id[cls.class_id][assessment_type] == '0':
                        #         assessment_user[user_id][class_id][new_assessment_id]['show'] = False
                        #         assessment_user[user_id][class_id][new_assessment_id]['procrastination'] = -1
                        #         # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                        #         # print()
                        #         continue
                        # except Exception:
                        #     continue

                        # assessment_id = new_assessment_id
                        if executionsfile.is_consistent:
                            file = executionsfile
                            TOKEN_TOTAL_SUBMISSOES_LISTAS = "== SUBMITION"
                        elif keystrokesfile.is_consistent:
                            file = keystrokesfile
                            TOKEN_TOTAL_SUBMISSOES_LISTAS = "#submit#"
                        else:
                            self.inconsistents += 1
                            continue

                        # Salta se o exercício tem um código inicial
                        if codefile.exercise_have_start_code:
                            exercise_id = online_judge.Helper.extract_exercise_id(codefile.id)
                            tmp_value = self.count_exercise_have_start_code.setdefault(exercise_id)
                            if tmp_value:
                                self.count_exercise_have_start_code[exercise_id] += 1
                            else:
                                self.count_exercise_have_start_code[exercise_id] = 1
                            continue

                        assessment_user[user_id][class_id][assessment_id]['show'] = True
                        if first_time:
                            assessment_id_ant = assessment_id
                            first_time = False

                        readiness = 0.0
                        procrastinacao_exercicio = 0.0
                        total_submissions = 0

                        start_date = datetime.fromisoformat(assessment_user[user_id][class_id][assessment_id]['start'])
                        end_date = datetime.fromisoformat(assessment_user[user_id][class_id][assessment_id]['end'])
                        minutos_totais_trabalho = (end_date - start_date).total_seconds() / 60
                        file.load_text()

                        for line in file.text.splitlines():

                            if TOKEN_TOTAL_SUBMISSOES_LISTAS in line:
                                total_submissions += 1
                                hora_submissao = online_judge.Helper.extract_datetime(line)
                                hora_fim_assessment = datetime.fromisoformat(assessment_user[user_id][class_id][assessment_id]['end'])
                                minutos_totais_entre_fim_do_trabalho_e_submissao = (hora_fim_assessment - hora_submissao).total_seconds() / 60
                                procrastinacao_exercicio += 1 - (minutos_totais_entre_fim_do_trabalho_e_submissao / minutos_totais_trabalho)

                        assessment_user[user_id][class_id][assessment_id]['sum_procrastination'] += procrastinacao_exercicio
                        assessment_user[user_id][class_id][assessment_id]['total_submissions'] += total_submissions

                        if assessment_id != assessment_id_ant:
                            if assessment_user[user_id][class_id][assessment_id_ant]['total_submissions'] != 0:
                                assessment_user[user_id][class_id][assessment_id_ant]['procrastination'] = \
                                    assessment_user[user_id][class_id][assessment_id_ant]['sum_procrastination'] / \
                                    assessment_user[user_id][class_id][assessment_id_ant]['total_submissions']
                                assessment_user[user_id][class_id][assessment_id_ant]['readiness'] = 1 - assessment_user[user_id][class_id][assessment_id_ant]['procrastination']
                            else:
                                assessment_user[user_id][class_id][assessment_id_ant]['procrastination'] = -1
                                assessment_user[user_id][class_id][assessment_id_ant][
                                    'readiness'] = -1

                            if assessment_user[user_id][class_id][assessment_id_ant]['show']:
                                self.save_data(keystrokesfile, semester_id, class_id, user_id, assessment_id_ant,
                                               assessment_user[user_id][class_id][assessment_id_ant]['title'],
                                               assessment_user[user_id][class_id][assessment_id_ant]['type'],
                                               assessment_user[user_id][class_id][assessment_id_ant]['start'],
                                               assessment_user[user_id][class_id][assessment_id_ant]['end'],
                                               assessment_user[user_id][class_id][assessment_id_ant][
                                                   'amount_exercises'],
                                               assessment_user[user_id][class_id][assessment_id_ant][
                                                   'readiness'],
                                               assessment_user[user_id][class_id][assessment_id_ant][
                                                   'sum_procrastination'],
                                               assessment_user[user_id][class_id][assessment_id_ant][
                                                   'total_submissions'])
                            assessment_id_ant = assessment_id

                    # print(f"user_id:{user_id}")
                    # print(f"class_id:{class_id}")
                    # print(f"assessment_id:{assessment_id}")
                    # print(f"total_submissions:{assessment_user[user_id][class_id][assessment_id]['total_submissions']}")
                    # print()
                    if assessment_user[user_id][class_id][assessment_id]['total_submissions'] != 0:
                        assessment_user[user_id][class_id][assessment_id]['procrastination'] = assessment_user[user_id][class_id][assessment_id]['sum_procrastination'] / assessment_user[user_id][class_id][assessment_id]['total_submissions']
                        assessment_user[user_id][class_id][assessment_id]['readiness'] = 1 - assessment_user[user_id][class_id][assessment_id]['procrastination']
                    else:
                        assessment_user[user_id][class_id][assessment_id]['procrastination'] = -1
                        assessment_user[user_id][class_id][assessment_id]['readiness'] = -1

                    if assessment_user[user_id][class_id][assessment_id]['show']:
                        self.save_data(keystrokesfile, semester_id, class_id, user_id, assessment_id,
                                       assessment_user[user_id][class_id][assessment_id]['title'],
                                       assessment_user[user_id][class_id][assessment_id]['type'],
                                       assessment_user[user_id][class_id][assessment_id]['start'],
                                       assessment_user[user_id][class_id][assessment_id]['end'],
                                       assessment_user[user_id][class_id][assessment_id]['amount_exercises'],
                                       assessment_user[user_id][class_id][assessment_id]['readiness'],
                                       assessment_user[user_id][class_id][assessment_id]['sum_procrastination'],
                                       assessment_user[user_id][class_id][assessment_id]['total_submissions'])

        df = pd.DataFrame({'ID': self.id_list,
                           'SEMESTER_ID': self.semester_id_list,
                           'CLASS_ID': self.class_id_list,
                           'USER_ID_': self.user_id_list,
                           'ASSESSMENT_TYPE': self.assessment_type_list,
                           'ASSESSMENTS_ID': self.assessments_id_list,
                           'DATE_START': self.date_start_list,
                           'DATE_END': self.date_end_list,
                           'READINESS_VALUE': self.readiness_value_list,
                           'IRBO_GRADE': self.readiness_IRBO_grade_list,
                           'SUM_PROCRASTINATION': self.sum_procrastination_list,
                           'SUM_COUNT_SUBMISSIONS': self.sum_count_submissions_list,
                           })

        Helper.convert_numericfields_to_numbers_in_dataframe(df)

        csvFilePath = '../reports/READINESS_ASSESSMENTS.csv'
        df.to_csv(csvFilePath,
                  encoding='utf-8', index=False)
        json_file_path = '../reports/READINESS_ASSESSMENTS.json'
        df.to_json(json_file_path, orient="records", indent=4)

    def save_data(self, keystrokesfile, semester_id, class_id, user_id, assessment_id, title, _type, start, end,
                  amount_exercises, readiness, sum_procrastination, total_submissions):
        # O Lab 0 seria combinados com o Lab 1, porém para liberar logo o relatório decidimos somente eliminar
        # o Lab 0. No relatório definitivo de 2024 essa junção entre Lab 0 e Lab 1 deve deve ser resolvida.
        # Eliminei os TPs também porque eles não fazem parte da análise da Presteza. Além do mais o valor da sum_procrastination
        # está vindo negativos em alguns TPs. Esse problema deve ser resolvido quando eu mudar a codificação para o padrão
        # das demais métricas (calculando para arquivo de código/log e depois acumulando os valores das métricas).
        # if title[:5] != "Lab 0" and title[:2] != "TP":
        if title[:5] != "Lab 0" and title[:2] != "TP":
            self.id_list.append(self.i)
            # self.date_start_list.append(str(keystrokesfile.datetime_start.date()))
            self.semester_id_list.append(semester_id)
            self.class_id_list.append(class_id)
            self.user_id_list.append(user_id)
            self.assessment_type_list.append(title[:5])
            self.assessments_id_list.append(assessment_id)
            self.date_start_list.append(start)
            self.date_end_list.append(end)
            # self.readiness_value_list.append(round(readiness, 10))

            # num_score é o próprio valor da métrica. Esse valor corresponde a um conceito I, R, B ou O. Esse conceitos são
            # chamados de grade.
            num_score = round(readiness, self.DECIMAL_PLACES)
            self.readiness_value_list.append(num_score)

            # Obtém um conceito IRBO a partir do valor da assertividade, isto é, num_score.
            self.readiness_IRBO_grade_list.append(
                Helper.IRBO_scale("P", num_score * 10))  # *10 para num_score ficar entre 0.0 e 10.0

            self.sum_procrastination_list.append(round(sum_procrastination, 10))
            self.sum_count_submissions_list.append(round(total_submissions, 10))
            self.i += 1
