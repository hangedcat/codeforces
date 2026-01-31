import sys

def solve():
    input = sys.stdin.buffer.readline
    
    rep = int(input())
    
    for _ in range(rep):
        length = int(input())
        color = list(map(int, input().split()))
        unique_set = set(color)
        num_unique = len(unique_set)
        
        result = float('inf')
        
        for val in unique_set:
            if val >= num_unique and val < result:
                result = val
                if result == num_unique:
                    break
        
        print(result)

if __name__ == "__main__":
    solve()