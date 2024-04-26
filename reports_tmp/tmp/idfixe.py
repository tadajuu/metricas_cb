import json
import os

ASSERTIV = None
LOGIC = None
SINTAXE = None
WCH = None
READINESS = None

DICT_AUX = None

path = '../reports/'
file_name1 = 'RELATION_ID_TYPE.json'
if os.path.exists(path + file_name1):
    with open(path + file_name1, 'r',  encoding='utf-8') as arquivo:
        DICT_AUX = json.load(arquivo)
else:
    print(f"Arquivo {path + file_name1} não encontrado")

file_name2 = 'ASSERTIV_ASSESSMENTS.json'
if os.path.exists(path + file_name2):
    with open(path + file_name2, 'r',  encoding='utf-8') as arquivo:
        ASSERTIV = json.load(arquivo)
else:
    print(f"Arquivo {path + file_name2} não encontrado")

file_name3 = 'LOGIC_ASSESSMENTS.json'
if os.path.exists(path + file_name3):
    with open(path + file_name3, 'r',  encoding='utf-8') as arquivo:
        LOGIC = json.load(arquivo)
else:
    print(f"Arquivo {path + file_name3} não encontrado")

file_name4 = 'SINTAXE_ASSESSMENTS.json'
if os.path.exists(path + file_name4):
    with open(path + file_name4, 'r',  encoding='utf-8') as arquivo:
        SINTAXE = json.load(arquivo)
else:
    print(f"Arquivo {path + file_name4} não encontrado")

file_name5 = 'WCH_ASSESSMENTS.json'
if os.path.exists(path + file_name5):
    with open(path + file_name5, 'r',  encoding='utf-8') as arquivo:
        WCH = json.load(arquivo)
else:
    print(f"Arquivo {path + file_name5} não encontrado")

file_name6 = 'READINESS_ASSESSMENTS.json'
if os.path.exists(path + file_name6):
    with open(path + file_name6, 'r',  encoding='utf-8') as arquivo:
        READINESS = json.load(arquivo)
else:
    print(f"Arquivo {path + file_name6} não encontrado")


def checkIsValidName(alias: str):
    alias = alias.upper()
    return "PRIMEIROS PASSOS" not in alias and "SIMULADO" not in alias and "EXTRA" not in alias and "DESAFIO" not in alias and "FINAL" not in alias and "ESPECIAl" not in alias


def GET_FIRST_ID_GROUP_LIST(dataset, fileOutput):
    NEW_ARR = []
    for obj in dataset:
        idTurma = str(obj["CLASS_ID"])
        nomeLab = obj["ASSESSMENT_TYPE"]
        idLabFixo = 0
        for listaName in DICT_AUX[idTurma]:
            if nomeLab in DICT_AUX[idTurma][listaName][0] and checkIsValidName(DICT_AUX[idTurma][listaName][1]):
                idLabFixo = listaName
                break

        obj["ASSESSMENTS_ID"] = int(idLabFixo)
        NEW_ARR.append(obj)
    with open(fileOutput, 'w', encoding='utf-8') as arquivo:
        json_formatado = json.dumps(NEW_ARR, ensure_ascii=False, indent=4)
        arquivo.write(json_formatado)


GET_FIRST_ID_GROUP_LIST(ASSERTIV, path + "ASSERTIV_ASSESSMENTS.json")
GET_FIRST_ID_GROUP_LIST(LOGIC, path + "LOGIC_ASSESSMENTS.json")
GET_FIRST_ID_GROUP_LIST(SINTAXE, path + "SINTAXE_ASSESSMENTS.json")
GET_FIRST_ID_GROUP_LIST(WCH, path + "WCH_ASSESSMENTS.json")
GET_FIRST_ID_GROUP_LIST(READINESS, path + "READINESS_ASSESSMENTS.json")