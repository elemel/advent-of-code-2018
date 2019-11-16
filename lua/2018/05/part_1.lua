local yulea = require("yulea")

local array = yulea.iterator.array
local chars = yulea.iterator.chars
local elements = yulea.iterator.elements
local trim = yulea.string.trim

local function reactive(a, b)
  return a ~= b and string.lower(a) == string.lower(b)
end

local function react(polymer, result)
  result = result or {}

  for unit in elements(polymer) do
    if #result >= 1 and reactive(unit, result[#result]) then
      table.remove(result)
    else
      table.insert(result, unit)
    end
  end

  return result
end

local polymer = array(chars(trim(io.read("*a"))))
polymer = react(polymer)
print(#polymer)
