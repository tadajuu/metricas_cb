import re
from metrics.Metric import Metric
from online_judge.ExecutionsFile import ExecutionsFile


class MasteryProgrammingLogic(Metric):
    """
    @auhor: Flávio José Mendes Coelho.
    @date: 27/01/2023.
    Calcula a métrica do domínio da lógica de programação (MPL).
    Ideia: o pressuposto é que não existam mais erros de sintaxe. Neste caso, calcula-se o MPL.
    Cálculo: ...
    O MPL mínimo vale 0.0 e o máximo vale 1.0.
    """

    def __init__(self):
        self.value = 0.0
        self.sum_grades = 0.0
        self.count_grades = 0
        self.taxa_acerto = 0
        self.grades = []
        self.max_grade = 0
        self.has_files_consistents: bool = False
        self.has_passed_all_CTs: bool = False

    def calculate(self, executionsfile: ExecutionsFile, taxa_acertos) -> None:
        """
        Realiza o cálculo da MPL.
        :param codefile: arquivo do código fonte do programador.
        :param keystrokesfile: arquivo de log com o registro de keystrokes e todos os eventos registrados durante
         uma ou mais sessões de codificação de um exercício ou prova no Codebench.
        :param executionsfile: arquivo que registra ações de submissão do código, testes no console e casos de
         test
        :return: None
        """

        # self.has_files_consistents = codefile.is_consistent and keystrokesfile.is_consistent \
        #     and executionsfile.is_consistent
        self.has_files_consistents = executionsfile.is_consistent

        self.value = 0.0
        self.sum_grades = 0.0
        self.count_grades = 0
        self.grades = []
        self._has_passed_all_CTs = False
        if executionsfile.is_consistent:
            executionsfile.load_text()
            text = executionsfile.text
            grades = self._get_grades(text)
            if grades:
                self._has_passed_all_CTs = max(grades) == 1.0
                grades = self._leave_only_one_100percent_grade(grades)
                self.grades = grades
                average_grade, sum_grades, count_grades = self._average(grades)
                #self.value = average_grade
                self.value = max(grades)*pow((1-0.001),pow(len(grades),1.5))
                self.max_grade = max(grades)
                self.sum_grades = sum_grades
                self.count_grades = count_grades

    def _leave_only_one_100percent_grade(self, grades: list):
        grades.sort()
        new_grades = []
        for grade in grades:
            new_grades.append(grade)
            if grade == 1.0:
                break
        return new_grades

    def _average(self, list_values: list) -> float:
        sum = 0.0
        for value in list_values:
            sum += value
        count_values = len(list_values)
        average_value = sum / count_values
        return average_value, sum, count_values

    def _get_grades(self, text: str) -> list:
        """
        Retorna todos os grades no text e os converte para [0.0, 1.0].
        :param text: texto do arquivo ExecutionsFile.
        :return: lista de grades.
        """
        PATTERN_GRADE1 = '-- GRADE:\n\d{1}%|-- GRADE:\n\d{2}%|-- GRADE:\n\d{3}%'
        PATTERN_GRADE2 = '\d{1}%|\d{2}%|\d{3}%'
        grades = []
        for match in re.finditer(PATTERN_GRADE1, text):
            grade_line = match.group()
            grade_str = re.search(PATTERN_GRADE2, grade_line).group()
            grade = float(grade_str[:-1])
            grade_converted = grade/100
            grades.append(grade_converted)
        return grades


    # Propriedades e setters

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value

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
