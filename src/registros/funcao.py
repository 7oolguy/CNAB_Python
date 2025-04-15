from abc import ABC, abstractmethod
import time
import random

class Funcao(ABC):
    def _add_zeros_left(self, value, length):
        return str(value).rjust(length, "0")

    def _add_zeros_right(self, value, length):
        return str(value).ljust(length, "0")

    def _add_zeros(self, value, length):
        return str(value).zfill(length)

    def gerar_numero_pagamento_unico(self) -> str:
        # timestamp em microssegundos (13 dígitos)
        base = int(time.time() * 1_000_000)  # ex: 1713198002540041
        # adiciona 2 dígitos aleatórios no final (00-99)
        sufixo = random.randint(0, 99)
        numero = int(f"{base}{sufixo}")  # pode dar até 15 dígitos
        return str(numero)[:15]
