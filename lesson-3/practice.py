# students = [
#     {"name": "Mike", "age": 13},
#     {"name": "John", "age": 32},
#     {"name": "Bob", "age": 92},
# ]
# students[1]["skills"] = ["HTML", "CSS", "JS"]
# students[1]["pocket"] = {
#     "left": ["Keys", "Snikers"],
#     "right": ["200$", "old dead fly"]
# }

# john = students[1]
# john = {}
# print(john.clear())


# print(john["skills"][2])
# print(john["pocket"]["right"][0])
# print("[POCKET STILL ALIVE]", john)

# ! del john["pocket"]["right"]
# print("[DELETED POCKET]", john)


# print("[Fly in pocket LEFT]", "old dead fly" in john["pocket"]["left"])
# print("[Fly in pocket RIGHT]", "old dead fly" in john["pocket"]["right"])

# print(students[1])

# print("[Previous students , before insert new user]", students)

# user = {
#     "name": input("Eneter your name : "),
#     "age": input("Eneter your age : ")
# }

# students.append(user)

# i = 0

# while i < len(students):
#     # filter
#     student = students[i]
#     if (int(student["age"]) < 25):
#         print(student)

#     # print(student["name"])
#     i += 1
