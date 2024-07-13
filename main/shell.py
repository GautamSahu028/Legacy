import legacy

while True:
    text = input('legacy > ')
    result, error = legacy.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)