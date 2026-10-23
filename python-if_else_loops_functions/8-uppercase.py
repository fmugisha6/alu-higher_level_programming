
#!/usr/bin/python3
def uppercase(str):
    result = ""
    for letter in str:
        code = ord(letter)
        if code >= 97 and code <= 122:
            code -= 32
        result += "{:c}".format(code)
    print("{}".format(result))
