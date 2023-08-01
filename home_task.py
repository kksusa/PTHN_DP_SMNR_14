import pytest


class User:
    def __init__(self, user_id, name, level):
        self.user_id = user_id
        self.name = name
        self.level = level

    def __str__(self):
        return f'Идентификационный номер: {self.user_id}; имя: {self.name}; уровень доступа:' \
               f' {self.level}\n'

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __ne__(self, other):
        return self.user_id != other.user_id

    def __gt__(self, other):
        return self.level < other.level

    def __lt__(self, other):
        return self.level > other.level


@pytest.fixture
def usr1():
    return User(12345, "Кирилл", 5)


@pytest.fixture
def usr2():
    return User(45678, "Ксения", 3)


@pytest.fixture
def usr3():
    return User(12345, "Михаил", 6)


def test_users_equality(usr1, usr3):
    assert usr1 == usr3


def test_users_non_equality(usr1, usr2):
    assert usr1 != usr2


def test_users_gt_equality(usr2, usr3):
    assert usr2 > usr3


def test_users_lt_equality(usr1, usr3):
    assert usr3 < usr1


def test_user_data_print(usr2):
    print(f"\n{usr2}")


if __name__ == '__main__':
    pytest.main()
