from nsetools import Nse
import pandas as pd, numpy as np
n = Nse()
print(n)
q = n.get_quote('infy')
print(q)