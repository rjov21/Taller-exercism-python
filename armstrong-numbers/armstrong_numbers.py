def is_armstrong_number(number):
    respuesta = False
    total = 0
    num = str(number)
    for x in num:
	    total += int(x) ** len(num)
    if total == number:
	    respuesta = True
    else:
	    respuesta = False
    return respuesta
