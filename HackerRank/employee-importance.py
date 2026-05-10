# You are given a data structure of employee information, which includes the employee's unique id, his
# importance value and his direct subordinates' id.

# For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They
# have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]],
# and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a
# subordinate of employee 1, the relationship is not direct.

# Now given the employee information of a company, and an employee id, you need to return the total
# importance value of this employee and all his subordinates.

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        # build the map
        employee_map = {}
        for employee in employees:
            employee_map[employee.id] = employee
        
        rv = 0
        stack = []
        stack.append(employee_map[id])
        
        while stack:
            employee = stack.pop()
            rv += employee.importance
            for s in employee.subordinates:
                stack.append(employee_map[s])
        
        return rv

