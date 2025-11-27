


class Student():
    def __init__(self, name, phone, age, email):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email


class Group():
    def __init__(self, title, profession):
        self.title = title
        self.profession = profession
        self.students = []
    
    def add_student(self):
        name = input("name: ")
        phone = input("phone: ")
        age = input("age: ")
        email = input("email: ")
        student = Student(name, phone, age, email)
        self.students.append(student)

    def views_students(self):
        count = 0
        for item in self.students:
            count+=1
            print(f"{count}, name: {item.name}, age: {item.age}")
    
    def update_student(self):
        self.views_students
        index = int(input("Qaysi talabani yangilsh kk? id: "))
        student = self.students[index-1]

        print("\nMa'lumotlarni yangilash, (bo'sh qoldirsangiz eski qiymat saqlanib qoladi)")

        new_name = input(f"Yangi ism: ({student.name})")
        if new_name:
            student.name = new_name
        
        new_phone = input(f"Yangi raqam: ({student.phone})")
        student.phone = new_phone

        new_age = input(f"Yangi yosh: ({self.age})")
        student.age = new_age

        new_email = input(f"Yangi email: ({student.email}): ")
        if new_email:
            student.email = new_email

        print("Student ma'lumotlari yangilandi")
    
    def delete_student(self):
        if not self.students:
            print("Hozircha student yoq")
        
        self.views_students

        try:
            index = int(input("O'chirmoqchi bo'lgan student ID: "))
            student = self.students.pop[index-1]
            print(f"{student.name} muvaffaqiyatli o'chirlidi")    
        except:
            print("Noto'g'ri ID tanlandi ")





class OTM():
    def __init__(self, title):
        self.title = title
        self.groups = []
    
    def add_groups(self):
        title = input("title: ")
        profession = input("profession: ")
        group = Group(title, profession)
        self.groups.append(group)
    
    def view_groups(self):
        count = 0
        for item in self.groups:
            count+=1
            print(f"{count}, title: {item.title}, profession: {item.profession}")
    
    def update_groups(self):
        self.view_groups()
        index = int(input("Guruhni yangilamoqchisiz? id: "))
        group = self.groups[index-1]

        print("\nMalumotlarni yangilash, (bosh qoldirsangiz eski qiymat saqlanib qoladi)")

        new_title = input(f"Yangi Guruh: ({group.title})")
        if new_title:
            group.title = new_title
        print("Guruh nomi yangilandi")
    
    def delete_groups(self):
        if not self.groups:
            print("Hozircha Guruh yo'q!")
            return
        
        self.view_groups()

        try:
            index = int(input("O'chirmoqchi bo'lgan Guruh ID: "))
            if index < 1 or index > len(self.groups):
                print("Noto'g'ri ID: ")
            
            group = self.groups.pop(index-1)
            print(f"{group.title}  muvaffaqiyatli o'chirildi")
        except Exception as e:
            print("Noto'g'ri ID tanlandi")




class ERP:
    def __init__(self):
        self.title = "ERP"
        self.otms = []
    
    def add_otm(self):
        title = input("title")
        otm = OTM(title)
        self.otms.append(otm)
    
    def view_otms(self):
        count = 0
        for item in self.otms:
            count+=1
            print(f"{count}, title: {item.title}")
    
    def delete_otm(self):
        if not self.otms:
            print("Hozircha OTM yo'q!")
            return

        self.view_otms()

        try:
            index = int(input("O'chirmoqchi bo'lgan OTM ID: "))
            
            if index < 1 or index > len(self.otms):
                print("Noto'g'ri ID!")
                return

            otm = self.otms.pop(index - 1)
            print(f"{otm.title} muvaffaqiyatli o'chirildi!")
        except Exception as e:
            print("Noto'g'ri ID tanlandi!", e)

erp = ERP()



def group_manager(group: Group):
    while True:
        choice = input("1. add student \n 2.view student \n 3. update student \n 4. delete student \n 5. exit \n>>> ")
        if choice == '1':
            print("==========")
            group.add_student()
            print("------------")
        elif choice == '2':
            print("==========")
            group.views_students()
            print("-----------")
        elif choice == '3':
            print("=========")
            group.update_student()
            print("----------")
        elif choice =='4':
            print("===========")
            group.delete_student()
            print("-----------")
        elif choice=='5':
            break
        else:
            print(f'birini tanlang: ')


     

def otm_manager(otm: OTM):
    while True:
        choice = input(" 1. add group \n 2. view groups \n 3. update groups \n 4. delete groups \n 5. exit \n >>> ")
        if choice == '1':
            print("========")
            otm.add_groups()
            print("---------")
        elif choice == '2':
            print("=========")
            otm.view_groups()
            print("----------")
            index = int(input("otm_id: "))
            group = otm.groups[index-1]
            group_manager(group)
        elif choice == "3":
            print("=========")
            otm.update_groups()
            print("---------")
        elif choice == '4':
            print("============")
            otm.delete_groups()
            print("----------")
        elif choice=='5':
            break
        else:
            print(f'Birini tanlang: ')


def erp_manager(ep: ERP):
    while True:
        choice = input(" 1. add otm  \n 2. views otm \n 3. update otm \n 4. delete otm  \n 5. exit \n >>>")
        if choice == '1':
            print("=========")
            ep.add_otm()
            print("----------")
        elif choice == '2':
            print("=========")
            ep.view_otms()
            print("-----------")
        elif choice == '3':
            print("=========")
            ep.view_otms()
            print("-----------")
            index = int(input("otm_id: "))
            otm = ep.otms[index-1]
            otm_manager(otm)
        elif choice == "4":
            print("==========")
            ep.delete_otm()
            print("----------")
        elif choice=='5':
            break
        else:
            print(f'Birini tanlang: ')

erp_manager(erp)


