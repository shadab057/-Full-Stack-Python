x = 10  # ✅
# 5 = 10  # ❌  SyntaxError
_x = 20  # ✅
x_5 = 30  # ✅
# my-var = 40  # ❌ SyntaxError
_2=50  # ✅
# if = 60  # ❌ SyntaxError (reserved word)
# for = 70  # ✅ (allowed, but not recommended)
# class = 80  # ✅ (allowed, but not recommended)
print(x, _x, x_5,_2)
# print(for, class)