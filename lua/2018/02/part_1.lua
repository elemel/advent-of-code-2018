local yulea = require("yulea")

local bytes = yulea.iterator.bytes
local distinct = yulea.iterator.distinct
local multiset = yulea.iterator.multiset
local values = yulea.iterator.values

local countCounts = {}

for line in io.lines() do
  multiset(distinct(values(multiset(bytes(line)))), countCounts)
end

print((countCounts[2] or 0) * (countCounts[3] or 0))
