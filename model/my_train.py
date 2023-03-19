
# Training
from trainer import Trainer
import os
print(os.getcwd());
print('Starting train ...')
t = Trainer(experiment_name = 'BIMODAL_fixed_512')
print('Trainer finished ...')
t.cross_validation(stor_dir = '../evaluation/', restart = False)
