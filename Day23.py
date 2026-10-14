#creating set
#stud={111,"amit","java","amit"}
#using set constructor
stud=set([111,"amit","java","amit"])
print(stud)


#union(|)-combine two or more set
stud1={"amit","manish"}
stud2={"ravina","aishwarya"}
stud3={"donald","elan"}
stud=stud1|stud2|stud3
print("all student")
print(stud)

#intersection(&)-to find common in two set
stud1={"amit","manish","ravina"}
stud2={"ravi","amit"}
stud=stud1&stud2
print("Common student")
print(stud)

#difference(-)-return element in one set but are not in other set
city1={"nagpur","mumbai","delhi","pune"}
city2={"mumbai","nagpur"}
city=city1-city2
print("Different city")
print(city)


#symmetric difference(^)-return element are not in both set
days={"monday","tuesday","wednesday","thursday","friday","saturday"}
attendance={"tuesday","friday","saturday","sunday"}
absent=days^attendance
print("employee absent on:")
print(absent)



