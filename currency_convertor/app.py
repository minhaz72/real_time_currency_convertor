from forex_python.convertor import CurrencyRate 
c= CurrencyRate()
ammoutn=  int(input('enter the ammount : '))
from_cur= input('Form Currency : ').upper()
to_cur= input('TO Currency : ').upper()
print(f'{from_cur }, to {to_cur }')
result= c.convert(from_cur , to_cur , ammoutn )
print(result )