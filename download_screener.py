#!/usr/bin/env python
# imput the desired URL to download on line 67 (for tarurl variable)
import requests
import random
import re

d1 = ["playful", "warm", "caring", "fluffy", "endearing", "tasteful", "affectionate", "personal"]
d2 = ["faithful", "gleaming", "shiny", "honest", "virtuous", "quaint", "homely", "vengeful", "patient"]
n1 = ["pangolin", "snake", "beetle", "iguana", "shark", "eagle", "tiger", "lion", "mammoth", "wren", "hawk", "lark"]
type = "placeholder"

def make_randname(suf):
    holder = []
    randlists = [d1, d2, n1]
    for x in randlists:
        holder.append(random.choice(x))
    stringy_name = "-".join(holder)
    # append the suffix to the randomized words in the post-joined string
    stringy_name += suf
    return stringy_name

def extract_suffix(fn):
    # use regex to target period to end of string
    match = re.search("\..*$", fn)
    # go from start and end of match to slice it out of source
    suffix = fn[match.start():match.end()]
    return suffix

def check_suffix(suf):
    # instantiate a boolean switch
    odd_end_encountered = False
    # convert the ending suffix to lowercase to account for capitalization possibility
    type = suf.lower()
    if type == ".jpg":
        print("downloading jpg file")
    elif type == ".jpeg":
        print("downloading jpeg file")
    elif type == ".png":
        print("downloading png file, like a scrub")
    elif type == ".gif":
        print("downloading gif")
    else:
        #  flip switch if odd suffix found
        odd_end_encountered = True
        print("Odd filetype encountered:\t" + type)
        print("File not downloaded")
    return odd_end_encountered

def download(url):
    get_response = requests.get(url)
    # target last part of url as the filename
    # make download randomizaer with choice append from test dicitonaries
    file_name = url.split("/")[-1]
    file_suffix = extract_suffix(file_name)
    dangerous_filetype = check_suffix(file_suffix)
    # check if it's an unapproved filetype
    if not dangerous_filetype:
        randomized_filename = make_randname(file_suffix)
        print("saved " + file_name + " as: \t" + randomized_filename)
        # make new filename then mode in which it's being opened
        with open(randomized_filename, "wb") as out_file:
            out_file.write(get_response.content)
        # automatically sends file to same dir as program is called from

#  !!!!!!!!!!!!!!!!!!!!!!!!!
# BELOW IS THE TARGET URL, CHANGE BASED ON WHAT FILE U WANT .... png
tar_url = "https://en.gfwiki.com/images/thumb/6/6f/Magal.png/180px-Magal.png"
# pass tar variable into download function
download(tar_url)

#Learned: writing to a file of the same name will override previous content
# so be careful when using with open and write arg

# match everything from the period to end of line
#     re.search("\..*$")


