def reverse_words(string):
    string= string.replace("\n"," ")
    string=string.split(" ")
    string.reverse()
    string=' '.join(string)
    return string

def main():
    string = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    print("input : ",string)
    print("\n")
    print("output : ",reverse_words(string))
    print("\n")

    string="Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"
    print("input : ",string)
    print("\n")
    print("output : ",reverse_words(string))
    print("\n")
    
if __name__=="__main__":
    main()
