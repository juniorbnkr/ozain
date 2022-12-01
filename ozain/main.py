# -*- coding: utf-8 -*-
from dataclasses import replace
from posixpath import split

def parser(usfm_file) -> dict:
    """
    # Ozain Parser
    Simple function to parse USFM files in **chapter-verse structure**.
    This function removes all formatting markdowns and preserves only text of file.
    The text will be organized in a dict, with chapter -> verse levels and remove all others markdowns.
    Some metadata (file_encoding, usfm_version etc) will be returned in the dict.

    ## Example
    Get the 9º verse of chapter 137 in Psalms.txt file.
    - **from ozain.main import parser**
    - **psalms = parser("Psalms.txt")**
    - **psalms[137][9]**

    Will return:
    > **Happy is the one who takes your babies and smashes them against the rocks!**

    USFM is a standard markdown for digital versions of the Bible in different languages.
    Organized by United Bible Societies, the USFM format is a attempt to unify the digital format for Bible texts in a single markdown.

    for more information, see: https://paratext.org/usfm/
    THis Lib is recommended for simplified versions (usfm-s)

    Parameters:
    usfm_file -> str:
        Location of text file

    Return:
        dict
    
    """
    c = ""
    usfm_obj = {}
    with open(usfm_file, "r") as ifile:
        for line in ifile:
            if isinstance('line', str) and len(line)>1:
                mark = line.split(" ")[0]
                if mark == '\\c': #define chapter level
                    c = int(line[3:].replace("\n",""))
                    usfm_obj[c] = {}
                    pass
                
                if mark == "\\v": # Define Verse level and text
                    v = int(line.split(" ")[1])
                    text = line.replace("\\v ","").replace("\n","")
                    text = text.replace(f"{v} ","")
                    text = remove_markdown(text)
                    if text[0] == " ":
                        text = text[1:]
                    usfm_obj[c][v] = text
                    pass

                if mark == "\\q2":
                    text = line.replace("\\q2","").replace("\n","")
                    text = text.replace(f"{v} ","")
                    text = remove_markdown(text)
                    if text[0] == " ":
                        text = text[1:]
                    usfm_obj[c][v] += text # append q2 in last verse
                    
                
                if mark == "\\id":
                    usfm_obj["file_id"] = line.replace(f"{mark} ","").replace("\n","")
                elif mark == "\\ide":
                    usfm_obj["file_encoding"] = line.replace(f"{mark} ","").replace("\n","")
                elif mark == "\\h":
                    usfm_obj["header"] = line.replace(f"{mark} ","").replace("\n","")
                elif mark == "\\usfm":
                    usfm_obj["usfm_version"] = line.replace(f"{mark} ","").replace("\n","")
                elif mark == "\\sts":
                    usfm_obj["status"] = line.replace(f"{mark} ","").replace("\n","")
                elif mark == "\\rem":
                    usfm_obj["remark"] = line.replace(f"{mark} ","").replace("\n","")
                elif mark[0:4] == "\\mt":
                    usfm_obj[mark.replace("\\","")] = line.replace(f"{mark} ","").replace("\n","")
                #more marks can be add here...
    return usfm_obj

def remove_markdown(line):
    replace_list = ["\\add*",
                    "\\add",
                    "\\f + \\ft",
                    "\\f*"]
    replace_list +=  ['\\ms1', '\\pn', '\\add', '\\+pn', '\\f']
    replace_list +=  ['\\q1', '\\b', '\\s1', '\\s2', '\\+pn']
    replace_list +=  ['\\r', '\\d', '\\sp', '\\qs']
    
    for item in replace_list:
        if item in line:
            line = line.replace(item,"")
    
    return line 

if __name__ == "__main__":
    while True:
        file = input("Type the file location and press enter:")
        if file:
            chap = input("now, type the CHAPTER and press enter: ") 
            vers = input("and now, the VERSE and press enter: ")
        else:
            print("!!!type a valid path!!!")
            print("")
            continue

        if chap and vers:
            print("")
            print(f"You select the verse {vers} of chapter {chap} in book file '{file.split('/')[-1]}' ")
            print("")
        else:
            print("!!! type valid chapter and verse !!!")
            print("")
            continue

        confirm = input("Type Y to confirm or N to return: ")
        print("")

        if confirm.lower() == "n":
            continue
        elif confirm.lower() == "y":
            try:
                usfm = parser(file)
                print(usfm[int(chap)][int(vers)])
                exit()
            except Exception as e:
                print(f"Error in file {file}")
                print(e)
        else:
            print("invalid option")
            exit()
    