milk_qty = 1000
coffee_qty = 1000
res = ''
d = {1:{'milk':0,'coffee':50},2:{'milk':15,'coffee':35},3:{'milk':20,'coffee':30},4:{'milk':35,'coffee':15},5:{'milk':50,'coffee':0}}
while milk_qty > 0 or coffee_qty > 0:
    if milk_qty <= 0:
        choice = int(input('only 1.black coffee available'))
        if choice == 1:
            res = 'milk'+':'+str(d[choice]['milk'])+','+'coffee'+':'+str(d[choice]['coffee'])
            milk_qty -= d[choice]['milk']
            coffee_qty -= d[choice]['coffee']
            print('milk left:',milk_qty,'coffee left',coffee_qty)
            print('milk')
            print(res)
        else:
            print('wrong choice')
    elif coffee_qty <= 0:
        choice = int(input('only 5.milk available'))
        if choice == 5:
            res = 'milk'+':'+str(d[choice]['milk'])+','+'coffee'+':'+str(d[choice]['coffee'])
            milk_qty -= d[choice]['milk']
            coffee_qty -= d[choice]['coffee']
            print('milk left:',milk_qty,'coffee left',coffee_qty)
            print('milk')
            print(res)
        else:
            print('wrong choice')
    else:    
        choice = int(input())
        if choice == 1:
            res = 'milk'+':'+str(d[choice]['milk'])+','+'coffee'+':'+str(d[choice]['coffee'])
            milk_qty -= d[choice]['milk']
            coffee_qty -= d[choice]['coffee']
            print('milk left:',milk_qty,'coffee left',coffee_qty)
            print('black coffee')
            print(res)
        elif choice == 2:
            res = 'milk'+':'+str(d[choice]['milk'])+','+'coffee'+':'+str(d[choice]['coffee'])
            milk_qty -= d[choice]['milk']
            coffee_qty -= d[choice]['coffee']
            print('milk left:',milk_qty,'coffee left',coffee_qty)
            print('strong coffee')
            print(res)
        elif choice == 3:
            res = 'milk'+':'+str(d[choice]['milk'])+','+'coffee'+':'+str(d[choice]['coffee'])
            milk_qty -= d[choice]['milk']
            coffee_qty -= d[choice]['coffee']
            print('milk left:',milk_qty,'coffee left',coffee_qty)
            print('medium coffee')
            print(res)
        elif choice == 4:
            res = 'milk'+':'+str(d[choice]['milk'])+','+'coffee'+':'+str(d[choice]['coffee'])
            milk_qty -= d[choice]['milk']
            coffee_qty -= d[choice]['coffee']
            print('milk left:',milk_qty,'coffee left',coffee_qty)
            print('light coffee')
            print(res)
        elif choice == 5:
            res = 'milk'+':'+str(d[choice]['milk'])+','+'coffee'+':'+str(d[choice]['coffee'])
            milk_qty -= d[choice]['milk']
            coffee_qty -= d[choice]['coffee']
            print('milk left:',milk_qty,'coffee left',coffee_qty)
            print('milk')
            print(res)
        else:
            print('wrong choice')
else:
    print('not available at the moment')