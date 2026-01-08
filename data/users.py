from models.user import User, Hobby
from datetime import date

student = User(
    first_name="yasha",
    last_name="kramarenko",
    email="yashaka@gmail.com",
    gender="Male",
    phone="9033247777",
    date_of_birth=date(1999, 12, 5),
    hobbies=[Hobby.READING],
    subjects=["Computer Science"],
    picture="test.jpg",
    address="Саратов, Усиевича 33а",
    state="Haryana",
    city="Karnal",
)