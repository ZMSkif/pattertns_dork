import itertools

def generate_patterns():
    patterns = set()

    params = ['(KW)', '(DE)', '(PT)', '(PP)', '(PF)']
    symbols = {
        '(KW)': [' / '],  # Слэш после параметра intext:
        '(DE)': [' / '],  # Слэш после параметра site:
        '(PF)': [' / ', '.'],  # Слэш или точка после (PF)
        '(PT)': [' / ', '?', '? / '],  # Слэш, вопросительный знак, или их комбинация после (PT)
        '(PP)': ['= '],  # Равно после (PP)
    }

    for num_params in range(2, 5):  # От 2 до 4 параметров
        for param_set in itertools.permutations(params, num_params):
            for symbol_set in itertools.product(*(symbols[param] for param in param_set)):
                pattern = []
                for param, symbol in zip(param_set, symbol_set):
                    entry = f'{param}'  # По умолчанию параметр без модификатора
                    if param == '(KW)':
                        entry = f'intext:{param}'
                    elif param == '(DE)':
                        entry = f'site:{param}'

                    pattern.append(entry)  # Добавляем параметр
                    pattern.append(symbol)  # Добавляем символ после параметра

                # Проверяем, должен ли последний символ быть удалён
                # Удаляем его только если это символ, несущий разделительную функцию, и он находится в конце
                if pattern[-1].strip() == '/':
                    pattern.pop()

                patterns.add(''.join(pattern))

    return patterns

def save_patterns_to_file(patterns, filename):
    with open(filename, 'w') as f:
        for pattern in sorted(patterns):  # Сортировка для последовательности в файле
            f.write(pattern + '\n')
    print(f"Patterns saved to {filename}")

# Генерация и сохранение шаблонов
patterns = generate_patterns()
save_patterns_to_file(patterns, "patterns.txt")
