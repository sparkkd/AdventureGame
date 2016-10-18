words_to_remove = ['at', 'please', 'a', 'about', 'all', 'an', 'another', 'any', 'around',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']

def Parse_Input(user_input):
    output = ""

    for char in user_input:
        if char.isalpha() or char.isdigit() or char == " ":
            output += char

    while "  " in output:
        output.replace("  ", "")

    output = output.strip().lower().split(" ")

    filtered = []

    for word in output:
        if word not in words_to_remove:
            filtered.append(word)
    
    return filtered
