from pathlib import Path
from selene import browser, have
from models.user import User, Hobby
from datetime import date


class RegistrationPage:
    def __init__(self):
        self._first_name = browser.element("#firstName")
        self._last_name = browser.element("#lastName")
        self._email = browser.element("#userEmail")
        self._phone = browser.element("#userNumber")
        self._date_input = browser.element("#dateOfBirthInput")
        self._subjects = browser.element("#subjectsInput")
        self._picture = browser.element("#uploadPicture")
        self._address = browser.element("#currentAddress")
        self._state = browser.element("#state")
        self._city = browser.element("#city")
        self._submit = browser.element("#submit")
        self._modal_title = browser.element("#example-modal-sizes-title-lg")
        self._table_values = browser.all(".table td:nth-child(2)")

    def _gender_value(self, gender: str) -> str:
        return "1" if gender == "Male" else "2" if gender == "Female" else "3"

    def open(self):
        browser.open("/automation-practice-form")
        return self

    def register(self, user: User):
        self.fill(user).submit()
        return self

    def fill(self, user: User):
        self._first_name.type(user.first_name)
        self._last_name.type(user.last_name)
        self._email.type(user.email)

        # Теперь формируем селектор для пола на основе user.gender
        gender_selector = f'label[for="gender-radio-{self._gender_value(user.gender)}"'
        browser.element(gender_selector).click()

        self._phone.type(user.phone)

        # Дата рождения
        self._date_input.click()
        browser.element(".react-datepicker__month-select").click()
        browser.element(f".react-datepicker__month-select option[value='{user.date_of_birth.month - 1}']").click()
        browser.element(".react-datepicker__year-select").click()
        browser.element(f".react-datepicker__year-select option[value='{user.date_of_birth.year}']").click()
        day_selector = f'[aria-label="Choose Sunday, December 5th, 1999"]'
        browser.element(day_selector).click()

        # Хобби
        for hobby in user.hobbies:
            browser.element(
                f'label[for="hobbies-checkbox-{["Reading", "Sports", "Music"].index(hobby.value) + 2}"]').click()

        # Предметы
        for subject in user.subjects:
            self._subjects.type(subject).press_enter()

        # Фото
        picture_path = str(Path(__file__).parent.parent.joinpath("photo", user.picture).resolve())
        self._picture.set_value(picture_path)

        # Адрес
        self._address.type(user.address)

        # Штат и город
        self._state.click()
        browser.element("#react-select-3-input").type(user.state).press_enter()
        self._city.click()
        browser.element("#react-select-4-input").type(user.city).press_enter()

        return self

    def submit(self):
        self._submit.click()
        return self

    def should_have_registered(self, user: User):
        self._modal_title.should(have.text("Thanks for submitting the form"))

        expected_texts = [
            f"{user.first_name} {user.last_name}",
            user.email,
            user.gender,
            user.phone,
            user.date_of_birth.strftime("%d %B,%Y"),
            user.subjects[0],
            user.hobbies[0].value,
            user.picture,
            user.address,
            f"{user.state} {user.city}",
        ]
        self._table_values.should(have.exact_texts(*expected_texts))
        return self