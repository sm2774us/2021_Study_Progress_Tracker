#!/usr/bin/env python

# import unittest
#
# if __name__ == "__main__":
#     suite = unittest.TestLoader().discover(".", pattern="*002_LC-426-Solution.py")
#     unittest.TextTestRunner(verbosity=2).run(suite)

import fnmatch
import os
import unittest

def all_test_modules(root_dir, pattern):
    test_file_names = all_files_in(root_dir, pattern)
    return [path_to_module(str) for str in test_file_names]

def all_files_in(root_dir, pattern):
    matches = []

    for root, dirnames, filenames in os.walk(root_dir):
        dirnames.sort()
        for filename in fnmatch.filter(sorted(filenames), pattern):
            matches.append(os.path.join(root, filename))

    return matches

def path_to_module(py_file):
    return strip_leading_dots( \
        replace_slash_by_dot(  \
            strip_extension(py_file)))

def strip_extension(py_file):
    return py_file[0:len(py_file) - len('.py')]

def replace_slash_by_dot(str):
    return str.replace('\\', '.').replace('/', '.')

def strip_leading_dots(str):
    while str.startswith('.'):
       str = str[1:len(str)]
    return str

module_names = all_test_modules('.', '*002_LC-426-Solution.py')
suites = [unittest.defaultTestLoader.loadTestsFromName(mname) for mname in module_names]

testSuite = unittest.TestSuite(suites)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(testSuite)