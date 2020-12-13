# Import module : import <module_name>

import random

## Show all module's functions

print(dir(random))

## Import a specific function from a module: from <module> import <funct>[,<funct>]

from random import randint

print(randint(100, 200))

## To install packages we use : pip install <package_name(s)>
## To list installed packages: pip list
## To get the current pip version: pip --version
## To upgrade pip: pip install pip --upgrade