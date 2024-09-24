balance=10000
pin_code=5533
path='c:/pop/record.txt'
enter=input("enter your card:")
for i in range (1,4):
    pin=int (input("enter the pin code :"))
    if pin==pin_code:
        print("correct")
        break
    else:
        print("wrong")
    if i==3:
        print("too many wrong attemps, your card is block :")
        quit()
print("welcome to your account")
print("note:*******please enter the correct spell as written below *************")

while True:
    action=input("Deposit / Withdraw:\n").lower()
    if action =="deposit":
        dep_amt=int(input("enter your deposit ammount :"))
        print("you enter ",dep_amt,"Rs , ammount.")
        st_1=f"you enter {dep_amt}Rs , ammount."
        print("Your previous Balance was ",balance,'Rs')
        st_2=f"Your previous Balance was {balance}Rs"
        balance=balance+dep_amt
        print("After Deposit your balance is ",balance,'Rs')
        st_3=f"After Deposit your balance is {balance}Rs"
        
        record_1=st_1+"\n"+st_2+"\n"+st_3+"\n\n"
        with open(path,'a')as file:
            file.write(record_1)
            
    elif action=="withdraw":
    
        while True:

            withd_amt=int(input("enter your Withdraw ammount :"))
            if withd_amt<=balance :
                print("you enter ",withd_amt,"Rs , ammount.")
                st_4=f"you enter {withd_amt}Rs , ammount."
                print("Your previous Balance was ",balance,'Rs')
                st_5=f"Your previous Balance was {balance}Rs"
                balance=balance-withd_amt
                print("After Withdrawing",withd_amt,"Rs ammount ,your balance is ",balance,'Rs')
                st_6=f"After Withdrawing {withd_amt} Rs ammount ,your balance is {balance} Rs"
                record_2=st_4+"\n"+st_5+"\n"+st_6+"\n\n"
                with open(path,'a')as file:
                    file.write(record_2)
                    
                break    
            else:
                print("Gareeb Insaan, Awqaat me reh kr piesy nikalwaa.")


    else:
        print("Invled Request.")
        continue
    break

print("thank You .")