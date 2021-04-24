import os
import sys

# GET USER INPUT #
user_file = ""
if len(sys.argv) > 1:
    user_file = sys.argv[1]

store_to = "archive.txt"
if len(sys.argv) > 2:
    store_to = sys.argv[2]
# GET USER INPUT #


# get dir of music
working_dir = user_file
get_file = os.listdir(working_dir)

# get all archived music urls
archiveFile = open(store_to, "r+")
archived = archiveFile.read().split("\n")
url_archived = {}
for sift in archived:
    if len(sift) > 1:
        url_archived.update({sift.split(" ")[1]: ""})
archiveFile.close()

# read files to append to archive
archiveFile = open(store_to, "a+")
for file in get_file:
    if os.path.isfile(working_dir + "\\" + file):
        # print(file)
        try:
            split_extension = file.split(".")
            split_extension.pop()
            youtube_v = split_extension.pop()[-11:]
        except Exception:
            print("Skipping file: " + file)

        # if key not found add to file
        if url_archived.get(youtube_v) is None:
            print("ARCHIVING: " + youtube_v)
            archiveFile.write("\nyoutube " + youtube_v)
    else:
        print(file + "Is not a File")
