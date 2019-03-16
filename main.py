from misc import *
from summary import *
import sys

function = sys.argv[1]
info = sys.argv[2]

globals()[function](info)