local yulea = require("yulea")

local accumulate = yulea.iterator.accumulate
local cycle = yulea.iterator.cycle
local firstDuplicate = yulea.iterator.firstDuplicate
local numbers = yulea.io.numbers

print(firstDuplicate(accumulate(cycle(numbers(io.stdin)))))
