.global start
.type start,@function
start:
    .option push
    .option norelax
    la gp, __global_pointer
    .option pop
    la sp, __stack_top
    li a0, 0
    add a0, a1, a2
    add a0, a1, a2
    add a0, a1, a2
    add a0, a1, a2
    add a0, a1, a2
    add a0, a1, a2
    add a0, a1, a2
    add a0, a1, a2
    add a0, a1, a2
    add a0, a1, a2
    add a0, a1, a2
    li a1, 1
    j L2
L1:
    lw a2, 0(a0)
    lw a3, 4(a0)
    lw a4, 8(a0)
    j exit
L2:
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    li a0, 0
    lui a0, 0x80000
    j L1

exit:
    wfi
    j exit
