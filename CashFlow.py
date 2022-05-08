import pandas as pd
import datetime

#cf = pd.read_csv('PF_Pivot1.csv', delimiter=';')
#Questa forma permette di trasformare le colonne numeriche in int con punto per decimale e senza punti per migliaia
cf = pd.read_csv("PF_Pivot1.csv", sep=';', header=0, skip_blank_lines=True, decimal=',',thousands='.')

print(cf.head(10))

def blank_cell(cf):
    '''Funzione completa per la sostituzione dei nomi nella
    colonna Fornitore dove le celle sono vuote la funzione
    riporta il nome della prima cella in alto non vuota fino a che
    trova una cella vuota '''
for i in range(len(cf)):
    if not pd.isna(cf.loc[i, 'Fornitore']):
        cp=cf.loc[i, 'Fornitore']
        print(cf.loc[i, 'Fornitore'])
    else:
        cf.loc[i, 'Fornitore']=cp
        #print('vuota')

'''Creazione della lista di tipi di pagamento unici 
attraverso l'uso di se()
la variabole pag contiene l'elenco unico dei tipi di pagamento'''

pag = set(cf.loc[0:,'Pagamento Documento'])

#DOTO List
'''
- creazione della colonna mese di pagamento in cui si indica il mese di pagamento. 
La colonna è popolata con una funzione che usa i valori nella colonna OrAcq - Data Effettiva Evasione e
se guesta è vuota dalla colonna OrAcq - Data Prevista Evasione e estrare il mese usando il modulo datetime
- una volta creata la tabella si possono creare delle funzioni di aggregazione legate al
 nome del fornitore,data pagamento e tipo di pagamento suddiviso per i mesi dell'anno e il totale
- nelle righe i nomi dei fornitori con gli importi aggregati e sommati per mese e tipo di pagamento
'''

'''La formula per raggruppare per colonne e fare la somma dei valori: 
questa stringa ci serve per raggruppare i fornitori per data e fare la somma dei valori indicati in sum'''

cf.groupby(['Fornitore','OrAcq - Data Prevista Evasione']).sum()

'''questo è il modo per scegliere la colonna da sommare, as_index=False server per riportare il nome del fornitore su tutte
le righe'''
cf.groupby(['Fornitore','OrAcq - Data Prevista Evasione'], as_index=False)['OrAcq - Importo Generale Evaso 1'].sum()

'''dopo questo è possibile usare le funzione groupby per sommare gli importi '''

'''le colonen da dropapre perché non mi servono
- Articolo, OrAcq - Numero Documento, Causale Documento, 

il comando prr dropapre in maniera permanente in pandas è:
df.drop('Articolo', inplace=True, axis=1)

'''

    