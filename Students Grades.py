def main():
    log()
    print("Welcome to Grade Central \n")
    while(True):
        start()
        x = input("What would you like to do today? (Enter a number): ")
        print()
        while not x in options:
            x = input("Error: Enter number between 1 and 6 inclusive: ")
            print()
              
        if x == "1":
            addSt()
            
        elif x == "2":
            grades()
           
        elif x == "3":
            avg()
            
        elif x == "4":
            remove()

        elif x == "5":
            save()
   
        elif x == "6" :
            if quit():
                save()
                print("GoodBye")
                exit()
            else:
                print()


def log():
    print("To exit enter 'exit' \n")
    l = input("Username: ")
    if(l == 'exit'):
        exit()
    p = input("Password: ")
    if(p == 'exit'):
        exit()
    if l in users:
        if (users[l] == p):
            print()
            print("Successful")
            print("Welcome, {} \n".format(l))
            return
    print()
    print("Username or Password wrong \n")
    log()


    
def start():
    print("  [1] - Add Student")
    print("  [2] - Enter Grades")
    print("  [3] - Student Average Grades")
    print("  [4] - Remove Student")
    print("  [5] - Save")
    print("  [6] - Exit")
    print("  'abort' - Abort any operation \n")
    print("Students:  {} \n".format(students))




def addSt():
    x = []
    t = 0
    name = input("Student Name to add: ")
    if(name == 'abort'):
        return
    name = name[0].upper() + name[1:].lower()
    if name in students:
        t = 1
    elif name.upper() in students:
        name = name.upper()
        t = 1
    elif name.lower() in students:
        name = name.lower()
        t = 1
    if t == 1:
        print("Student alrrady exist with same name")
    else:
        grades = input("His Grades: ")
        if(grades == 'abort'):
            return
        g = grades.split()
        for f in g:
            if f.isdigit():
              x.append(int(f))
            else:
                print("Please enter only number and between each mark a space")
                t = 2
                break
        if t == 0:
            students[name] = x
            ac  = name
            for f in students[name]:
                ac = ac +" " + str(f)
            x = open("Students.txt","a")
            x.write(ac)
            x.close()
            print("Saving............... \n") 
            return



def grades():
    t = 0
    name = input("Student Name: ")
    if(name == 'abort'):
        return
    name = name[0].upper() + name[1:].lower()
    if name in students:
        t = 1
    elif name.upper() in students:
        name = name.upper()
        t = 1
    elif name.lower() in students:
        name = name.lower()
        t = 1
    if t == 1:
        grades = input("His Grades: ")
        if(grades == 'abort'):
            return
        g = grades.split()
        x = []
        for f in g:
            if f.isdigit():
              x.append(int(f))
            else:
                print("Please enter only number and between each mark a space")
                t = 0
                break
        if t == 1:
            students[name] = students[name] + x
            print("Adding grades....")
            print("Done \n")
            save()
            return
                
    else:
        print("Student does not exist \n")
    


def avg():
    t = 0
    print("  [1] - All averages")
    print("  [2] - Specifc Student \n")
    z = input("Enter number: ")
    if(z == 'abort'):
        return
    if(z == "1"):
        for a in students:
            h = students[a]
            f = s.mean(h)
            print("Student name: {}".format(a))
            print("Average Grade: {} \n".format(f))  
    else:
        name = input("Student Name: ")
        if(name == 'abort'):
            return
        name = name[0].upper() + name[1:].lower()
        if name in students:
            t = 1
        elif name.upper() in students:
            name = name.upper()
            t = 1
        elif name.lower() in students:
            name = name.lower()
            t = 1
        if t == 1:
            print("Calculating......")
            x = s.mean(students[name])
            print("Done")
            print("Student name: {}".format(name))
            print("Average Grade: {} \n".format(x))
        else:
            print("Student does not exist \n")



def remove():
    t = 0
    name = input("Student Name: ")
    if(name == 'abort'):
        return
    name = name[0].upper() + name[1:].lower()
    if name in students:
        t = 1
    elif name.upper() in students:
        name = name.upper()
        t = 1
    elif name.lower() in students:
        name = name.lower()
        t = 1
    if t == 1:
        print("Deleting.....")
        del students[name]
        print("Done \n")
        save()
    else:
        print("Student does not exist \n")



def save():
    ac = ""
    for k in students:
        ac = ac + k
        for j in students[k]:
            ac = ac + " " + str(j)
        ac = ac + "\n"
    print(ac)
    x = open("Students.txt","w")
    x.write(ac)
    x.close()
    print("Saving............... \n")



def quit():
      y = input("Sure? (Enter yes/no): ")
      while(not(y == "yes") and not(y == "no")):
          y = input("Try again yes/no: ")
      return (y == "yes")


    
def getP():
    st = open("pwd.txt","r")
    f = st.read()
    s = f.split()
    p = {}
    for y in s:
        if s.index(y)%2 == 0:
            p[y] = s[s.index(y)+1]
    st.close()
    return p



def getS():
    st = open("Students.txt","r")
    f = st.read()
    s = f.split()
    p = {}
    for y in s:
        l = []
        if not y.isdigit():
            for mn in s[(s.index(y)+1):]:
                if not mn.isdigit():
                    break
                l.append(int(mn))
            p[y] = l
    st.close()
    return p

   

import statistics as s
users = getP()
options = ["1","2","3","4","5","6"]
students = getS()
main()



