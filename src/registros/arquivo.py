from .funcao import Funcao

class Arquivo(Funcao):
    def __init__(self):
        # Initialize attributes with default values
        self._identificacao = "1"                               # N # (001) - Identificação do arquivo
        self._tipoInscricao = "2"                               # N # (002) 2=CNPJ - Tipo de inscrição da empresa
        self._baseFornecedor = "055233019000684"                # N # (003-017) - CNPJ do fornecedor
        self._nomeFornecedor = "BRADESCO"                       # A # (018-047) - Nome do fornecedor #TODO - Ajustar para 30 caracteres with spaces
        self._enderecoFornecedor = ""                           # A # (048-087) - Endereço do fornecedor (BRANCO)
        self._cepFornecedor = "00000"                           # N # (088-092) - CEP do fornecedor (ZEROS)
        self._cepComplementoFornecedor = "000"                  # N # (093-095) - Complemento CEP do fornecedor (ZEROS)
        self._codigoBanco = "237"                               # N # (096-098) - Código do banco
        self._codigoAgencia = "03396"                           # N # (099-103) - Código da agência
        self._digitoAgencia = "0"                               # A # (104) - Dígito da agência
        self._contaCorrenteFornecedor = "0000000002202"         # N # (105-117) - Conta corrente do fornecedor
        self._digitoContaCorrente = "0 "                        # A # (118-119) - Dígito da conta corrente
        self._numeroPagamento = ""                              # A # (120-135) - Número do pagamento (RANDOM UNIQUE NUMBER GENERATOR)
        self._carteira = "000"                                  # N # (136-138) - Carteira do banco
        self._nossoNumero = "000000000000"                      # N # (139-150) - Obrigatorio
        self._seuNumero = ""                                    # A # (151-165) - Seu número titulo rastreado (BRANCO)
        self._dataVencimento = ""                               # N # (166-173) - Data de vencimento do título AAAAMMDD
        self._dataEmissaoDocumento = "00000000"                 # N # (174-181) - Data de emissão do documento AAAAMMDD
        self._dataLimiteDesconto = "00000000"                   # N # (182-189) - Data limite para desconto AAAAMMDD
        self._zeros = "0"                                       # N # (190) - Zeros
        self._fatorVencimento = "0000"                          # N # (191-194) - Fator de vencimento (Posição 6 a 9 do código de barras ou os 4 primeiros dígitos do 5º campo campo da linha digitavel, quando for diferente de 0)
        self._valorDocumento = ""                               # N # (195-204) - Valor do documento (Obrigatorio)
        self._valorPagamento = ""                               # N # (205-219) - Valor do pagamento (Deve ser igual o valor do documento, menos o valor de desconto ou mais Acréscimo, se houver)
        self._valorDesconto = "000000000000000"                 # N # (220-234) - Valor do desconto (Deve ser igual o valor do Pagamento, menos o valor do documento, exceto se o valor do documento for igual a zero)
        self._valorAcrescimo = "000000000000000"                # N # (235-249) - Valor do acréscimo (Deve ser igual o valor do pagamento, menos o valor do documento, exceto se o valor do documento for igual a zero)
        self._tipoDocumento = "05"                              # N # (250-251) - Tipo de documento (01=Nota Fiscal/Fatura, 02=Fatura, 03=Nota Fiscal, 04=Duplicatas, 05=Outros)
        self._numeroNotaFiscal = "0000000000"                   # N # (252-261) - Número da nota fiscal (se o campo anterior for 1 ou 3, este campo passa a aser numerico)
        self._serieDocumento = ""                               # A # (262-263) - Série do documento (se o campo anterior for 1 ou 3, este campo passa a aser numerico)(BRANCO)
        self._modalidadePagamento = "05"                        # N # (264-265) - Modalidade de pagamento (01=Crédito em c/c, 02=Cheque OP, 05=Crédito em c/c real time, 03=DOC COMPE, 08=TED, 30=Rastreamento de Títulos)
        self._dataEfetivacaoPagamento = ""                      # N # (266-273) - Data efetivação do pagamento AAAAMMDD
        self._moeda = ""                                        # A # (274-276) - Obrigatório fixo (BRANCO)
        self._situacaoAgendamento = "01"                        # N # (277-278) - Situacao de Agendamento Preencher com o código 01
        self._informaçãoRetorno = ""                            # A # (279-288) - Informação de retorno (Valido somente para o arquivo de retorno) (BRANCO)
        self._tipoMovimento = "0"                               # N # (289) - Tipo de movimento (0=Inclusão, 5=Alteração, 9=Exclusão)
        self._codigoMovimento = "00"                            # N # (290-291) - Código de movimento (00=Autoriza Agendamento, 25=Desautoriza Agendamento, 50=Efetuar Alegação)
        self._horarioConsultaSaldoRT = ""                       # A # (292-295) - Horário da consulta de saldo real time (02-Cheque OP, 05= Credito em conta real time, 08=TED)
        self._saldoDisponivel = ""                              # A # (296-310) - Saldo disponível (Valido somente para o arquivo de retorno)
        self._valorTaxaPreFunding = ""                          # A # (311-325) - Valor da taxa de pre-funding (Valido somente para o arquivo de retorno)
        self._reserva1 = ""                                     # A # (326-331) - Reservado para uso futuro (Brancos)
        self._sacadorAvalista = ""                              # A # (332-371) - Nome do sacador/avalista (Brancos) Somente para titulos de cobranca
        self._reserva2 = ""                                     # A # (372) - Reservado para uso futuro (Brancos)
        self._nivelInfoRetorno = ""                             # A # (373) - Nível de informação de retorno (Brancos)
        self._informacaoComplementar = ""                       # A # (374-413) - (Brancos)
        self._codigoAreaEmpresa = "01"                          # N # (414-415) - Código da área da empresa (Brancos)
        self._campoUsoEmpresa = ""                              # A # (416-450) - Campo de uso da empresa (Brancos)
        self._reserva3 = ""                                     # A # (451-472) - (Brancos)
        self._codigoLancamento = "00000"                        # N # (473-477) - Código do lançamento (Exclusivo para modalidades 01,02,03,05,08; Indica o código de lançamento no extrato de conta corrente)
        self._reserva4 = ""                                     # A # (478) - (Brancos)
        self._tipoContaFornecedor = "1"                         # N # (479) - Tipo de conta do fornecedor (1=Indica que o credito ao fornecedor será realizado em conta corrente, 2=Indica que o credito ao fornecedor será realizado em conta poupança)
        self._contaComplementar = ""                            # N # (480-486) - Conta complementar (Obrigatório quando o cliente pagador possuir mais de uma conta para debito dos pagamentos. DEVERA SER SOLICITADO AO BANCO)
        self._reserva5 = ""                                     # A # (487-494) - (Brancos)
        self._numeroSequencialRegistro = "000002"               # N # (495-500) - Número sequencial do registro (Brancos)
