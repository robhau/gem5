cd firmware
make
cd ..
scons build/ALL/gem5.opt --linker=mold -j$(nproc)
# run with MinorCPU and with TimingSimpleCPU

build/ALL/gem5.opt --debug-flags=Exec,Minor -r --outdir=cpu_minor configs/control_hazard.py

build/ALL/gem5.opt --debug-flags=Exec -r --outdir=cpu_timing configs/control_hazard.py --useTiming
