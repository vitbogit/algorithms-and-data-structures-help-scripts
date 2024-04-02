import random
import datetime
import pyfiglet

# ----------------------------------
#               Description
# ----------------------------------

# Генератор связных неориентированных графов

# Принцип работы:
# 1) Строится "позвоночник", соединяющий все вершины
# 2) Случайным образом добавляются новые ребра

# ----------------------------------
#               Settings
# ----------------------------------

NUMBER_OF_GRAPHS = 1  # Число графов 
GRAPH_SIZE = 10  # Размер каждого графа
DENSITY = 1  # Плотность (>=0)
STORAGE_TYPE = 1 # 0 - adjacency_list, 1 - edges_list, 2 - adjacency_matrix

OUTPUT_TO_FILE = True  # Выводить в файл
OUTPUT_FILE_NAME = "generated_undirected_graph_.txt"  # Имя выходного файла (дополнится номером)

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

# Simple settings validator:
def validate_settings():
    if not NUMBER_OF_GRAPHS > 0:
        print("Вы собирались распечатать 0 графов...")
        exit()
    if not GRAPH_SIZE > 0:
        print("Вы собирались распечатать графы размера 0...")
        exit()
    if not DENSITY >= 0:
        print("Вы собирались распечатать графы с отрицательной плотностью...")
        exit()
    if not STORAGE_TYPE in [0, 1, 2]:
        print("Вы собирались распечатать графы с отрицательной плотностью...")
        exit()

# Greeter:
def greeter():
    print(pyfiglet.figlet_format("Undirected graph generator", font = "slant"  ) )
    print(pyfiglet.figlet_format(str(datetime.datetime.now().time().replace(microsecond=0)), font = "bulbhead"  ) ) 
    print(
          "\nЧисло графов:", NUMBER_OF_GRAPHS,
          "\nРазмер графов:", GRAPH_SIZE,
          "\nПлотность графов:", DENSITY,
          "\nВид хранения графов:", STORAGE_TYPE, " // 0=adjacency_list, 1=edges_list, 2=adjacency_matrix",
          "\nПечатать в файл:", OUTPUT_TO_FILE,
          "\nИмя выходного файла:", OUTPUT_FILE_NAME
          )

# ----------------------------------
#               Main logic
# ----------------------------------

def generate_undirected_graph(n):
    # Создаем пустой граф
    graph = [[] for _ in range(n)]
    
    # Создаем "позвоночник", чтобы гарантировать связность графа
    for i in range(n - 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)
        
    # Добавляем дополнительные ребра случайным образом
    for _ in range(n * DENSITY):
        v = random.randint(0, n - 1)
        q = random.randint(0, n - 1)
        if v != q and q not in graph[v]:
            graph[v].append(q)
            graph[q].append(v)
            
    return graph
    

# ----------------------------------
#               Call
# ----------------------------------

# Greeter:
greeter()

# Simple settings validation:
validate_settings()

# Repeat for each graph:
for i in range(NUMBER_OF_GRAPHS):
    
    # Generate matrix 
    graph = generate_undirected_graph(GRAPH_SIZE) 

    # Transform if needed
    if STORAGE_TYPE == 0:  # adjacency_list
        pass
    elif STORAGE_TYPE == 1:  # edges_list
        graph = edges_list_from_adjacency_list(graph)
        
    elif STORAGE_TYPE == 2:  # adjacency_matrix
        graph = adjacency_matrix_from_adjacency_list(graph)
        
    # Output
    if OUTPUT_TO_FILE:
        with open(OUTPUT_FILE_NAME.replace(".txt", str(i) + ".txt"), 'w') as f:
            f.write(str(graph))
    else:
        print("\n", "-"*50, "\n\nGraph", i, ":\n\n", str(graph))



    
