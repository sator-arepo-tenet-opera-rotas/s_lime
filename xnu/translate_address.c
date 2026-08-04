// logical_addr is 16-bit address, returns 21-bit physical addres
def translate_address(logical_addr):
    logical_page = logical_addr >> 13
    physical_page = MPR[logical_page]
    return (physical_page << 13) | (logical_addr & 0x1FFF)
