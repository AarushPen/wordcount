def wordcount(file):
    file=open(file)
    lines = file.readlines()
    count=0
    for eachline in lines:
        word=eachline.split()
        count=count+len(word)
    print(count)

wordcount("wordcount.py")
