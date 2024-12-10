from itertools import zip_longest
with open('input') as f: data = f.read().strip()
nums = [int(c) for c in data]

# Build a list of free space areas
free_list = []
block = 0
for file_size, free_size in zip(nums[::2], nums[1::2]):
    block += file_size
    if free_size: free_list.append([block, free_size])
    block += free_size

def get_files():
# Get all files in reverse order as [file_id, start_block, length]
# This omits file ID 0 but that neither moves nor adds to the checksum
    file_id = len(nums) // 2
    block = sum(nums)
    for a, b in zip(nums[-1::-2], nums[-2::-2]):
        block -= a
        yield file_id, block, a
        file_id -= 1
        block -= b

def get_file_blocks():
# Get all individual file blocks in reverse order as [file_id, block]
    for file_id, block, length in get_files():
        for i in range(length-1, -1, -1):
            yield file_id, block + i

def get_free_blocks():
# Get all individual free block numbers in ascending order
    for block, size in free_list:
        for i in range(size): yield block + i

def get_free_area(size):
# Get the first free area of length >= size
# Return the actual object in the free_list so it can be updated in place
    itr = filter(lambda x: x[1] >= size, free_list)
    return next(itr, None)

def use_blocks(free_entry, length):
# Mark blocks as used. 'free_entry' is an object in the free_list
    block, free_len = free_entry
    if length < free_len:
        free_entry[0] = block + length
        free_entry[1] = free_len - length
    else:
        free_list.remove(free_entry)

def part1():
# This doesn't alter any of the data structures
    cksum = 0
    itr = zip_longest(get_file_blocks(), get_free_blocks())
    for file_data, free_block in itr:
        if file_data:
            file_id, file_block = file_data
            if free_block and free_block < file_block:
                cksum += file_id * free_block
            else:
                cksum += file_id * file_block
    return cksum

def part2():
    cksum = 0
    for file_id, block, length in get_files():
        free_entry = get_free_area(length)
        free_block = free_entry[0] if free_entry else None
        if free_block and free_block < block:
            block = free_block
            use_blocks(free_entry, length)
        for i in range(length):
            cksum += file_id * (block+i)
    return cksum
    
print(part1())
print(part2())
