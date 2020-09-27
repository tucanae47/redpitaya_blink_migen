#!/usr/bin/python3
# this code is based on redpid. See LICENSE for details.

from migen import *

from litex_boards.platforms.redpitaya import Platform
from blink import Blink

if __name__ == "__main__":
    platform = Platform()
    blink = Blink(platform)
    platform.add_source_dir("verilog")
    platform.build(blink)