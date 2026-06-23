"""- **Enunciado do Desafio:** Crie um programa em Python que cadastre os preços de vários produtos em uma loja. O sistema deve receber esses valores de forma contínua numa lista principal até o usuário decidir parar. Após a inserção, o programa deve varrer essa lista principal e enviar os produtos que custam menos de R$50 *para uma lista chamada* ‘*produtosbaratos*‘ , *e os que custam R* $50 ou mais para uma lista chamada **`produtos_caros`**. Ao final, exiba as três listas.
- **🚀 Requisitos/Critérios de Sucesso:**
    - Usar um laço de repetição com **`break`** para leitura contínua.
    - Usar o **`.append()`** corretamente em três momentos diferentes.
    - Usar um laço de repetição (**`for`** ou **`for`** com **`enumerate()`**) para iterar os valores.
    - Imprimir a lista geral, a lista dos baratos e a lista dos caros separadamente usando *f-strings*."""

precos = []
produtos_barato = []
produto_caro = []
while True:
    precos.append(float(input('Informe o preço do produto: R$')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
for valor in precos:
    if valor < 50:
        produtos_barato.append(valor)
    elif valor >= 50:
        produto_caro.append(valor)
print('-=' * 20)
print(f'Os preços informados foram: {precos}')
produtos_barato.sort()
print(f'Os preços mais baratos foram: {produtos_barato}')
produto_caro.sort()
print(f'E os preços mais caros foram: {produto_caro}')
print('-=' * 20)