import math
import nope

def lesbian(operation,varnum):
    
    varnum = int(varnum)
    a = []
    b = []
    c = 10-varnum
    b.append(int(operation))
    b.append(int(varnum))



    i = 0
    while i < varnum:

        e = input(f"Please enter variable {i+1}: ")
            
        try:
            float(e)
            a.append(float(e))
            b.append(float(e))
            i += 1
        except ValueError:
            nope.nah(e,"7")
            pass

    
    for j in range(c):
        a.append(float(0))
        b.append(float(0))

        
    match operation:
        case "1":
            
            k = math.fsum(a)
            
            print("\nTotal is:", k)
            
            b.append(k)
            
        case "2":
            
            l = a.pop(0)
            
            m =l-math.fsum(a)
            print("Remainder is:",m)
            
            b.append(m)
            
        case "3":
            
            n = math.prod(a[0:varnum])
            
            print("\nTotal is:", n)
            
            b.append(n)
            
        case "4":
            
            p = a[0]
            
            for q in range(varnum-1):
                print(p," divided by",a[q+1]," equals:",p/a[q+1])
                p = p/a[q+1]
            print("Remainder is: ", p)
            
            b.append(p)
            
        case "5":
            
            r = "invalid"
                
            for s in range(varnum):
                
                t = a[s]
                
                if t > -1:
                    u = math.sqrt(t)
                    
                    print("The square root of",t," is",u)
                    b.append(u) 
                    
                else:
                    
                    print("The square root of",t," is",r)
                    b.append(r) 
                
    
    for v in range(c):
        b.append(float(0))
    
            
    return b