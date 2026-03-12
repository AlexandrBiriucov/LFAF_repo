import re
file_path='commands.txt' 
TOKEN_TYPES = [
    ("INTERFACE", r"interface"),
    ("IP", r"ip"),
    ("MASK", r"mask"),
    ("ROUTE", r"route"),
    ("VIA", r"via"),
    ("ENABLE", r"enable"),
    ("IP_ADDRESS", r"\d+\.\d+\.\d+\.\d+"),
    ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("NUMBER", r"\d+"),
]

def lexer(code):
    tokens = []

    words = code.split()

    for word in words:
        matched = False
        for token_type, pattern in TOKEN_TYPES:
            if re.fullmatch(pattern, word):
                tokens.append((token_type, word))
                matched = True
                break
        
        if not matched:
            tokens.append(("UNKNOWN", word))

    return tokens


# code = """
# interface eth0
# ip 192.168.1.1
# route 0.0.0.0 via 192.168.1.254
# enable
# """


try: 
    with open(file_path,'r') as file:
        code=file.read()




except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

tokens = lexer(code)

for token in tokens:
    print(token)