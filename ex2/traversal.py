import numpy as np
class node:
    x = 0
    y = 0
    id = 0
    name = None
    linked_nodes = []
    def __init__(self,name,x,y):
        self.x = x
        self.y = y
        self.name = name
        pass

def get_node_vector(origin_node: node, target_node: node):
    distance = np.sqrt((origin_node.x - target_node.x)**2 + (origin_node.y-target_node.y))
    angle = np.arctan2((origin_node.y-target_node.y), (origin_node.x - target_node.x)) * (180/np.pi)
    return [distance,angle]

def link_node(node_1:node,node_2:node):
    node_1.linked_nodes.append(node_2)
    node_2.linked_nodes.append(node_1)

class graph:
    total_nodes = 0
    nodes = []
    id_name_pair = {}
    def __init__(self):
        pass
    
    def append_node(self,node:node):
        self.nodes.append()
        node.id = self.total_nodes
        self.id_name_pair = {node.name:node.id}
        self.total_nodes += 1

    def get_node_id(self,name : str):
        return self.id_name_pair[name]
    
    def get_node_name(self,id: int):
        return self.nodes[id]

    def find_path(start_node,end_node):
        pass



node_1 = node("node 1",1,-1)
node_2 = node("node 2",0,0)

print(get_node_vector(node_1,node_2))