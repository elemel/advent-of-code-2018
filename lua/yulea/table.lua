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
  mapValues = mapValues,
  reverse = reverse,
  sumValues = sumValues,
}
