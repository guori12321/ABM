infile = open("chinalazy.txt","r")
rules = infile.readlines()

outfile = open("GuoRuiList.txt", "w")

for i in rules:
    #skip the blank line
    if i == "\n":
        continue
#flag means whether there are "!@#$," in the rule. I could not deal with those symbols in the rule list, so I just regardless of them
#The RegExp is too slow. So I alo regardless "*^+?"
    flag = True
    for j in "!@#$,*^+?":
        if j in i:
            flag = False
            break
    if flag:
        #delete the "\n" at the end of i
        i = i[:-1]

        #I delete the "||" at the beginning of the rules
        if i[0] == "|" and i[1] == "|":
            i = i[2:]
        #Idelete the "|" at the beginning of the rules
        if i[0] == "|":
            i = i[1:]

        #I can't deal with other "|" as well
        if "|" in i:
            continue

        #The RegExp is too slow. Thus I delete those codes.
        #The replace doesn't work. In fact, I convert the "+*?" to "\+\*\?" in the rules of content.js through Vim.
        '''i.replace("\*", "\\\\\\\*")
        i.replace("\+", "\\\\\\\+")
        '''
        outfile.write("\""+ i + '\",\n')
