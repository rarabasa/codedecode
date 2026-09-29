print("DO YOU WANT TO CODE OR DECODE YOUR MESSAGE?")
a=input(" I WANT TO: ")
if a=="code":
    print("OKAY")
    x=input("ENTER YOUR MESSAGE: ")
    word=x.split(" ")
    if len(x)>=3:

        b=x.replace(x[0], "")
        c=b+x[0]
        d="!@#"+c+"!@#"
        print(d)
         
    else:
        print(word[::-1])

if a=="decode":
    print("OKAY")
    y=input("ENTER YOUR MESSAGE: ")
    if len(y)<=3:
        print(y[::-1])
    else:
        e=y.replace("!@#"," ")
        n=len(y)
        z=e.replace(e[0],e[n-1])
        print(z)
print("THANK YOU FOR USING OUR SERVICE")