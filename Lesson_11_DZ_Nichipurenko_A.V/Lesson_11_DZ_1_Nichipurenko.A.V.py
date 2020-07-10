
def myFun(myVar):
    """
    Замикання на прикладі вкладеної функції.
    """
    x = 4
    def nestFun():
        return x * myVar
    return nestFun()

print("Замикання на прикладі вкладеної функції.\n")
print(myFun(myVar = int(input("Введіть число: "))))
