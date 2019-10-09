import os

__script_folder = os.path.dirname(os.path.realpath(__file__))
os.environ['GUTENBERG_DATA'] = os.path.join(__script_folder, "..", "data", "gutenberg")

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

from .gutenberg_lite import load_etext, strip_headers

def get_gutenberg_text(gutenberg_id):
  text = strip_headers(load_etext(gutenberg_id)).strip()
  text = text.replace("’","'").replace("“","\"").replace("”","\"")
  return text

