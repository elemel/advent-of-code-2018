local frequency = 0

for line in io.lines() do
  frequency = frequency + tonumber(line)
end

print(frequency)
