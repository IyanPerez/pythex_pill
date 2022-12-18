
print("---COMPROBADOR DE HORAS TRABAJADAS---")

def comprobar_horas_trabajadas():   
    horas=float(input("Introduzca las horas trabajadas: "))
    print(horas)
    if horas>=7.45 and horas<=8.15:                       
        resultado="--> Cumple minimos"
    elif horas>8.15:                       
        resultado="--> Exceso de horas, MAÑANA RECIBIRÁ UN CORREO DE RECUSOS HUMANOS!!!"         
    else:                                
        resultado="--> No cumple minimos, MAÑANA RECIBIRÁ UN CORREO DE RECUSOS HUMANOS!!!"
    return resultado

print(comprobar_horas_trabajadas())
print(comprobar_horas_trabajadas())
print(comprobar_horas_trabajadas())

# print("---COMPROBADOR DE ZONA EN UN EVENTO---")

""" def comprobar_butaca():
    num_butaca=int(input("Introduzca el num. de butaca (0-300):"))

    if 0<num_butaca<=100:
        zona="FOSO"
    elif 100<num_butaca<=150:
        zona="TRIBUNA IZQ"
    elif 150<num_butaca<=200:
        zona="TRIBUNA DCHA"
    elif 200<num_butaca<=250:
        zona="TRIBUNA CENTRAL"
    else:
        zona="ZONA VIP"
    return "Su zona es: " + zona 

print(comprobar_butaca())
print("Disfrute del evento")"""