import json
import site
import subprocess
import sys
import yaml


PData = {'1. Version python': sys.version,
         '2. virtual environment': sys.exec_prefix,
         '3. python executable location': sys.executable,
         '4. pip location': subprocess.getoutput("which pip"),
         '5. PYTHONPATH': sys.path,
         '6. installed packages': subprocess.getoutput("pip freeze"),
         '7. site-packages location': site.getsitepackages()
         }

with open('infopython.json', 'w') as out_json:
    json.dump(PData, out_json, ensure_ascii=False, sort_keys=True, indent=4)
with open('infopython.yml', 'w') as out_yml:
    yaml.dump(PData, out_yml, default_flow_style=False)
