def currency_convert(ammount): 
    print( 'enter country titel : ')
    titel=  int('choose a titel via number \n 1. USA \n 2.CND \n  3.AUD \n  4.INR \n  5.JPY \n  6. NZD 7. OMR \n 8.  RUB ')
    if titel ==  1 : 
        print(f' {ammount } bd taka to USA  dollar is {ammount * 102 }')
        
    elif titel ==  2 : 
        print(f' {ammount } bd taka to CND   dollar is {ammount * 74}')
    elif titel ==  3 : 
        print(f' {ammount } bd taka to Austrelian dollar :  dollar is {ammount * 67.04 }')
    elif titel ==  4 : 
        print(f' {ammount } bd taka to Indian ruppy  is {ammount *1.63 }')
    elif titel ==  5 : 
        print(f' {ammount } bd taka to  japanise yan  is {ammount * 0.73}')
    elif titel ==  6 : 
        print(f' {ammount } bd taka to  NZ   dollar is {ammount * 61.82 }')
    elif titel ==  7 : 
        print(f' {ammount } bd taka to  oman  is {ammount * 263.83 }')
    elif titel ==  8 : 
        print(f' {ammount } bd taka to russian rubel  is {ammount * 1.63 }')
    else : 
        print('invalid input : ')
        
amm=  int(input('enter the ammount : '))
print(currency_convert(amm))