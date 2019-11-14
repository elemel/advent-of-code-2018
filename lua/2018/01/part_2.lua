local yulea = require("yulea")

local cycle = yulea.iterator.cycle
local map = yulea.iterator.map

local changes = cycle(map(io.lines(), tonumber))
local frequency = 0
local seen = {}

repeat
  seen[frequency] = true
  frequency = frequency + changes()
until seen[frequency]

print(frequency)
