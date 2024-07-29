import mysql.connector as d
import random

# Connect to the database
try:
    mydb = d.connect(
        host="localhost",
        user="root",
        password="",
        db="bank"
    )
    mycur = mydb.cursor()
except d.Error as err:
    print(f"Error: {err}")
    exit(1)

def validMobile(mobile_no):
    return mobile_no.isdigit() and len(mobile_no) == 10

def checkMobile(mobile_no):
    sql = "SELECT * FROM registration WHERE mobile_no = %s"
    mycur.execute(sql, (mobile_no,))
    result = mycur.fetchall()
    return len(result) > 0

def generate_otp():
    otp = ''.join(random.choices("1234567890", k=6))
    return otp

def accountInfo():
    print("\t \t YOUR OPTIONS")
    print('''\n1. Open New Account \n2. Display all account details.\n3. Display category wise account details. 
4. Update details \n5. Delete account \n6. About us \n7 comment or recomentations''')

    option = int(input("Enter your choice:"))

    if option == 1:
        print("\t \t YOUR OPTIONS")
        print("1. Saving account \n2. Current account ")
        op = int(input("Enter your choice:"))

        acc_holder_name = input("Enter your name: ")
        adhar_card_number= input("Enter your adhar card number: ")
        PAN_NUMBER=input("Enter your pan card number : ")
        mobile_no = input("Enter your mobile number: ")
        city = input("Enter your city: ")
        acc_type = "saving" if op == 1 else "current"
        balance = int(input("Enter your Balance: "))


        if balance < 1000:
            print("Please deposit amount greater than 1000")
            return

        sql = "INSERT INTO account (acc_holder_name,adhar_card_number,PAN_NUMBER, mobile_no, city, acc_type, balance) VALUES (%s, %s, %s, %s, %s,%s,%s)"
        values = (acc_holder_name,adhar_card_number,PAN_NUMBER,mobile_no, city, acc_type, balance)
        mycur.execute(sql, values)
        mydb.commit()
        print("Record inserted successfully...")

    elif option == 2:
        print("Display all account list")
        sql = "SELECT * FROM account"
        mycur.execute(sql)
        result = mycur.fetchall()
        for i in result:
            print(i)
        
    elif option == 3:
        print("Display category wise account list")
        print("Enter choice\n1. Saving \n2. Current")
        choice = int(input("Enter Your Choice:"))

        acc_type = 'saving'  
        if choice == 1:
            sql = f"SELECT * FROM account WHERE acc_type='{acc_type}'"
            mycur.execute(sql)
            result = mycur.fetchone()
            for i in result:
                print(i)
        elif choice == 2:
            sql = f"SELECT * FROM account WHERE acc_type='{acc_type}'"
            mycur.execute(sql)
            result = mycur.fetchone()
            for i in result:
                print(i)
        else:
            print("Enter Between 1 To 2")

        #sql = f"SELECT * FROM account WHERE acc_type='{acc_type}'"
        #mycur.execute(sql)
        #result = mycur.fetchall()
        #for i in result:
         #   print(i)

    elif option == 4:
        print("Update Info")
        acc_number = input("Enter your account number: ")
        print("\t \t YOUR OPTIONS")
        print("\n1. Name \n2. Mobile No \n3. Balance")
        option = int(input("Enter your choice: "))

        if option == 1:
            acc_holder_name = input("Enter new name: ")
            sql = "UPDATE account SET acc_holder_name=%s WHERE acc_number=%s"
            values = (acc_holder_name, acc_number)
            try:
                mycur.execute(sql, values)
                mydb.commit()
                print("Name updated successfully.")
            except d.Error as err:
                print(f"Error: {err}")

        elif option == 2:
            mobile_no = input("Enter new mobile number: ")
            sql = "UPDATE account SET mobile_no=%s WHERE acc_number=%s"
            values = (mobile_no, acc_number)
            try:
                mycur.execute(sql, values)
                mydb.commit()
                print("Mobile number updated successfully.")
            except d.Error as err:
                print(f"Error: {err}")

        elif option == 3:
            print("1.Deposite\n 2.Withdraw")
            ch = int(input("Enter choice"))
            if ch == 1:
                try:
                    new_balance = float(input("Enter amount to add to balance: "))
                    sql_select = "SELECT balance FROM account WHERE acc_number=%s"
                    mycur.execute(sql_select, (acc_number,))
                    current_balance = mycur.fetchone()[0]
                    updated_balance = current_balance + new_balance

                    sql_update = "UPDATE account SET balance=%s WHERE acc_number=%s"
                    values = (updated_balance, acc_number)
                    mycur.execute(sql_update, values)
                    mydb.commit()
                    print(f"Balance updated successfully. New balance: {updated_balance}")
                except ValueError:
                    print("Invalid amount entered. Please enter a numeric value.")
                except d.Error as err:
                    print(f"Error: {err}")      
            elif ch == 2:
                try:
                    with_balance = float(input("Enter amount to withdraw from balance: "))
                    sql_select = "SELECT balance FROM account WHERE acc_number=%s"
                    mycur.execute(sql_select, (acc_number,))
                    current_balance = mycur.fetchone()[0]
                    if with_balance > current_balance:
                        print("insufficient balance!")
                    else:
                        updated_balance = current_balance - with_balance
                        sql_update = "UPDATE account SET balance = %s WHERE acc_number = %s"
                        values = (updated_balance, acc_number)
                        mycur.execute(sql_update, values)
                        mydb.commit()
                        print(f"Balance updated successfully. New balance: {updated_balance}")
                except ValueError:
                    print("Invalid amount entered. Please enter a numeric value.")
                except d.Error as err:
                    print(f"Error: {err}")  
                    updated_balance = current_balance - new_balance

                    sql_update = "UPDATE account SET balance=%s WHERE acc_number=%s"
                    values = (updated_balance, acc_number)
                    mycur.execute(sql_update, values)
                    mydb.commit()
                    print(f"Balance updated successfully. New balance: {updated_balance}")
                except ValueError:
                    print("Invalid amount entered. Please enter a numeric value.")
                except d.Error as err:
                    print(f"Error: {err}")      
        else:
            print("Please enter 1 to 3 ")


    elif option == 5:
        acc_number = int(input("\nEnter account number that you want to delete:"))
        sql = "DELETE FROM account WHERE acc_number=%s"
        values = (acc_number,)
        mycur.execute(sql, values)
        mydb.commit()
        print("Account deleted...")

    elif option == 6:
        print("""About Your Project:
        Welcome to Bank Management System, your solution for efficient bank management.
        Simplify onboarding, payroll, performance tracking & engagement with our user-friendly project.

        Team ByteFighter Members:
            1. Shivam Chavan
            2. Pranav Mane
            3. Sahil Sawant
            4. Raghavendra Mokashi
            5. Pravin Jamadade

        Contact Us
        Need Support? Contact us.
              
              Project guide :- G. U. Sutar""")

    elif option == 7:
        print("enter suggetions about this project: \n ")
        
    else:
        print("\nPlease enter a correct option...")

while True:
    print("-----------Welcome to Bank Management System------------")
    print("Options:\n")
    print("1. Registration \n2. Login \n3. Exit")
    print("")
    op = int(input("Enter your choice: "))

    if op == 1:
        print("Registration")
        name = input("Enter name: ")
        while True:
            mobile_no = input("Please enter mobile number: ")
            if not validMobile(mobile_no):
                print("Invalid mobile number. Please enter a 10-digit number.\n")
                continue
            if not checkMobile(mobile_no):
                print("")
                #continue
            break
            print("Mobile number does not exist. Please try again.")

        password = input("Enter password: ")


        sql = "SELECT * FROM registration WHERE mobile_no = %s"
        mycur.execute(sql, (mobile_no,))
        result = mycur.fetchall()

        if not result:
            sql = "INSERT INTO registration (mobile_no, name, password) VALUES (%s, %s, %s)"
            values = (mobile_no, name, password)
            mycur.execute(sql, values)
            mydb.commit()
            print("Registration successful...")
        else:
            print("\nRecords already exist...")

    elif op == 2:
        print("Login")
        print("-------------")

        while True:
            mobile_no = input("Please enter mobile number: ")
            if not validMobile(mobile_no):
                print("Invalid mobile number. Please enter a 10-digit number.\n")
                continue
            if not checkMobile(mobile_no):
                print("Mobile number does not exist. Please try again.")
                continue
            break

        password = input("Enter your password: ")

        otp = generate_otp()
        print("Generated OTP: ", otp)

        user_otp = input("Please enter the OTP: ")

        if user_otp == otp:
            print("OTP is correct!")
        else:
            print("OTP is incorrect.")
            continue

        sql = "SELECT * FROM registration WHERE mobile_no = %s AND password = %s"
        values = (mobile_no, password)
        mycur.execute(sql, values)
        result = mycur.fetchall()

        if result:
            print("\nLogin successful...")
            accountInfo()
        else:
            print("\nWrong mobile number or password\n\n")

    elif op == 3:
        print("\nThank you... Visit again")
        print("=====================")
        break

    else:
        print("\nPlease enter option between 1 to 3")