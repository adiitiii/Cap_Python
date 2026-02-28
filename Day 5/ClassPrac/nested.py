math =int(input("Enter marks for math: "))
eng =int(input("Enter marks for english: "))
science =int(input("Enter marks for science: "))

if(math >= 40):
    if(eng >= 40):
        if(science >= 40):
            if((math+eng+science / 3) >= 95):
                print("Passed with distinction")
            else:
                print("Pass")
        else:
            print("Fail")
    else:
        print("Fail")
else:
    print("Fail")