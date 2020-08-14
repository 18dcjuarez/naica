#! /usr/bin/python
import os
from funciones import (date_setter, date_error, invesment_setter, rate_setter, quantities_setter,
                        date_format)
import constant

resp_date = {
    'success': False,
    'message': '2020-12-12',
}

inv_amount = 0.0
annual_rate =  0

while resp_date['success'] is False:
    resp_date = date_setter()
    if resp_date['success'] is False:
        resp_date = date_error(resp_date['message'])

while inv_amount <= 0.0:
    inv_amount = invesment_setter()

while annual_rate <= 0:
    annual_rate = rate_setter()

os.system('cls' if os.name == 'nt' else 'clear')  # Limpia contenido de consola windows o unix

rate, revenues, isr = quantities_setter(inv_amount=inv_amount, annual_rate=annual_rate)
aux_calc = revenues - isr

print('Fecha inversión: {}'.format(resp_date['message']))
print('Inversión: {}'.format(inv_amount))
print('Tasa anual: {}% \n'.format(annual_rate))

print('MES   Cut off date   Initial Capital   Rate    Revenues    ISR     Accumulated Revenues')

for index in range(12):
    print('{index}     {fecha}        {inv}        {rate}      {revenues}      {isr}          {accrev}'
        .format(index=index+1 if (index+1 > 9) else '0{}'.format(index+1),
                fecha=date_format(index=index + 1, date=resp_date['message']), inv=inv_amount, 
                rate=round(rate, 2), revenues=round(revenues, 2), isr=round(isr, 2), 
                accrev=round(aux_calc * (index + 1), 2)
        )
    )
print('\nTOTAL      NaN            NaN          NaN      {totalrevs}      {totalisr}          NaN'
    .format(totalrevs=round(revenues*12, 2), totalisr=round(isr*12, 2))
)
