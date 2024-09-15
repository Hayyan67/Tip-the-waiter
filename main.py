amt=int(input('Enter a number'))
tip=int(input('Enter the amount'))

def total_cut(amt,tip):
    total=amt+tip/100*amt
    print('Total is:',total)
    total_cut(amt,tip)