from sklearn.preprocessing import StandardScaler
import torch
import numpy as np
import random

input_dim = 64
grams_num = 2
unfound_value = 0
scaler = StandardScaler()

# Random seed 42
## On CPU
random.seed(42) # For random
np.random.seed(42) # For numpy
torch.manual_seed(42) # For torch CPU

## On GPU
torch.cuda.manual_seed(42)
torch.cuda.manual_seed_all(42)
torch.backends.cudnn.deterministic = True