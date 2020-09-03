class HashTableEntry:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'HashTableEntry({repr(self.key)}, {repr(self.value)})'

data = [None,None,None,None,None,None,None,None]


def my_hashing_function(s):
    string_bytes = s.encode()
    total = 0
    for b in string_bytes:
        total += b
    return total



def get_slot(s):
    hash_val = my_hashing_function(s)
    return hash_val % len(data)

def put(key,value):
    slot = get_slot(key)
    data[slot] = HashTableEntry(key,value)

def get(key):
    slot = get_slot(key)
    hash_entry = data[slot]
    
    if hash_entry is not None:
        return hash_entry.value
    return data[slot].value

def delete(key):
    put(key, None)



# print(my_hashing_function("Tyker"))
# print(get_slot('Tyker'))
# print(get_slot('Tylery'))
# print(get_slot('Banan'))
# print(get_slot('bar'))
# print(get_slot('baz'))


put("Tyker", 23525)
put('foo', 999)
print(data)
print(get("Tyker"))

# print(my_hashing_function('bar'))
# print(my_hashing_function('baz'))