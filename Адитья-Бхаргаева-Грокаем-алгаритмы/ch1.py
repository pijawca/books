'''
Имеется отсортированный список из 128 имен, и вы ищете в нем зна-
чение методом бинраного поиска. Какое максимальное количество
проверок для этого может потребоваться?
'''

def search(lst, item):
    low = 0
    high = len(lst) - 1
    attempts = 0
    
    while low <= high:
        attempts += 1
        mid = (low + high) // 2
        guess = lst[mid]
        
        print(f'Попытка {attempts} : индекс {mid} : значение {guess}')
        
        if guess == item + 1:
            print(f'Количество попыток: {attempts}')
            return mid
        
        if guess > item + 1:
            high = mid - 1
        else:
            low = mid + 1
            
    return None

my_list = list(range(1, 128))
index = search(my_list, 64)

'''
Предположим, размер списка увеличился вдвое. Как изменится мак-
симальное количество проверок?
'''

def search(lst, item):
    low = 0
    high = len(lst) - 1
    attempts = 0
    
    while low <= high:
        attempts += 1
        mid = (low + high) // 2
        guess = lst[mid]
        
        print(f'Попытка {attempts} : индекс {mid} : значение {guess}')
        
        if guess == item + 1:
            print(f'Количество попыток: {attempts}')
            return mid
        
        if guess > item + 1:
            high = mid - 1
        else:
            low = mid + 1
            
    return None

my_list = list(range(1, 256))
index = search(my_list, 128)