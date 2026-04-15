# Programa de Cashback

## Acesso
- Front-end (Github Pages): https://giovannatvrs.github.io/cashback-api/
- Back-end (Railway): https://cashback-api-production-43b9.up.railway.app

## Descrição
Aplicação web em que o usuário pode ver o resultado do cálculo de cashback de uma compra inserindo tipo de cliente, valor da compra e desconto. O app informa o valor de cashback e exibe todas as consultas registradas com o IP do usuário.

## Linguagens de Programação e Banco de Dados Escolhidos
Esse projeto foi desenvolvido com Python no back-end utilizando o framework FastAPI e HTML, CSS e Javascript no front-end. O banco de dados escolhido foi o PostgreSQL

## Decisões
O backend foi desenvolvido utilizando FastAPI devido à sua performance, facilidade de validação de dados com Pydantic e simplicidade na criação de APIs REST. Enquanto o frontend foi desenvolvido com HTML, CSS e JavaScript puro, consumindo a API via fetch, para manter simplicidade e foco na integração com o backend.
A lógica de cálculo de cashback foi implementada no backend para garantir consistência das regras de negócio.

Odem do cálculo do cashback:

1. Aplicação do desconto no valor da compra
2. Cálculo do cashback base (5% sobre o valor final)
3. Aplicação do bônus de 10% sobre o cashback base para clientes VIP
4. Aplicação da regra promocional: compras acima de R$ 500 recebem o dobro do cashback final

Essa ordem foi definida com base na interpretação do cenário 1 apresentado no desafio, priorizando que o desconto sempre afeta a base de cálculo do cashback.


## Como rodar o programa localmente
No terminal, digitar:
git clone https://github.com/giovannatvrs/cashback-api.git

No PyCharm, VSCode ou outras IDES, digitar os comandos:

python3 -m venv .venv

source .venv/bin/activate
(Os comandos acima são de ativação do ambiente virtual no Linux)

pip install -r requirements.txt  

uvicorn backend.main:app --host 127.0.0.1 --port 8000

Acessar a aplicação pela url:
http://127.0.0.1:5500/


## Melhorias Futuras
- Implementação de sistema de autenticação e login para acessar dados.
- Barra de busca.
- Paginação.
- Filtros e ordenação


## Página
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/134d20ed-0da3-4810-99fa-e003787266be" />





