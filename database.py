def D():
    my_dict = {}
    listname = []
    listage = []
    for i in range (0, 3):
        name = raw_input("Enter the name: ")
        age = int(raw_input("Enter the age: "))
        listname.append(name)
        listage.append(age)
    my_dict['Name'] = listname
    my_dict['Age'] = listage
    return my_dict    
            
        
if __name__ == "__main__":
    print D()
