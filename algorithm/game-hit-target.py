def solution(mtrx):
    for i in mtrx:
        if '>' in i and 'x' in i :
            return i.index('>')<i.index('x')
        elif '<' in i and 'x' in i :
            return i.index('<')>i.index('x')
        else: continue
    
    for i in range(len(mtrx)):
        col=[j[i] for j in mtrx]
        if '^' in col and 'x' in col :
            return col.index('^')>col.index('x')
        elif 'v' in col and 'x' in col :
            return col.index('v')<col.index('x')
        
    return False