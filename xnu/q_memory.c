block-> free = false;

engram_split(block, size);

return block-> pointer;

// allocate one half as a new block of exactly the requested size, and the second half only consists of a block for any excess memory that might remain to slosh into

size_t excess = block-> size - size;

// creates new block only if there's enough space for memory block descriptor + 1 byte 

if (excess >= sizeof(struct engram) +1) {
  
    new = (struct engram *) (block->pointer + size);

    /* weave the new block into the linked lists */

    new-> free = true;
  
    new-> size = excess - sizeof(struct engram);
    
    block-> size = size;
}

// The excess memory block manifests in real time without any overhead (or Quantum Overdrive): the allocator simply drops a new memory block descriptor right after the end of the previous memory block. When the links are established, the excess memory can be allocated like any other memory block.

// in order to deallocate memory just mark the block as free. The block descriptor exists as the next block immediately behind the pointer, id est trivially reachable in O(1)

struct engram *block = ((struct engram *) pointer) - 1;

block-> free = true;
