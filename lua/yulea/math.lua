local function accumulate(iterator)
  return coroutine.wrap(function()
    local result = 0

    for element in iterator do
      result = result + element
      coroutine.yield(result)
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

local function sum(iterator)
  local result = 0

  for element in iterator do
    result = result + element
  end

  return result
end

return {
  accumulate = accumulate,
  max = max,
  min = min,
  sum = sum,
}
