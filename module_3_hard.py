
def calculate_structure_sum (*args):
    sumtotal = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            sumtotal += arg
        elif isinstance(arg, str):
            sumtotal += len(arg)
        elif isinstance(arg, (list,tuple,set)):
            sumtotal += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            sumtotal += calculate_structure_sum(*arg.items())
        elif arg is None:
            pass
    return sumtotal

data_structure= [
      [1, 2, 3],
      {'a': 4, 'b': 5},
      (6, {'cube': 7, 'drum': 8}),
      "Hello",
      ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
result = calculate_structure_sum(data_structure)

print(result)
