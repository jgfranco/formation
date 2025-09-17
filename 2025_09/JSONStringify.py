def stringify(obj) -> str:
    if obj == None: return None
    
    if type(obj) == int or type(obj) == float:
        return str(obj)
    
    if type(obj) == str: 
        return f'"{obj}"'

    if type(obj) == list:
       parts = [stringify(val) for val in obj]
       return f"[{', '.join(parts)}]"


    
    parts = []
    for key in obj:
        print(key)
        if obj.get(key) is not None:
            parts.append(f'"{key}": {stringify(obj[key])}')
    return f"{{{', '.join(parts)}}}"
    


print(stringify(None) == None)

print(stringify("hello")  == '"hello"')

print(stringify(42) == '42')

print(stringify(3.14) == '3.14')

print(stringify({"x": 5, "y": "Oliver"}) == '{"x": 5, "y": "Oliver"}')

# Test list input
print(stringify([1, "hello", "null", {"x": 5, "y": "Oliver"}]) == '[1, "hello", "null", {"x": 5, "y": "Oliver"}]')

# Test dictionary input
print(stringify({"key1": "value1", "key2": "null", "key3": {"subkey": 42}}) ==
  '{"key1": "value1", "key2": "null", "key3": {"subkey": 42}}')
