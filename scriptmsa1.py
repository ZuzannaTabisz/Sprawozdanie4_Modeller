from modeller import *
from modeller.automodel import *

env = Environ()
env.io.atom_files_directory = ['.', './atom_files']

a = AutoModel(env, alnfile='msa1.pir',
              knowns=('4AE6','5X3F','3J4Q'), sequence='seq')
a.starting_model = 1
a.ending_model = 2
a.make()
a.write("model1.pdb")

