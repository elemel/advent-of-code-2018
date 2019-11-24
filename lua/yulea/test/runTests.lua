local ansicolors = require("yulea.test.ansicolors")

local testSuites = {
  iteratorTest = require("yulea.test.iteratorTest"),
  stringTest = require("yulea.test.stringTest"),
  tableTest = require("yulea.test.tableTest"),
}

for testSuiteName, testCases in pairs(testSuites) do
  for testCaseName, testCase in pairs(testCases) do
    local testName = testSuiteName .. "." .. testCaseName

    if pcall(testCase) then
      print(ansicolors("%{green}" .. testName .. ": PASS"))
    else
      print(ansicolors("%{red}" .. testName .. ": FAIL"))
    end
  end
end
