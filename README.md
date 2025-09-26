Para rodar o programa, você precisa de um dataset e de dois arquivos auxiliares

Os arquivos auxiliares são:
cache_notes -> um arquivo csv com cada nota de cada aluno para cada lista de exercícios
user_ids -> um arquivo de texto com os ids de todos os alunos do período 
coloque eles na pasta aux_files (lá já tem esses arquivos, mas pro dataset 2025-2; dá para aproveitar pra seguir o template na hora de fazer o do dataset que vai usar)

o dataset precisa estar dentro de um diretório chamado dataset. dê o nome do dataset da seguinte forma: "ano-periodo"
exemplo:
/dataset
  /2025-2

mude o path do dataset no arquivo /online_judge/codebench_dataset_path.txt e no arquivo /online_judge/__init__.py na variável classes_path (lá pela linha 558)

Para executar o cálculo das métricas, é só rodar o programa /main/main.py

Qualquer dúvida ou problema, entrar em contato: jeremiasvs2005@gmail.com
