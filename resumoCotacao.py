def moeda(cota, moeda='R$ '):
    return f'{moeda}{cota}'.replace('.', ',')

def resumo(cota1, cota2, cota3):
    print('='*35)
    print('COTAÇÃO NESTE MOMENTO'.center(30))
    print(f'Dólar: {moeda(cota1)}')
    print(f'Euro: {moeda(cota2)}')
    print(f'Bitcoin: {moeda(cota3)}')
    print('='*35)