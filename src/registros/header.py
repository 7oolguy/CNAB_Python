from datetime import datetime
from .funcao import Funcao

class Header(Funcao):
    def __init__(self):
        # ----------------------------------------------N - Numerico
        # ----------------------------------------------A - Alfanumerico
        self._identificadorRegistro = "0"             # N  # (001 - constant)
        self._codigoComunicacao = "00147905"          # N  # (002-009 - Fornecido pelo Bradesco)
        self._tipoInscricao = "2"                     # N  # (010 - constant)
        self._baseEmpresaPag = "055233019000684"      # N  # (011-019 | 020-023 | 024-025 - Número de Inscrição)
        self._nomeEmpresaPag = "BRADESCO"             # A  # (026-065 - Nome da empresa pagadora) #TODO - Ajustar para 65 caracteres with spaces
        self._tipoServiço = "20"                      # N  # (066-067 - constant)
        self._codigoOrigem = "1"                      # N  # (068 - constant)
        self._numeroRemessa = ""                      # N  # (069-073 - Sequencial do arquivo Crescente)
        self._numeroRetorno = "00000"                 # N  # (074-078 - Desconsiderado Fixo zeros (Somente Arquivo Retorno))
        self._dataGravacao = ""                       # N  # (079-086 - Data de Gravação do arquivo AAAAMMDD)
        self._horaGravacao = ""                       # N  # (087-092 - Hora de Gravação do arquivo HHMMSS)
        self._densidadeGravacao = ""                  # A  # (093-097 - Brancos)
        self._unidadeDensidadeGravacao = ""           # A  # (098-100 - Brancos)
        self._identificacaoModuloMicro = ""           # A  # (101-105 - Brancos)
        self._tipoProcessamento = "0"                 # N  # (106 - Desconsiderado (Somente Arquivo Retorno))
        self._reservadoEmpresa = ""                   # A  # (107-180 - para uso Empresa)
        self._reservadoBanco1 = ""                    # A  # (181-260 - para uso Banco Brancos)
        self._reservadoBanco2 = ""                    # A  # (261-477 - para uso Banco Brancos)
        self._numeroListaDebito = ""                  # N  # (478-486 - Número da lista de débito)
        self._reservadoBanco3 = ""                    # A  # (487-494 - para uso Banco Brancos)
        self._numeroSequencialRegistro = "000001"     # N  # (495-500 - constant)

    @property
    def nomeEmpresaPag(self):
        return self._nomeEmpresaPag
    @nomeEmpresaPag.setter
    def nomeEmpresaPag(self, nomeEmpresaPag):
        if len(nomeEmpresaPag) <= 40:
            self._nomeEmpresaPag = nomeEmpresaPag.ljust(40, " ")
        else:
            raise ValueError('Error - Nome da empresa pagadora inválido.')

    @property
    def numeroRemessa(self):
        return self._numeroRemessa
    @numeroRemessa.setter
    def numeroRemessa(self, numeroRemessa):
        if numeroRemessa.isdigit():
            self._numeroRemessa = self._add_zeros(numeroRemessa, 5)
        else:
            raise ValueError('Error - Sequencial do arquivo invalido.')

    @property
    def dataGravacao(self):
        return self._dataGravacao
    @dataGravacao.setter
    def dataGravacao(self, dataGravacao):
        if isinstance(dataGravacao, datetime):
            self._dataGravacao = dataGravacao.strftime("%Y%m%d")
        else:
            raise ValueError('Error - Data de gravação inválida.')

    @property
    def horaGravacao(self):
        return self._horaGravacao
    @horaGravacao.setter
    def horaGravacao(self, horaGravacao):
        if isinstance(horaGravacao, datetime):
            self._horaGravacao = horaGravacao.strftime("%H%M%S")
        else:
            raise ValueError('Error - Hora de gravação inválida.')

    @property
    def densidadeGravacao(self):
        return self._densidadeGravacao
    @densidadeGravacao.setter
    def densidadeGravacao(self, densidadeGravacao):
        if len(densidadeGravacao) <= 5:
            self._densidadeGravacao = densidadeGravacao.ljust(5, " ")
        else:
            raise ValueError('Error - Densidade de gravação inválida.')

    @property
    def unidadeDensidadeGravacao(self):
        return self._unidadeDensidadeGravacao
    @unidadeDensidadeGravacao.setter
    def unidadeDensidadeGravacao(self, unidadeDensidadeGravacao):
        if len(unidadeDensidadeGravacao) <= 3:
            self._unidadeDensidadeGravacao = unidadeDensidadeGravacao.ljust(3, " ")
        else:
            raise ValueError('Error - Unidade de densidade inválida.')

    @property
    def identificacaoModuloMicro(self):
        return self._identificacaoModuloMicro
    @identificacaoModuloMicro.setter
    def identificacaoModuloMicro(self, identificacaoModuloMicro):
        if len(identificacaoModuloMicro) <= 5:
            self._identificacaoModuloMicro = identificacaoModuloMicro.ljust(5, " ")
        else:
            raise ValueError('Error - Identificação do módulo micro inválida.')

    @property
    def reservadoEmpresa(self):
        return self._reservadoEmpresa

    @property
    def reservadoBanco1(self):
        return self._reservadoBanco1
    @reservadoBanco1.setter
    def reservadoBanco1(self, reservadoBanco1):
        if len(reservadoBanco1) <= 80:
            self._reservadoBanco1 = reservadoBanco1.ljust(80, " ")
        else:
            raise ValueError('Error - Reservado banco inválido.')

    @property
    def reservadoBanco2(self):
        return self._reservadoBanco2
    @reservadoBanco2.setter
    def reservadoBanco2(self, reservadoBanco2):
        if len(reservadoBanco2) <= 217:
            self._reservadoBanco2 = reservadoBanco2.ljust(217, " ")
        else:
            raise ValueError('Error - Reservado banco inválido.')

    @property
    def numeroListaDebito(self):
        return self._numeroListaDebito
    @numeroListaDebito.setter
    def numeroListaDebito(self, numeroListaDebito):
        if numeroListaDebito.isdigit():
            self._numeroListaDebito = self._add_zeros(numeroListaDebito, 9)
        else:
            raise ValueError('Error - Número da lista de débito inválido.')

    @property
    def reservadoBanco3(self):
        return self._reservadoBanco3
    @reservadoBanco3.setter
    def reservadoBanco3(self, reservadoBanco3):
        if len(reservadoBanco3) <= 8:
            self._reservadoBanco3 = reservadoBanco3.ljust(8, " ")
        else:
            raise ValueError('Error - Reservado banco inválido.')

    @property
    def numeroSequencialRegistro(self):
        return self._numeroSequencialRegistro
