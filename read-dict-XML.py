#importo tutti i moduli necessari
import os, path
import xmltodict
import pandas as pd
from xml.parsers.expat import ExpatError
from pathlib import Path

#Dichiarazioni delle Variabili di lavoro
xml_dir='allegati/xmlfiles/EMESSE/'
dst_path="allegati/xmlfiles/INVALIDI/"
ex_dic={'Denominazione_emit':[],'CodiceFiscale_emit':[],'IVA_emit':[], 'Deniminazione_comm':[]
        ,'CodiceFiscale_comm':[],'IVA_comm':[]}
non_validi=[]

def file_xml_list(path):
    #legge ricursivamente i file nella direcotry data
    for root, dirs, files in os.walk(path, topdown = True):
        for name in files:
            print(os.path.join(root, name))
       # for name in dirs:
       #     print(os.path.join(root, name))

def nome_file(path):
    #la funzione verifica che estra il file da un path verificando che sia un file 
    path = Path(path)
    head, tail = os.path.split(path)
    if path.is_file():
        return tail
    else:
        print('Path does not refer to a valid File\nProvide a correct path to File!')
   
def file_xml_read(path):
    #NB nella versione defintiva la variabile va in radice
    #legge il file xml ed estrae i dai in un DataFrame
    try:
        with open(path, encoding='unicode_escape') as fd:
            obj = xmltodict.parse(fd.read())
            df = pd.DataFrame(obj)
            return df
            #resta da inserie i dati del dataframe in un dizionario (e successivamente in un db)
    except xmltodict.expat.ExpatError:
        #se non risce ad aprire il file aggiunge il nome ad una lista
        #Aggiunta filtro se file .DS (apple)
        if name.startswith('.DS_'):
            pass
        else:
            non_validi.append(nome_file(path))
            print (non_validi) 

def dict_Header(df):
    #TODO inderie il controllo tra denominazione (aziende) e Nome Cognome (ditte individuali)
    try:
        #estraggo i valori dal Dataframe da inserire nel Dizionario   
        emit=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CedentePrestatore']['DatiAnagrafici']['Anagrafica']['Denominazione']
        cf_emit=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CedentePrestatore']['DatiAnagrafici']['CodiceFiscale']
        piva_emit=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CedentePrestatore']['DatiAnagrafici']['IdFiscaleIVA']['IdCodice']
        comm=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CessionarioCommittente']['DatiAnagrafici']['Anagrafica']['Denominazione']
        cf_comm=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CessionarioCommittente']['DatiAnagrafici']['CodiceFiscale']
        piva_comm=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CessionarioCommittente']['DatiAnagrafici']['IdFiscaleIVA']['IdCodice']
        #Inserisco i valori nel Dizionario
        ex_dic['Denominazione_emit'].append(emit)
        ex_dic['CodiceFiscale_emit'].append(cf_emit)
        ex_dic['IVA_emit'].append(piva_emit)
        ex_dic['Deniminazione_comm'].append(comm)
        ex_dic['CodiceFiscale_comm'].append(cf_comm)
        ex_dic['IVA_comm'].append(piva_comm)
    except KeyError as e:
        #Se non esiste il campo Denominazione prendo il Nome e il Cognome
        emit=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CedentePrestatore']['DatiAnagrafici']['Anagrafica']['Denominazione']
        cf_emit=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CedentePrestatore']['DatiAnagrafici']['CodiceFiscale']
        piva_emit=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CedentePrestatore']['DatiAnagrafici']['IdFiscaleIVA']['IdCodice']
        comm_n=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CessionarioCommittente']['DatiAnagrafici']['Anagrafica']['Nome']
        comm_c=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CessionarioCommittente']['DatiAnagrafici']['Anagrafica']['Cognome']
        cf_comm=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CessionarioCommittente']['DatiAnagrafici']['CodiceFiscale']
        piva_comm=df['p:FatturaElettronica']['FatturaElettronicaHeader']['CessionarioCommittente']['DatiAnagrafici']['IdFiscaleIVA']['IdCodice']
        #Inserisco i valori nel Dizionario
        ex_dic['Denominazione_emit'].append(emit)
        ex_dic['CodiceFiscale_emit'].append(cf_emit)
        ex_dic['IVA_emit'].append(piva_emit)
        ex_dic['Deniminazione_comm'].append(comm_n+' '+comm_c)
        ex_dic['CodiceFiscale_comm'].append(cf_comm)
        ex_dic['IVA_comm'].append(piva_comm)
        #print ('I got a KeyError - reason "%s"' % str(e))
        #print(comm_n+' '+comm_c)
    
    

def dict_xml_create(path):
       for root, dirs, files in os.walk(path, topdown = True):
        for name in files:
            #se il dile inizia con .DS (file srchivio Apple)
            if name.startswith('.DS_'):
                pass
            else:
                #print(name)
                df=file_xml_read(os.path.join(root, name))
                dict_Header(df)
            