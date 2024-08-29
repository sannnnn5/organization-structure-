# def adddep(it):
#     it = {"IT Departament Head" : "person2",
#         "Team" : [it_mng1, it_mng2, it_mng3]}
#     try:
#         while True:
#             user = input("Enter Dep for add employer: ")
#             if user == "it":
#                 userit = input()
#                 if userit == "IT Departament Head":
#                     it["IT Departament Head"] = input("Enter name of new employer: ")
#                     return it
#                 elif userit == "Team":
#                     it["Team"].append(input("Enter name of new employer: "))
#                     return it
#                 it["Team"].append(userit)
#     except ValueError:
#         print("Invalid input")



# def adddep(finance,it,security):
#     it = {"IT Departament Head" : "person2",
#         "Team" : [it_mng1, it_mng2, it_mng3]}
#     try:
#         while True:
#             user = input("Enter Dep for add employer: ")
#             if user == "it":
#                 userit = input()
#                 if userit == "IT Departament Head":
#                     it["IT Departament Head"] = input("Enter name of new employer: ")
#                     return it
#                 elif userit == "Team":
#                     it["Team"].append(input("Enter name of new employer: "))
#                     return it
#                 it["Team"].append(userit)
#     except ValueError:
#         print("Invalid input")





finance_mng1 = {"Finance Department Manager 1": "person mng1 from finance",
                "Team": ["assistant"]}

finance = {"Finance Department Head": "person1",
           "Team": [finance_mng1]}

it = {}
security = {}

usss = {"finance": finance,
        "it": it,
        "security": security
        }

usi = input("Enter department (finance / it / security): ")

if usi in usss:
    for i in usss[usi]:
        usch = input("What to do? ")
        if i == usch:
            print(i," is " ,usss[usi][i])
            break



else:
    print("Department not found.")
