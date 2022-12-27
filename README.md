# joplin_to_obsidian_clean_image_errors
If you use Joplin and want to migrate to Obsidian and used **https://github.com/luxi78/joplin2obsidian** 
Some images will not be displayed due to link format

This script is a quick way to clean image links errors when converting joplin notes to obsidian notes, for example it will convert the following link
# (original) ->>  <img width="604" height="336" src=":/63d12eb8a04741c3b32ccdcf8eca0e23"/>

to simpler syntax as following (in all markdown file
# (new line) ->>  ![[63d12eb8a04741c3b32ccdcf8eca0e23.png]]

If you use it on windows and have second language (Arabic, Turkish ..etc) don't forget to change the file encoding variable in the script

## How to use it

1- Excute the covnersion from Joplin to Obsidian **https://github.com/luxi78/joplin2obsidian** 
2- Copy the script to your vault 
3- run the script "python convert_img.py"
4- enjoy your obsidian!
