calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    return string in list_to_search


print(string_info('LoSs'))
print(string_info('WiN'))
print(string_info('drAw'))
print(is_contains('London', ['London', 'Paris', 'Warsaw', 'Moscow']))
print(is_contains('Mozambik', ['USA', 'France', 'Japan', 'Mexico', 'Urban']))
print(is_contains('Каспийское', ['Балтийское', 'Красное', 'Японское', 'Черное', 'Каспийское', 'Карибское']))

print(calls)