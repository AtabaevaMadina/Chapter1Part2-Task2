students=int(input("Skol'ko studentov:"))
apples=int(input("Skol'ko apples:"))
distribute=apples//students
basket=apples%students
print("po {} u kajdogo studenta".format(distribute))
print('ostalos {} apple'.format(basket))