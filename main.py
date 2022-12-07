
from equation import Equação
from time import sleep


def run_balance():

    print('=================================================')
    print('insira a equação que voce deseja balancear.')
    print('Exemplo: (H)2 + (O)2 = (H)2(O)1')
    user_input = input('>>> ')
    try:
        equation = Equação(user_input)
        print('Balanced equation: ' + equation.balance())
        sleep(3)
        run_balance()
    except IndexError:
        print('[ERRO!]\n'
              'tente novamente...')
        sleep(3)
        run_balance()

run_balance()