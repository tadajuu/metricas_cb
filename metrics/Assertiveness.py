import re
from metrics.Metric import Metric
from online_judge.CodeFile import CodeFile
from online_judge.KeystrokesFile import KeystrokesFile
from online_judge.ExecutionsFile import ExecutionsFile

class Assertiveness(Metric):
    """
    @auhor: Flávio José Mendes Coelho.
    @date: 27/01/2023.
    Calcula a métrica da assertividade, obtida por
                            assertividade = count_chars / count_keystrokes.
    A variável count_chars é o número de caracteres da versão final do código fonte.
    A variável count_keystrokes é o número de keystrokes registradas na IDE do Codebench, durante uma ou mais sessões
    de codificação de um exercício ou prova.
    Ao se avaliar um único arquivo de código, o valor da assertividade deve variar dentro do intervalo
    0.0 < assertividade <= 1.0. Nesse caso, uma assertividade igual
    a zero indica que o aluno não acertou 100% dos casos de teste. Uma assertividade maior que 1.0, indica que há
    menos keystrokes registrados do que o esperado, pois deveria ser verdade que count_chars <= count_keystrokes.
    Para verificar esses casos, criamos um certificador (certifier) que indica se o cálculo da assertividade pode
    ou não ser feito com consistência, a partir dos arquivos fornecidos. O certificador assume os seguintes valores:
    < 0.0: cálculo da assertividade teria inconsistência, pois houve mais deleções do que keystrokes na codificação;
           pode indicar erro na coleta de dados do CodeBench.
    = 0.0: aluno não alcançou êxito em 100% dos casos de teste.
    0.0 < certifier < 1.0: provável erro na coleta dos dados; faltam alguns keystrokes esperados.
    = 1.0: o total de keystrokes menos o total de deleções no arquivo de log resulta no tamanho do arquivo fonte.
           Nesse caso, considera-se que a contagem de keystrokes está correta e a assertividade pode ser calculada.
    > 1.0: provável erro na coleta dos dados; faltam alguns keystrokes esperados ou deleções.
    A assertividade para um arquivo de código somente é calculada quando certificador = 1.0.

    Para avaliar a assertividade de um trabalho (lista de problemas que pode ser um homework ou um exam),
    utilizamos:
                assertividade = total de count_chars do trabalho / total de count_keystrokes do trabalho.
    Nesse caso, o certificador pode ser igual a 0.0, ou seja, admitimos que o aluno não tenha e obtido 100% de sucesso
    nos casos de teste, em alguns arquivos de código do trabalho. Porém, a assertividade de um trabalho é calculada
    fora desta classe, em um relatório que navegue pelos trabalhos e seus exercícios. Esta classe, então, fornece
    para um dado arquivo de código, os valores de count_chars e count_keystrokes que serão acumulados e utilizados
    para o cálculo da assertividade do trabalho.
    """

    def __init__(self):
        self.count_keystrokes_adds = 0
        self.count_keystrokes_dels = 0
        self.certifier = None
        self._value = 0.0
        self._cnt_chars = 0
        self._cnt_keystrokes = 0
        self.has_files_consistents: bool = False
        self.has_passed_all_CTs: bool = False
        self.strength: bool = self.has_passed_all_CTs
        self.MAX_ASSERTIVENESS = 1.0

    def calculate_strong_weak(self, codefile: CodeFile, keystrokesfile: KeystrokesFile, executionsfile: ExecutionsFile) -> None:
        """
        Realiza o cálculo da assertividade.
        # :param strength: true, exige 100% de sucessos nos CTS; false, admite menos que 100% de sucessos nos CTs.
        :param codefile: arquivo do código fonte do programador.
        :param keystrokesfile: arquivo de log com o registro de keystrokes e todos os eventos registrados durante
         uma ou mais sessões de codificação de um exercício ou prova no Codebench.
        :param executionsfile: arquivo que registra ações de submissão do código, testes no console e casos de
         test
        :return: None
        """

        self.has_files_consistents = codefile.is_consistent and keystrokesfile.is_consistent \
            and executionsfile.is_consistent

        # if self.has_files_consistents and self.has_passed_all_CTs:
        # if self.has_files_consistents:

        self.cnt_chars: int = 0
        if codefile.is_consistent:
            self.cnt_chars: int = self._count_chars(codefile)

        self.cnt_keystrokes: int = 0
        self.count_keystrokes_adds: int = 0
        self.count_keystrokes_dels: int = 0
        difference = 0
        if keystrokesfile.is_consistent:
            keystrokes_fields = self._prepare_keystrokes_fields(keystrokesfile)
            self.count_keystrokes_adds, self.count_keystrokes_dels = self._count_keystrokes_adds_dels(keystrokes_fields)
            difference = self.count_keystrokes_adds - self.count_keystrokes_dels

        self.certifier = 0.0
        self.value: float = 0.0
        if difference > 0:
            self.cnt_keystrokes = self.count_keystrokes_adds
            self.certifier = self.cnt_chars / difference
            self.has_passed_all_CTs = self._has_code_passed_all_CTs(executionsfile)
            self.strength = self.has_passed_all_CTs and 0.7 <= self.certifier <= 1.3
            if 0.7 <= self.certifier <= 1.3:
                self.value = self.cnt_chars / self.cnt_keystrokes

    def calculate(self, codefile: CodeFile, keystrokesfile: KeystrokesFile, executionsfile: ExecutionsFile) -> None:
        """
        Realiza o cálculo da assertividade.
        # :param strength: true, exige 100% de sucessos nos CTS; false, admite menos que 100% de sucessos nos CTs.
        :param codefile: arquivo do código fonte do programador.
        :param keystrokesfile: arquivo de log com o registro de keystrokes e todos os eventos registrados durante
         uma ou mais sessões de codificação de um exercício ou prova no Codebench.
        :param executionsfile: arquivo que registra ações de submissão do código, testes no console e casos de
         test
        :return: None
        """

        self.has_files_consistents = codefile.is_consistent and keystrokesfile.is_consistent \
            and executionsfile.is_consistent

        # if self.has_files_consistents and self.has_passed_all_CTs:
        # if self.has_files_consistents:

        self.cnt_chars: int = 0
        if codefile.is_consistent:
            self.cnt_chars: int = self._count_chars(codefile)

        self.cnt_keystrokes: int = 0
        self.count_keystrokes_adds: int = 0
        self.count_keystrokes_dels: int = 0
        difference = 0
        if keystrokesfile.is_consistent:
            keystrokes_fields = self._prepare_keystrokes_fields(keystrokesfile)
            self.count_keystrokes_adds, self.count_keystrokes_dels = self._count_keystrokes_adds_dels(keystrokes_fields)
            difference = self.count_keystrokes_adds - self.count_keystrokes_dels

        self.certifier = 0.0
        self.value: float = 0.0
        if difference > 0:
            self.cnt_keystrokes = self.count_keystrokes_adds
            self.certifier = self.cnt_chars / difference
            self.has_passed_all_CTs = self._has_code_passed_all_CTs(executionsfile)
            self.strength = self.has_passed_all_CTs and 0.7 <= self.certifier <= 1.3
            if self.strength:
                self.value = self.cnt_chars / self.cnt_keystrokes
                if self.value > self.MAX_ASSERTIVENESS:
                    self.value = self.MAX_ASSERTIVENESS

    def _has_code_passed_all_CTs(self, executionsfile: ExecutionsFile) -> bool:
        """
        O cálculo da assertividade pressupões que o programador obteve êxito em 100% dos casos de testes (CTs).
        Este método verifica essa pré-condição para o cálculo.
        :param executionsfile: é o arquivo que registra ações submissão do código a testes no console e a casos de
         teste.
        :return: True se o código passou em 100% dos CTs e False em caso contrário.
        """
        return executionsfile.has_code_passed_all_CTs()

    def _count_chars(self, codefile: CodeFile) -> int:
        """
        Retorna a quantidade de caracteres no código fonte.
        :param codefile: é o arquivo do código fonte.
        :return: inteiro representando a quantidade de caracteres no arquivo do código fonte.
        """
        codefile.load_text()
        # Por enquanto, não removerei as linhas de comentários do código. Elas contarão no cálculo da assertividade,
        # pois se o programador consume muito tempo comentando o código, isso é um indício de que
        # o código não se explica por si (ver livro Clean Code), o que seria um sinal de baixa assertividade.
        # codefile_text_no_comment_lines: str = self._delete_comment_lines(codefile.text)
        # length_text: int = len(codefile_text_no_comment_lines)
        length_text: int = len(codefile.text)
        return length_text

    def _delete_comment_lines(self, codefile_text: str) -> str:
        """
        Deleta as linhas de comentários. Linhas com comentários em final de linha não são deletadas.
        Minha versão não está reconstruindo as linhas corretamente. Possivelmente, vou ajustar/reultizar o código
        da fonte abaixo. Mas, enquanto ele lê o arquivo, eu já pego o texto pronto
        pelo parâmetro do método.
        Fontes:
        "Write a program to delete comment lines from a file in Python"
        by Rajkumar BhattacharyaFebruary 28, 2022
        https://www.codingconception.com/python-examples/write-a-program-to-delete-comment-lines-from-a-file-in-python/
        reading the file
        :param codefile_text: texto contendo várias linhas.
        :return: texto sem linhas de comentários.
        """
        # Meu método
        # new_text = ""
        # for line in codefile_text.splitlines():
        #     if not (line.startswith("#") or line.startswith(" #")
        #             or line.startswith("  #") or line.startswith("   #")
        #             or line.startswith("    #") or line.startswith("\t#")):
        #         new_text = new_text + line + "\n"
        # return new_text[:-1]  # retira o último "\n" inserido
        # --------------------------------------------------------------------------
        # Método das fontes abaixo:
        # Fonte:
        # "Write a program to delete comment lines from a file in Python"
        # by Rajkumar BhattacharyaFebruary 28, 2022
        # https://www.codingconception.com/python-examples/write-a-program-to-delete-comment-lines-from-a-file-in-python/
        # reading the file
        # with open("oldfile.py") as fp:
        #     contents = fp.readlines()
        # # initialize two counter to check mismatch between "(" and ")"
        # open_bracket_counter = 0
        # close_bracket_counter = 0
        # # whenever an element deleted from the list length of the list will be decreased
        # decreasing_counter = 0
        # for number in range(len(contents)):
        #     # checking if the line contains "#" or not
        #     if "#" in contents[number - decreasing_counter]:
        #         # delete the line if startswith "#"
        #         if contents[number - decreasing_counter].startswith("#"):
        #             contents.remove(contents[number - decreasing_counter])
        #             decreasing_counter += 1
        #         # delete the character after the "#"
        #         else:
        #             newline = ""
        #             for character in contents[number - decreasing_counter]:
        #                 if character == "(":
        #                     open_bracket_counter += 1
        #                     newline += character
        #                 elif character == ")":
        #                     close_bracket_counter += 1
        #                     newline += character
        #                 elif character == "#" and open_bracket_counter == close_bracket_counter:
        #                     break
        #                 else:
        #                     newline += character
        #             contents.remove(contents[number - decreasing_counter])
        #             contents.insert(number - decreasing_counter, newline)
        # return contents
        pass

    def _prepare_keystrokes_fields(self, keystrokesfile: KeystrokesFile) -> list[dict]:
        """
        Prepara os campos de keystrokes que vem dos registros do arquivo de keystrokes (log) e retorna uma lista
        em que cada item é um dicionários na forma:
        ItemDict = {'text': textfield_value, 'removed': removedfield_value, 'origin': originfield_value}
        :param keystrokesfile: é o arquivo de log com o registro de keystrokes e todos os eventos registrados durante
         uma ou mais sessões de codificação de um exercício ou prova no Codebench.
        :return: lista de ItemDict.
        """
        PATTERN_TEXTFIELD_REMOVEDFIELD_ORIGINFIELD = '\"text\":\[\".*\"\],\"removed\":\[\".*\"\],\"origin\":.*\"'
        keystrokesfile.load_text()
        dirty_keystrokes: list = re.findall(PATTERN_TEXTFIELD_REMOVEDFIELD_ORIGINFIELD, keystrokesfile.text)
        keystrokes_fields: list[dict] = self._extract_keystrokes_fields(dirty_keystrokes)
        return keystrokes_fields

    def _extract_keystrokes_fields(self, dirty_keystrokes: list) -> list[dict]:
        """
        Extrai da lista dirty_keystrokes, registros com os campos 'text', 'removed' e 'origin' e seus respectivos
        valores (teclas pressionadas) e coloca cada registro em uma lista em que cada item é um dicionários na forma:
        ItemDict = {'text': textfield_value, 'removed': removedfield_value, 'origin': originfield_value}
        :param dirty_keystrokes: lista de registros (strings) de keystrokes.
        :return: lista de ItemDict.
        """
        keystrokes_fields = []
        for line in dirty_keystrokes:
            textfield_value = self._extract_textfield_value(line)
            removedfield_value = self._extract_removedfield_value(line)
            originfield_value = self._extract_originfield_value(line)

            # Elimina aspas dos extremos
            textfield_value = textfield_value[1:-1]
            removedfield_value = removedfield_value[1:-1]
            originfield_value = originfield_value[1:-1]

            dict_log = {'text': textfield_value, 'removed': removedfield_value, 'origin': originfield_value}
            keystrokes_fields.append(dict_log)
        return keystrokes_fields

    def _extract_textfield_value(self, line: str) -> str:
        """
        Extrai o valor do campo 'text' da string line.
        :param line: uma string contendo o campo 'text' e seu valor (uma ou mais keystrokes).
        :return: string com keystrokes.
        """
        PATTERN_TEXTFIELD = '\"text\":.*\"\],"r'
        dirty_textfield = re.findall(PATTERN_TEXTFIELD, line)
        textfield = dirty_textfield[0][0:len(dirty_textfield[0]) - 3]
        PATTERN_BRACKETS = '\[.*\]'
        dirty_textfield_value = re.findall(PATTERN_BRACKETS, textfield)
        textfield_value = dirty_textfield_value[0][1:-1]
        return textfield_value

    def _extract_removedfield_value(self, line: str) -> str:
        """
        Extrai o valor do campo 'removed' da string line.
        :param line: uma string contendo o campo 'removed' e seu valor (uma ou mais keystrokes).
        :return: string com keystrokes.
        """
        PATTERN_REMOVEDFIELD = '"removed\":\[.*\"\],\"o'
        dirty_removedfield = re.findall(PATTERN_REMOVEDFIELD, line)
        removedfield = dirty_removedfield[0][0:len(dirty_removedfield[0]) - 3]
        PATTERN_BRACKETS = '\[.*\]'
        dirty_removedfield_value = re.findall(PATTERN_BRACKETS, removedfield)
        removedfield_value = dirty_removedfield_value[0][1:-1]
        return removedfield_value

    def _extract_originfield_value(self, line: str) -> str:
        """
        Extrai o valor do campo 'origin' da string line.
        :param line: uma string contendo o campo 'origin' e seu valor ("+input", "paste", "undo", "delete", etc).
        :return: string um valor do campo 'origin'.
        """
        PATTERN_ORIGINFIELD = '"origin\":.*\"'
        dirty_originfield = re.findall(PATTERN_ORIGINFIELD, line)
        originfield = dirty_originfield[0]
        PATTERN_ORIGINFIELD_VALUE = ':.*'
        dirty_originfield_value = re.findall(PATTERN_ORIGINFIELD_VALUE, originfield)
        originfield_value = dirty_originfield_value[0][1:]
        return originfield_value

    def _count_keystrokes_adds_dels(self, keystrokes_fields: list) -> tuple[int, int]:
        """
        Conta quantos keystrokes foram adicionados e quantos foram deletados e retorna essas contagens.
        :param keystrokes_fields: uma lista de em que cada item é um dicionários na forma:
        ItemDict = {'text': textfield_value, 'removed': removedfield_value, 'origin': originfield_value}
        :return: tupla com keystrokes adicionadas e keystrokes deletadas.
        """
        especial_chars = {'single_quote': '\\"', 'enter': '","', 'tab': ' ', 'delete': '""'}
        count_adds = 0
        count_dels = 0
        for keystrokes_field in keystrokes_fields:
            text_field = keystrokes_field['text']
            removed_field = keystrokes_field['removed']

            text_field_modified = ""
            removed_field_modified = ""
            if text_field != "":
                text_field_modified = self._prepare_field_for_counting(text_field, especial_chars)
            if removed_field != "":
                removed_field_modified = self._prepare_field_for_counting(removed_field, especial_chars)

            count_adds += len(text_field_modified)
            count_dels += len(removed_field_modified)

        # count_ks: int = count_adds - count_dels
        return count_adds, count_dels

    def _prepare_field_for_counting(self, field: str, especial_chars: dict) -> str:
        """
        Substitui caracteres especiais da string field (tabs, aspas e enter) para "?".
        :param field: string com o valor de um campo de ItemDict.
        :return: field com "?" em lugar de caracteres especiais.
        """
        if field == especial_chars['delete']:
            field = ''
        else:
            if len(re.findall(especial_chars['enter'], field)) >= 1:
                field = field.replace(especial_chars['enter'], '?')

            # if bool(re.search(especial_chars['tab'], field)):
            #     field = field.replace(especial_chars['tab'], '?')

            if self._exists_tab_chars(field):
                field = self._replace_tab_chars(field)

            # if bool(re.search(especial_chars['quotation_marks'], '"' + field + '"')):
            # if bool(re.search(especial_chars['quotation_marks'], field)):
            #     field = field.replace(especial_chars['quotation_marks'], '??')

            if bool(re.search(especial_chars['single_quote'], field)):
                field = field.replace(especial_chars['single_quote'], '?')
        return field

    def _replace_tab_chars(self, original_text: str) -> str:
        """
        Implementa um PDA com as operações de remoção/adição de caracteres para construir a string
        de saída, text_out.
        Este PDA é necessário porque o caractere TAB "\\t" não é reconhecido de forma atômica na string de entrada,
        mas de forma separada, ou seja, text[k] = "\\" e text[k+1] = "t". E há também o TAB "\t".
        test_inputs = ["\t", "\\t", "\\\t", "\\", "\\\\", "\\\\t", "\t\t", "\t\\t", "\\t\t", "\t\t\t", "\\t\t\\t",
                       "\\\t\t", "a", "aaaa", "aaa\taaa", "aaa\\taaa", "aaa\\t\\taaa", "aaa\\t\taaa", "aaa\t\\taaa",
                       "aaa\t", "aaaaa\\t", "aaaaaa\t\t", "aaaaaaa\\t\\t", "aaaaa\\t\t\\t", "aaa\\taaa\taaa",
                       "aaa\taaa\\taaa", "aaa\\taaa\\taaa", "aaa\taaa\taaa", "\\\aaaa\\taaaaaa\\taaaaaa\\ta",
                       "\\\aaaa\\aaa	aaataaaaaa\\a", "    ", "	\t"]
        :param original_text: string contendo ocorrências de TABs ("\\t" ou "\t").
        :return: text_out: cópia de original_text, porém, com todas as ocorrências de TABs trocadas por "?".
        """
        pda = {('q0', "\\"): ('q1', "", "\\"),
               ('q0', "t"): ('q3', "", "t"),
               ('q0', "$"): ('q3', "", "$"),
               ('q0', "\t"): ('q2', "", "?"),

               ('q1', "\\"): ('q1', "", "\\"),
               ('q1', "t"): ('q2', "\\", "?"),
               ('q1', "$"): ('q3', "", "$"),
               ('q1', "\t"): ('q2', "", "?"),

               ('q2', "\\"): ('q1', "", "\\"),
               ('q2', "t"): ('q3', "", "t"),
               ('q2', "$"): ('q3', "", "$"),
               ('q2', "\t"): ('q2', "", "?"),

               ('q3', "\\"): ('q1', "", "\\"),
               ('q3', "t"): ('q3', "", "t"),
               ('q3', "$"): ('q3', "", "$"),
               ('q3', "\t"): ('q2', "", "?")
               }
        initial_state = 'q0'
        ANY_CHAR_EXCEPT_SPECIAL_CHARS = "$"  # representa qualquer caracteres exceto "\\" e "t"
        SPECIAL_CHARS = ["\\", "t", "\t"]
        invisible_TAB = "    "
        if original_text == invisible_TAB:
            text = "\t"
        text = list(original_text)
        text_out = ""
        state = initial_state
        i: int = 0
        while i < len(text):
            if text[i] not in SPECIAL_CHARS:
                char = text[i]
                text[i] = ANY_CHAR_EXCEPT_SPECIAL_CHARS
            new_state, pop_symbol, push_symbol = pda[(state, text[i])]
            # print(state, "(", text[i], ")" , " -> ", new_state, accept)
            if pop_symbol != "":
                text_out = text_out[:-1]  # remove último e atribui
            if push_symbol == ANY_CHAR_EXCEPT_SPECIAL_CHARS:
                text_out += char
            else:
                text_out += push_symbol
            state = new_state
            i += 1
        return text_out

    def _exists_tab_chars(self, original_text: str) -> bool:
        """
        Implementa um DFA reconhecer o caractere TAB em um string. O TAB pode ser o carctere "\t" ou o caractere
        invisível que corresponde à "\t". Este DFA é necessário porque o caractere TAB "\\t" não é reconhecido
        de forma atômica na string de entrada, mas de forma separada, ou seja, text[k] = "\\" e text[k+1] = "t".
        Para testes:
        test_inputs = ["\t", "\\t", "\\\t", "\\", "\\\\", "\\\\t", "\t\t", "\t\\t", "\\t\t", "\t\t\t", "\\t\t\\t",
                       "\\\t\t", "a", "aaaa", "aaa\taaa", "aaa\\taaa", "aaa\\t\\taaa", "aaa\\t\taaa", "aaa\t\\taaa",
                       "aaa\t", "aaaaa\\t", "aaaaaa\t\t", "aaaaaaa\\t\\t", "aaaaa\\t\t\\t", "aaa\\taaa\taaa",
                       "aaa\taaa\\taaa", "aaa\\taaa\\taaa", "aaa\taaa\taaa",
                       "\\\	aaaa\\taaa	aaa\\ta	aaaaa		\\ta", "\\\aaaa\\aaa	aaataaaaaa\\a", "    ",
                       "	\t"]
        :param original_text: string contendo ocorrências de "\\t" ou o TAB invisível.
        :return: accetp: True se aceita, oiu False se não aceita a entrada no parâmetro original_text.
        """
        dfa = {('q0', "\\"): 'q1',
               ('q0', "t"): 'q3',
               ('q0', "$"): 'q3',
               ('q0', "\t"): 'q2',

               ('q1', "\\"): 'q4',
               ('q1', "t"): 'q2',
               ('q1', "$"): 'q3',
               ('q1', "\t"): 'q2',

               ('q2', "\\"): 'q2',
               ('q2', "t"): 'q2',
               ('q2', "$"): 'q2',
               ('q2', "\t"): 'q2',

               ('q3', "\\"): 'q1',
               ('q3', "t"): 'q3',
               ('q3', "$"): 'q3',
               ('q3', "\t"): 'q2',

               ('q4', "\\"): 'q1',
               ('q4', "t"): 'q2',
               ('q4', "$"): 'q3',
               ('q4', "\t"): 'q2'
               }
        accept_state = 'q2'
        initial_state = 'q0'
        state = initial_state
        ANY_CHAR_EXCEPT_SPECIAL_CHARS = "$"  # representa qualquer caracteres exceto "\\" e "t"
        SPECIAL_CHARS = ["\\", "t", "\t"]
        invisible_TAB = "    "
        if original_text == invisible_TAB:  # caso especial quando a entrada só tem um TAB invisível.
            text = "\t"
        text = list(original_text)
        i: int = 0
        accept = False
        while i < len(text):
            if text[i] not in SPECIAL_CHARS:
                text[i] = ANY_CHAR_EXCEPT_SPECIAL_CHARS
            state = dfa[(state, text[i])]
            if state == accept_state:
                accept = True
                break
            i += 1
        return accept

    # Propriedades e setters
    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value

    @property
    def cnt_chars(self) -> int:
        return self._cnt_chars

    @cnt_chars.setter
    def cnt_chars(self, cnt_chars: int):
        self._cnt_chars = cnt_chars

    @property
    def cnt_keystrokes(self) -> int:
        return self._cnt_keystrokes

    @cnt_keystrokes.setter
    def cnt_keystrokes(self, cnt_keystrokes: int):
        self._cnt_keystrokes = cnt_keystrokes

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
