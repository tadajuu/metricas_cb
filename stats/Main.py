from stats.Correlations import Correlations

__author__ = 'Flávio José Mendes Coelho'


def main():
    print("Processando relatórios de Correlações...")
    corr = Correlations()
    corr.create_SUMARY_METRICS_CSV()
    corr.add_grade_TP_means_columns()
    corr.process_Pearson_correlations_matplot1()


if __name__ == '__main__':
    main()
