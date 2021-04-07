from itertools import permutations
class Knapsack:
    def __init__(self, maxweight):
        self.items = []
        self.maxweight = maxweight
        self.value = 0

    def add_item(self,item):
        if self.weight + item["weight"] <= self.maxweight:
            self.items.append(item)
            self.value += item["value"]
            self.weight += item["weight"]

    def drop_item(self,item):
        if item in items:
            self.items.drop(item)
            self.value -= item["value"]
            self.weight -= item["weight"]

def maximum_value(maximum_weight, items):

    for elem in items:

        elem["spec_w"] = calc_specific_weight(elem)
        print(elem)

    # print(max(permutated_generator(maximum_weight, items)))
    #    return max(permutated_generator(maximum_weight, items))
    pass

def calc_specific_weight(elem):
    return elem["value"] / elem["weight"]

'''
def permutated_generator(maximum_weight, items):
    for permutated_items in permutations(items):
        total_weight = 0
        total_value = 0

        # print(permutated_items)
        for item in permutated_items:
            # print(item)
            total_weight += item["weight"]
            if total_weight <= maximum_weight:

                total_value += item["value"]
                # print(total_weight, total_value)
            else:
                total_weight -= item["weight"]

            yield total_value
'''

print(maximum_value(
    105,
    [
        {"weight": 25, "value": 350},
        {"weight": 35, "value": 400},
        {"weight": 45, "value": 450},
        {"weight": 5, "value": 20},
        {"weight": 25, "value": 70},
        {"weight": 2, "value": 500},
        {"weight": 12, "value": 75},
        {"weight": 12, "value": 75},
        {"weight": 12, "value": 75},
        {"weight": 12, "value": 75}
    ]
))