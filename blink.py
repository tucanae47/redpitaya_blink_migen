# this code is based on redpid. See LICENSE for details.
from migen import *
from misoc.interconnect import csr_bus
from misoc.interconnect.csr import AutoCSR, CSRStatus, CSRStorage
from pitaya_ps import SysCDC, Sys2CSR, SysInterconnect, PitayaPS, sys_layout
from crg import CRG


class Blink(Module):
    def __init__(self, platform):
        self.submodules.ps = PitayaPS(platform.request("cpu"))
        self.submodules.crg = CRG(platform.request("clk125"),
                self.ps.fclk[0], ~self.ps.frstn[0])
        led = platform.request("user_led", 0)
        counter = Signal(32)
        self.sync += counter.eq(counter + 1)
        self.comb += led.eq(counter[26])
      
