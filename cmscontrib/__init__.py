#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Programming contest management system
# Copyright © 2010-2012 Giovanni Mascellani <mascellani@poisson.phc.unipi.it>
# Copyright © 2010-2012 Stefano Maggiolo <s.maggiolo@gmail.com>
# Copyright © 2010-2012 Matteo Boscariol <boscarim@hotmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This directory holds utilities to import and export data to and
from CMS for different formats. Examples are ContestImport and
ContestExport, whose aim is to be one the inverse of the other (hence
losing no data in the process).

"""

import hashlib


def sha1sum(path):
    """Calculates the SHA1 sum of a file, given by its path.

    path (string): path of the file we are interested in.

    return (string): SHA1 sum of the file in path.

    """
    buffer_length = 8192
    with open(path, 'rb') as fin:
        hasher = hashlib.new("sha1")
        buf = fin.read(buffer_length)
        while buf != '':
            hasher.update(buf)
            buf = fin.read(buffer_length)
        return hasher.hexdigest()
