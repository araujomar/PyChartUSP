# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_save(chart_name, main_path, file_type="CSV"):
    paths = glob.glob(f"{main_path}\\*.{file_type}")
    df = pd.DataFrame()
    for f in paths:
       with open(f) as file:
           txt = file.readlines()
           list_temp = []
           for row in txt:
               row_temp = row.split(",")
               list_temp.append([float(row_temp[0]), float(row_temp[-1])])
           filename = f.split("\\")[-1].split(".")[0]    
           df_temp = pd.DataFrame(columns=["Wavenumber (cm)", filename], data=list_temp)
           df_temp.set_index("Wavenumber (cm)", inplace=True, drop=True)
           df = pd.concat([df, df_temp],  axis=1)
    
    ################SAVING CHARTS
    figsize = (16,8)
    x_max = 3500
    x_min = 450
    y_max = 100
    y_min = 0
    per = 200
    df.plot(use_index=True, 
            xlabel="Wavenumber (cm)", 
            ylabel = "Intensity (a.u.)",
            figsize=figsize, 
            xlim=(x_max, x_min),
            ylim=(y_min, y_max),
            
        )
    plt.tick_params(labelleft=False, left=False)
    plt.xticks(np.arange(x_min, x_max, per))
    plt.legend(bbox_to_anchor=(1.0, 0.68))
    plt.savefig(f".\\charts\\FTIR\\{chart_name}.png")
    df.to_excel(f".\\charts\\FTIR\\{chart_name}.xlsx", index=True)




main_path = r"C:\Users\ARAUJO.MARIANA\Developer\PyChartUSP\charts\FTIR\data"
read_save("FTIR_1", main_path)