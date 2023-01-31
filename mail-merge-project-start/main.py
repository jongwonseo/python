PLACEHOLDER = "[name]"

with open("./mail-merge-project-start/Input/Names/invited_names.txt") as names_file:
  names = names_file.readlines()

print(names)
  
with open("./mail-merge-project-start/Input/Letters/starting_letter.txt") as letter_file:
  letter_contents = letter_file.read()
  
  for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    
    # print(new_letter)
    with open (f"./mail-merge-project-start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
      completed_letter.write(new_letter)
      