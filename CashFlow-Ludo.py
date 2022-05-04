import pandas as pd
import numpy as np
import math


def getMesiAnniFromDate(date_effettive, date_previste):
    mesi = []
    anni = []
    for i, de in enumerate(date_effettive):
        if str(de) != 'nan' and str(de) != 'Non definito':
            spl = de.split()
            mesi.append(spl[1])
            anni.append(int(spl[2]))
        else:
            dp = date_previste[i]
            if str(dp) != 'nan':
                spl = dp.split()
                mesi.append(spl[1])
                anni.append(int(spl[2]))
            else:
                mesi.append('nan')
                anni.append(-1)

    return mesi, anni

def formatFornitore(fornitori):
    fornitori_formatted = []
    for f in fornitori:
        if str(f) != 'nan':
            f_attuale = f
            fornitori_formatted.append(f)
        else:
            fornitori_formatted.append(f_attuale)

    return fornitori_formatted



def preprocessing(df):

    date_effettive = df['OrAcq - Data Effettiva Evasione'].values
    date_previste = df['OrAcq - Data Prevista Evasione'].values
    mesi, anni = getMesiAnniFromDate(date_effettive, date_previste)

    fornitori = df['Fornitore'].values
    fornitori_formatted = formatFornitore(fornitori)


    df_prep = pd.DataFrame()
    df_prep['Fornitore'] = fornitori_formatted
    df_prep['Mese'] = mesi
    df_prep['Anno'] = anni

    return df_prep

df = pd.read_csv("PF_Pivot1.csv", sep=';', encoding='utf-8')
print(df.describe(include='all'))
print(df.columns)

df_new = preprocessing(df)

print("FINE")