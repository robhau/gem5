OUTPUT_ARCH(riscv)
MEMORY
{
    rom(rx) : ORIGIN =  0x80000000, LENGTH = 0x8000000
    ram(!rx) : ORIGIN = ORIGIN(rom) + LENGTH(rom), LENGTH = 0x8000000
}

ENTRY(start)

SECTIONS
{
    . = ORIGIN(rom);
    .text :
    {
        *(.text)
        . = ALIGN(4);
    } > rom

    PROVIDE(__stack_top = ORIGIN(ram) + LENGTH(ram));
    PROVIDE(__global_pointer = ORIGIN(ram) + LENGTH(ram) / 2);
}
