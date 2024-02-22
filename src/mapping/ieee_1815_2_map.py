#%%
import pandas as pd 
import json 
import os

from collections import defaultdict
#%%
# get data 
current_folder = os.getcwd()
with open(os.path.join(current_folder,'mesa_mapping.config'), 'r') as f:
    data = json.load(f)
 
# get reference_map
reference_map = pd.read_excel(os.path.join(current_folder,r'ieee1547_mappings.xlsx'),sheet_name='Sheet1')


#%%
def number_of_data_type(data):
    '''by checking the number of each type, we want to make sure type I equal or large than type O'''
    intervals = []
    last_zero_index = None
    last_data_type = None   
    for i, item in enumerate(data):
        if item["index"] == 0:
            if last_zero_index is not None:
                intervals.append((i - last_zero_index, last_data_type))
                print(f'data type {last_data_type} number : {i - last_zero_index}')
            last_zero_index = i
            last_data_type = item['data_type']   
    
    if last_zero_index is not None and last_zero_index != len(data) - 1:
        interval = len(data) - last_zero_index
        intervals.append((interval, last_data_type))
        print(f'data type {last_data_type} number : {interval}')
    return intervals

#%%
def normalize_description(description, item):
    #NOTE: not every item has 'category' 
    description = description.replace("Set ", "") # This is for schedule
    if item.get('category') == "mode_enable":
        # get the pattern
        normalized = description.replace("Operating Mode - ", "").replace("Enabled", "").replace("Enable", "").strip()
        if not normalized.endswith("Mode"):
            normalized += " Mode"
        normalized += " Enable"
        return normalized.split(".")[0]  # only get firt sentence. 
    else:
        # only get firt sentence
        return description.split(".")[0]


def get_mesa_map(data):
    '''get full mapping with combined mapped points for identical first descriptions'''
    # we want to combine similar description (same input/output) into one tuple
    #NOTE: description may has little bit offset between "O" and "I"
    #NOTE: grouping description only based on the FIRST setence.
    #NOTE: also for mode_enable category, such description need some exceptions 
    #NOTE: for schedule categroty, description also need to delelte 'SET" 
    description_groups = defaultdict(list)
    for item in data:
        normalized_description = normalize_description(item['description'], item)
        description_groups[normalized_description].append(item['name'])
         
    result = defaultdict(lambda: {'mapped_points': []})
    
    for description, names in description_groups.items():
        key_group = defaultdict(list)
        for name in names:
            parts = name.split('.')
            if len(parts) > 1:
                key = '.'.join(parts[:-1])
                mapped_point = parts[-1]
                key_group[key].append(mapped_point)
        
        for key, mapped_points in key_group.items():
            # get tuples if needed
            if len(mapped_points) > 1:
                combined = tuple((mapped_points))   
                result[key]['mapped_points'].append(combined)
            else:
                result[key]['mapped_points'].extend(mapped_points)
    
    return dict(result)

mesa_map = get_mesa_map(data)

#%% 
def parse_reference_map_entry(entry):
    """understand reference map and get the mapped_points if key are not in mesa config"""
    if (not entry) or (not isinstance(entry,str)):
        return []
    parts = entry.split(',')
    mapped_points = []
    for i in parts:
        if (":" in i):
            lhs, rhs = [], []
            subparts = i.split(':')
            for p in subparts:
                if '-' in p:
                    split_parts= p.split('-')  # Split by '-'
                    lhs.append(split_parts[0])
                    rhs.append(split_parts[1] if len(split_parts) > 1 else '')  
                else:
                    mapped_points.append(p)
            for l,r in zip(lhs,rhs):
                    mapped_points.append((l,r))   
        elif (":" not in i) and ('-' in i):
            subparts = i.split('-')
            for p in subparts:
                mapped_points.append(p)
                
        else:
            mapped_points.append(i)
    return mapped_points

def get_filtered_maps(mesa_map, reference_map):
    '''get filtered map then fill non-exist maps by directly using reference map'''
    filtered_map = {}
    notexist_keys = []
    in_mesa_keys = []
    for refs in reference_map['IEC 61850-7-420']:
        refs = refs.split(', ')
        for ref in refs:
            # search key in mesa_map
            if ref.lower() in (key.lower() for key in mesa_map.keys()):
                filtered_map[ref] = mesa_map[ref]
                in_mesa_keys.append(ref)
            else:
                # if key NOT in mesa_map ，check IEEE 1815.2 column
                if 'IEEE 1815.2' in reference_map:
                    entry = reference_map[reference_map['IEC 61850-7-420'].str.contains(ref, na=False)]['IEEE 1815.2'].iloc[0]
                    mapped_points = parse_reference_map_entry(entry)
                    print(f'point is {ref},searched enetry is {entry},mapped point is {mapped_points}')
                    if mapped_points:
                        filtered_map[ref] = {'mapped_points': mapped_points}
                    else:
                        notexist_keys.append(ref)
                else:
                    notexist_keys.append(ref)                     
    return filtered_map, notexist_keys,in_mesa_keys


filtered_map,notexist_keys,in_mesa_keys = get_filtered_maps(mesa_map,reference_map)

            
# %%
with open('ieee_1815_2_map.txt','w') as json_file:
    json.dump(filtered_map,json_file,indent=4)
# %%
