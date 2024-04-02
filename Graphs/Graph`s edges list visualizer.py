from webweb import Web

# ----------------------------------
#               Description
# ----------------------------------

# Визуально отображает граф

# Необходимо подавать граф в виде списка ребер

# ----------------------------------
#               Settings
# ----------------------------------

PATH = "generated_undirected_graph_0.txt"

# ----------------------------------
#          Main logic and call
# ----------------------------------

with open(PATH, 'r') as f:
    edges_list = eval(f.read())

web = Web(edges_list)

web.display.radius = 8
web.display.charge = 5000
web.display.showNodeNames= True

web.show()
