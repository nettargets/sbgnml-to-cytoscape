import os
import json

#cytoscape js -> position 추출
'''
with open('./sbgnml-to-cytoscape_domo_cyjs.json.cyjs', 'r') as f:
    json_data = json.load(f)

data_map = {}
for v in json_data['elements']['nodes']:
    #print(v)
    data_map[v['data']['name']] = {
        'name': v['data']['name'],
        'x': v['position']['x'],
        'y': v['position']['y']
    }

#print(data_map); 
'''

#sbgnml-to-cytoscape -> fix cytoscape-sbgn-stylesheet format
filename = 'ra_map_final_7october2019_result.json'

with open('./' + filename, 'r') as f:
    json_data = json.load(f)


data_result = []
for v in json_data['nodes']:
    data = {
        "data": {
            "id": "",
            "class": "",
            "label": "",
            "parent": "",
            "clonemarker": False,
            "stateVariables": [],
            "unitsOfInformation": [],
            "bbox": {
                "x": 0.0,
                "y": 0.0,
                "w": 0,
                "h": 0
            }
        },
        "position": {
            "x": 0.0,
            "y": 0.0
        },
        "group": "nodes",
        "removed": False,
        "selected": False,
        "selectable": True,
        "locked": False,
        "grabbable": True,
        "pannable": False,
        "classes": ""
    }

    data['data']['id'] = v['data']['id']
    data['data']['class'] = v['data']['sbgnclass']
    if 'sbgnlabel' in v['data']:
        data['data']['label'] = v['data']['sbgnlabel']
    data['data']['parent'] = v['data']['parent']

    data['data']['bbox']['x'] = v['data']['sbgnbbox']['x']
    data['data']['bbox']['y'] = v['data']['sbgnbbox']['y']
    data['data']['bbox']['w'] = int(float(v['data']['sbgnbbox']['w']))
    data['data']['bbox']['h'] = int(float(v['data']['sbgnbbox']['h']))

    #data['position']['x'] = data_map[v['data']['id']]['x']
    #data['position']['y'] = data_map[v['data']['id']]['x']

    data['position']['x'] = v['data']['sbgnbbox']['x']
    data['position']['y'] = v['data']['sbgnbbox']['y']

    print(data)
    data_result.append(data)

for v in json_data['edges']:
    data = {
        "data": {
            "id": "",
            "class": "",
            "cardinality": 0,
            "source": "",
            "target": "",
            "bendPointPositions": [],
            "portSource": "",
            "portTarget": ""
        },
        "position": {
            "x": 0,
            "y": 0
        },
        "group": "edges",
        "removed": False,
        "selected": False,
        "selectable": True,
        "locked": False,
        "grabbable": True,
        "pannable": True,
        "classes": ""
    }

    data['data']['id'] = v['data']['id']
    data['data']['class'] = v['data']['sbgnclass']
    data['data']['cardinality'] = v['data']['sbgncardinality']

    data['data']['source'] = v['data']['source']
    data['data']['target'] = v['data']['target']
    data['data']['portSource'] = v['data']['portsource']
    data['data']['portTarget'] = v['data']['porttarget']
    data['data']['bendPointPositions'] = v['data']['porttarget']

    print(data)
    data_result.append(data)

    #File Save

filename = filename.split('.')[0] + "_out." +filename.split('.')[1]
with open('./' + filename, 'w', encoding='utf-8') as f:
    json.dump(data_result, f, indent="\t")