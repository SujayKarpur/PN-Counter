"""
Implementation of a Positive-Negative Counter using 2 Grow-Only Counters
"""


class G_Counter:

    """
    Implements a Grow-only counter with the following API
    G_Counter(number_of_nodes)          - initiates a new grow-only counter with 
                                          an ID number_of_nodes 
                                          a vector of values where values[i] corresponds to the perceived number of increments at node i
    value()                             - current value 
    increment()                         - increase the value at the current node by one
    merge(node)                         - merge (aka sync) the current node with node 
    """

    def __init__(self, number_of_nodes: int) -> None:
        self.id = number_of_nodes
        self.values = [0] * number_of_nodes 

    def value(self) -> int:
        return sum(self.values) 

    def increment(self) -> None:
        self.values[self.id] += 1  

    def merge(self, other: 'G_Counter'):
        for i in range(len(other)):
            try:
                self.values[i] = max(self.values[i], other.values[i])
            except:
                self.values.append(other.values[i]) 

    def __repr__(self) -> str:
        return f"Counter{self.id}: {self.values}" 
    


class PN_Counter:

    """
    Implements a Positive-Negative counter with the following API
    PN_Counter(number_of_nodes)         - initiates a new positive-negative counter with 
    value()                             - current value 
    increment()                         - increase the value at the current node by one
    decrement()                         - decrease the value at the current node by one 
    merge(node)                         - merge (aka sync) the current node with node 
    """
    