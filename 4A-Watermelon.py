weight: str = int(input())

def watermelon(x) -> str:
    if x % 2 == 0 and x != 2:
        return 'YES' 
    else:
        return 'NO'

print(watermelon(weight))



