table = {'00':'I','01':'I','02':'I','03':'I','10':'I','11':'I','12':'I','13':'I','20':'I','21':'I','22':'I','23':'I'}

def read(cache,line):
    
    state = table[cache+line]
    
    if state == 'I':
        print()
        print("Cache",cache,"Bus Read",line)
        print("Miss")
        print()
        return False
    elif state == 'E':
        print()
        print("Hit")
        print(table[cache+line],"-->",end="")
        print(table[cache+line])
        print()
    elif state == 'S':
        print()
        print("Hit")
        print(table[cache+line],"-->",end="")
        print(table[cache+line])
        print()
    elif state == 'M':
        print()
        print("Hit Dirty")
        print(table[cache+line],"-->",end="")
        print(table[cache+line])
        print()
    elif state == 'O':
        print()
        print("Hit Dirty")
        print(table[cache+line],"-->",end="")
        print(table[cache+line])
        print()

    return True

def bus_read(cache,line):
    state = table[cache+line]
    
    if state == 'I':
        print("Cache",cache,"Bus Read",line)
        print("Miss")
        print(state,"-->",state)
        print("End Bus Read")
        print()
        return False
    elif state == 'E':
        print("Hit")
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'S'
        print(table[cache+line])
    elif state == 'S':
        print("Hit")
        print(table[cache+line],"-->",end="")
        print(table[cache+line])
    elif state == 'M':
        print("Hit Dirty")
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'O'
        print(table[cache+line])
    elif state == 'O':
        print("Hit Dirty")
        print(table[cache+line],"-->",end="")
        print(table[cache+line])

    return True

def write(cache,line):
    state = table[cache+line]

    if state == 'I':
        print()
        print("Miss")
        print()
        return False
    elif state == 'E':
        print()
        print("Hit")
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'M'
        print(table[cache+line])
        print
    elif state == 'S':
        print()
        print("Hit")
        print()
        return False
    elif state == 'M':
        print()
        print("Hit Dirty")
        print(table[cache+line],"-->",end="")
        print(table[cache+line])
        print()
    elif state == 'O':
        print()
        print("Hit Dirty")
        print()
        return False

    return True
    

def bus_write(cache,line):
    state = table[cache+line]

    print("Cache",cache,"Bus Write",line)
    
    if state == 'I':
        print("Miss")
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'I'
        print(table[cache+line])
    elif state == 'M':
        print("Hit Dirty")
        print("Flush")
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'I'
        print(table[cache+line])
    elif state == 'O':
        print("Hit Dirty")
        print("Flush")
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'I'
        print(table[cache+line])
    else:
        print("Flush")
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'I'
        print(table[cache+line])
        
    print("End Bus Write")
    print()

def evict_bus_write(cache,line):
    state = table[cache+line]

    print("Cache",cache,"Bus Write",line)
    
    if state == 'E':
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'S'
        print(table[cache+line])
    elif state == 'S':
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'S'
        print(table[cache+line])
    else:
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'I'
        print(table[cache+line])
        
    print("End Bus Write")
    print()

def read_memory(cache,line):
    print("Cache",cache)
    print(table[cache+line],"-->",end="")

    table[cache+line] = 'E'

    print(table[cache+line])
    print("Memory Read")
    print()

def evict(cache,line):
    state = table[cache+line]

    print("Cache",cache,"Bus Write",line)
    
    if state=='E':
        print()
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'I'
        print(table[cache+line])
    elif state == 'S':
        print()
        print(table[cache+line],"-->",end="")
        table[cache+line] = 'I'
        print(table[cache+line])
    elif state == 'M':
        if cache != '0':
            data = evict_bus_write('0',line)

        if cache != '1':
            data = evict_bus_write('1',line)

        if cache != '2':
            data = evict_bus_write('2',line)
    elif state == 'O':
        if cache != '0':
            data = evict_bus_write('0',line)

        if cache != '1':
            data = evict_bus_write('1',line)

        if cache != '2':
            data = evict_bus_write('2',line)

        
        
        
#Input File

file1 = input("Input file name: ")
f = open(file1, 'r')

f.read(0)

for line in f:
    cache = str(line[0])
    action = str(line[1])
    line = str(line[2])

    print(cache+action+line,end="")

    if action == 'e':
        evict(cache,line)
        
    elif action == 'r':
        data = read(cache,line)
        flag = False
        if not data:

            if cache != '0':
                data = bus_read('0',line)
                if data == True:
                    flag = True
            if cache != '1':
                data = bus_read('1',line)
                if data == True:
                    flag = True
            if cache != '2':
                data = bus_read('2',line)
                if data == True:
                    flag = True
                    
            if not flag:
                read_memory(cache,line)
            else:
                print()
                print("Cache",cache,",Bus Write",line)
                print(table[cache+line],"-->",end="")
                
                table[cache+line] = 'S'

                print(table[cache+line])
                print()
            
            
    elif action == 'w':
        data = write(cache,line)
        if not data:

            if cache != '0':
                data = bus_write('0',line)

            if cache != '1':
                data = bus_write('1',line)

            if cache != '2':
                data = bus_write('2',line)

            print("Cache",cache,",Bus Write",line)
            print(table[cache+line],"-->",end="")
            
            table[cache+line] = 'M'

            print(table[cache+line])
