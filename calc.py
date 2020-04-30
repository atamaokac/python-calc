# 整数を2つ入力する
print('整数を2つ1行で入力してください。')
A, B = input().split()
a = int(A)
b = int(B)
print('入力された数は', a, b)
# 足し算
print('和は', a+b)
# 引き算
print('差は', a-b)
# 掛け算
print('積は', a*b)
# 割り算
print('商は', a//b, ', 余りは', a % b) # 未完成。余りも必要。
