import pandas as pd

cf = pd.read_csv('PF_Pivot1.csv', delimiter=';')
print(cf.head(10))

#crea nuova variabile che contiene lelenco fornitori
f = cf.loc[0:,'Fornitore']
'''La modifica fianle non ustilizzerà la nuova variabile ma la modifica sarà 
fatta direttamente nelal tabella'''

def blank_cell(f):
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