# ----------------------------------
#               Description
# ----------------------------------

ВНИМАНИЕ, КОД НЕ РАБОЧИЙ
ВНИМАНИЕ, КОД НЕ РАБОЧИЙ
ВНИМАНИЕ, КОД НЕ РАБОЧИЙ
ВНИМАНИЕ, КОД НЕ РАБОЧИЙ

# Преобразователь графов


# ----------------------------------
#               Settings
# ----------------------------------

INPUT_PATH = "generated_undirected_graph_0.txt"
OUTPUT_PATH = "converted_graph.txt"

# 0 - adjacency_list, 1 - edges_list, 2 - adjacency_matrix
INPUT_FORMAT = 2
OUTPUT_FORMAT =1

# ----------------------------------
#         Additional functions
# ----------------------------------

# Transformer
def edges_list_from_adjacency_list(matrix):
    n = len(matrix)
    edges_list = []
    for v in range(n):
        for q in matrix[v]:
            if v < q:
                edges_list.append([v, q])
    return edges_list

# Transformer
def adjacency_matrix_from_adjacency_list(adjacency_list):
    # Get the number of vertices
    n = len(adjacency_list)

    # Initialize the adjacency matrix with zeros
    adjacency_matrix = [[0]*n for _ in range(n)]

    # Fill the adjacency matrix based on the adjacency list
    for i in range(n):
        for j in adjacency_list[i]:
            adjacency_matrix[i][j] = 1
            adjacency_matrix[j][i] = 1  # Since the graph is undirected
            
    return adjacency_matrix

# ----------------------------------
#               Call
# ----------------------------------

# Читаем граф из файла
with open(INPUT_PATH, 'r') as f:
    graph = eval(f.read())

print(graph)
exit()

# Преобразуем граф в нужный формат
if INPUT_FORMAT == OUTPUT_FORMAT:
    pass
else:
    adj
    

# Записываем граф в другой файл
with open(OUTPUT_PATH, 'w') as f:
    f.write(str(converted_graph))
