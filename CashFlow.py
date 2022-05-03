import pandas as pd
import datetime

cf = pd.read_csv('PF_Pivot1.csv', delimiter=';')
print(cf.head(10))

#crea nuova variabile che contiene lelenco fornitori
#f = cf.loc[0:,'Fornitore']
'''La modifica fianle non ustilizzerà la nuova variabile ma la modifica sarà 
fatta direttamente nelal tabella'''

def blank_cell(cf):
    '''Funzione comoleta per la sostituzione dei nomi nella
    colonna Fornitore dove le celle sono vuote la funzione
    riporta il nome della prima cella in alto fino a che
    non trova un nuova cella vuota '''
for i in range(len(cf)):
    if not pd.isna(cf.loc[i, 'Fornitore']):
        cp=cf.loc[i, 'Fornitore']
        print(cf.loc[i, 'Fornitore'])
    else:
        cf.loc[i, 'Fornitore']=cp
        #print('vuota')

'''Creazione della lista di modi di pagamento unico 
attraverso l'uso di se()
la variabole pag è l'elenco unico dei tipi di pagamento'''

pag = set(cf.loc[0:,'Pagamento Documento'])

#DOTO List
'''
- creazione della colonna mese di pagamento in cui si indica il mese di pagamento. 
La colonna è popolata con una funzione che usa i valori nella colonna OrAcq - Data Effettiva Evasione e
se guesta è vuota dalla colonna OrAcq - Data Prevista Evasione e estrare il mese usando il modulo datetime
- una volta creata la tabella si possono creare delle funzioni di aggregazione che abbia come
 il nome del fornitore il tipo di pagamento i mesi dell'anno e il totale
- nelle righe i nomi dei fornitori con gli importi aggregati e sommasi per mese e tipo di pagamento
'''
