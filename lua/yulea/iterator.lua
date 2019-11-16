local function array(iterator, result)
  result = result or {}

  for element in iterator do
    table.insert(result, element)
  end

  return result
end

local function bytes(s)
  return coroutine.wrap(function()
    for i = 1, #s do
      coroutine.yield(string.byte(s, i))
    end
  end)
end

local function chars(s)
  return coroutine.wrap(function()
    for i = 1, #s do
      coroutine.yield(string.sub(s, i, i))
    end
  end)
end

local function cycle(iterator)
  return coroutine.wrap(function()
    local elements = {}

    for element in iterator do
      coroutine.yield(element)
      table.insert(elements, element)
    end

    while true do
      for _, element in ipairs(elements) do
        coroutine.yield(element)
      end
    end
  end)
end

local function distinct(iterator)
  return coroutine.wrap(function()
    local seen = {}

    for element in iterator do
      if not seen[element] then
        coroutine.yield(element)
        seen[element] = true
      end
    end
  end)
end

local function elements(t)
  return coroutine.wrap(function()
    for _, e in ipairs(t) do
      coroutine.yield(e)
    end
  end)
end

local function enumerate(iterator, index)
  index = index or 1

  return coroutine.wrap(function()
    for element in iterator do
      coroutine.yield(index, element)
      index = index + 1
    end
  end)
end

local function filter(iterator, predicate)
  return coroutine.wrap(function()
    for element in iterator do
      if predicate(element) then
        coroutine.yield(element)
      end
    end
  end)
end

local function keys(t)
  return coroutine.wrap(function()
    for k in pairs(t) do
      coroutine.yield(k)
    end
  end)
end

local function min(iterator, less)
  local result

  if less then
    for element in iterator do
      if result == nil or less(element, result) then
        result = element
      end
    end
  else
    for element in iterator do
      if result == nil or element < result then
        result = element
      end
    end
  end

  return result
end

local function map(iterator, mapper)
  return coroutine.wrap(function()
    for element in iterator do
      coroutine.yield(mapper(element))
    end
  end)
end

local function max(iterator, less)
  local result

  if less then
    for element in iterator do
      if result == nil or less(result, element) then
        result = element
      end
    end
  else
    for element in iterator do
      if result == nil or result < element then
        result = element
      end
    end
  end

  return result
end

local function multiset(iterator, result)
  result = result or {}

  for element in iterator do
    result[element] = (result[element] or 0) + 1
  end

  return result
end

local function range(first, last, step)
  first = first or 1
  last = last or math.huge
  step = step or 1

  return coroutine.wrap(function()
    for i = first, last, step do
      coroutine.yield(i)
    end
  end)
end

local function sum(iterator)
  local result = 0

  for element in iterator do
    result = result + element
  end

  return result
end

local function values(t)
  return coroutine.wrap(function()
    for _, v in pairs(t) do
      coroutine.yield(v)
    end
  end)
end

return {
  array = array,
  bytes = bytes,
  chars = chars,
  cycle = cycle,
  distinct = distinct,
  elements = elements,
  enumerate = enumerate,
  filter = filter,
  keys = keys,
  min = min,
  map = map,
  max = max,
  multiset = multiset,
  range = range,
  sum = sum,
  values = values,
}
