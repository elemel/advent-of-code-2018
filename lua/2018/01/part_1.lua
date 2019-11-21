local yulea = require("yulea")

local numbers = yulea.io.numbers
local sum = yulea.iterator.sum

print(sum(numbers(io.stdin)))
