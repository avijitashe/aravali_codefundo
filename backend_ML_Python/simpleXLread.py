import pandas as pd 
import matplotlib.pyplot as plt 

print("Hello Avijit. This is Pandas for ML")

"""
  File "simpleXLread.py", line 4
    print 'Hello Avijit'

is an error in Python 3.7

----------------

When you run it first time, the matplot lib works for a while...

(pandas-ml) avijit@avijit-Inspiron-3521:~/Desktop/Python/codefundo_2018$ python simpleXLread.py 
/home/avijit/anaconda2/envs/pandas-ml/lib/python3.7/site-packages/matplotlib/font_manager.py:229: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
  'Matplotlib is building the font cache using fc-list. '
Hello Avijit

-----------------
But, henceforth it is rather quick

(pandas-ml) avijit@avijit-Inspiron-3521:~/Desktop/Python/codefundo_2018$ python simpleXLread.py 
Hello Avijit. This is Pandas for ML

"""

from sklearn import ensemble, model_selection, preprocessing, tree

# We need just 3 libraries to go ahead