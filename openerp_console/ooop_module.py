# -*- encoding: utf-8 -*-
########################################################################
#
#   Openerp Console
#   Copyright (C) 2011 Impulzia S.L. All Rights Reserved.
#   Gamaliel Toro <argami@impulzia.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
########################################################################
from osv import osv, fields
#from ooop import OOOP  # expecting to load in the console ooop as second option
from rfoo.utils import rconsole

_cr = None
_self = None
_uid = None


class impulzia_console(osv.osv):
    def __init__(self,  cr, uid):
        super( osv.osv, self ).__init__(cr, uid)
        _self = self
        _cr = cr
        _uid = uid
        rconsole.spawn_server()
        print '>>>>>>>>>>>>>>>>>>>>>>>>>> Console Loaded <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
        print '>>>>>>>>>>>>>>>>>>>>>>> access with rconsole <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 
    _name = 'impulzia.console'
    _columns = {}
impulzia_console()

