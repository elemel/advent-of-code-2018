local function trim(s)
   return string.match(s, "^%s*(.-)%s*$")
end

return {
  trim = trim,
}
