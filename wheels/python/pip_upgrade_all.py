'''nov.5
todo:
    1. supress successful (recursive) lines
'''

import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
