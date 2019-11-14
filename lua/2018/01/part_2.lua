local iterator = require("iterator")

local changes = iterator.cycle(iterator.map(io.lines(), tonumber))
local frequency = 0
local seen = {}

repeat
  seen[frequency] = true
  frequency = frequency + changes()
until seen[frequency]

print(frequency)
