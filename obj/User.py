class User:
  def __init__(self, user_id, user_name, followers=0):
    self.id = user_id
    self.username = user_name
    self.followers = followers

  def follow(self, user):
    self.followers+=1
    user.followers+=1