import datetime


class User:
    """
    # Don't forget to write a docstring!
    # This class enables the storing and handling of user data in an organized way
      It represents known user data"""


    def __init__(self, full_name, birthday): 
        """
        # BIRTHDAY FORMAT: yyyy/mm/dd

        # initialization or (in other languages), constructor
        # this method is called every time a new instance of the class is called
        # (self)) is a reference to the new object that's being created"""

        self.full_name = full_name
        self.birthday = datetime.datetime.strptime(birthday, '%Y/%m/%d').date()  # yyyy/mm/dd
         
        self.first_name = full_name.split(' ')[0]
        self.last_name = full_name.split(' ')[-1]


    def age(self):
        """
        # BIRTHDAY FORMAT: yyy/mm/dd
        # calculates the age of a person given their birthdate"""

        current_date = datetime.datetime.now()
        is_after_birthday = (current_date.month, current_date.day) < (self.birthday.month, self.birthday.day)

        return current_date.year - self.birthday.year - is_after_birthday
    
