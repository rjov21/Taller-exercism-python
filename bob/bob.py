def response(hey_bob):
    
    x = len(hey_bob)
    respuesta = "Whatever."
    if x == 0:
        respuesta = "Fine. Be that way!"
    else:
        if  hey_bob[x - 1] == "?" or hey_bob[x - 1] == " ":
            respuesta = "Sure."    
        if hey_bob.isupper() == True and hey_bob[x - 1] == "?":
            respuesta == "Calm down, I know what I'm doing!"
        if hey_bob.isupper() == True:
            respuesta = "Whoa, chill out!"
        if  hey_bob[len(hey_bob) - 4] == " " and hey_bob[len(hey_bob) - 1] == " ":
            respuesta = "Whatever."
        if hey_bob.strip() == "":
            respuesta = "Fine. Be that way!"
    return respuesta
