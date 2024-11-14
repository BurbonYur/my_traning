calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    result = len(string), string.upper(), string.lower()
    return result

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in list_to_search:
        i = i.lower()
        if string == i:
            result = True
            return result
        else:
            result = False
    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban','BaNaN','urBAN']))
print(is_contains('cycle',['recycling','cyclic']))
print(calls)