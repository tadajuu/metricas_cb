from metrics.Metric import Metric
from online_judge.KeystrokesFile import KeystrokesFile


class ActiveCodingTime(Metric):
    """
    @auhor: Flávio José Mendes Coelho.
    @date: 07/02/2023.
    @auhor: Flávio José Mendes Coelho.
    @date: 07/02/2023.
    Calcula o Tempo Ativo de Codificação (ACT - Active Coding Time) de um aluno durante um exercício.
    O ACT é uma medida do quanto um aluno se dedica ativamente à codificação de um exercício,
    uma lista, ou várias listas. Isto é calculado somando-se os intervalos de tempo de cada evento de digitação
    (keystroke), exceto os intervalos de tempo maiores que um limite L. A grandeza do ACT
    é fornecida em segundos.
    """

    def __init__(self):
        self.value: float = 0.0
        self.limit: float = 60.0     # default 60s.
        self.has_files_consistents: bool = False

    def calculate(self, keystrokesfile: KeystrokesFile, limit: float = 60.0) -> None:
        self.value: float = 0.0
        self.has_files_consistents: bool = keystrokesfile.is_consistent

        if keystrokesfile.is_consistent:
            self.limit = limit
            keystrokesfile.load_text()
            text = keystrokesfile.text.splitlines()
            self.value = self._counting_active_time(text, limit, keystrokesfile)

    def _counting_active_time(self, text: str, limit: float, keystrokesfile: KeystrokesFile) -> float:
        dummy_datetime = keystrokesfile.dummy_datetime
        is_first_time = True
        time_accumulator = 0.0
        for line in text:
            date = keystrokesfile.extract_datetime(line)

            if is_first_time:
                prev_date = date
                # caso 1: is_first_time and !dummy_datetime
                if date != dummy_datetime:
                    is_first_time = False
                # else: caso 2: is_first_time and dummy_datetime
            else:
                # caso 3: !is_first_time and !dummy_datetime
                if date == dummy_datetime:
                    date = prev_date
                # else: caso 4: !is_first_time and !dummy_datetime

            # Calcula o intervalo de tempo entre datas consecutivas e acumula o intervalo
            date_diff = date - prev_date
            if abs(date_diff.total_seconds()) <= limit:
                time_accumulator += date_diff.total_seconds()
            prev_date = date

        return time_accumulator

    # Propriedades e setters
    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value

    # Propriedades e setters
    @property
    def limit(self) -> float:
        return self._limit

    @limit.setter
    def limit(self, limit: float):
        self._limit = limit




