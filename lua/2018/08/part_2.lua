local yulea = require("yulea")

local array = yulea.table.array
local flatMap = yulea.iterator.flatMap
local map = yulea.iterator.map
local mapper = yulea.table.mapper
local numbers = yulea.io.numbers
local rep = yulea.iterator.rep
local sum = yulea.math.sum
local take = yulea.iterator.take

local function value(nums)
  local childCount = nums()
  local metadataCount = nums()

  if childCount == 0 then
    return sum(take(nums, metadataCount))
  end

  local childValues = array(map(rep(nums, childCount), value))
  return sum(flatMap(take(nums, metadataCount), mapper(childValues)))
end

print(value(numbers(io.stdin)))
