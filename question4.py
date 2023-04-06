def factorial(x):
    if(x<0):
        return -1
    if(x<=1):
        return 1
    return x*factorial(x-1)

def main():
    for x in range(1,8):
        print("value:",(x*2))
        print(factorial(x*2))

    
if __name__=="__main__":
    main()
