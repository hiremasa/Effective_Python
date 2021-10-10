# for の後のelse
for i in range(3):
    print('Loop', i)
else:
    print('Else block')


#実行されない
for i in range(3):
    print('Loop', i)
    if i == 1:
        break
else:
    print('Else block')

#空シーケンスだとelseがすぐ実行される
for x in []:
    print('Never RUns')
else:
    print('For Else Block')

#elseブロックはwhileブロックが頭で失敗したときにも実行される
while False:
    print('Nevet Runs')
else:
    print('While Else Blocks')

#使用例: 互いに素
a = 4
b = 9

for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0 :
        print('Not coprinme')
        break
else:
    print('Coprime')
