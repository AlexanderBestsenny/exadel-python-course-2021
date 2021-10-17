
tree = {
   "node1": {
       "node11": {
           "node111": [1, 2, 3],
           "node112": [31, 5]
       },
       "node12": [31]
   },
   "node2": [7, 8, 9]
}


def collect_leaves(tree_element):
    if isinstance(tree_element, list):
        return tree_element
    if type(tree_element) is dict:
        result = list()
        for leave in tree_element:
            result.extend(collect_leaves(tree_element[leave]))
        return result
    return list()


res = collect_leaves(tree)
print(res)

assert collect_leaves([1, 2, 3]) == [1, 2, 3]

