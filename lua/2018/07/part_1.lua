local heap = require("skew_heap")
local yulea = require("yulea")

local array = yulea.iterator.array
local elements = yulea.iterator.elements
local keys = yulea.iterator.keys
local map = yulea.iterator.map

local function parseRequirement(line)
  return {string.match(
    line, "Step (.) must be finished before step (.) can begin%.")}
end

local requirements = array(map(io.lines(), parseRequirement))

local inputs = {}
local outputs = {}

for requirement in elements(requirements) do
  local input, output = table.unpack(requirement)

  inputs[output] = inputs[output] or {}
  inputs[output][input] = true

  outputs[input] = outputs[input] or {}
  outputs[input][output] = true
end

local available = heap:new()

for step in keys(outputs) do
  if not inputs[step] then
    available:insert(step, true)
  end
end

local completed = {}

while not available:empty() do
  local step = available:pop()
  table.insert(completed, step)

  local outputs = outputs[step]

  if outputs then
    outputs[step] = nil

    for output in keys(outputs) do
      inputs[output][step] = nil

      if not next(inputs[output]) then
        inputs[output] = nil
        available:insert(output, true)
      end
    end
  end
end

print(table.concat(completed))
