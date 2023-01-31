from User import User
      
user_1 = User("001", "angela",3)
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_2.followers)
