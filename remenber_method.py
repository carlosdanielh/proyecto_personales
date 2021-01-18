#! python 3
'''
remember_method.py will recall you all method for each structure data
list
set
dictionary
'''
import os
import random
structure = {

            'string': [
                        'fcapitalize()',
                        'casefold()',
                        'center()',
                        'count()',
                        'encode()',
                        'endswith()',
                        'expandtabs()',
                        'find()',
                        'format()',
                        'format_map()',
                        'index()',
                        'isalnum()',
                        'isalpha()',
                        'isdecimal()',
                        'isdigit()',
                        'isidentifier()',
                        'islower()',
                        'isnumeric()',
                        'isprintable()',
                        'isspace()',
                        'istitle()',
                        'isupper()',
                        'join()',
                        'ljust()',
                        'lower()',
                        'lstrip()',
                        'maketrans()',
                        'partition()',
                        'replace()',
                        'rfind()',
                        'rindex()',
                        'rjust()',
                        'rpartition()',
                        'rsplit()',
                        'rstrip()',
                        'split()',
                        'splitlines()',
                        'startswith()',
                        'strip()',
                        'swapcase()',
                        'title()',
                        'translate()',
                        'upper()',
                        'zfill()'],

            'dictionaries': [
                        'clear()',
                        'copy()',
                        'fromkeys()',
                        'get()',
                        'items()',
                        'keys()',
                        'pop()',
                        'popitem()',
                        'setdefault()',
                        'update()',
                        'values()'],

            'lists': [
                        'append()',
                        'clear()',
                        'copy()',
                        'count()',
                        'extend()',
                        'index()',
                        'insert()',
                        'pop()',
                        'remove()',
                        'reverse()',
                        'sort()'],

            'sets': [
                        'frozenset()',
                        'add()',
                        'clear()',
                        'copy()',
                        'difference()',
                        'difference_update()',
                        'discard()',
                        'intersection()',
                        'intersection_update()',
                        'isdisjoint()',
                        'issubset()',
                        'issuperset()',
                        'pop()',
                        'remove()',
                        'symmetric_difference()',
                        'symmetric_difference_update()',
                        'union()',
                        'update()'],

            'built_in:': [
                        'print()',
                        'print()',
                        'abs()',
                        'round()',
                        'min()',
                        'max()',
                        'min()',
                        'sorted()',
                        'sum()',
                        'len()',
                        'type()']

}

os.system('cls')
list_key_from_structure = list(structure.keys())
estructura_aleatoria = random.choice(list_key_from_structure)

print(f'Buenos dias Carlos!!! Hoy explicame, de la estructura de datos \
{estructura_aleatoria.upper()}, estos 5 metodos:\n')

list_all_structure_values = structure[estructura_aleatoria]
set_method = set()
set_is_full = False
while not set_is_full:
    method = random.choice(list_all_structure_values)
    set_method.add(method)
    if len(set_method) == 5:
        set_is_full = True

for values in set_method:
    print(f'- {values}')

len_methods_structure = len(list_all_structure_values)
print(f'\nEn total son: {len_methods_structure}')
