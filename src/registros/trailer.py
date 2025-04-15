class Trailler():
    def __init__(self):
        self._identificacao_registro = 9                 # N # (001) - Identificação do arquivo
        self._quantidadeRegistro = ''                    # N # (002-007) - Quantidade de registros do arquivo (incluindo todos os headers, transacoes e o proprio trailer)
        self._valorTotal = ''                            # N # (008-024) - Valor total do arquivo (somatório dos valores de todas as transações)
        self._reserva = ''                               # A # (025-494) - Brancos
        self._numeroSequencial = ''                      # N # (495-500) - Número sequencial do registro (constant)
