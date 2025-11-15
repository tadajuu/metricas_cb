from os import listdir
import os.path
from online_judge.File import File
from online_judge.CodeFile import CodeFile
from online_judge.KeystrokesFile import KeystrokesFile
from online_judge.ExecutionsFile import ExecutionsFile
from online_judge.GradesFile import GradesFile
from online_judge.LoginFile import LoginFile
import online_judge

__author__ = 'Flávio José Mendes Coelho'


class User:

    def __init__(self, user_id: str, class_path: str):
        self.user_id = user_id
        self.user_path: str = class_path + "/" + self.user_id
        self.codefiles_path: str = self.user_path + "/codes" + "/"
        self.keystrokesfiles_path: str = self.user_path + "/codemirror" + "/"
        self.executionsfiles_path: str = self.user_path + "/executions" + "/"
        self.gradesfiles_path: str = self.user_path + "/grades" + "/"
        self.loginfiles_path: str = self.user_path
        self.loginfiles: dict = self._load_loginfiles_association()
        self.codefiles, self.keystrokesfiles, self.executionsfiles, self.is_consistent = self._load_same_id_associations()
        # self.is_consistent: bool = self._update_consistency()

    def _load_gradesfiles_association(self) -> dict:
        if os.path.exists(self.gradesfiles_path):
            executionsfile_file_names = [f for f in listdir(self.executionsfiles_path) if f.endswith(".log")]
            gradesfiles = {}
            previous_gradesfile_id = ""
            for executionsfile_file_name in executionsfile_file_names:
                gradesfile_id = GradesFile.extract_id(executionsfile_file_name)
                if gradesfile_id != previous_gradesfile_id:
                    gradesfile_name = gradesfile_id + ".log"
                    gradesfile = GradesFile(gradesfile_name, self.gradesfiles_path)
                    gradesfiles[gradesfile_id] = gradesfile
                    previous_gradesfile_id = gradesfile_id
        else:
            raise FileExistsError(f"User._load_gradesfiles_association(): "
                                  f"Diretório {self.gradesfiles_path} não encontrado")
        return gradesfiles

    def _load_loginfiles_association(self):
        file_name = "logins.log"
        loginfiles = {}
        try:
            with open(self.loginfiles_path + "/" + file_name, 'r') as fr:
                lines = fr.readlines()
                for line in lines:
                    date_time = line[0:19]
                    loginfile = LoginFile(date_time, file_name, self.loginfiles_path)
                    if line.endswith("login.\n"):
                        loginfile.set_status_to_login()
                    elif line.endswith("logout.\n"):
                        loginfile.set_status_to_logout()
                    loginfiles[date_time] = loginfile
            fr.close()
        except (OSError, FileNotFoundError, PermissionError):
            print(f"User._load_loginfiles_association(): Erro ao manipular o arquivo "
                  f"{self.loginfiles_path + file_name}.")
        finally:
            return loginfiles

    def _load_same_id_associations(self) -> tuple[dict, dict, dict]:
        codefile_names = self._try_load_codefile_names()
        keystrokesfile_names = self._try_load_keystrokesfile_names()
        executionsfile_names = self._try_load_executionsfile_names()

        file_ids_union = self._get_union_set_from_ids(codefile_names, keystrokesfile_names, executionsfile_names)
        file_ids: list = list(file_ids_union)
        file_ids.sort()

        codefiles = {}
        keystrokesfiles = {}
        executionsfiles = {}
        user_consistency = False
        for file_id in file_ids:
            codefile_name = file_id + ".py"
            exercise_have_initial_code = online_judge.LUT_EWSC.exercise_have_start_code(file_id)
            codefile = CodeFile(codefile_name, self.codefiles_path, exercise_have_initial_code)
            codefiles[file_id] = codefile

            keystrokesfile_name = file_id + ".log"
            keystrokesfile = KeystrokesFile(keystrokesfile_name, self.keystrokesfiles_path)
            keystrokesfiles[file_id] = keystrokesfile

            executionsfile_name = file_id + ".log"
            executionsfile = ExecutionsFile(executionsfile_name, self.executionsfiles_path)
            executionsfiles[file_id] = executionsfile

            user_consistency = codefile.is_consistent and keystrokesfile.is_consistent and executionsfile.is_consistent
            # if file_id == "4447_1366":
            #     print("codefile.is_consistent", codefile.is_consistent)
            #     print("keystrokesfile.is_consistent", keystrokesfile.is_consistent)
            #     print("executionsfile.is_consistent", executionsfile.is_consistent)
            #     print("exercise_have_initial_code", exercise_have_initial_code)
            # files_consistency = codefile.is_consistent and keystrokesfile.is_consistent and executionsfile.is_consistent
            # if user_consistency:
            #     user_consistency = files_consistency

        return codefiles, keystrokesfiles, executionsfiles, user_consistency

    def _try_load_codefile_names(self) -> list:
        codefile_names = []
        if os.path.exists(self.codefiles_path):
            codefile_names = [f for f in listdir(self.codefiles_path) if f.endswith(".py")]
        else:
            raise FileExistsError(f"User._try_load_keystrokesfile_names(): Diretório {self.codefiles_path} "
                                  f"não encontrado")
        return codefile_names

    def _try_load_keystrokesfile_names(self) -> list:
        keystrokesfile_names = []
        if os.path.exists(self.keystrokesfiles_path):
            keystrokesfile_names = [f for f in listdir(self.keystrokesfiles_path) if f.endswith(".log")]
        else:
            raise FileExistsError(f"User._try_load_keystrokesfile_names(): Diretório {self.keystrokesfiles_path} "
                                  f"não encontrado")
        return keystrokesfile_names

    def _try_load_executionsfile_names(self) -> list:
        executionsfile_names = []
        if os.path.exists(self.keystrokesfiles_path):
            executionsfile_names = [f for f in listdir(self.executionsfiles_path) if f.endswith(".log")]
        else:
            raise FileExistsError(f"User._try_load_keystrokesfile_names(): Diretório {self.keystrokesfiles_path} "
                                  f"não encontrado")
        return executionsfile_names

    def _get_union_set_from_ids(self, codefile_names: list, keystrokesfile_names: list,
                                executionsfile_names: list) -> set:
        """
        As instâncias de KeystrokesFile, CodeFile e ExecutionFile possuem o mesmo id, que é o nome do arquivo
        sem a extensão do arquivo. Como podem ocorrer inconsistências, isto é, um certo arquivo de código existir,
        mas seu correspondente de keystrokes não, estou juntando todos os ids em um conjunto união. Os objetos são
        instanciados a partir desse conjunto. Isso ajuda a criar de forma correta os objetos relativos a esses ids
        cobrindo os casos em que o arquivo não existe no diretório correspondente. Neste caso (ausência do arquivo),
        posteriormente, o objeto é setado com is_consistent = False.
        """
        # Remove extensões e põe resultados em conjuntos
        codefile_ids: set = set(map(File.extract_id, codefile_names))
        keystrokesfile_ids: set = set(map(File.extract_id, keystrokesfile_names))
        executionsfile_ids: set = set(map(File.extract_id, executionsfile_names))

        # A união dos conjuntos de ids
        file_ids_union = set().union(codefile_ids, keystrokesfile_ids, executionsfile_ids)
        return file_ids_union

    # def _update_consistency(self) -> bool:
    #     consistency = False
    #     for codefile, keystrokesfile, executionsfile in zip(self.codefiles.values(),
    #                                                         self.keystrokesfiles.values(),
    #                                                         self.executionsfiles.values()):
    #         if codefile.id == keystrokesfile.id and keystrokesfile.id == executionsfile.id:
    #             consistency = codefile.is_consistent and keystrokesfile.is_consistent and executionsfile.is_consistent
    #             if not consistency:
    #                 break
    #         else:
    #             raise ValueError(f"User._update_consistency(): desigualdade encontrada entre ids de CodeFile, "
    #                              f"KeystrokesFile e ExecutionsFile")
    #     return consistency

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        self._user_id = user_id

    @property
    def user_path(self):
        return self._user_path

    @user_path.setter
    def user_path(self, user_path: str):
        self._user_path = user_path

    @property
    def codefiles(self) -> dict:
        return self._codefiles

    @codefiles.setter
    def codefiles(self, codefiles: dict):
        self._codefiles = codefiles

    @property
    def keystrokesfiles(self) -> dict:
        return self._keystrokesfiles

    @keystrokesfiles.setter
    def keystrokesfiles(self, keystrokesfiles: dict):
        self._keystrokesfiles = keystrokesfiles

    @property
    def executionsfiles(self) -> dict:
        return self._executionsfiles

    @executionsfiles.setter
    def executionsfiles(self, executionsfiles: dict):
        self._executionsfiles = executionsfiles

    @property
    def is_consistent(self):
        return self._is_consistent

    @is_consistent.setter
    def is_consistent(self, is_consistent: bool):
        self._is_consistent = is_consistent

    # @property
    # def LUT_ewic():
    #     return _LUT_ewic
    #
    # @LUT_ewic.setter
    # def LUT_ewic(__LUT_ewic: LUT_ExercisesWithoutInitialCode):
    #     _LUT_ewic = __LUT_ewic

