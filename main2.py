from datetime import date, datetime


class Student:
    def __init__(self, first_name, last_name, date_of_birth, phone,
                 hair_color=None, height=None):

        # validate first_name
        if not first_name or type(first_name) is not str:
            raise ValueError(f'Invalid first_name value: {first_name}')

        # validate last_name
        if not last_name or type(last_name) is not str:
            raise ValueError(f'Invalid last_name value: {last_name}')

        # validate phone
        if not phone or type(phone) is not str:
            raise ValueError(f'Invalid phone value: {phone}')

        # validate date_of_birth
        if type(date_of_birth) is not date:
            raise TypeError(f'Invalid type date_of_birth: {type(date_of_birth)}')

        # init
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.hair_color = hair_color
        self.height = height

    def get_full_years(self) -> int:
        now = datetime.now().date()
        return int((now - self.date_of_birth).days / 365)

############################################


st1 = Student('2345345345', 'Kaminskyi', date_of_birth=date(1990, 1, 23), phone='380935786917')
st2 = Student('2345345345', 'Kaminskyi', date_of_birth=date(1992, 3, 15), phone='380935786917')
print(st1.get_full_years())
print(st2.get_full_years())
