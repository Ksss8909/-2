# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, n=','):
	#разделение строк на участников
	first = set(group1.split(n))
	second = set(group2.split(n))
	common_participants = first.intersection(second)
	return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
#поиск общих участников встречи
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)

participants_first_group_comma = "Иванов,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"

print (find_common_participants(participants_first_group_comma, participants_second_group_comma, n=','))





