
from cc3d import CompuCellSetup
        

from FoamSteppables import FoamSteppable

CompuCellSetup.register_steppable(steppable=FoamSteppable(frequency=1))


CompuCellSetup.run()
