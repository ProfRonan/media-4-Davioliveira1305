"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE O SEU CÓDIGO AQUI.
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))
    nota_3 = float(input('Digite a terceira nota: '))
    nota_4 = float(input('Digite a quarta nota: '))
    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    print(f'A média aritmética é: {media:.2f}.')


if __name__ == '__main__':
    main()
