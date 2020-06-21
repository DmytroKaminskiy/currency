from datetime import date, datetime


class Student:
    def __init__(self, first_name, last_name, date_of_birth, phone,
                 hair_color=None, height=None):

        # 1. Height cm 100 < height < 250
        # 2. hair_color values_list ('blond', 'red', 'black', ...)
        # 3. date_of_birth cannot be in future
        # 4. phone (len(phone) > 9, should be integers)
        # 5. Display all information about student (method)
        # Bonus add tests

        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.hair_color = hair_color
        self.height = height
        self.validate()

    # validation
    def validate(self):
        self.validate_date_of_birth()
        self.validate_first_name()
        self.validate_last_name()
        self.validate_phone()

    def validate_first_name(self):
        # validate first_name
        if not self.first_name or type(self.first_name) is not str:
            raise ValueError(f'Invalid first_name value: {self.first_name}')

    def validate_last_name(self):
        # validate last_name
        if not self.last_name or type(self.last_name) is not str:
            raise ValueError(f'Invalid last_name value: {self.last_name}')

    def validate_phone(self):
        # validate phone
        if not self.phone or type(self.phone) is not str:
            raise ValueError(f'Invalid phone value: {self.phone}')

    def validate_date_of_birth(self):
        if type(self.date_of_birth) is not date:
            raise TypeError(f'Invalid type date_of_birth: {type(self.date_of_birth)}')

    # end validation methods

    def get_full_years(self) -> int:
        now = datetime.now().date()
        return int((now - self.date_of_birth).days / 365)

############################################


if __name__ == '__main__':
    st2 = Student('2345345345', 'Kaminskyi', date_of_birth=date(1992, 3, 15), phone='380935786917')
    assert st2.get_full_years() == 28
    assert st2.last_name == 'Kaminskyi'

    # check type error
    try:
        Student('2345345345', 'Kaminskyi', date_of_birth=123, phone='380935786917')
    except TypeError as exc:
        assert type(exc) is TypeError
