# Quick hack to fix image location in Obsidian for all markdown files converted from Joplin (Images can't be rendered correctly)\
#
# Search and replace image links in markdown file to render the images correctly in Obsidian for Example: 
#
# (original) ->>  <img width="604" height="336" src=":/63d12eb8a04741c3b32ccdcf8eca0e23"/>
# (new line) ->>  ![[63d12eb8a04741c3b32ccdcf8eca0e23.png]]

import os

file_encoding = 'windows-1256'
pattern = "src=\":/"
prefix_pattern = "![["
postfix_pattern =  "]]"
file_counter = 1

def get_list_of_md_files():
    # Getting the current work directory (cwd)
    thisdir = os.getcwd()

    # list of all markdown files
    list_of_files = []

    # Get a list of all markdown files inside current directory
    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        for file in f:
            if file.endswith(".md"):    # match only (*.md) files 
                list_of_files.append(os.path.join(r, file))

    return list_of_files

# Quick search for file extention
def find_image_extention(filename, search_path=".\\resources"):
    for root, dir, files in os.walk(search_path):
        if (filename + ".png") in files:
            return  ".png"
        elif (filename + ".jpg") in files:
            return  ".jpg"        
        elif (filename + ".jpeg") in files:
            return  ".jpeg"         
        elif (filename + ".svg") in files:
            return  ".svg"         
        elif (filename + ".gif") in files:
            return ".gif" 
    #default return .jpg
    return ".jpg"

def clean_image_link_in_markdown(file_name):
    global file_counter, file_encoding
    # Open the file
    file_input = open(file_name, encoding=file_encoding)
    # file_input = open(file_name).readlines()
    file_output = ""
    counter_of_changes = 0

    # search for each line contain the pattern and replace the image path
    for line in file_input:
        if pattern in line:
            new_image_name = line.split(":/")
            new_image_name = new_image_name[1].split("\"")
            new_image_name = new_image_name[0]
            extention_name = find_image_extention(new_image_name)
            new_image_name = prefix_pattern + new_image_name + extention_name + postfix_pattern
            file_output += new_image_name
            counter_of_changes += 1
            #print(line + new_image_name)
        else:
            file_output += line

    #output file to write the result to
    fout = open(file_name, "wt", encoding=file_encoding)
    fout.writelines(file_output)
    print(str(file_counter) + " -> Changes: " + str(counter_of_changes)+  "  ##  " + file_name)
    file_counter += 1

#-------------------- Converter --------------------#

# Get list of filtered files (only .md)
list_of_files = get_list_of_md_files()

for each_file in list_of_files:
    clean_image_link_in_markdown(each_file)
