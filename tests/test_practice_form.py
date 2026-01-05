from classes.formPage import FormPage
from classes.userData import UserData


def test_demo_aqa():
    """Тест: заполнение и отправка формы."""
    # Инициализация данных пользователя
    user = UserData()

    # Инициализация страницы формы
    form_page = FormPage()

    # Открытие страницы
    form_page.open("/automation-practice-form")

    # Последовательное заполнение формы
    form_page.fill_name(user.first_name, user.last_name)
    form_page.fill_email(user.email)
    form_page.select_gender(user.gender)
    form_page.fill_phone(user.phone)
    form_page.fill_date_of_birth(
        user.date_of_birth['day'],
        user.date_of_birth['month'],
        user.date_of_birth['year']
    )
    form_page.select_hobbies(user.hobbies)
    form_page.fill_subjects(user.subjects)
    form_page.upload_picture(user.picture)
    form_page.fill_address(user.address)
    form_page.select_state_and_city(user.state, user.city)

    # Отправка формы
    form_page.submit_form()

    # Проверка результатов
    form_page.verify_submission()
    form_page.verify_data(user)