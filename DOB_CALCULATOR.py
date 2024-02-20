from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    while True:
        try:
            dob_input = input("Enter your date of birth in YYYY-MM-DD format (e.g. 1990-01-01): ")
            dob = datetime.strptime(dob_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    age = calculate_age(dob)
    print("You are {} years old.".format(age))

if __name__ == "__main__":
    main()
