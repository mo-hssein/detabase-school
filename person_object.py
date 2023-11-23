from datetime import datetime


class Person:
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

    def get_full_data(self) -> str:
        return f"The name is : {self.get_name()}\nThe age is : {self.get_age()}\nThe gender is : {self.get_gender()}\nThe address is : {self.get_address()}\nThe phone is : {self.get_phone()}\nThe GPA is : {self.get_GPA()}\nThe adjective is : {self.get_adjective()}\nThe date of join is : {self.get_date_of_join()}\n"

    def __str__(self) -> str:
        return self.get_full_data()


employee = Person(
    "Mohamed",
    24,
    "Egypt, Al Fayoum",
    "01127014781",
    4.2,
    "Student",
    "25/11/2022",
    "Mele",
)

print(employee.get_full_data())
