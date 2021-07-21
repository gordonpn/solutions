"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        subordinates: List[int] = []
        employee_dict: Dict[int, Tuple[int, List[int]]] = {}
        importance_sum = 0
            
        for employee in employees:
            employee_dict[employee.id] = (employee.importance, employee.subordinates)
            if employee.id == id:
                importance_sum += employee.importance
                subordinates.extend(employee.subordinates)
                
        for subordinate_id in subordinates:
            importance_sum += employee_dict[subordinate_id][0]
            subordinates.extend(employee_dict[subordinate_id][1])
            
        return importance_sum
            
         
        