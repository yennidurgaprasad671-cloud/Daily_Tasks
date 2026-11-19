"""10. University Staff Management (Hierarchical Inheritance)
A university has different staff types such as Professor, LabAssistant, and
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance
to manage and display their information"""

class Staff:
    def __init__(self, name: str, staff_id: str, department: str, salary: float):
        self.name = name
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def display_info(self) -> None:
        print(f"ID: {self.staff_id} | Name: {self.name}")
        print(f"Department: {self.department} | Salary: ${self.salary:,.2f}")


class Professor(Staff):
    def __init__(
        self,
        name: str,
        staff_id: str,
        department: str,
        salary: float,
        specialization: str,
        courses_taught: list[str],
    ):
        super().__init__(name, staff_id, department, salary)
        self.specialization = specialization
        self.courses_taught = courses_taught

    def display_info(self) -> None:
        print("--- Professor ---")
        super().display_info()
        print(f"Specialization: {self.specialization}")
        print(f"Courses: {', '.join(self.courses_taught)}\n")


class LabAssistant(Staff):
    def __init__(
        self,
        name: str,
        staff_id: str,
        department: str,
        salary: float,
        lab_assigned: str,
        shift: str,
    ):
        super().__init__(name, staff_id, department, salary)
        self.lab_assigned = lab_assigned
        self.shift = shift

    def display_info(self) -> None:
        print("--- Lab Assistant ---")
        super().display_info()
        print(f"Lab Assigned: {self.lab_assigned} | Shift: {self.shift}\n")


class Administrator(Staff):
    def __init__(
        self,
        name: str,
        staff_id: str,
        department: str,
        salary: float,
        role: str,
        office_location: str,
    ):
        super().__init__(name, staff_id, department, salary)
        self.role = role
        self.office_location = office_location

    def display_info(self) -> None:
        print("--- Administrator ---")
        super().display_info()
        print(f"Role: {self.role} | Office: {self.office_location}\n")


if __name__ == "__main__":
    staff_members: list[Staff] = [
        Professor(
            name="Dr. Priya Nair",
            staff_id="STF-101",
            department="Computer Science",
            salary=95000,
            specialization="Distributed Systems",
            courses_taught=["Operating Systems", "Cloud Computing"],
        ),
        LabAssistant(
            name="Rohan Verma",
            staff_id="STF-204",
            department="Electronics",
            salary=42000,
            lab_assigned="VLSI & Embedded Lab",
            shift="Morning",
        ),
        Administrator(
            name="Ananya Rao",
            staff_id="STF-309",
            department="Academic Affairs",
            salary=68000,
            role="Registrar Coordinator",
            office_location="Admin Block, Room 202",
        ),
    ]

    for member in staff_members:
        member.display_info()
