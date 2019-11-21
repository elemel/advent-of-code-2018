local function accumulate(iterator, reducer)
  reducer = reducer or function(a, b) return a + b end

  return coroutine.wrap(function()
    local result = iterator()

    if result ~= nil then
      coroutine.yield(result)

      for element in iterator do
        result = reducer(result, element)
        coroutine.yield(result)
      end
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

local function firstDuplicate(iterator)
  local seen = {}

  for element in iterator do
    if seen[element] then
      return element
    end

    seen[element] = true
  end

  return nil
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
      local result = mapper(element)

      if result ~= nil then
        coroutine.yield(result)
      end
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

local function rep(v, n)
  n = n or math.huge

  return coroutine.wrap(function()
    for i = 1, n do
      coroutine.yield(v)
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

local function take(iterator, n)
  return coroutine.wrap(function()
    for i = 1, n do
      coroutine.yield(iterator())
    end
  end)
end

return {
  accumulate = accumulate,
  cycle = cycle,
  distinct = distinct,
  enumerate = enumerate,
  filter = filter,
  firstDuplicate = firstDuplicate,
  min = min,
  map = map,
  max = max,
  range = range,
  rep = rep,
  sum = sum,
  take = take,
}
