import json
import re
from collections import defaultdict
import sys

def parse_functions(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Extract all JSON-like dictionaries
    dicts = re.findall(r'\{.*?\}', content, re.DOTALL)
    
    functions = []
    for d in dicts:
        # Convert string to dict
        data = json.loads(d)
        functions.append(data)
    return functions

def find_common_selectors(functions):
    selector_map = defaultdict(set)

    for func_dict in functions:
        for func, selector in func_dict.items():
            selector_map[selector].add(func)

    print("Functions with the same selector but different names across dictionaries:\n")
    for selector, funcs in selector_map.items():
        if len(funcs) > 1:
            print(f"Selector: {selector}")
            for func in funcs:
                print(f"  - Function: {func}")
            print()

if __name__ == '__main__':
    file_path = sys.argv[1]  # Replace with your file path
    functions = parse_functions(file_path)
    find_common_selectors(functions)
    print("Check completed.")
