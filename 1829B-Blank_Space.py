rep = int(input())

for i in range(rep):
    lenght = int(input())
    arr = input().split(' ')
    arr = ''.join(arr)
    blank = '0'

    while blank in arr:
        blank += '0'

    print(len(blank)-1)

