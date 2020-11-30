"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
import random
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_main(self):
        """Função que testa se a saída do programa corresponde ao que foi especificado."""
        # Lista de valores que serão retornados pela função input.
        input_returns = [str(random.randint(-100, 100)) for x in range(4)]
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            input_returns = list(map(int, input_returns))
            result = sum(input_returns) / len(input_returns)
            result = f'A média aritmética é: {result}.'
            assert mock_input.call_count == 4
            mock_print.assert_called_with(result)


if __name__ == '__main__':
    unittest.main()
