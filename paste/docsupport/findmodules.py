"""
Finds all modules in a packages, loads them, and returns them.
"""

import os
from paste.util.import_string import import_module

def find_modules(package):
    pkg_name = package.__name__
    modules = []
    base = os.path.abspath(package.__file__)
    if os.path.basename(os.path.splitext(base)[0]) == '__init__':
        base = os.path.dirname(base)
    if os.path.isdir(base):
        for module_fn in os.listdir(base):
            base, ext = os.path.splitext(module_fn)
            full = os.path.join(base, module_fn)
            if (os.path.isdir(full)
                and os.path.exists(os.path.join(full, '__ini__.py'))):
                modules.extend(import_module(pkg_name + '.' + base))
            elif ext == '.py':
                modules.append(import_module(pkg_name + '.' + base))
    else:
        modules.append(package)
    return modules
