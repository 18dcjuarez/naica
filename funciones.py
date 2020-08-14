#! /usr/bin/python
import os
from datetime import datetime, date
import constant

# FUNCIÓN QUE PIDE LA FECHA DEL USUARIO
def date_setter():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia contenido de consola windows o unix
    aux_date = input("Ingresa la fecha \"AAAA-MM-DD\": ")
    return date_validator(aux_date)


# OPCIONES DE ERROR
def date_error(error_message):
    os.system('cls' if os.name == 'nt' else 'clear') # Limpia contenido de consola windows o unix
    print('{}'.format(error_message))
    resp = input('Ingresa \"s\" para reintentar o \"n\" para tomar la fecha actual: ')
    if resp.lower() == 's':
        return date_setter()
    elif resp.lower() == 'n':
        td = datetime.now()
        return {
            'success': True,
            'message': '{anio}-{month}-{day}'.format(anio=td.year, month=td.month, day=td.day)
        }
    else:
        date_error(error_message)


# FUNCIONES DE VALIDACION 
def date_validator(input_date):
    input_date_array = input_date.split("-")
    formated_date = date(int(input_date_array[0]), int(input_date_array[1]), int(input_date_array[2]))
    if len(input_date_array) != 3:  # Primer filtro de fecha, verifica que se haya introducido año, mes y día
        return {
            'success': False,
            'message': 'Formato incorrecto',
        }
    
    for i, item in enumerate(input_date_array):
        if i == 0:  # Verifica que el año tenga un formato correcto
            if len(item) != 4:
                return {
                    'success': False,
                    'message': 'El año es incorrecto incorrecto',
                }
        else :  # verifica que formato de día y mes sea correcto
            if len(item) != 2:
                return {
                    'success': False,
                    'message': 'El mes o día es incorrecto',
                }
            if i == 1: # verifica el mes
                if 0 >= int(item) or int(item) >= 13:
                    return {
                        'success': False,
                        'message': 'El mes es incorrecto',
                    }
            if i == 2: # verifica el día
                if 0 >= int(item) or int(item) > constant.DAYSOFMONTH[input_date_array[1]]:
                    return {
                        'success': False,
                        'message': 'El día es incorrecto',
                    }
    if formated_date < datetime.now().date():
        return {
            'success': False,
            'message': 'La fecha no puede ser anterior a la de hoy'
        }
    return {
        'success': True,
        'message': input_date
    }

# PIDE EL MONTO A INVERTIR
def invesment_setter():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia contenido de consola windows o unix
    invesment = input("Ingresa el monto a invertir: ")
    return float(invesment)

# PIDE LA TASA DE RETORNO
def rate_setter():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia contenido de consola windows o unix
    rate = input("Ingresa la tasa anual: ")
    return int(rate)

# FUNCION CON OPERACIONES PARA CALCULAR TABLA DE AMORTIZACIÓN
def quantities_setter(inv_amount, annual_rate):
    rate = annual_rate/100
    revenues = (inv_amount * rate)/12
    isr = ((constant.ISR/100)*inv_amount)/12
    return rate, revenues, isr

#REGRESA UNA FECHA CON EL FORMATO ESPECIFICADO
def date_format(index, date):
    date_array = date.split("-")
    date_array[1] = str(int(date_array[1]) + index)
    if int(date_array[1]) > 12:
        aux_res = int(date_array[1]) - 12
        date_array[0] = str(int(date_array[0]) + 1)
        date_array[1] = str(aux_res)
    return '{anio}-{month}-{day}'.format(
        anio=date_array[0],
        month=date_array[1] if (int(date_array[1]) > 9) else '0{}'.format(date_array[1]), 
        day=date_array[2]
    )