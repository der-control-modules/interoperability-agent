#%%
import pandas as pd 
import json 
import os
#%%
# get folder 
current_folder = os.getcwd()
 
 
# get reference_map
reference_map = pd.read_excel(os.path.join(current_folder,r'ieee1547_mappings.xlsx'),sheet_name='Sheet1')

def get_maps(reference_map):
    '''get filtered map then fill non-exist maps by directly using reference map'''
    filtered_map = {}
    notexist_keys = []
    for ref in reference_map['IEC 61850-7-420']:
        # if key NOT in mesa_map ，check IEEE 1815.2 column
        mapped_points = reference_map[reference_map['IEC 61850-7-420'].str.contains(ref, na=False)]['IEEE 2030.5'].iloc[0]
        if mapped_points:
            filtered_map[ref] = {'mapped_points': mapped_points}
        else:
            notexist_keys.append(ref)
                        
    return filtered_map, notexist_keys 

# %%
