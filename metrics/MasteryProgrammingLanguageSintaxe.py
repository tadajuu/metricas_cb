import re
from metrics.Metric import Metric
from online_judge.ExecutionsFile import ExecutionsFile


class MasteryProgrammingLanguageSintaxe(Metric):
    """
    @auhor: Salomão (ajustes: Flávio José Mendes Coelho).
    @date: 19/07/2023.
    Calcula a métrica do domínio da sintaxe da linguagem de programação (MLS).
    Ideia: determinar o conciente de erro de Jadud e normaliza para 0.0~1.0.
    O MLS mínimo vale 0.0 e o máximo vale 1.0.
    """

    def __init__(self):
        self.value = 0.0
        self.scores_normalized = 0.0
        self.total_pairs = 0
        self.lista_seq = []
        self.has_files_consistents: bool = False
        self.has_passed_all_CTs: bool = False

    def calculate(self, executionsfile: ExecutionsFile) -> None:
        """
        Realiza o cálculo da MLS.
        :param executionsfile: arquivo que registra ações de submissão do código, testes no console e casos de
         test
        :return: None
        """

        # self.has_files_consistents = codefile.is_consistent and keystrokesfile.is_consistent \
        #     and executionsfile.is_consistent
        self.has_files_consistents = executionsfile.is_consistent

        self.value = 0.0
        self.scores_normalized = 0.0
        self.total_pairs = 0
        self.has_passed_all_CTs = False
        if executionsfile.is_consistent:
            executionsfile.load_text()
            text = executionsfile.text
            scores_normalized, total_pairs, lista_seq = self._error_quotient_Jadud(text)
            if total_pairs != 0:
                self.scores_normalized = scores_normalized
                self.total_pairs = total_pairs
                self.lista_seq = lista_seq
                error_quotient = scores_normalized / total_pairs
                self.value = 1 - error_quotient

    def _get_error_line(self, line_string):
        line = ''
        for char in line_string:
            if 48 <= ord(char) <= 57:
                line = line + char
            else:
                break
        return int(line)

    def _error_quotient_Jadud(self, content):
        # Create consecutive pairs of errors for submition cases
        executions = content.split('-- CODE: \n')
        errors_pairs = []
        errors_descriptions = []
        for i in range(len(executions)):
            is_test = False
            code = executions[i]
            if i > 0:
                #mudei para submission pois o dataset atual não guarda os testes
                is_test = '== RUN (' in executions[i - 1].split('\n')[-2]
            if '-- ERROR:\n' in code and is_test:
                errors_descriptions.append(code.split('-- ERROR:\n')[1])
            elif not ('-- ERROR:\n' in code) and is_test:
                errors_descriptions.append('')
        for error_description in errors_descriptions:
            line = ''
            error_type = ''
            if 'line' in error_description:
                if 'File "XXXX", line ' in error_description:
                    line_string = error_description.split('File "XXXX", line ')[1]
                    line = self._get_error_line(line_string)
                    if '-- TEST CASE' in line_string:
                        error_type = \
                        error_description.split('-- TEST CASE')[0].split('\n')[-2]
                    else:
                        error_type = \
                        error_description.split('-- GRADE')[0].split('\n')[-2]
                    #error_type = error_description.split('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')[0].split('\n')[-3]
                elif 'main.py", line ' in error_description:
                    print("entrei aqui uma vez na vida")
                    line_string = error_description.split('main.py", line ')[1]
                    line = self._get_error_line(line_string)
                    if '-- TEST CASE' in line_string:
                        error_type = \
                            error_description.split('-- TEST CASE')[0].split('\n')[-2]
                    else:
                        error_type = \
                            error_description.split('-- GRADE')[0].split('\n')[-2]
            errors_pairs.append((error_type, line))
        if len(errors_pairs) == 1:
            if errors_pairs[0] == ('', ''):
                errors_pairs.append(('', ''))
            else:
                errors_pairs.append(errors_pairs[0])
        # Computation of scores
        total_pairs = 0
        scores_summation = 0
        l_soma = 0
        conjuntos = []
        size_conjunto = 0
        iniciou = False
        mean_p_i = 0
        lista_seq = []
        for i in range(len(errors_pairs) - 1):
            scs = 0
            # None consecutive error
            if (errors_pairs[i][0] == '' and errors_pairs[i + 1][0] == '') and (
                    errors_pairs[i][1] == '' and errors_pairs[i + 1][1] == ''):
                scores_summation = scores_summation + 0.0
                scs += 0
            # Two consecutive errors:
            elif (errors_pairs[i][0] != '' and errors_pairs[i + 1][0] != '') and (
                    errors_pairs[i][1] != '' and errors_pairs[i + 1][1] != ''):
                scores_summation = scores_summation + 8.0
                scs += 8.0
                # Two consecutive different errors
                if (errors_pairs[i][0] != errors_pairs[i + 1][0]) and (
                        errors_pairs[i][1] != errors_pairs[i + 1][1]) and (
                        errors_pairs[i][0] != '' and errors_pairs[i + 1][0] != ''):
                    scores_summation = scores_summation + 0.0
                    scs += 0
                # Same error two consecutive times, but in different lines (which implies in two different errors)
                elif (errors_pairs[i][0] == errors_pairs[i + 1][0]) and (
                        errors_pairs[i][1] != errors_pairs[i + 1][1]) and (
                        errors_pairs[i][0] != '' and errors_pairs[i + 1][0] != ''):
                    scores_summation = scores_summation + 0.0
                    scs += 0
                # One error two consecutive times
                elif (errors_pairs[i][0] == errors_pairs[i + 1][0]) and (
                        errors_pairs[i][1] == errors_pairs[i + 1][1]):
                    scores_summation = scores_summation + 3.0
                    scs += 3.0
            total_pairs = total_pairs + 1
            lista_seq.append(scs)
            if scs == 11:
                if iniciou:
                    size_conjunto += 1
                else:
                    iniciou = True
                    size_conjunto += 1
            else:
                if iniciou:
                        conjuntos.append(size_conjunto)
                        iniciou = False
        for seq in conjuntos:
            l_soma += seq
        mean_p_i = (l_soma+len(conjuntos))/(2*total_pairs) if total_pairs != 0 else 0
        scores_normalized = scores_summation / 11.0
        return scores_normalized, total_pairs, lista_seq


    # Propriedades e setters

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value

    @property
    def total_pairs(self) -> float:
        return self._total_pairs

    @total_pairs.setter
    def total_pairs(self, total_pairs: float):
        self._total_pairs = total_pairs

    @property
    def scores_normalized(self) -> float:
        return self._scores_normalized

    @scores_normalized.setter
    def scores_normalized(self, scores_normalized: float):
        self._scores_normalized = scores_normalized

    @property
    def has_files_consistents(self) -> bool:
        return self._has_files_consistents

    @has_files_consistents.setter
    def has_files_consistents(self, has_files_consistents: bool):
        self._has_files_consistents = has_files_consistents

    @property
    def has_passed_all_CTs(self) -> bool:
        return self._has_passed_all_CTs

    @has_passed_all_CTs.setter
    def has_passed_all_CTs(self, has_passed_all_CTs: bool):
        self._has_passed_all_CTs = has_passed_all_CTs
