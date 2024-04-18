class Operation:
    def __init__(self, type, index, data_object):
        self.type = type
        self.index = index
        self.data_object = data_object


def dfs(graph, v, used=None):
    # init the used array
    if used is None:
        used = set()
    # update the used array
    used.add(v)
    # process leaves
    if v not in graph:
        return True
    # process neighbors otherwise
    result = True
    for neighbor in graph[v]:
        if neighbor not in used:
            result = result and dfs(graph, neighbor, used)
        else:
            return False
    return result


def fill_graph(graph, nodes):
    write_type = "w"
    for i in range(0, len(nodes)):
        for j in range(0, i):
            # check the requirements of the edge in the graph:
            #   1) the same data_object
            #   2) one of the type is write_type
            if nodes[i].data_object == nodes[j].data_object and nodes[i].index != nodes[j].index and (
                    nodes[i].type == write_type or nodes[j].type == write_type):
                # init a new set neighbours for the vertex in the graph
                if nodes[j].index not in graph:
                    graph[nodes[j].index] = set()
                # add edge to the graph
                graph[nodes[j].index].add(nodes[i].index)


def fill_nodes(nodes, history):
    for i in range(0, len(history), 3):
        nodes.append(Operation(history[i], int(history[i + 1]), history[i + 2]))


def main():
    # collect input data to a suitable format
    nodes = []
    fill_nodes(nodes, input().split(" "))
    # create the conflict graph using the collected data
    graph = {}
    fill_graph(graph, nodes)
    # run dfs algorithm to find any loop in the graph
    print(dfs(graph, 1))


if __name__ == '__main__':
    main()
