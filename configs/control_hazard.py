import argparse

import m5
from m5.objects import *

parser = argparse.ArgumentParser(
    prog="Firmware", description="Minimal working example for control hazard"
)

parser.add_argument("--useTiming", dest="timing", action="store_true")

args = parser.parse_args()
system = System()

print(args.timing)
if not args.timing:
    system.cpu = RiscvMinorCPU()
    system.cpu.fetch2InputBufferSize = 1
    system.cpu.fetch2CycleInput = False
    system.cpu.decodeInputBufferSize = 1
    system.cpu.decodeInputWidth = 1
    system.cpu.decodeCycleInput = False
    system.cpu.executeInputWidth = 1
    system.cpu.executeCycleInput = False
    system.cpu.executeIssueLimit = 1
    system.cpu.executeCommitLimit = 1
    system.cpu.executeInputBufferSize = 1
    system.cpu.executeMaxAccessesInMemory = 1
    system.cpu.executeLSQMaxStoreBufferStoresPerCycle = 1
    system.cpu.executeLSQTransfersQueueSize = 1


else:
    system.cpu = RiscvTimingSimpleCPU()


system.clk_domain = SrcClockDomain()
system.clk_domain.clock = "64MHz"
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_ranges = [
    # memory region ram
    AddrRange(start=0x80000000, size=0x10000000),
]


# memory
system.mem_mode = "timing"
system.memory = SimpleMemory()
system.memory.range = system.mem_ranges[0]
system.memory.latency = "15.625ns"

# System Bus
system.membus = SystemXBar()
# connect memory ports to target ports
system.membus.mem_side_ports = system.memory.port

# connect cpu ports to initiator ports
system.membus.cpu_side_ports = system.cpu.dcache_port
system.membus.cpu_side_ports = system.cpu.icache_port
system.membus.cpu_side_ports = system.system_port
# system bus byte width
system.membus.width = 4


system.cpu.createInterruptController()
system.cpu.createThreads()


system.cpu.isa[0].riscv_type = "RV32"


system.workload = RiscvBareMetal()
system.workload.bootloader = "firmware/firmware.elf"

root = Root(full_system=True, system=system)

m5.instantiate()
exit_event = m5.simulate(100000000000)

print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}.")
