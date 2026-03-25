import random
import re

# Define the regex-like patterns for Variant 2
regex_patterns = [
    r"\u? N^2 (O|P)^3 Q^* R^+",
    r"(X|Y|Z)^3 8^+ (9|0)",
    r"(H|i) (J|K) L^* N?"
]

# Function to generate a random choice from a group or single character
def generate_from_token(token):
    if token.startswith("(") and token.endswith(")"):  # it's a group
        group_content = token[1:-1]
        options = group_content.split("|")
        return random.choice(options)
    elif token.startswith("\\u"):  # optional μ
        return "μ" if random.choice([True, False]) else ""
    else:
        return token

# Function to parse and generate strings from a simple regex-like pattern
def generate_from_pattern(pattern):
    # Split by space for simplicity
    tokens = pattern.split()
    result = []
    sequence = []  # for bonus: track processing

    for token in tokens:
        base = token
        repeat_min = repeat_max = 1

        # Check for repetitions: ^*, ^+, ^? and limits
        if "^*" in token:
            base = token.replace("^*", "")
            repeat_min, repeat_max = 0, 5
        elif "^+" in token:
            base = token.replace("^+", "")
            repeat_min, repeat_max = 1, 5
        elif "^?" in token:
            base = token.replace("^?", "")
            repeat_min, repeat_max = 0, 1
        elif "^" in token and token[-1].isdigit():  # exact repetition like ^2
            parts = token.split("^")
            base = parts[0]
            repeat_min = repeat_max = int(parts[1])

        # Generate repeated characters
        count = random.randint(repeat_min, repeat_max)
        generated = ''.join(generate_from_token(base) for _ in range(count))
        result.append(generated)
        sequence.append(f"Processed '{token}' -> '{generated}'")

    return ' '.join(result), sequence

# Generate examples
for pattern in regex_patterns:
    generated_string, process_sequence = generate_from_pattern(pattern)
    print("Generated string:", generated_string)
    print("Processing sequence:")
    for step in process_sequence:
        print(" ", step)
    print()