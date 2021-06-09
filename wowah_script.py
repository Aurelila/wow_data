import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.colors as mcolors

# Read in the dataset:
wowah1 = pd.read_csv('wowah_data.csv')

# Check out the data info:
wowah1.info()

# Check out the head:
wowah1.head()

# Check out the tail:
wowah1.tail()