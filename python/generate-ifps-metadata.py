from PIL import Image 
from IPython.display import display 
import json

# READ METADATA IF YOU ALREADY HAVE A JSON FILE

with open("./all-traits.json", 'r') as f:
        traits = json.load(f)

with open("./ifps-images.json", 'r') as f:
    hashes = json.load(f)
    
for k,v in hashes.items():
    print(k,v)
    # traits[v]["image"] = 'https://gateway.pinata.cloud/ipfs/QmNRLbvV4mEDpbQ1ai75Z3UD1AU2PsbDCuNsHeCQDs6v4C'
    traits[v]["image"] = k

with open('./all-traits.json', 'w') as outfile:
    json.dump(traits, outfile, indent=4)