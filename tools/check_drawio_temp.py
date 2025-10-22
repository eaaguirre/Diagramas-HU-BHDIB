import sys
import xml.etree.ElementTree as ET
from collections import Counter

PATH = r"d:\Repositorios\VASS-BHD\Diagramas-HU-BHDIB\Diagramas-HU-BHDIB\batik-1.19\hu990929\Diagrama_Secuencia 1.with_HU.drawio"

try:
    tree = ET.parse(PATH)
    root = tree.getroot()
except Exception as e:
    print(f"ERROR: cannot parse XML: {e}")
    sys.exit(1)

# find all mxCell elements
cells = root.findall('.//mxCell')
ids = []
refs = []
for c in cells:
    cid = c.get('id')
    if cid:
        ids.append(cid)
    # collect parent/source/target
    for a in ('parent','source','target'):
        v = c.get(a)
        if v:
            refs.append((cid,a,v))

# duplicates
dups = [item for item,count in Counter(ids).items() if count>1]
if dups:
    print('DUPLICATE IDS FOUND:')
    for d in dups:
        print(' -', d)
else:
    print('No duplicate ids')

# missing references
missing = []
id_set = set(ids)
for cid,a,v in refs:
    if v not in id_set:
        missing.append((cid,a,v))

if missing:
    print('\nMISSING REFERENCES:')
    for cid,a,v in missing:
        print(f" - cell id={cid} references {a}='{v}' which does not exist")
else:
    print('\nNo missing parent/source/target references')

# check for mxCell children under an mxCell (nested mxCell)
nested = []
for parent in root.findall('.//mxCell'):
    for child in list(parent):
        if child.tag.endswith('mxCell'):
            nested.append((parent.get('id'), child.get('id')))

if nested:
    print('\nNested mxCell elements found (parent -> child):')
    for p,c in nested:
        print(f' - {p} -> {c}')
else:
    print('\nNo nested mxCell elements detected')

print('\nChecked file:', PATH)
