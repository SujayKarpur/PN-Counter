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
        """initialize a new Grow-only counter"""
        self.id = number_of_nodes
        self.values = [0] * (number_of_nodes + 1) #we just added a new node 

    def value(self) -> int:
        """value of the current counter"""
        return sum(self.values) 

    def increment(self) -> None:
        """increment the value at the current node"""
        self.values[self.id] += 1  

    def merge(self, other: 'G_Counter'):
        """combine `other` and self into a single, consistent state"""
        for i in range(len(other)):
            try:
                self.values[i] = max(self.values[i], other.values[i])
            except:
                self.values.append(other.values[i]) 

    def __repr__(self) -> str:
        """"""
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
    

    def __init__(self, number_of_nodes: int):
        self.id = number_of_nodes
        self.decrements: G_Counter = G_Counter(number_of_nodes)
        self.increments: G_Counter = G_Counter(number_of_nodes)

    
    def value(self) -> int:
        return self.increments.value() - self.decrements.value()

    def increment(self) -> None:
        self.increments.increment()

    def decrement(self) -> None:
        self.decrements.increment()

    def merge(self, other: 'PN_Counter') -> None:
        self.increments.merge(other.increments)
        self.decrements.merge(other.decrements)
    
    def __repr__(self) -> str: 
        pass 