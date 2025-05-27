# Gerador de Dicionários com Multithreading

O programa é um gerador de dicionários em Python que utiliza multithreading para criar combinações de palavras.

## Definições

- Geração de palavras com tamanho mínimo e máximo definido.
- Exportação para arquivos de texto
- Processamento paralelo usando multithreading
- Contagem de tempo e total de palavras geradas

## Requisitos

- Python 3.12 ou superior
- Executador / Compilador (ex. VSCode)

## Como Usar

O programa pode ser executado via linha de comando com os seguintes argumentos:

# python dictionary_generator.py --min 4 --max 6

### Argumentos Disponíveis

- `--min`: Tamanho mínimo das palavras (obrigatório)
- `--max`: Tamanho máximo das palavras (obrigatório)
- `--charset`: Conjunto de caracteres para gerar as palavras (opcional, padrão: a-z0-9)
- `--prefix`: Prefixo para todas as palavras (opcional)
- `--suffix`: Sufixo para todas as palavras (opcional)
- `--output`: Nome do arquivo de saída (opcional, padrão: dicionario.txt)
- `--threads`: Número de threads para geração (opcional, padrão: 4)

### Exemplos de Uso

1. Gerar palavras de 4 a 6 caracteres usando letras minúsculas e números:

python3 dictionary_generator.py --min 4 --max 6

2. Gerar palavras com prefixo e sufixo específicos:

python3 dictionary_generator.py --min 4 --max 6 --prefix "test_" --suffix "_123"

3. Usar um conjunto de caracteres personalizado:

python3 dictionary_generator.py --min 4 --max 6 --charset "abc123!@#"

4. Especificar um arquivo de saída diferente:

python3 dictionary_generator.py --min 4 --max 6 --output "meu_dicionario.txt"

## Notas de Desempenho

- O programa utiliza multithreading para otimizar a geração de combinações.
- O número de threads pode ser ajustado conforme a necessidade.

## Limitações

- Considere o espaço em disco necessário para o arquivo de saída.
