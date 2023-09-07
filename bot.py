import os
import subproces
import sys

def sub():
  subprocess.call(". /path/to/env.sh", shell = True)
  subprocess.call("python something.py", shell = True)
