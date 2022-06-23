import re
from typing import List, Tuple

import yaml
import sortedcontainers
from dataclasses import dataclass
from Levenshtein import distance as levenshtein_distance


@dataclass(frozen=True)
class Node:
    item: object
    path: Tuple[int]


def astar_search(start, action_list, evaluator):
    next_it = sortedcontainers.SortedSet(key=lambda x: -evaluator(x.item))
    visited = set()

    next_it.add(Node(start, path=()))

    element = None
    while next_it and evaluator((element := next_it.pop()).item) != 0:
        visited.add(element.item)
        for i, action in enumerate(action_list):
            activations = action(element.item)
            for activation in activations:
                if activation not in visited:
                    next_it.add(Node(activation, element.path + (i,)))

    return element


def match_regex(in_string, out_string):
    def fun(text):
        last_start = 0
        pattern = re.compile(in_string)
        replacement = out_string
        output = []
        while match := pattern.search(text[last_start:]):
            output.append(text[:last_start] + pattern.sub(replacement, text[last_start:], 1))
            last_start += match.start() + 1
        return output

    return fun


def read_miu(data):
    rules = data["rules"]
    rule_list = []
    for in_string, out_string in rules.items():
        rule_list.append(match_regex(in_string, out_string))
    return data["start"], rule_list, lambda element: levenshtein_distance(data["end"], element)


def main():
    with open('rules.yaml', "r") as file:
        data = yaml.safe_load(file)
        print(astar_search(*read_miu(data)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
