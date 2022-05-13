for num in range(1, 101):
    string = ''

    # ここから記述
    
    # 3の倍数の場合
    if num % 3 == 0:
        string += 'Fizz'

    # 5の倍数の場合
    if num % 5 == 0:
        string += 'Buzz'
        
    # 3の倍数でも5の倍数でもない場合
    if string =='':
        string+=str(num)

    # ここまで記述

    print(string)