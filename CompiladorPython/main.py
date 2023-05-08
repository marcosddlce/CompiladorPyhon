import re
import colorama

colorama.init()

archivo = open("pruebax.txt")

operadores = {
    '==': 'Equality op',
    '<=': 'Less than or equal op',
    '>=': 'Greater than or equal op',
    '!=': 'Not equal op',
    ':=': 'Assignment op',
    '++': 'Increment op',
    '--': 'Decrement op',
    '/\*': 'Start of multi-line comment',
    '\*/': 'End of multi-line comment',
    '//': 'comment line',
    '=': 'Assignment op',
    '+': 'Addition op',
    '-': 'Subtraction op',
    '/': 'Division op',
    '*': 'Multiplication op',
    '<': 'Lessthan op',
    '>': 'Greaterthan op'
}

tipo_de_dato = {
    'int': 'integer type',
    'float': 'Floating point',
    'char': 'Character type',
    'long': 'long int'
}

simbolo_de_puntuacion = {
    ':': 'colon',
    ';': 'semi-colon',
    '.': 'dot',
    ',': 'comma',
    '(': 'left parenthesis',
    ')': 'right parenthesis',
    '{': 'left brace',
    '}': 'right brace',
    '[': 'left bracket',
    ']': 'right bracket'
}


identificador = {
    'a': 'id',
    'b': 'id',
    'c': 'id',
    'd': 'id'
}

palabras_reservadas = {
    'main': 'reserved keyword',
    'if': 'reserved keyword',
    'then': 'reserved keyword',
    'else': 'reserved keyword',
    'end': 'reserved keyword',
    'do': 'reserved keyword',
    'while': 'reserved keyword',
    'repeat': 'reserved keyword',
    'until': 'reserved keyword',
    'cin': 'reserved keyword',
    'cout': 'reserved keyword',
    'real': 'reserved keyword',
    'int': 'reserved keyword',
    'boolean': 'reserved keyword'
}

a = archivo.read()

contador = 0
program = a.split("\n")
for line in program:
    contador = contador + 1
    print("Línea #", contador, "\n", line)

    # Remover comentarios de una línea
    line = re.sub(r'//.*$', '', line)

    # Buscar comentarios de múltiples líneas
    if '/*' in line and '*/' in line:
        print("Comentario: " + line)
        #line = re.sub(r'/\*.*?\*/', '', line)
        comment_start = line.index('/*')
        comment_end = line.index('*/', comment_start + 2) + 2
        comment = line[comment_start:comment_end]
        #line = line.replace(comment, '')
        print("Comentario: " + comment)
    elif '/*' in line:
        print("Comentario: " + line)
        comment_start = line.index('/*')
        comment = line[comment_start:]
        line = line.replace(comment, '')
        print("Comentario: " + comment)
        for i in range(contador, len(program)):
            if '*/' in program[i]:
                comment_end = program[i].index('*/') + 2
                comment += program[i][:comment_end]
                line += program[i][comment_end:]
                #contador = i + 1
                break

    # Encontrar todos los tokens en la línea
    tokens = re.findall(r'[a-zA-Z_]\w*|==|<=|>=|!=|!|:=|/\*|\*/|//|\+\+|--|=|\+|-|/|\*|<|>|;|\(|\)|\{|\}|\[|\]|\d+\.\d+|\d+', line)

    print("Tokens:", tokens)
    print("Línea #", contador, "\npropiedades:\n")

    for token in tokens:
        if token in operadores:
            print(colorama.Fore.GREEN + operadores[token] + ": "+ token + colorama.Fore.RESET)
        elif token in tipo_de_dato:
            print(colorama.Fore.MAGENTA + tipo_de_dato[token] + ": "+ token + colorama.Fore.RESET)
            print("Tipo de dato:", tipo_de_dato[token])
        elif token in simbolo_de_puntuacion:
            print(colorama.Fore.RED + simbolo_de_puntuacion[token] + ": "+ token + colorama.Fore.RESET)
        elif re.match(r'^\d+\.\d+$', token):
            print(colorama.Fore.YELLOW + "Literal decimal:", token + colorama.Fore.RESET)
        elif token.isdigit():
            print(colorama.Fore.YELLOW + "Literal entero:", token + colorama.Fore.RESET)
        elif token in palabras_reservadas:
            print(colorama.Fore.BLUE + palabras_reservadas[token] + ": "+ token + colorama.Fore.RESET)
        elif token.isalpha():
            print("Identificador:", token)
        elif token.startswith("//"):
            print(colorama.Fore.YELLOW + "Comentario de línea: " + token + colorama.Fore.RESET)
        else:
            print("Token no reconocido:", token)




    print("_" * 30)