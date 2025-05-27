import argparse
import itertools
import threading
import queue
import time
from typing import List, Set

class DictionaryGenerator:
    def __init__(self, min_length: int, max_length: int, charset: str, 
                 prefix: str = "", suffix: str = "", output_file: str = "dicionario.txt"):
        self.min_length = min_length
        self.max_length = max_length
        self.charset = charset
        self.prefix = prefix
        self.suffix = suffix
        self.output_file = output_file
        self.word_queue = queue.Queue()
        self.stop_event = threading.Event()
        self.lock = threading.Lock()
        self.total_words = 0

    def generate_combinations(self, length: int) -> None:
        "Gera todas as combinações possíveis para um determinado comprimento."
        for combo in itertools.product(self.charset, repeat=length):
            word = self.prefix + ''.join(combo) + self.suffix
            self.word_queue.put(word)

    def writer_thread(self) -> None:
        "Thread responsável por escrever as palavras no arquivo."
        with open(self.output_file, 'w', encoding='utf-8') as f:
            while not (self.stop_event.is_set() and self.word_queue.empty()):
                try:
                    word = self.word_queue.get(timeout=1)
                    f.write(word + '\n')
                    with self.lock:
                        self.total_words += 1
                    self.word_queue.task_done()
                except queue.Empty:
                    continue

    def generate(self, num_threads: int = 4) -> None:
        "Inicia a geração do dicionário usando múltiplas threads."
        start_time = time.time()
        
        # Inicia a thread de escrita
        writer = threading.Thread(target=self.writer_thread)
        writer.start()

        # Cria e inicia as threads de geração
        generator_threads = []
        for length in range(self.min_length, self.max_length + 1):
            thread = threading.Thread(target=self.generate_combinations, args=(length,))
            generator_threads.append(thread)
            thread.start()

        # Aguarda todas as threads de geração terminarem
        for thread in generator_threads:
            thread.join()

        # Sinaliza para a thread de escrita que pode parar
        self.stop_event.set()
        writer.join()

        end_time = time.time()
        print(f"\nGeração concluída!")
        print(f"Tempo total: {end_time - start_time:.2f} segundos")
        print(f"Total de palavras geradas: {self.total_words}")
        print(f"Arquivo salvo em: {self.output_file}")

def main():
    parser = argparse.ArgumentParser(description='Gerador de Dicionários com Multithreading')
    parser.add_argument('--min', type=int, required=True, help='Tamanho mínimo das palavras')
    parser.add_argument('--max', type=int, required=True, help='Tamanho máximo das palavras')
    parser.add_argument('--charset', type=str, default='abcdefghijklmnopqrstuvwxyz0123456789',
                      help='Conjunto de caracteres para gerar as palavras')
    parser.add_argument('--prefix', type=str, default='', help='Prefixo para todas as palavras')
    parser.add_argument('--suffix', type=str, default='', help='Sufixo para todas as palavras')
    parser.add_argument('--output', type=str, default='dicionario.txt',
                      help='Nome do arquivo de saída')
    parser.add_argument('--threads', type=int, default=4,
                      help='Número de threads para geração')

    args = parser.parse_args()

    generator = DictionaryGenerator(
        min_length=args.min,
        max_length=args.max,
        charset=args.charset,
        prefix=args.prefix,
        suffix=args.suffix,
        output_file=args.output
    )

    generator.generate(num_threads=args.threads)

if __name__ == '__main__':
    main() 
