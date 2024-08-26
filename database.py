# finance_mng1 = {"Finance Departament Maneger 1 `person name`" :["assistent1"]}
# finance_mng2 = {"Finance Departament Maneger 2 `person name`" :["assistent1"]}
# finance_mng3 = {"Finance Departament Maneger 3 `person name`" :["assistent1"]}

# it_mng1 = {"IT Departament Maneger 1 `person name`" :["assistent1"]}
# it_mng2 = {"IT Departament Maneger 2 `person name`" :["assistent1"]}
# it_mng3 = {"IT Departament Maneger 3 `person name`" :["assistent1"]}

# security_mng1 = {"Security Departament  Maneger 1 `person name`" :["assistent1"]}
# security_mng2 = {"Security Departament  Maneger 2 `person name`" :["assistent1"]}
# security_mng3 = {"Security Departament  Maneger 3 `person name`" :["assistent1"]}

# finance = {"Finance Departament Head `person name` ":[finance_mng1, finance_mng2, finance_mng3]}
# it = {"IT Departament Head `person name` ":[it_mng1, it_mng2, it_mng3]}
# security = {"Security Departament Head `person name` ":[security_mng1, security_mng2, security_mng3]}

# user1 = {"Organization Head `person name` ":[finance, it, security]}
# for i in user1.values():
    
#     for x in i:
#         print(f"{x}\n")

finance_mng1 = {"Finance Departament Maneger 1" :"person mng1 from finance",
                "Team" : ["assistent"]}
finance_mng2 = {"Finance Departament Maneger 2" : "person mng2 from finance",
                "Team" : ["assistent"]}
finance_mng3 = {"Finance Departament Maneger 3" : "person mng3 from finance",
                "Team" : ["assistent1"]}

it_mng1 = {"IT Departament Maneger 1" :"person mng1 from it",
            "Team" : ["assistent1"]}
it_mng2 = {"IT Departament Maneger 2" : "person mng2 from it",
            "Team" : ["assistent1"]}
it_mng3 = {"IT Departament Maneger 3" :"person mng3 from it",
            "Team" : ["assistent1"]}

security_mng1 = {"Security Departament  Maneger 1" : "person mng1 from security",
                "Team" : ["assistent1"]}
security_mng2 = {"Security Departament  Maneger 2 " :"person mng2 from security",
                "Team" : ["assistent1"]}
security_mng3 = {"Security Departament  Maneger 3 " : "person mng3 from security",
                "Team" : ["assistent1"]}



#  ORGANIZATION
president = {"president" : "person"}
finance = {"Finance Departament Head ": "person1",
            "Team" : [finance_mng1, finance_mng2 ,finance_mng3]}
it = {"IT Departament Head" : "person2",
        "Team" : [it_mng1, it_mng2, it_mng3]}
security = {"Security Departament Head" : "person3",
            "Team" : [security_mng1, security_mng2, security_mng3]}
group = [finance ,it ,security]


organization = {"eyof2025":"http//:",
                "organization head": president,
                "organization group": group}



# edition side
def adddep(it):
    it = {"IT Departament Head" : "person2",
        "Team" : [it_mng1, it_mng2, it_mng3]}
    try:
        while True:
            user = input("Enter Dep for add employer: ")
            if user == "finance" or user == "it" or user == "security":
                user = input()
                # ar dasrulebula
    except ValueError:
        print("Invalid input")

