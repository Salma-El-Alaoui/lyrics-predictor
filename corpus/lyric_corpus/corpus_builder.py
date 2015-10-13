import codecs
import glob, os



# file paths
INPUT_DIR = "./" # specify path here
OUTPUT_DIR = "./" # specify path here
if not os.name == 'posix':
    INPUT_DIR = ".\\"
    OUTPUT_DIR = ".\\"


contraction_1 = ["in’","in'","in‘"] # Workin' -> Working
contraction_2 = ["’ll","'ll","‘ll"] # You'll -> You will
contraction_3 = ["’ve","'ve","‘ve"] # We've -> We have
contraction_4 = ["let’s","let's","let‘s"] # Let's -> Let us
contraction_5 = ["i’m","i'm","i‘m"] # I'm -> I am
contraction_6 = ["’re","'re","‘re"] # We're -> We are

# Irregular forms: "ain't", "won't", "shan't". "n't" can only be attached to an auxiliary verb which is itself not contracted.

#contraction_7 = ["ain’t","ain't","ain‘t"] # TO SPECIAL, can be: am not, is not, are not, has not, and have not
contraction_8 = ["won’t","won't","won‘t"] # won't -> will not
contraction_9 = ["shan’t","shan't","shan‘t"] #shan't -> shall not
contraction_10 = ["n’t","n't","n‘t"] # don't -> do not
correct_10_1 = [" hav "]
correct_10_2 = [" ca "]

remove_chars = [';',':', '#', '’', '+', '*','§','$','%','&','(',')','=',']','[','|','{','}','≠','¡','¶',
                '¬','”','£','ﬁ','^','\\','~','–','…','∞','˛','÷','’','#','’','','±','≤','<','>','≥','“',
                '˜','·','¯','˙','„','^','´','`','°','"',"'","‘", "@","ﬂ", "ñ", "ü", "û", "ø", "ú", "ù","ö",
                "õ", "ô", "ó", "ò", "ð","ï", "î", "í","ì", "ë", "ê", "é", "è", "ç", "æ", "å", "ä", "ã", "â",
                "á", "à", "ß", "Þ", "þ", "Ý", "Ü", "Û", "Ú", "Ù", "Ø", "×","Ö", "Õ", "Ô", "Ó", "Ò", "Ñ", "Ð",
                "Ï", "Î", "Í", "Ì", "Ë", "Ê", "É", "È", "Ç", "Æ", "Å", "Ä", "Ã", "Â","Á","À", "¿", "¾", "½",
                "¼", "»", "º", "¹", "¸", "µ", "³", "²", "±", "®", "«", "ª", "©", "¨", "¦", "¥", "¤", "¢","ý","�"]


remove_backslash = ['/']
remove_hyphen_underscore = ['-','_']

bad_line_endings = [",\n"]
good_line_endings = [".\n", "!\n", "?\n" ]
lastline_bad_endings = [","]
lastline_good_endings = [".n", "!", "?" ]

file_list = {"sum":0}

def clean_line(line):
    #print("O: " + line)

    line = line.lower()

    for char in contraction_1:
        line = line.replace(char,"ing")

    for char in contraction_2:
        line = line.replace(char," will")

    for char in contraction_3:
        line = line.replace(char," have")


    for char in contraction_4:
        line = line.replace(char,"let us")

    for char in contraction_5:
        line = line.replace(char,"i am")

    for char in contraction_6:
        line = line.replace(char," are")

    for char in contraction_8:
        line = line.replace(char,"will not")

    for char in contraction_9:
        line = line.replace(char,"shall not")

    for char in contraction_10:
        line = line.replace(char," not")

    for char in correct_10_1:
        line = line.replace(char," have ")

    for char in correct_10_2:
        line = line.replace(char," can ")

    for char in remove_chars:
        line = line.replace(char,"")

    for char in remove_backslash:
        line = line.replace(char," ")

    for char in remove_hyphen_underscore:
        line = line.replace(char," ")

    #print("N: "+line)

    if(len(line)>2): # no blank lines

        # case last line
        if not line.endswith("\n"):

            for endings in lastline_good_endings:
                if(line.endswith(endings)):
                    #print("GOOD LL: " + line)
                    return line

            for endings in lastline_bad_endings:
                if(line.endswith(endings)):
                    line = line.replace(endings,".")
                    #print("BAD to GOOD LL: " + line)
                    return line

            line = line + "."
            #print("STANDARD LL: " +line)
            return line


        # case normal line
        for endings in good_line_endings:
            if(line.endswith(endings)):
                #print("GOOD: " + line)
                return line

        for endings in bad_line_endings:
            if(line.endswith(endings)):
                line = line.replace(endings,".\n")
                #print("BAD to GOOD: " + line)
                return line

        # no punctuation, put a dot at the end
        line = line.replace("\n", ".\n")
        #print("STANDRAD: " + line)
        return line

    else:
        # if its a blank line return it
        return line



os.chdir(INPUT_DIR)
for file in glob.glob("*.txt"):

    artist = file.split("_",1)[0]

    if artist in file_list:
        file_list[artist]+=1
        file_list["sum"]+=1
        # if there is no key yet, init with count 1
    else:
        file_list[artist] = 1
        file_list["sum"]+=1


    r_song =  codecs.open(file , 'r', encoding='utf-8')
    lines = r_song.readlines()
    r_song.close()

    os.chdir(OUTPUT_DIR)
    new_filename = artist+"_"+str(file_list[artist])+".txt"

    w_song =  codecs.open(new_filename , 'w', encoding='utf-8')

    for line in lines:

        cleaned_line = clean_line(line)
        w_song.write(cleaned_line)

    w_song.close()
    os.chdir(INPUT_DIR)

print(file_list)


