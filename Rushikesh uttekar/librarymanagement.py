library = { "book1 " : {"title" : "Limitless" , "author" : "Jim Kwik" ,"year" : 1960, "status" :"avail"},
           "book2 " : {"title" : "Death on the Nile" , "author" : "Agatha Christie" ,"year" : 1970,"status" :"avail"},
           "book3 " : {"title" : "Murder on the orient express" , "author" : "Agatha Christie" ,"year" : 1980, "status" :"avail"}
           }


def add_book():
        book_count = 3
        new_book = f"book{book_count+1}"
        Title = input("Enter Title : ")
        auth = input("Enter author : ")
        year = int(input("Enter year : "))
        stat = input("Enter stat: ")
        library[new_book]={"title" :Title , "author" : auth, "year" : year ,"status": stat }
        book_count +=1
        print(library[new_book].items())
               

def borrow():
    which_book = input("enter the book name : ")
    for x,y in library.items() :
       title =  y.get("title")
       if which_book == title :
           library[x].update({"status": "not avail"})
           print(library[x].items())
           
def return_book():
    which_book = input("enter the book name : ")
    for x,y in library.items() :
       title =  y.get("title")
       if which_book == title :
           library[x].update({"status": "avail"})
           print(library[x].items())
           

def display() :
    for x,y in library.items() :
        print(library[x].items())
        

def search_book():
    search_book = input("enter book name or author name : ")
    for x,y in library.items():
        book_name = y.get("title")
        auth_name = y.get("author")
        if (search_book == book_name) or (search_book == auth_name) :
            print(library[x].values())
            


flag =1
print("operations : 1. Add books \n2. Borrow book \n3. Return books \n4. Display books \n5.Search book")
while flag :
   
    op = int(input("enter operation no. : "))
    
    if op == 1 :
        add_book()
    elif op == 2 : 
        borrow()
    elif  op == 3 :
        return_book()
    elif  op == 4 :
        display()
    elif  op == 5 :
        search_book()

    cont = input("do you wanna continue : ")
    if cont == 'y' or cont == 'Y' :
        flag = 1
    else :
        flag = 0    