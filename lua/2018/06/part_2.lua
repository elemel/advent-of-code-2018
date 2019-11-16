local yulea = require("yulea")

local array = yulea.iterator.array
local elements = yulea.iterator.elements
local keys = yulea.iterator.keys
local min = yulea.iterator.min
local map = yulea.iterator.map
local max = yulea.iterator.max
local sum = yulea.iterator.sum
local values = yulea.iterator.values

local function parseCoordinate(line)
  local x, y = string.match(line, "(%d+), (%d+)")
  return {tonumber(x), tonumber(y)}
end

local function manhattanDistance(x1, y1, x2, y2)
  return math.abs(x2 - x1) + math.abs(y2 - y1)
end

local function totalDistance(coordinates, x, y)
  return sum(map(values(coordinates), function(coordinate)
    return manhattanDistance(x, y, table.unpack(coordinate))
  end))
end

local coordinates = array(map(io.lines(), parseCoordinate))

local minX = min(map(elements(coordinates), function(c) return c[1] end))
local minY = min(map(elements(coordinates), function(c) return c[2] end))

local maxX = max(map(elements(coordinates), function(c) return c[1] end))
local maxY = max(map(elements(coordinates), function(c) return c[2] end))

local size = 0

for x = minX, maxX do
  for y = minY, maxY do
    local distance = totalDistance(coordinates, x, y)

    if distance < 10000 then
      if x == minX or y == minY or x == maxX or y == maxY then
        assert(false)
      end

      size = size + 1
    end
  end
end

print(size)
