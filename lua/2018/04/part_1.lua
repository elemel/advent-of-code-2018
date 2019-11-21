local yulea = require("yulea")

local array = yulea.table.array
local max = yulea.iterator.max
local keys = yulea.table.keys
local mapValues = yulea.table.mapValues
local sumValues = yulea.table.sumValues
local values = yulea.table.values

local lines = array(io.lines())
table.sort(lines)

local guard_id
local asleep_since
local guard_minutes_asleep = {}
local minutes_asleep

for _, line in ipairs(lines) do
  local minute_str, observation =
    string.match(line, "^%[%d%d%d%d%-%d%d%-%d%d %d%d:(%d%d)] (.+)$")

  local minute = tonumber(minute_str)

  if observation == "falls asleep" then
    asleep_since = minute
  elseif observation == "wakes up" then
    for i = asleep_since, minute - 1 do
      minutes_asleep[i] = (minutes_asleep[i] or 0) + 1
    end
  else
    guard_id = tonumber(string.match(observation, "^Guard #(%d+) begins shift"))
    guard_minutes_asleep[guard_id] = guard_minutes_asleep[guard_id] or {}
    minutes_asleep = guard_minutes_asleep[guard_id]
  end
end

local guards_asleep = mapValues(guard_minutes_asleep, sumValues)

local chosen_guard_id = max(keys(guards_asleep), function(a, b)
  return guards_asleep[a] < guards_asleep[b]
end)

minutes_asleep = guard_minutes_asleep[chosen_guard_id]

local chosen_minute = max(keys(minutes_asleep), function(a, b)
  return minutes_asleep[a] < minutes_asleep[b]
end)

print(chosen_guard_id * chosen_minute)
