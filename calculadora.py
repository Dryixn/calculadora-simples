from time import sleep

print('''
------------------------------------------
              CALCULADORA
------------------------------------------''')

resp = 'S'

while True:
    if resp == 'S':
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))

    n1 = float(n1)
    n2 = float(n2)

    resp = 'N'
    soma = n1 + n2
    subtracao = n1 - n2
    divisao = n1 / n2
    multiplicacao = n1 * n2
    raiz = n1 ** (1/n2)

    print('Escolha um número de sua escolha:')
    escolha = str(input('''
    [0] Somar
    [1] Subtrair
    [2] Dividir
    [3] Multiplicar
    [4] Potência
    [5] Raiz
    [6] Escolher outros números
    [7] Sair do programa

    Escolha: '''))

    if escolha == '0':
        print('-' * 30)
        print(f'A soma dos números {n1} e {n2} é {soma:.2f}')
    elif escolha == '1':
        print('-' * 30)
        print(f'A subtração dos números {n1} e {n2} é {subtracao:.2f}')
    elif escolha == '2':
        print('-' * 30)
        print(f'A divisão dos números {n1} e {n2} é {divisao:.2f}')
    elif escolha == '3':
        print('-' * 30)
        print(f'A multiplicação dos números é {n1} e {n2} é {multiplicacao:.2f}')
    elif escolha == '4':
        try:
            potencia = n1 ** n2
            print('-' * 30)
            print(f'A potência dos números {n1} e {n2} é {potencia:.2f}')
        except OverflowError:
            print('[ERRO] Número muito grande, tente outro valor.')
    elif escolha == '5':
        print('-' * 30)
        print(f'A raiz do números é {n1} e {n2} é {raiz:.2f}')
    elif escolha == '6':
        print('-' * 30)
        while True:
            n1 = float(input('Primeiro número: '))
            n2 = float(input('Segundo número: '))
            if isinstance(n1, float) and isinstance(n2,float):
                break
            else:
                print('[ERRO] Não foi digitado o esperado. Digite um número.')
    elif escolha == '7':
        print('Ok. O programa está sendo finalizado....')
        sleep(2)
        break
    else:
        print('-' * 30)
        print('[Erro] Escolha inválida. Escolha um número de 0 a 7.')
print('-' * 30)
