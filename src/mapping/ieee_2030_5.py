 
import pandas as pd 
import os
import re 
 
 
# get folder 

current_folder = os.getcwd()
 
 
# get reference_map
reference_map = pd.read_excel(os.path.join(current_folder,r'ieee1547_mappings.xlsx'),sheet_name='Sheet1')

def get_transfer_type(key_length,point_length):
    if key_length>1:
        if point_length >1:
            type_str ='map_list'
        else:
            type_str='unknown'
    elif point_length>1:
        type_str ='broadcast'
    else:
        type_str = 'one_to_one'
    return type_str

def get_mapped_point_len(mapped_points):
    
    if isinstance(mapped_points,float):
        return 0
    pairs = re.findall(r'(\w+::\w+)\s*=\s*(\d+)', mapped_points)
    if pairs:
        return len(pairs)
    else:
        return max(len(mapped_points.split(' ')), len(mapped_points.split(',')))

def determine_writable(mapped_points):
    if isinstance(mapped_points,str):
        return any('O' in point for point in mapped_points)
    else:
        return False 

def get_maps(reference_map):
    '''get filtered map then fill non-exist maps by directly using reference map'''
    maps = {}
    notexist_keys = []
    for ref in reference_map['IEC 61850-7-420']:
        # if key NOT in mesa_map ，check IEEE 1815.2 column
        mapped_points = reference_map[reference_map['IEC 61850-7-420'].str.contains(ref, na=False)]['IEEE 2030.5'].iloc[0]
        if mapped_points:
            point_length = get_mapped_point_len(mapped_points)
            key_length = len(ref.split(','))
            maps[ref] = {
            'mapped_points': mapped_points,
            'transform_type': get_transfer_type(key_length,point_length),
            'writable':determine_writable(mapped_points)
        }
        else:
            notexist_keys.append(ref)
       
    return maps, notexist_keys 
maps, notexist_keys = get_maps(reference_map)
# %%
