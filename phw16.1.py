user_stroke = input(
    "Введите математическое выражение\nДопускаются только числа, операции и скобки\n+ - * / ()\n"
)


def find_num_and_ops(input_str):
    input_str = input_str.replace(" ", "")
    symbols = {"numbers": [], "operators": []}
    current_symbol = ""
    for symbol in input_str:
        if symbol.isdigit():
            current_symbol += symbol
        elif symbol in "/*+-()":
            if current_symbol:
                symbols["numbers"].append(current_symbol)
                current_symbol = ""
            symbols["operators"].append(current_symbol)

    return symbols


print(find_num_and_ops(user_stroke))

dictionary_variable = {"+": (lambda x, y: int(x) + int(y), 0)}
