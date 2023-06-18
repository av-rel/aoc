# --- Day 12: JSAbacusFramework.io ---

import json

json_doc = json.loads(open(0).read())

def traverse_json(obj): 
    if type(obj) == int: return obj, obj
    elif type(obj) == list: return (sum(s) for s in zip(*[traverse_json(x) for x in obj]))
    elif type(obj) == dict:
        v = [sum(s) for s in zip(*[traverse_json(x) for x in obj.values()])]
        # --- Part Two ---
        return v[0], 0 if "red" in obj.values() else v[1]
    return 0, 0

print(*traverse_json(json_doc), sep = '\n')
