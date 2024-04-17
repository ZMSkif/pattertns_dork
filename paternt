import itertools

def generate_patterns():
    patterns = []

    params = ['(KW)', '(DE)', '(PT)', '(PP)', '(PF)']
    symbols = {
        '(KW)': ['/', ' '],
        '(DE)': ['/', ' '],
        '(PT)': ['/', ' '],
        '(PP)': ['/', ' '],
        '(PF)': ['/', ' ']
    }

    # Создание всех возможных комбинаций шаблонов
    for num_params in range(2, 5):  # Ограничение до 4 параметров
        for param_set in itertools.permutations(params, num_params):
            for symbol_set in itertools.product(*(symbols[param] for param in param_set)):
                pattern = []
                for i, (param, symbol) in enumerate(zip(param_set, symbol_set)):
                    if len(pattern) > 0:
                        # Если параметр (KW) и он первый, добавляем intext:
                        if param == '(KW)' and i == 0:
                            pattern.append(f'intext:{param}')
                        # Если параметр (KW), но не первый, добавляем в двойные кавычки
                        elif param == '(KW)':
                            pattern.append(f'"{param}"')
                        # Если параметр (DE) и он первый, добавляем site:
                        elif param == '(DE)':
                            pattern.append(f'site:.{param}')
                        else:
                            pattern.append(f'{symbol}{param}')
                    else:
                        # Если первый параметр (KW), добавляем intext:
                        if param == '(KW)':
                            pattern.append(f'intext:{param}')
                        # Всегда добавляем site: перед первым параметром (DE)
                        elif param == '(DE)'  and i == 0:
                            pattern.append(f'site:{param}')
                        else:
                            pattern.append(f'{param}')


                # Если (PP) в конце, добавляем знак "=" или "=*"
                if param_set[-1] == '(PP)':
                    pattern.append('=')
                patterns.append(''.join(pattern))

    return patterns


def save_patterns_to_file(patterns, filename):
    with open(filename, 'w') as f:
        for pattern in patterns:
            f.write(pattern + '\n')
    print(f"Patterns saved to {filename}")

# Генерация шаблонов
patterns = generate_patterns()

# Сохранение шаблонов в файл
save_patterns_to_file(patterns, "patterns.txt")
