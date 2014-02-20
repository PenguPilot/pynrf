# -*- coding: utf-8 -*-
"""
	raw listen, receive bytes in raw mode
"""
__author__	= """Alexander Krause <alexander.krause@ed-solutions.de>"""
__date__ 		= "2012-11-22"
__version__	= "0.1.0"

import os
import sys
import time

sys.path=[os.path.dirname(os.path.realpath(__file__))+'/../']+sys.path

from lib.cdc import CDC_nRF


dev = CDC_nRF(sys.argv[1])

dev._bus.setDTR(True)
dev._bus.timeout = None
while True:
   print dev._bus.read()
