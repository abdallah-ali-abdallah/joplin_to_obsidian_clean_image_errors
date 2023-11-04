# Quick hack to fix image location in Obsidian for all markdown files converted from Joplin (Images can't be rendered correctly)\
#
# Search and replace image links in markdown file to render the images correctly in Obsidian for Example: 
#
# (original) ->>  <img width="604" height="336" src=":/63d12eb8a04741c3b32ccdcf8eca0e23"/>
# (new line) ->>  ![[63d12eb8a04741c3b32ccdcf8eca0e23.png]]

import os
import re
import argparse

file_encoding = 'windows-1256'

file_counter = 1


def get_list_of_md_files(obsidian_vault_folder_path):
    # Getting the current work directory (cwd)
    thisdir = obsidian_vault_folder_path

    # list of all markdown files
    list_of_files = []

    # Get a list of all markdown files inside current directory
    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        for file in f:
            if file.endswith(".md"):    # match only (*.md) files 
                list_of_files.append(os.path.join(r, file))

    return list_of_files

def convert_img_to_md(line):
    match = re.search(r'<img .*?src="([^"]*)".*?>', line)
    if match:
        img_src = match.group(1)
        md_format = '![[{}]]'.format(img_src)
        return md_format
    return line

def clean_image_link_in_markdown(file_name):
    global file_counter, file_encoding
    # Open the file
    file_input = open(file_name, encoding=file_encoding)
    # file_input = open(file_name).readlines()
    file_output = ""
    counter_of_changes = 0

    # search for each line contain the pattern and replace the image path
    for line in file_input:
        convert_img_to_md(line)
        file_output += line

    #output file to write the result to
    fout = open(file_name, "wt", encoding=file_encoding)
    fout.writelines(file_output)
    print(str(file_counter) + " -> Changes: " + str(counter_of_changes)+  "  ##  " + file_name)
    file_counter += 1

#-------------------- Converter --------------------#
print("--------------------------- JOPLIN->OBSIDIAN Image fixing -----------------------------\n\n")
print("Fix all imgs tages from markdown files exported from Joplin to obsidian")
print("example fix as following")
print('<img width="570" height="289" src="../_resources/image-20221018233328391_7efe3d2ff69146a8ae5b37b674.png" class="jop-noMdConv">   --> ![["../_resources/20221018233328391_7efe3d2ff69146a8ae5b37b674.png"]]')
print("----------------------------------------------------------------------------------------\n\n")

# Create the parser
parser = argparse.ArgumentParser(description="Folder where obsidian vault is located")

# Add the arguments
parser.add_argument('--input-folder', dest='path', type=str, help='the folder which contain all exported MD files to process and rename image tags')

# Execute the parse_args() method
args = parser.parse_args()

if os.path.isdir(args.path):
    print(f"{args.path} is a valid directory")
else:
    print(f"{args.path} is not a valid directory. Please provide a valid directory.")
    
# Get list of filtered files (only .md)
list_of_files = get_list_of_md_files(args.path)

for each_file in list_of_files:
    clean_image_link_in_markdown(each_file)
