from pathlib import Path
from selene import browser, have
from pages.userData import UserData


class FormPage:
    """Класс, представляющий страницу формы."""

    def open(self, url: str):
        """Открыть страницу формы."""
        browser.open(url)

    def fill_name(self, first_name: str, last_name: str):
        """Заполнить поля имени и фамилии."""
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)

    def fill_email(self, email: str):
        """Заполнить поле email."""
        browser.element('#userEmail').type(email)

    def select_gender(self, gender: str):
        """Выбрать пол."""
        label_for = 'gender-radio-1' if gender == 'Male' else 'gender-radio-2'
        browser.element(f'label[for="{label_for}"]').click()

    def fill_phone(self, phone: str):
        """Заполнить поле телефона."""
        browser.element('#userNumber').type(phone)

    def fill_date_of_birth(self, day: int, month: int, year: int):
        """Заполнить дату рождения."""
        browser.element('#dateOfBirthInput').click()

        # Выбор месяца
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'.react-datepicker__month-select option[value="{month}"]').click()

        # Выбор года
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()

        # Выбор дня
        date_label = f'Choose Sunday, December {day}th, {year}'
        browser.element(f'[aria-label="{date_label}"]').click()

    def select_hobbies(self, hobbies: list):
        """Выбрать увлечения."""
        if 'Reading' in hobbies:
            browser.element('label[for="hobbies-checkbox-2"]').click()

    def fill_subjects(self, subjects: list):
        """Заполнить предметы."""
        for subject in subjects:
            browser.element('#subjectsInput').type(subject).press_enter()

    def upload_picture(self, picture_name: str):
        """Загрузить фотографию."""
        picture_path = str(
            Path(__file__).parent.parent.joinpath('photo', picture_name).resolve()
        )
        browser.element('#uploadPicture').set_value(picture_path)

    def fill_address(self, address: str):
        """Заполнить адрес."""
        browser.element('#currentAddress').type(address)

    def select_state_and_city(self, state: str, city: str):
        """Выбрать штат и город."""
        browser.element("#state").click()
        browser.element("#react-select-3-input").type(state).press_enter()

        browser.element("#city").click()
        browser.element("#react-select-4-input").type(city).press_enter()

    def submit_form(self):
        """Отправить форму."""
        browser.element('#submit').click()

    def verify_submission(self):
        """Проверить успешную отправку формы."""
        browser.element('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form')
        )

    def verify_data(self, user_data: UserData):
        """Проверить отображаемые данные в таблице."""
        expected_texts = [
            f'{user_data.first_name} {user_data.last_name}',
            user_data.email,
            user_data.gender,
            user_data.phone,
            f'0{user_data.date_of_birth["day"]} December,{user_data.date_of_birth["year"]}',
            user_data.subjects[0],
            user_data.hobbies[0],
            user_data.picture,
            user_data.address,
            f'{user_data.state} {user_data.city}'
        ]

        browser.all('.table td:nth-child(2)').should(have.exact_texts(*expected_texts))