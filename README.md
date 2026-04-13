# Exercícios PythonPOO

Este repositório contém exercícios em Python que demonstram conceitos básicos de programação e orientação a objetos.

## Estrutura dos arquivos

- `advinha.py` - Jogo de adivinhação simples com `random` e `input`.
- `aluno.py` - Classe para manipular nome de aluno, gerar maiúsculas/minúsculas e contar letras.
- `ano.py` - Verifica se um ano é bissexto e informa quantos dias ele tem.
- `codicodebara.py` - Gera um código numérico aleatório de 12 dígitos.
- `contabancaria.py` - Classe que simula operações básicas de conta bancária.
- `inteiro.py` - Verifica se um número inteiro é par ou ímpar.
- `letra.py` - Conta letras e posições em uma frase (lógica precisa de ajuste para corresponder ao enunciado esperado).
- `multadocarro.py` - Calcula multa de velocidade segundo um limite de 80 km/h.
- `nome.py` - Separa primeiro e último nome a partir do nome completo.
- `num.py` - Separa número em unidades, dezenas, centenas e milhares.
- `pensar.py` - Jogo de adivinhação com repetição até acertar.
- `poo.py` - Exemplo básico de classe, atributos e métodos de instância.
- `triangulo.py` - Verifica se três lados podem formar um triângulo.
- `viagem.py` - Calcula preço de passagem com tarifas diferentes por distância.

## Comentários por exercício

### `advinha.py`
- Jogo simples de adivinhação com `random` e `input`.
- Aceita apenas uma tentativa por execução.
- Bom domínio de estruturas básicas e uso de biblioteca padrão.

### `aluno.py`
- Usa classe para manipular nome e calcular letras.
- Funciona, mas poderia melhorar o estilo de nomes (`Aluno` em vez de `aluno`) e a formatação do código.
- Mostra boa noção de strings e métodos de classe.

### `ano.py`
- Verificação correta de ano bissexto com regra completa.
- Usa lógica condicional adequada.
- Excelente prática de manipulação de condições.

### `codicodebara.py`
- Gera 12 dígitos aleatórios.
- Não calcula dígito verificador verdadeiro de código de barras.
- Bom para treinar `random` e compreensão de listas.

### `contabancaria.py`
- Implementa classe `ContaBancaria` com `depositar`, `sacar` e `consultar_saldo`.
- Boa aplicação de OOP e interação com usuário.
- Falta validação de valores negativos e pode melhorar consistência de variáveis.

### `inteiro.py`
- Verifica par ou ímpar usando `% 2`.
- Exemplo direto e correto.
- Boa prática de controle de fluxo simples.

### `letra.py`
- Classe para contar letras e posições.
- Lógica de posições não segue completamente o enunciado esperado.
- Bom uso de classes, mas precisa ajuste de lógica.

### `multadocarro.py`
- Calcula multa corretamente ao ultrapassar 80 km/h.
- Simples e funcional.
- Ótimo para praticar aritmética e condicionais.

### `nome.py`
- Separa primeiro e último nome usando `split()`.
- Implementação clara e adequada.
- Boa prática com strings.

### `num.py`
- Separa número em unidades, dezenas, centenas e milhares.
- Usa `zfill` para garantir 4 dígitos.
- Exercício bem feito.

### `pensar.py`
- Jogo de adivinhação com loop `while` até acertar.
- Mostra entendimento de repetição.
- Deve remover a linha que imprime o número secreto para preservar a lógica do jogo.

### `poo.py`
- Exemplo básico de classe `aprendiz` com métodos.
- Demonstra instâncias, atributos e métodos.
- Bom nível inicial de POO.

### `triangulo.py`
- Verifica se três lados formam um triângulo pela desigualdade triangular.
- Correto e direto.
- Boa prática de lógica geométrica simples.

### `viagem.py`
- Calcula preço de passagem com tarifa variável.
- Simples e efetivo.
- Domínio básico de condições e cálculos.

## Nível de aprendizado

### Nível atual
- **Iniciante / Iniciante-Intermediário**
- Você domina:
  - `input()` e `print()`
  - Condicionais `if/else`
  - Loops simples (`while`)
  - Classes e métodos básicos
  - Manipulação de strings e números

### Próximos passos recomendados
- Usar nomes de classes em maiúsculas e variáveis mais claras.
- Modularizar com funções para reduzir repetição.
- Validar entradas do usuário e tratar valores inválidos.
- Ajustar lógica nos exercícios que atualizam posições e verificações.
- Evitar expor valores secretos ao usuário em jogos.

> Você já tem uma base sólida em lógica e está começando a aplicar orientação a objetos. Continue praticando e melhorando a organização do código.
