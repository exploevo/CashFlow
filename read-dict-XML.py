#importo tutti i moduli necessari
import os, path
import xmltodict
import pandas as pd
from xml.parsers.expat import ExpatError
from pathlib import Path

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
   
non_validi=[]
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
        non_validi.append(nome_file(path))
        print (non_validi)

ex_dic={'Denominazione_emit':[],'CodiceFiscale_emit':[],'IVA_emit':[], 'Deniminazione_comm':[]
        ,'CodiceFiscale_comm':[],'IVA_comm':[]}
def dict_Header(df):
    #TODO inderie il controllo tra denominazione (aziende) e Nome Cognome (ditte individuali)
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
    
xml_dir='allegati/xmlfiles/EMESSE/'
ex_dic={'Denominazione_emit':[],'CodiceFiscale_emit':[],'IVA_emit':[], 'Deniminazione_comm':[]
        ,'CodiceFiscale_comm':[],'IVA_comm':[]}

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
            