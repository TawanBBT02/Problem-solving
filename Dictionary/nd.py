# Level 1 Dictionary
university_data = {
'name': 'XYZ University',
'location': 'Technology City',
'faculties': {
# Level 2 Dictionary
'information_technology': {
'departments': {
# Level 3 Dictionary
'software_engineering': {'courses': ['Software Development', 'Database Systems']},
'networking': {'courses': ['Computer Networks', 'Network Security']}
}
},
'business': {
'departments': {
'management_systems': {'courses': ['Business Intelligence', 'IT Management']},
'finance_technology': {'courses': ['Fintech', 'Blockchain']}
}
}
}
}
# Displaying data from Nested Dictionary
print("University Name:", university_data['name'])
print("Location:", university_data['location'])
# Displaying data from Level 2 Dictionary
print("\nFaculty of Information Technology:")
print("Departments:", university_data['faculties']['information_technology'])
# Displaying data from Level 3 Dictionary
print("\nInformation Technology Branch - Software Engineering:")
print("Courses:", university_data['faculties']['information_technology']['departments']['software_engineering']['courses'])