groupmates = [
{
	"name": "Александр",
	"surname": "Иванов",
	"exams": ["Информатика", "ЭЭиС", "Web"],
	"marks": [4, 3, 5]
},
{
	"name": "Иван",
	"surname": "Петров",
	"exams": ["История", "АиГ", "КТП"],
	"marks": [4, 4, 4]
},
{
	"name": "Иван",
	"surname": "Петров",
	"exams": ["Философия", "ИС", "КТП"],
	"marks": [5, 5, 5]
},
{
	"name": "Максим",
	"surname": "Кравец",
	"exams": ["Информатика", "ИС", "Web"],
	"marks": [4, 5, 4]
},
{
	"name": "Светлана",
	"surname": "Банькина",
	"exams": ["ЭЭиС", "АиГ", "Физика"],
	"marks": [5, 4, 4]
}
]

def print_students (students):
	print (u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
	for student in students:
		print (student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)