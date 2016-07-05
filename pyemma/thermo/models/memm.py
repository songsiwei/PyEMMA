# This file is part of PyEMMA.
#
# Copyright (c) 2016 Computational Molecular Biology Group, Freie Universitaet Berlin (GER)
#
# PyEMMA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as _np
from pyemma.msm import MSM as _MSM
from pyemma._base.subset import SubSet as _SubSet

class ThermoMSM(_MSM, _SubSet):
    def __init__(
        self, P, active_set, nstates_full,
        pi=None, reversible=None, dt_model='1 step', neig=None, ncv=None):
        super(ThermoMSM, self).__init__(
            P, pi=pi, reversible=reversible, dt_model=dt_model, neig=neig, ncv=ncv)
        self.active_set = active_set
        self.nstates_full = nstates_full
    @property
    def f(self):
        return self.free_energies
    @property
    def free_energies(self):
        return -_np.log(self.stationary_distribution)
