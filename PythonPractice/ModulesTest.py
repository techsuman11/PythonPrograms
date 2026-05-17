import SumanMath as sm
"""
If the other module is not in the project path, then we need to write the additional code as below:
Assume that the module is in C:\\Code folder then
(We can also manually add the path in environment variables)

import sys
sys.path.append("C:\\Code")
"""

print(sm.sum(10,20))    #30
print(sm.subtract(20,10))   #10
print(sm.multiply(10,20))   #200

