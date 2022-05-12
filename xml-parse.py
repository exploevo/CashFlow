import xmltodict
import pandas as pd

with open('allegati/IT0446499048202238_F0016.xml') as fd:
    obj = xmltodict.parse(fd.read())

#paese = obj['p:FatturaElettronica']['FatturaElettronicaHeader']['DatiTrasmissione']['IdTrasmittente']['IdPaese']

df = pd.DataFrame(obj)

print (df['p:FatturaElettronica']['FatturaElettronicaHeader'])
print (df['p:FatturaElettronica']['FatturaElettronicaBody'])

'''NOTE PER FATTURE ELETTRONICHE
La fattura elettronica ha un formato ben preciso che include diversi campi per cui bisogna specificare delle informazioni o codici.

Le modalità di pagamento ammesse per la fattura elettronica con i relativi codici sono le seguenti:
Contanti (MP01)
Assegno (MP02)
Assegno circolare (MP03)
Contanti presso Tesoreria (MP04)
Bonifico (MP05)
Vaglia cambiario (MP06)
Bollettino bancario (MP07)
Carta di credito (MP08)
RID (MP09)
RID utenze (MP10)
RID veloce (MP11)
Riba (MP12)
MAV (MP13)
Quietanza erario stato (MP14)
Giroconto su conti di contabilità speciale (MP15)
Domiciliazione bancaria (MP16)
Domiciliazione postale (MP17)\

La condizione di pagamento può essere impostata su:

Non configurato: non viene gestito il tipo di pagamento; TP01 Pagamento a rate: viene impostato un pagamento a rate dove è possibile impostare una sola rata, nel caso infatti in cui il cliente non abbia saldato la fattura al momento dell’emissione o sia necessario indicare dei dati Bancari, attraverso questo tipo di pagamento sarà possibile impostare tali dati. TP02 Pagamento completo: va impostato nel caso in cui il pagamento sia stato già completato; TP03 Anticipo: nel caso in cui un cliente depositi un anticipo si potrà utilizzare questa modalità di pagamento indicando i dati specifici.

TipoDocumento: formato alfanumerico; lunghezza di 4 caratteri; i valori ammessi sono i seguenti:
TD01 Fattura
TD02 Acconto/Anticipo su fattura
TD03 Acconto/Anticipo su parcella
TD04 Nota di Credito
TD05 Nota di Debito
TD06 Parcella
TD20 Autofattura \

DataRiferimentoTerminiPagamento: la data deve essere rappresentata secondo il formato ISO 8601:2004, con la seguente precisione: YYYY-MM-DD.

GiorniTerminiPagamento: formato numerico di lunghezza massima pari a 3. Vale 0 (zero) per pagamenti a vista.

DataScadenzaPagamento: la data deve essere rappresentata secondo il formato ISO 8601:2004, con la seguente precisione: YYYY-MM-DD.

ImportoPagamento: formato numerico nel quale i decimali vanno separati dall'intero con il carattere '.' (punto). La sua lunghezza va da 4 a 15 caratteri.

 **TODO LIST**
Elementi da mettere a fuoco:\
1 Pandas Filter\
2 upload multiplo file\
3 creazione dizionario con dati selezionati\
'''