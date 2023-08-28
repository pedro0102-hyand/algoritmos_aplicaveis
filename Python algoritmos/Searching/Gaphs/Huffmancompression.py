import heapq
from collections import defaultdict
class Node:
    def init (self,simbolo,freq):
        self.simbolo=simbolo
        self.freq=freq
        self.left=None
        self.right=None
def huffman__tree(freq_tab):
    heap=[]
    for simbolo, freq in freq_tab.items():
        heapq.heappush(heap,(freq,Node(simbolo,freq)))
    while len(heap)>1:
        freq1,node1=heapq.heappop(heap)
        freq2,node2=heapq.heappop(heap)
        merged_node=Node(None,freq1+freq2)
        merged_node.left=node1
        merged_node.right=node2
        heapq.heappus(heap,(merged_node.freq,merged_node))
    return heap[0][1]
def huffman_code(root):
    codes={}
    def trav(node,code=""):
        if node is None:
            return
        if node.simbolo is not None:
            codes[node.simbolo]=code
            return
        trav(node.left,code+"0")
        trav(node.right,code+"1")
    trav(root)
    return codes
def compress(txt):
    freq_tab=defaultdict(int)
    for simbolo in txt:
        freq_tab[simbolo]+=1
    root=huffman__tree(freq_tab)
    codes=huffman_code(root)
    compressed=""
    for simbolo in txt:
        compressed+=codes[simbolo]
    return compressed, root
def descompress(compresset,root):
    descompressed=""
    node=root
    for bit in compresset:
        if bit=="0":
            node=node.left
        else:
            node=node.right
        if node.simbolo is not None:
            descompressed+=node.simbolo
            node=root
    return descompressed
