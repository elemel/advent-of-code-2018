local function defaultLess(v1, v2)
  return v1 < v2
end

local function less(t1, t2, less)
  less = less or defaultLess

  for i = 1, math.min(#t1, #t2) do
    if less(t1[i], t2[i]) then
      return true
    elseif less(t2[i], t1[i]) then
      return false
    end
  end

  return #t1 < #t2
end

local function mapValues(t, mapper, result)
  result = result or {}

  for k, v in pairs(t) do
    result[k] = mapper(v)
  end

  return result
end

local function reverse(t)
  local i = 1
  local j = #t

  while i < j do
    t[i], t[j] = t[j], t[i]

    i = i + 1
    j = j - 1
  end
end

local function sumValues(t)
  local result = 0

  for _, v in pairs(t) do
    result = result + v
  end

  return result
end

return {
  less = less,
  mapValues = mapValues,
  reverse = reverse,
  sumValues = sumValues,
}
