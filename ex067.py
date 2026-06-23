print('Faça um programa que mostre a tabuada de vários números, um de cada vez,'
      'para cada valor digitado pelo usuário. O programa será interronpido quando'
      'o número solicitador for negativo.')
print('-=' * 20)
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-=' * 20)
    if num < 0:
        break
    for cont in range(0, 11):
        print(f'{num} x {cont:2} = {num * cont:2}')
    print('-=' * 20)
print('PROGRAMA FINALIZADO...')