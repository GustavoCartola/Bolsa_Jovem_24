import time

# Função para realizar o algoritmo de ordenação por inserção (insertion sort)
def insertionSort(array):
    comparisons = 0  # Contador para o número de comparações
    swaps = 0  # Contador para o número de trocas
    for i in range(1, len(array)):
        comparisons += 1  # Incrementa o contador de comparações a cada iteração do loop externo
        current_value = array[i]  # Armazena o valor atual que será inserido
        j = i - 1

        # Move os elementos que são maiores que current_value uma posição à frente
        while j >= 0 and current_value < array[j]:
            array[j + 1] = array[j]  # Desloca o elemento maior para a direita
            j -= 1
            swaps += 1  # Incrementa o contador de trocas quando os elementos são deslocados
        array[j + 1] = current_value  # Insere o current_value na posição correta

    return comparisons, swaps

# Abre o arquivo e lê os dados
file = open('facul/conj100aleat.txt', 'r')
array = []
for i in file:
    array.append(int(i))  # Adiciona cada número inteiro do arquivo ao array

start = time.time()  # Inicia o cronômetro
comparisons, swaps = insertionSort(array)  # Ordena o array e conta comparações e trocas
end = time.time()  # Termina o cronômetro

processing_time = end - start  # Calcula o tempo total de processamento

# Exibe o array ordenado e as estatísticas de desempenho
print(array)
print(comparisons)
print(swaps)
print('Tempo de Processamento: {:.3f} ms'.format(processing_time * 1000))  # Exibe o tempo em milissegundos
