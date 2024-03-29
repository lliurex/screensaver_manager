#!/usr/bin/python3

# Copyright (C) 2006 James Westby <jw+debian@jameswestby.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

from setuptools import setup

setup(name='python3-screensaver-manager',
      version='0.1',
      description='enable or disable screensaver',
      url='http://lliurex.net',
      package_dir={'lliurex.screensaver': 'src'},
      packages=['lliurex.screensaver'],
      maintainer='Raul Rodrigo Segura',
      maintainer_email='raurodse@gmail.com',
     )
