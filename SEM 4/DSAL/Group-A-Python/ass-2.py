class SetADT:
    def __init__(self):
        self.elements = []

    def add(self, new_element):
        if new_element not in self.elements:
            self.elements.append(new_element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def contains(self, element):
        return element in self.elements

    def size(self):
        return len(self.elements)

    def iterator(self):
        return iter(self.elements)

    def intersection(self, other_set):
        intersection_set = SetADT()
        for element in self.elements:
            if other_set.contains(element):
                intersection_set.add(element)
        return intersection_set

    def union(self, other_set):
        union_set = SetADT()
        for element in self.elements:
            union_set.add(element)
        for element in other_set.elements:
            union_set.add(element)
        return union_set

    def difference(self, other_set):
        difference_set = SetADT()
        for element in self.elements:
            if not other_set.contains(element):
                difference_set.add(element)
        return difference_set

    def is_subset(self, other_set):
        for element in self.elements:
            if not other_set.contains(element):
                return False
        return True


# Example usage:
set1 = SetADT()
set1.add(1)
set1.add(2)
set1.add(3)

set2 = SetADT()
set2.add(2)
set2.add(3)
set2.add(4)

print("Set 1:", list(set1.iterator()))
print("Set 2:", list(set2.iterator()))

print("Intersection:", list(set1.intersection(set2).iterator()))
print("Union:", list(set1.union(set2).iterator()))
print("Difference (Set 1 - Set 2):", list(set1.difference(set2).iterator()))
print("Is Set 1 a subset of Set 2:", set1.is_subset(set2))
