import timeit
import re

#--------------------------------------------------------------
# TODO: COMMENTS
#--------------------------------------------------------------


def add_to_file(string):
    new_file.write(string)

def add_to_list(string):
    list.append(string)


def remove_0000(line):
    if "0.0.0.0 " in line:
        line = line.replace("0.0.0.0 ", "")
    #print(line)
    return line


def remove_127(line):
    if "127.0.0.1 " in line:
        line = line.replace("127.0.0.1 ", "")
    return line


def remove_www(line):
    if "www." in line:
        line = line.replace("www.", "")
    return line


def remove_space(line):
    if re.match(r'\s', line):
        return True
    else:
        return False


def remove_line_comments(line):
    if line.startswith("#"):
        return True
    else:
        return False


def delete_comments(line):
    if "#" in line and not line.startswith("#"):
        line, comment = line.split("#", 1)
        line = line.strip()
    return line


def remove_http(line):
    if "http://" in line:
        line = line.replace("http", "")
    elif "https://" in line:
        line = line.replace("https", "")
    return line


def format_for_host(line, option):
    if option == "www":
        line = local_host + www + line.strip() + "\n"
    elif option == "none":
        line = local_host + line.strip() + "\n"
    return line


def zero_or_broadcast(line, option):
    if option == "127":
        if line.startswith("127.0.0.1"):
            line = line.replace("0.0.0.0", "127.0.0.1")
    elif option == "0":
        if line.startswith("0.0.0.0"):
            line = line.replace("127.0.0.1", "0.0.0.0")
    return line


def open_readfile(filename):
    file = open(filename, "r")
    return file


def open_writefile(filename):
    file = open(filename, "w+")
    return file


def my_default_formatter():
    for line in file:
        if remove_space(line) or remove_line_comments(line):
            pass
        else:
            line = remove_http(line)
            line = remove_0000(line)
            line = remove_127(line)
            line = remove_www(line)
            line = delete_comments(line)


            host_line = format_for_host(line, "none")
            add_to_list(host_line)
            #print(f"no www: {line}")
            line = format_for_host(line, "www")
            add_to_list(line)
            #print(f"with www: {line}")


def get_uniques(list):
    list = set(list)
    return list

local_host = "127.0.0.1 "
www = "www."
start = timeit.default_timer()
list = []
file = open_readfile("list.txt")
new_file = open_writefile("new_list.txt")
input = []
expect = []


my_default_formatter()
list = get_uniques(list)
for item in list:
    add_to_file(item)

time_span = timeit.default_timer() - start
print(time_span)
file.close()
new_file.close()
