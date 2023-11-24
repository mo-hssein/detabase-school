from datetime import datetime
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(
        self, name, age, address, phone, GPA, adjective, date_of_join, gender
    ) -> None:
        """
        - The main object of all person in our project

        Prametars:;
        - Name (str) : name of person
        - Age (int) : age of person
        - Address (str) : address of person
        - Phone (str) : phone of person
        - GPA (float) : GPA of person
        - Adjective (str) : adjective of person
        - Date_of_join (int) : date of join of person
        - Gender (str) : gender of person

        Return:
        - None

        """
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone = phone
        self.__GPA = GPA
        self.__adjective = adjective
        self.__date_of_join = datetime.strptime(date_of_join, "%d/%m/%Y").date()
        self.__gender = gender

    def get_name(self) -> str:
        """
        - This feature is used to display the person's name

        Prametars:
        - None

        Return:
        - Name of person

        """
        return self.__name

    def set_name(self, new_name) -> None:
        """
        - This feature is used to modify a person's name

        Prametars:
        - new_name (str): The new name of persin

        Return:
        - None

        Raise:
        - ValueError: '{new_name}' is not str, The name must be a str

        """
        if not isinstance(new_name, str):
            raise ValueError(f"'{new_name}' is not str, The name must be a str")
        else:
            self.__name = new_name

    def get_age(self) -> int:
        """
        - This feature is used to display the person's age

        Prametars:
        - None

        Return:
        - None

        """
        return self.__age

    def set_age(self, new_age) -> None:
        """
        - This feature is used to modify a person's age

        Prametars:
        - new_age (int): The new age of persin

        Return:
        - None

        Raise:
        - ValueError: '{new_age}' is not int, The age must be an int

        """
        if type(new_age) != int:
            raise ValueError(f"'{new_age}' is not int, The age must be an int")
        else:
            self.__age = new_age

    def get_address(self) -> str:
        """
        - This feature is used to display the person's address

        Prametars:
        - None

        Return:
        - Address of person

        """
        return self.__address

    def set_address(self, new_address) -> None:
        """
        - This feature is used to modify a person's address

        Prametars:
        - new_address (str): The new address of persin

        Return:
        - None

        Raise:
        - ValueError: '{new_address}' is not str, The address must be a str

        """
        if type(new_address) != str:
            raise ValueError(f"'{new_address}' is not str, The address must be a str")
        else:
            self.__address = new_address

    def get_phone(self) -> int:
        """
        - This feature is used to display the person's phone

        Prametars:
        - None

        Return:
        - phone of person

        """
        return self.__phone

    def set_phone(self, new_phone) -> None:
        """
        - This feature is used to modify a person's phone

        Prametars:
        - new_phone (str): The new phone of persin

        Return:
        - None

        Raise:
        - ValueError: '{new_phone}' is not str, The phone must be a str

        """
        if type(new_phone) != str:
            raise ValueError(f"'{new_phone}' is not str, The phone must be a str")
        else:
            self.__phone = new_phone

    def get_GPA(self) -> float:
        """
        - This feature is used to display the person's GPA

        Prametars:
        - None

        Return:
        - GPA of person

        """
        return self.__GPA

    def set_GPA(self, new_GPA) -> None:
        """
        - This feature is used to modify a person's GPA

        Prametars:
        - new_GPA (float): The new GPA of persin

        Return:
        - None

        Raise:
        - ValueError: '{new_GPA}' is not float, The GPA must be a float
        - ValueError: The GPA must be between 0 and 4.0
        """
        if type(new_GPA) != float:
            raise ValueError(f"'{new_GPA}' is not float, The GPA must be a float")
        elif new_GPA > 4.0 or new_GPA < 0:
            raise ValueError(f"The GPA must be between 0 and 4.0")
        else:
            self.__GPA = new_GPA

    def get_adjective(self) -> str:
        """
        - This feature is used to display the person's adjective

        Prametars:
        - None

        Return:
        - adjective of person

        """
        return self.__adjective

    def set_adjective(self, new_adjective) -> None:
        """
        - This feature is used to modify a person's adjective

        Prametars:
        - new_adjective (str): The new adjective of persin

        Return:
        - None

        Raise:
        - ValueError: '{new_GPA}' is not float, The GPA must be a float

        """
        if type(new_adjective) != str:
            raise ValueError(
                f"'{new_adjective}' is not str, The adjective must be a str"
            )
        else:
            self.__adjective = new_adjective

    def get_date_of_join(self) -> int:
        """
        - This feature is used to display the person's date of join

        Prametars:
        - None

        Return:
        - The person's date of join

        """
        return self.__date_of_join.strftime("%d/%m/%Y")

    def set_date_of_join(self, new_date) -> None:
        """
        - This feature is used to modify the person's date of join

        Prametars:
        - new_date (int): the new date of join

        Return:
        - None

        Raise:
        - ValueError: '{new_date}' is not str, The date of join must be a str

        """
        if type(new_date) != str:
            raise ValueError(f"'{new_date}' is not str, The date of join must be a str")
        else:
            self.__date_of_join = new_date

    def get_gender(self) -> str:
        """
        - This feature is used to display the person's gender

        Prametars:
        - None

        Return:
        - The person's gender

        """
        return self.__gender

    def set_gender(self, new_gender) -> None:
        """
        - This feature is used to modify the person's gender

        Prametars:
        - new_gender (str): the new of person's gender

        Return:
        - None

        Raise:
        - ValueError: '{new_date}' is not str, The date of join must be a str
        - ValueError: The gender you entered is unknown, Gender must be Male or Female
        """
        gender = ["Male", "Female"]
        if type(new_gender) != str:
            raise ValueError(f"'{new_gender}' is not str, The gender must be a str")
        elif new_gender not in gender:
            raise ValueError(
                f"The gender you entered is unknown, Gender must be Male or Female"
            )
        else:
            self.__gender = new_gender

    @abstractmethod
    def get_full_data(self) -> str:
        return f"The name is : {self.get_name()}\nThe age is : {self.get_age()}\nThe gender is : {self.get_gender()}\nThe address is : {self.get_address()}\nThe phone is : {self.get_phone()}\nThe GPA is : {self.get_GPA()}\nThe adjective is : {self.get_adjective()}\nThe date of join is : {self.get_date_of_join()}"

    def __str__(self) -> str:
        return self.get_full_data()


class Administrative(Person):
    def __init__(
        self,
        name,
        age,
        address,
        phone,
        GPA,
        adjective,
        date_of_join,
        gender,
        salary,
        responsibilities,
    ) -> None:
        super().__init__(
            name, age, address, phone, GPA, adjective, date_of_join, gender
        )
        """
        - The Administrative object 

        Prametars:;
        - Name (str) : name of Administrative
        - Age (int) : age of Administrative
        - Address (str) : address of Administrative
        - Phone (str) : phone of Administrative
        - GPA (float) : GPA of Administrative
        - Adjective (str) : adjective of Administrative
        - Date_of_join (int) : date of join of Administrative
        - Gender (str) : gender of Administrative
        - Salary (int) : salary of the Administrative
        - responsibilities (list) : responsibilities of the Administrative

        Return:
        - None

        """
        self.__salary = salary
        self.__responsibilities = responsibilities

    def get_salary(self) -> int:
        """
        - This feature is used to display an Administrative's salary

        Prametars:
        - None

        Return:
        - The Administrative's salary
        """
        return self.__salary

    def set_salary(self, new_salary) -> None:
        """
        - This feature is used to modify an Administrative's salary

        Prametars:
        - new_salary (int): the new of Administrative's salary

        Return:
        - None

        Raise:
        - ValueError: '{new_salary}' is not int, The salary must be int
        """
        if isinstance(new_salary, int):
            self.__salary = new_salary
        else:
            raise ValueError(f"'{new_salary}' is not int, The salary must be int")

    def get_responsibilities(self) -> list:
        """
        - This feature is used to display an Administrative responsibilities

        Prametars:
        - None

        Return:
        - The Administrative responsibilities
        """
        return self.__responsibilities

    def set_responsibilities(self, new_responsibilities) -> None:
        """
        - This feature is used to modify an Administrative responsibilities

        Prametars:
        - new_responsibilities (list): the new Administrative responsibilities

        Return:
        - None

        Raise:
        - ValueError: '{new_salary}' is not int, The salary must be int
        """
        if isinstance(new_responsibilities, list):
            self.__responsibilities = new_responsibilities
        else:
            raise ValueError(
                f"'{new_responsibilities}' is not list, The responsibilities must be list"
            )

    def get_full_data(self) -> str:
        return (
            f"Data of the {self.get_adjective()} is : \n"
            + super().get_full_data()
            + f"\nThe Salary is {self.__salary}\nThe Responsibilities is : {self.__responsibilities}"
        )


class Teacher(Administrative):
    def __init__(
        self,
        name,
        age,
        address,
        phone,
        GPA,
        adjective,
        date_of_join,
        gender,
        salary,
        responsibilities,
        courses,
    ) -> None:
        super().__init__(
            name,
            age,
            address,
            phone,
            GPA,
            adjective,
            date_of_join,
            gender,
            salary,
            responsibilities,
        )
        """
        - The teacher object 

        Prametars:;
        - Name (str) : name of teacher
        - Age (int) : age of teacher
        - Address (str) : address of teacher
        - Phone (str) : phone of teacher
        - GPA (float) : GPA of teacher
        - Adjective (str) : adjective of teacher
        - Date_of_join (int) : date of join of teacher
        - Gender (str) : gender of teacher
        - Salary (int) : salary of the teacher
        - responsibilities (list) : responsibilities of the teacher
        - courses (list) : courses of teacher

        Return:
        - None

        """
        self.__courses = courses

    def get_courses(self) -> list:
        """
        - This feature is used to display a teacher's courses

        Prametars:
        - None

        Return:
        - The Teacher's courses
        """
        return self.__courses

    def set_salary(self, new_courses) -> None:
        """
        - This feature is used to modify an a teacher's courses

        Prametars:
        - new_courses (list): the new courses of teachers

        Return:
        - None

        Raise:
        - ValueError: '{new_salary}' is not int, The salary must be int
        """
        if isinstance(new_courses, list):
            self.__courses = new_courses
        else:
            raise ValueError(f"'{new_courses}' is not list, The courses must be list")

    def get_full_data(self) -> str:
        return (
            "Data of the teacher is : \n"
            + super().get_full_data()
            + f"\nThe courses is : {self.__courses}"
        )


class Student(Person):
    def __init__(
        self,
        name,
        age,
        address,
        phone,
        GPA,
        adjective,
        date_of_join,
        gender,
        subscription,
        parent_phone,
        level,
        courses,
    ) -> None:
        super().__init__(
            name, age, address, phone, GPA, adjective, date_of_join, gender
        )
        """
        - The student object 

        Prametars:
        - Name (str) : name of student
        - Age (int) : age of student
        - Address (str) : address of student
        - Phone (str) : phone of student
        - GPA (float) : GPA of student
        - Adjective (str) : adjective of student
        - Date of join (int) : date of join of student
        - Gender (str) : gender of student
        - Subscription (int) : subscription of student
        - Parent phone (str) : Parent phone of student
        - level (int) : level of student
        - courses (list) : courses of student

        Return:
        - None

        """
        self.__subscription = subscription
        self.__parent_phone = parent_phone
        self.__level = level
        self.__courses = courses

    def get_full_data(self) -> str:
        return (
            f"The data of student is :\n"
            + super().get_full_data()
            + f"\nThe subscription is : {self.__subscription}\nThe Parent phone is : {self.__parent_phone}\nThe level is : {self.__level}\nThe courses is {self.__courses}"
        )


class Workman(Administrative):
    def __init__(
        self,
        name,
        age,
        address,
        phone,
        GPA,
        adjective,
        date_of_join,
        gender,
        salary,
        responsibilities,
    ) -> None:
        super().__init__(
            name,
            age,
            address,
            phone,
            GPA,
            adjective,
            date_of_join,
            gender,
            salary,
            responsibilities,
        )
        """
        - The Workman object 

        Prametars:;
        - Name (str) : name of workman
        - Age (int) : age of workman
        - Address (str) : address of workman
        - Phone (str) : phone of workman
        - GPA (float) : GPA of workman
        - Adjective (str) : adjective of workman
        - Date_of_join (int) : date of join of workman
        - Gender (str) : gender of workman
        - Salary (int) : salary of the workman
        - responsibilities (list) : responsibilities of the workman

        Return:
        - None

        """

    def get_full_data(self) -> str:
        return super().get_full_data()


class Database:
    def __init__(self) -> None:
        self.__Teacher = []
        self.__Administrative = []
        self.__Workman = []
        self.__Student = []

    def add_Teacher(self, Teacher):
        self.__Teacher.append(Teacher)

    def add_Administrative(self, Administrative):
        self.__Administrative.append(Administrative)

    def add_Workman(self, Workman):
        self.__Workman.append(Workman)

    def add_Student(self, Student):
        self.__Student.append(Student)

    def get_Teacher_list(self):
        for Teacher in self.__Teacher:
            return Teacher

    def get_Administrative_list(self):
        for Administrative in self.__Administrative:
            return Administrative

    def get_Workman_list(self):
        for Workman in self.__Workman:
            return Workman

    def get_Student_list(self):
        for Student in self.__Student:
            return Student


db = Database()

Mohamed = Administrative(
    "Mohamed",
    25,
    "Egypt",
    "01127014781",
    3.5,
    "Security",
    "22/10/2022",
    "Male",
    3500,
    ["Maintaining security", "inspecting visitors"],
)
Ahmed = Teacher(
    "Ahmed",
    26,
    "Egypt",
    "01127014781",
    4.0,
    "Security",
    "22/10/2022",
    "Male",
    10000,
    ["Maintaining security"],
    ["x", "y"],
)
Ali = Student(
    "Ali",
    25,
    "Egypt",
    "01127014781",
    3.5,
    "Student",
    "22/10/2022",
    "Male",
    3500,
    "012121212121",
    5,
    ["sds", "sdss"],
)


db.add_Administrative(Mohamed)
db.add_Teacher(Ahmed)
db.add_Student(Ali)

print(db.get_Teacher_list())
