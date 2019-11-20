local yulea = require("yulea")

local array = yulea.iterator.array
local map = yulea.iterator.map
local mapper = yulea.table.mapper
local numbers = yulea.iterator.numbers
local rep = yulea.iterator.rep
local sum = yulea.iterator.sum
local take = yulea.iterator.take

local function value(nums)
  local childCount = nums()
  local metadataCount = nums()

  if childCount == 0 then
    return sum(take(nums, metadataCount))
  end

  local childValues = array(map(rep(nums, childCount), value))
  return sum(map(take(nums, metadataCount), mapper(childValues)))
end

print(value(numbers(io.stdin)))
