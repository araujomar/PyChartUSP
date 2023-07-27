# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import glob
import pandas as pd

def transform():
    folder = input("Caminho da pasta: ") 
    paths = glob.glob(fr"{folder}\*")
    columns= [
        "Time (min)",
        "Temperature (°C)",
        "Weight (mg)",
        "Balance Purge Flow (mL/min)",
        "Sample Purge Flow (mL/min)",
        "Deriv. Weight (%/°C)"
        ]
    f = paths[0]
    for f in paths:
        filename = f.split("\\")[-1].split(".")[0]
        dfd = pd.DataFrame(columns=columns)            
        with open(f) as file:
            txt = file.readlines()
            list_temp = []
            for row in txt:
                if row != "\n":
                    row_temp = row.split(";")
                    list_temp.append(row_temp)
            
        df_temp = pd.DataFrame(columns=columns, data=list_temp)
        dfd = pd.concat([dfd, df_temp], ignore_index=True)
    
        for c in columns:    
            dfd[c] = dfd[c].apply(float)
        dfd["Relative Mass (%)"] = dfd["Weight (mg)"].apply(
            lambda x: (x / dfd["Weight (mg)"][0]) * 100
            )
        dfd = dfd[[
            'Time (min)',
            'Weight (mg)',
            'Deriv. Weight (%/°C)',        
            'Relative Mass (%)',
            'Temperature (°C)',
            'Balance Purge Flow (mL/min)',         
            'Sample Purge Flow (mL/min)'
            ]]
        dfd.to_csv(f"{folder}\\{filename}_new.txt", sep="\t", header=True, index=False)


transform()