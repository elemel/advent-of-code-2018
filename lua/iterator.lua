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

local function enumerate(iterator, index)
  index = index or 1

  return coroutine.wrap(function()
    for element in iterator do
      coroutine.yield(index, element)
      index = index + 1
    end
  end)
end

local function map(iterator, mapper)
  return coroutine.wrap(function()
    for element in iterator do
      coroutine.yield(mapper(element))
    end
  end)
end

return {
  cycle = cycle,
  enumerate = enumerate,
  map = map,
}
