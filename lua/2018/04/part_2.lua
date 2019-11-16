local yulea = require("yulea")

local array = yulea.iterator.array
local max = yulea.iterator.max
local keys = yulea.iterator.keys
local values = yulea.iterator.values

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

local chosen_guard_id
local chosen_minute
local max_count = -math.huge

for guard_id, minutes_asleep in pairs(guard_minutes_asleep) do
  for minute, count in pairs(minutes_asleep) do
    if count > max_count then
      chosen_guard_id = guard_id
      chosen_minute = minute
      max_count = count
    end
  end
end

print(chosen_guard_id * chosen_minute)
