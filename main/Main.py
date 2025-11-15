import online_judge.Helper
import subprocess
from online_judge.CodebenchLog import CodebenchLog
from main.GradeProcessor import GradeProcessor
from main.ReadinessProcessor import ReadinessProcessor
from main.AssertivenessProcessor import AssertivenessProcessor
from main.SyntaxProcessor import SyntaxProcessor
from main.LogicProcessor import LogicProcessor
from main.WCHProcessor import WeeklyCodingHoursProcessor
from datetime import datetime
from IRBO.IRBOProcessor import IRBOProcessor

__author__ = 'Flávio José Mendes Coelho'


def main():
    # dt_start_str = '2023-01-18 00:00:00.000'
    # dt_end_str = '2023-02-07 00:00:00.000'
    # dt_start = datetime.fromisoformat(dt_start_str)
    # dt_end = datetime.fromisoformat(dt_end_str)

    #esse está ok! unico erro foi de escrita, já que o usuario digitou com "ç" um código,
    # e o programa nao reconheceu!
    print("Processando relatórios de Domínio da Lógica...")
    LogicProc = LogicProcessor()
    LogicProc.process()

    print("Processando relatórios de Domínio da Sintaxe...")
    SyntaxProc = SyntaxProcessor()
    SyntaxProc.process()

    print("Processando relatórios de Assertividade...")
    assertivProc = AssertivenessProcessor()
    assertivProc.process()

    print("Processando relatórios de Grades...")
    gradeProc = GradeProcessor()
    gradeProc.process()

    #ID_USER, ID_ASSESSMENT, ID_CLASS, YEAR, SEMESTER, ASSESSMENT_DATE_START, GRADE
    #print("Processando valores IRBO...")
    #irbo_proc = IRBOProcessor()
    #irbo_proc.process()

    print("Processando relatórios sobre Horas Semanais de Codificação...")
    WCHProc = WeeklyCodingHoursProcessor()
    WCHProc.process()

    print("Processando relatórios sobre Presteza...")
    ReadinessProc = ReadinessProcessor()
    ReadinessProc.process()

    #print("Executando idfixe.py...")
    #path = "/Users/fcoelho/Documents/Dev/doutorado/cb-metrics/reports/"
    #subprocess.run(["python3", path + "idfixe.py"])


if __name__ == '__main__':
    main()
