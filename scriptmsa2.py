from modeller import *
from modeller.automodel import *

env = Environ()
env.io.atom_files_directory = ['.', './atom_files']

a = AutoModel(env, alnfile='msa2.pir',
              knowns=('6Y05','4WIH','1CTP','6F14','3J4Q','2F7E'), sequence='seq')
a.starting_model = 1
a.ending_model = 2
a.make()
a.write("model2.pdb")

