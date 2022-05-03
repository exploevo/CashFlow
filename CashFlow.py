import pandas as pd

cashflow = pd.read_csv('PF_Pivot1.csv', delimiter=';')
print(cashflow.head(10))

def blank_cell():
    '''Funzione da completare per la sostituzione dei nomi nella
    colonna fonritori dove le celle sono vuote 
    La funzione va impelementara è stato testato solo il ciclo '''
    for i in range(len(f)):
        if not pd.isna(f[i]):
            cp=f[i]
            print(f[i])
        else:
            f[i]=cp
            #print('vuota')