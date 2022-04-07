class User():
  first_name = ""
  last_name = ""
  email_address = ""
  phone_number = ""
  allergies = ""
  food_diet = ""

  def get_full_name(self):
    return "{} {}".format(self.first_name, self.last_name)


class fullMenu():
  mealItems = []
  date = ""
  sort = ""
  search = ""


class Meal():
  name = ""
  serving_size = ""
  full_description = ""
  ingredients = ""


class Price():
  amount = ""
  quantity = ""
  totalPrice = ""


class Order(Meal, Price):
  orderId = ""
  orderedMeal = Meal.name
  quantity = Meal.serving_size
  short_description = ""
  isPacked = False
  additional_needs = ""
  price = Price.totalPrice


user = User()  # instantiate the user class
user.first_name = "Sosu"
user.last_name = "Alfred"
user.phone_number = "+233203580427"
user.email_address = "sosualfred@gmail.com"
user.allergies = "crab, gluten"
