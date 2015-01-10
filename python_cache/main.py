from KComputer import Computer

computer = Computer()
value = computer.Compute(5, 2)
print '1) 5^2 =', value

value = computer.Compute(5, 2)
print '2) 5^2 =', value

value = computer.Compute(5, 3)
print '3) 5^3 =', value

print '--- Clear cache ---'
computer.ClearCache()
value = computer.Compute(5, 2)
print '4) 5^2 =', value
