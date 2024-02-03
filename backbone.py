import csv

def add_word():
    word=input("enter word")
    meaning=input("enter meaning")
    example=input("enter example")
    entry=[word,meaning,example]
    with open("brain.csv","w",newline="") as f:
        csv=csv.writer(f,delimiter=",")
        csv.writerow(entry)
def edit_word():
    list=[]
    print("enter word to edit :" )
    entry=input(":").lower()
    with open("brain.csv","r") as f1:
        csv_r=csv.reader(f)
        for row in csv_r:
            if (row[0]==entry):
                print(row)
                i=input("do u want to edit y/n :").lower()
                if i=="y":
                    i=int(input("do u want to edit 1.meaning 2.example :"))
                    if i==1:
                        word1=input("enter meaning")
                        row[1]=word1
                    elif i==2:
                        word1=input("enter example")
                        row[2]=word1
                    else:
                        print("invalid")
                        break
                elif i=="n":
                    break
            list.append(row)
                