

# Redpitaya migen experiments
Based on [Linien](https://github.com/hermitdemschoenenleben/linien) project, build a blink on redpitaya. (source files are taken and modfied from Linien)

# Requirements
Python3 
Litex setup is modified from default to use my forks (in which migen-boards was mofied to add repitaya platform and migen was modified to fix a bug when adding verilog sources), for this. 

# Usage 

* Init dependencies cloning 

`./litex_setup init`

* install them locally

`./litex_setup install`

* generate gateware 
`python make.py`

* copy and flash to repitaya

`scp build/top.bit root@rp-f0490a:~/`

`ssh root@rp-f0490`

`cat top.bit > /dev/xdevcfg`


