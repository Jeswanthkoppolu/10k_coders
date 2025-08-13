# # single inheritance
# class parentactor():
#     def __init__(self, name, p_worth):
#         self.p_name = name
#         self.p_worth = p_worth
#         print(f"{self.p_name} is the parent")
#     def p_assets(self):
#         print(f"{self.p_name}'s assets are {self.p_worth}cr")

# class childactor(parentactor):
#     def __init__(self, p_name, c_name, p_worth):
#         super().__init__(p_name, p_worth)
#         self.c_name = c_name
#         print(f"{self.c_name} came by the reference of {self.p_name}")
#     def c_assets(self, c_worth):
#         self.c_worth = c_worth
#         print(f"{self.c_name} has a net worth of {self.c_worth}cr")
#     def total_assets(self):
#         print(f"Total assets of {self.c_name} = {self.p_worth + self.c_worth}cr")

#     # Method Overriding
#     def p_assets(self):
#         print(f"Overridden: {self.c_name}'s parent {self.p_name} had assets worth {self.p_worth}cr")

# pk = childactor("pk", "ram", 150)
# pk.c_assets(100)
# pk.total_assets()
# pk.p_assets()  



# # multilevel inheritance
# class grandparentactor:
#     def __init__(self, gp_name, gp_worth):
#         self.gp_name = gp_name
#         self.gp_worth = gp_worth
#         print(f"{self.gp_name} is the grandparent")
#     def gp_assets(self):
#         print(f"{self.gp_name}'s assets are {self.gp_worth}cr")

# class parentactor(grandparentactor):
#     def __init__(self, gp_name, gp_worth, p_name, p_worth):
#         super().__init__(gp_name, gp_worth)
#         self.p_name = p_name
#         self.p_worth = p_worth
#         print(f"{self.p_name} is the parent")
#     def p_assets(self):
#         print(f"{self.p_name}'s assets are {self.p_worth}cr")

# class childactor(parentactor):
#     def __init__(self, gp_name, gp_worth, p_name, p_worth, c_name):
#         super().__init__(gp_name, gp_worth, p_name, p_worth)
#         self.c_name = c_name
#         print(f"{self.c_name} came by the reference of {self.p_name} and grandparent {self.gp_name}")
#     def c_assets(self, c_worth):
#         self.c_worth = c_worth
#         print(f"{self.c_name} has a net worth of {self.c_worth}cr")
#     def total_assets(self):
#         total = self.gp_worth + self.p_worth + self.c_worth
#         print(f"Total family assets of {self.c_name} = {total}cr")

#     # Method Overriding
#     def p_assets(self):
#         print(f"Overridden: {self.c_name}'s parent {self.p_name} had assets worth {self.p_worth}cr")

# pk = childactor("mega star", 200, "kalyan", 150, "Ram")
# pk.c_assets(100)
# pk.total_assets()
# pk.gp_assets()  # From grandparent
# pk.p_assets()   # Overridden in child




# # Multiple Inheritance
# class FilmCareer:
#     def __init__(self, name, debut_year):
#         self.name = name
#         self.debut_year = debut_year
#         print(f"{self.name} started career in {self.debut_year}")
#     def career_info(self):
#         print(f"{self.name} has been in the industry since {self.debut_year}")

# class FamilyWealth:
#     def __init__(self, family_name, total_worth):
#         self.family_name = family_name
#         self.total_worth = total_worth
#         print(f"{self.family_name} family has a net worth of {self.total_worth}cr")
#     def wealth_info(self):
#         print(f"Total family wealth of {self.family_name} is {self.total_worth}cr")

# class StarKid(FilmCareer, FamilyWealth):
#     def __init__(self, name, debut_year, family_name, total_worth, personal_worth):
#         FilmCareer.__init__(self, name, debut_year)
#         FamilyWealth.__init__(self, family_name, total_worth)
#         self.personal_worth = personal_worth
#         print(f"{self.name} is a star kid from the {self.family_name} family")
#     def total_assets(self):
#         total = self.total_worth + self.personal_worth
#         print(f"Total assets family + personal of {self.name} = {total}cr")

#     # Method Overriding
#     def wealth_info(self):
#         print(f"Overridden: {self.name}'s personal worth is {self.personal_worth}cr")
#         print(f"family wealth: {self.family_name} family has {self.total_worth}cr")

# sk = StarKid("ram charan", 2007, "mega", 300, 120)
# sk.career_info()     # From FilmCareer
# sk.wealth_info()     # Overridden version
# sk.total_assets()    # New method in StarKid




#Hierarchical inheritance
class FamilyWealth:
    def __init__(self, family_name, total_worth):
        self.family_name = family_name
        self.total_worth = total_worth
        print(f"{self.family_name} family has a net worth of {self.total_worth}cr")
    def wealth_info(self):
        print(f"Total family wealth of {self.family_name} is {self.total_worth}cr")


class FilmCareer(FamilyWealth):  # Child 1
    def __init__(self, name, debut_year, family_name, total_worth):
        super().__init__(family_name, total_worth)
        self.name = name
        self.debut_year = debut_year
        print(f"{self.name} started film career in {self.debut_year}")
    def career_info(self):
        print(f"{self.name} has been acting since {self.debut_year}")

    #  Method Overriding
    def wealth_info(self):
        print(f"{self.name} inherited wealth from the {self.family_name} family: {self.total_worth}cr")

class BusinessHeir(FamilyWealth):  # Child 2
    def __init__(self, name, company, family_name, total_worth):
        super().__init__(family_name, total_worth)
        self.name = name
        self.company = company
        print(f"{self.name} is managing the company '{self.company}'")
    def business_info(self):
        print(f"{self.name} is the CEO of {self.company}")

    # Method Overriding
    def wealth_info(self):
        print(f"{self.name} is managing {self.total_worth}cr worth of family assets through {self.company}")

# Film career child
actor = FilmCareer("ram", 2007, "mega", 300)
actor.wealth_info()      # Overridden version
actor.career_info()
print()

# Business heir child
heir = BusinessHeir("ram", "Rc Jewels", "mega", 300)
heir.wealth_info()       # Overridden version
heir.business_info()

