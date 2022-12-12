import sys

def check_password(password):
  # Check if password has 1 capital letter
  has_capital = False
  for c in password:
    if c.isupper():
      has_capital = True
      break

  # Check if password has 4 lowercase letters
  has_four_lower = False
  lower_count = 0
  for c in password:
    if c.islower():
      lower_count += 1
  if lower_count >= 4:
    has_four_lower = True

  # Check if password has 1 number
  has_number = False
  for c in password:
    if c.isdigit():
      has_number = True
      break

  # Return whether password is valid
  return has_capital and has_four_lower and has_number

def main():
  password = input("Enter password: ")

  # Check if password is valid
  if check_password(password):
    print("Password is valid.")
  else:
    print("Password is not valid. Please try again.")

    # Give user 3 tries
    for i in range(3):
      password = input("Enter password: ")
      if check_password(password):
        print("Password is valid.")
        return
      else:
        print("Password is not valid. Please try again.")

    # If user has not entered a valid password after 3 tries, exit program
    print("Too many attempts. Exiting program.")
    sys.exit(1)

if __name__ == "__main__":
  main()
