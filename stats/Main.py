from stats.Correlations import Correlations

_author_ = 'Flávio José Mendes Coelho'


def main():
    print("Processando relatórios de Correlações...")
    corr = Correlations()
    # Antes de executas as próximas duas linhas:
    # 1. Execute main.Main (do package main) para gerar os REPORTs das métricas (pelo menos para LSA).
    # 2. Execute as próximas duas linhas somente uma vez e depois comente. Toda vez que você executar o passo 1,
    # execute este passo 2.
    corr.create_SUMARY_METRICS_CSV()
    corr.add_grade_TP_means_columns()
    corr.process_Pearson_correlations_matplot1()


if __name__ == '__main__':
    main()