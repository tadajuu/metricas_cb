from online_judge.File import File
import os
import re
from datetime import datetime

__author__ = 'Flávio José Mendes Coelho'


class KeystrokesFile(File):

    def __init__(self, file_name: str, path: str):
        super().__init__(file_name, path)
        self.dummy_datetime = datetime.fromisoformat('2000-01-01 00:00:00.000')
        if self.is_consistent:
            first_line, last_line = self._read_first_last_lines(self.path + self.name)
            self.datetime_start: datetime = self.extract_datetime(first_line)
            self.datetime_end: datetime = self.extract_datetime(last_line)
        else:
            self.datetime_start: datetime = self.dummy_datetime
            self.datetime_end: datetime = self.dummy_datetime

    def _read_first_last_lines(self, file_name: str):
        """
        Adaptado de: https://www.codingem.com/how-to-read-the-last-line-of-a-file-in-python/
                https://stackoverflow.com/questions/3346430/what-is-the-most-efficient-way-to-get-first-and-last-line-of-a-text-file#:~:text=use%20f.,Line%20Before%20Last%20Line...
        """
        with open(file_name, "rb") as f:
            first_line = f.readline().decode()  # decode converte de binário para texto
            last_line = self._read_last_line(f)
        return first_line, last_line

    def _read_last_line(self, file: object) -> str:
        """
        Retorna a última linha do arquivo contendo uma datetime.
        Adaptado de: https://www.codingem.com/how-to-read-the-last-line-of-a-file-in-python/
        """
        last_line_str = ""
        try:
            PATTERN_DATE = r'\d{4}-\d{2}-\d{2}'
            PATTERN_TIME = r'\d{2}:\d{2}:\d{2}\.\d{3}'
            PATTERN_DATETIME = PATTERN_DATE + r'T' + PATTERN_TIME + r'Z'
            file.seek(0, os.SEEK_END)  # Jump to end of file.

            # Verificar se o arquivo tem apenas uma linha
            file_position = file.tell()  # Obtém a posição atual no arquivo
            file.seek(0, os.SEEK_SET)  # Voltar para o início do arquivo
            content = file.read()  # Ler todo o conteúdo

            # Se o arquivo tiver apenas uma linha, retornamos essa linha
            if file_position == len(content):
                return content.decode().strip()  # Decodifica para string e remove quebras de linha

            # Se o arquivo tem mais de uma linha, podemos continuar a busca pela última linha
            while not bool(re.search(PATTERN_DATETIME, last_line_str)):
                file.seek(-len(last_line_str) - 2, os.SEEK_CUR)  # Volta no arquivo
                count = 0
                while True:
                    byte = file.read(1)
                    if byte == b"\n" or not byte:  # Até encontrar o fim da linha ou EOF
                        break
                    file.seek(-2, os.SEEK_CUR)  # Volta sobre o byte lido e mais um
                    count += 1
                last_line_str = file.read(count).decode()  # Decodifica para string

            return last_line_str
        except OSError:
            file.seek(0)
            raise OSError(f"KeystrokeFile.read_last_line(): falha ao tratar arquivo {self.path + self.name}")

    def extract_datetime(self, line: str) -> datetime:
        date_str = KeystrokesFile.extract_date(line)
        time_str = KeystrokesFile.extract_time(line)
        datetime_str = date_str + " " + time_str
        try:
            if time_str[-1] == "Z":
                # for debugging: print(datetime_str[:-1])       # debug
                _datetime = datetime.fromisoformat(datetime_str[:-1])
            else:
                # for debugging: print(datetime_str, " <<<<<<<< dummy_datetime") # debug
                _datetime = self.dummy_datetime
        except ValueError:
            print(f"Exceção em KeystrokesFile.extract_datetime(): {ValueError}")
            print(f"KeystrokesFile: {str(self.path)}, id: {str(self.id)}, _datetime: {datetime_str.__str__()}")
        except UnboundLocalError:
            print(f"Exceção em KeystrokesFile.extract_datetime(): {UnboundLocalError}")
            print(f"KeystrokesFile: {str(self.path)}, id: {str(self.id)}, _datetime: {datetime_str.__str__()}")
        return _datetime

    # @staticmethod
    # def extract_date(line: str) -> str:
    #     PATTERN_DATE = r'\d+-\d+-\d+'
    #     date_lst = re.findall(PATTERN_DATE, line)
    #     if date_lst:
    #         date_str = date_lst[0]
    #         date_str = date_str + " "  # Espaço em branco ajuda em insert_zeros_in_date().
    #         date_str = KeystrokesFile.insert_zeros_in_date(date_str)
    #     else:
    #         date_str = '2000-01-01'
    #     return date_str

    @staticmethod
    def extract_date(line: str) -> str:
        PATTERN_DATE = r'\d+-\d+-\d+'
        date_lst = re.findall(PATTERN_DATE, line)
        if date_lst:
            date_str = date_lst[0]
            # O teste abaixo serve cobrir casos excepcionais quando date_str já vem
            # com mm e dd contendo zero à esquerda. Exemplo: 2020-01-2, 2021-4-09, 2022-03-05, etc.
            if len(date_str) < len("aaaa-mm-dd"):
                date_str = date_str + " "  # Espaço em branco ajuda em insert_zeros_in_date().
                date_str = KeystrokesFile.insert_zeros_in_date(date_str)
        else:
            date_str = '2000-01-01'
        return date_str

    # @staticmethod
    # def extract_time(line: str) -> str:
    #     PATTERN_TIME = r'\d+:\d+:\d+\.\d+#'
    #     time_lst = re.findall(PATTERN_TIME, line)
    #     if time_lst:
    #         time_str = time_lst[0][:-1]     # [:-1] elimina o "#" no final da string
    #     else:
    #         time_str = '00:00:00.000'
    #     return time_str

    @staticmethod
    def extract_time(line: str) -> str:
        #PATTERN_TIME = r'\d+:\d+:\d+\.\d+#'
        PATTERN_TIME = r'\d+:\d+:\d+\.\d+Z'
        time_lst = re.findall(PATTERN_TIME, line)
        if time_lst:
            time_str = time_lst[0]
        else:
            time_str = '00:00:00.000'
        return time_str

    @staticmethod
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

    @property
    def datetime_start(self):
        return self._datetime_start

    @datetime_start.setter
    def datetime_start(self, datetime_start: str):
        self._datetime_start = datetime_start

    @property
    def datetime_end(self):
        return self._datetime_end

    @datetime_end.setter
    def datetime_end(self, datetime_end: str):
        self._datetime_end = datetime_end

    @property
    def dummy_datetime(self):
        return self._dummy_datetime

    @dummy_datetime.setter
    def dummy_datetime(self, dummy_datetime: str):
        self._dummy_datetime = dummy_datetime
