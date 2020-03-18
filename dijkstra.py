from dataclasses import dataclass


@dataclass
class Vertex():
    name:   str
    number: int

def extract_data(filename):
    graph = {}
    graph["start"] = {}
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        total_values = []
        global layers
        layers = 0
        for line in lines:
            values = line.split()
            total_values += values
            print(total_values)
            layers += 1
        global added, added_copy
        added, added_copy= set(), set()
        vertex_num = 0

        for layer_num in range(layers):
            added_copy = set()
            # print("Current vertex_num, layer_num : {} {}".format(vertex_num, layer_num))
            if vertex_num < len(total_values):
                if layer_num == 0:
                    graph["start"].update({f"v{vertex_num}": total_values[vertex_num]})
                    graph[f"v{vertex_num}"] = {}
                    added.add(f"v{vertex_num}")
                    vertex_num += 1
                else:
                    for item in range(layer_num + 1):
                        for el in added:
                            el_num = int(el[1:])
                            print(f"Current vert: {vertex_num}; el_num: {el_num}; layer: {layer_num}")
                            if vertex_num - el_num == layer_num or vertex_num - el_num == layer_num + 1:
                                print("true")
                                graph[el].update({f"v{vertex_num}": total_values[vertex_num]})
                                graph[f"v{vertex_num}"] = {}
                                added_copy.add(f"v{vertex_num}")
                        vertex_num += 1
                    added = set()
                    added.update(added_copy)
                    print(f"Set Updated, layer: {layer_num}")
            else:
                break
        for key, value in graph.items():
            if value == {}:
                graph[key] = {"end" : 0}

    return total_values, graph


values, graph = extract_data("./triangle_data/very_easy.txt")
breakpoint()


def dijkstra():
    print("Hello Dijkstra")


