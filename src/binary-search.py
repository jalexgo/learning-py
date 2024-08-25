
print('set list length')
numberOfElements = int(input())
sample = list(range(numberOfElements))

print('len', len(sample))
print('Give me a number to search')
numberToSearch = int(input())

high = len(sample) - 1
low = 0
iterations = 0
pointer = high // 2


while True:    
    iterations+=1
    pointer = (low + high) // 2
    selectedItem = sample[pointer]

    print('selected', pointer)
    if selectedItem == numberToSearch:
        print('Ready')
        break
    elif selectedItem > numberToSearch:
        high = pointer - 1
    else:
        low = pointer + 1

print(iterations)