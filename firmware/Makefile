CC=riscv64-unknown-elf-
CC_FLAGS = -march=rv32imafc -mabi=ilp32f -mfdiv -mdiv
CC_FLAGS += -O3 -ffreestanding -Wall -ffreestanding -nostartfiles
CC_FLAGS += -Wl,-T,linker.ld
firmware.elf: start.s
	$(CC)gcc $(CC_FLAGS) start.s -o firmware.elf
	$(CC)objdump -D firmware.elf > firmware.txt

clean:
	rm firmware.elf
