# Ex1
# Compute len() recursively
def comprimento(lst):
    if lst == []:
        return 0
    else:
        return 1 + comprimento(lst[1:])

# Ex2
# Return bool if/if not value exists in list
def ocorre(lst, x):
    if lst == []:
        return False
    if lst[0] == x:
        return True
    
    return(ocorre(lst[1:], x))

# Ex8
# 
def substituir(lst,x,y):
    if lst == []:
        return []
    
    rec = substituir(lst[1:],x,y)
    return [y]+rec if lst[0]==x else lst[1:]+rec

if __name__ == '__main__':
    print(comprimento([1,2,59]))

    print(ocorre([1,2,59], 3))

    print(substituir([1,2,59],1,5))