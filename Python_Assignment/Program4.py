class Programmer:
    def __init__(self, name, employee_id, role):
        self.name = name
        self.employee_id = employee_id
        self.role = role

# Example usage:
programmer1 = Programmer("John Doe", "MS123", "Software Engineer")
programmer2 = Programmer("Jane Smith", "MS456", "Data Scientist")

# Accessing information
print("Programmer 1:")
print("Name:", programmer1.name)
print("Employee ID:", programmer1.employee_id)
print("Role:", programmer1.role)
print()

print("Programmer 2:")
print("Name:", programmer2.name)
print("Employee ID:", programmer2.employee_id)
print("Role:", programmer2.role)
