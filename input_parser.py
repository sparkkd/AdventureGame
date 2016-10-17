def Parse_Input(user_input):
    output = ""

    for char in user_input:
        if char.isalpha() or char.isdigit() or char == " ":
            output += char

    while "  " in output:
        output.replace("  ", "")
    
    return output.strip().lower().split(" ")
