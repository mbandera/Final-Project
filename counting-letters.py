def countingletter(filename, mychar):
    f.open(filename, 'r')
    count = 0;
    run = True
    while run:
        letter = f.read(1)
        letter = letter.lower()
        if letter == "":
            break
        else:
            if letter == mychar:
                count = count + 1
                
    print(count)
    
countingletter(filename="constitution.txt", mychar="o")
countingletter("constitution.txt", "a")
    