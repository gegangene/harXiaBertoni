model_big='''
     1  2  3  4  5  6  7  8  9
    1
    2   B     B     B     B
    3
    4   B     B     B     B
    5
    6   B     B     B     B
    7
    8   B     B     B     B
    9
'''

model_staircase='''
     1  2  3  4 
    1
    2   B     B
    3      x xO
    4   B  x  B
    5   Ox x
    
'''
model_lateral='''
     1  2  3  4 
    1      
    2   B  O  B
    3      x
    4   B  x  B
    5   Ox x
    
'''
model_transverse='''
     1  2  3  4 
    1
    2   B     B
    3   Ox x
    4   B  x  B
    5   Ox x
    
'''
model_LOS='''
     1  2  3  4 
    1
    2   B     B
    3   Ox x xO
    4   B     B
    5
'''

models_merged='''
    [S]chodkowy:    [B]oczny:       [P]oprzeczny:
     1  2  3  4     1  2  3  4      1  2  3  4 
    1              1               1
    2   B     B    2   B  O  B     2   B     B
    3      x xO    3      x        3   Ox x
    4   B  x  B    4   B  x  B     4   B  x  B
    5   Ox x       5   Ox x        5   Ox x
Legenda:   
B — budynek; O — miejsca umieszczenia anten; x — przebieg trasy'''
