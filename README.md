# URLForHost
URLForHost formats URLs so that you can use them in your host file.

##### Clone repository:

`https://github.com/jsornes/URLForHost.git`

By adding a line like: "127.0.0.1 somesite.com" you can blacklist all sites that start with "somesite.com." You can swap the "127.0.0.1" with "0.0.0.0".

There are several lists to help you blacklist dangerous sites (whatever dangerous means to you.)
Some of them can be put into your host file as is, but some are not and for those lists. URLForHost is a tool to be a bit more lazy.

### Functions:
* **remove_0000(line)**: takes a line (string) of input and if it contains "0.0.0.0 " that part gets removed. Returns line.

* **remove_127(line)**: takes a line (string) of input and if it contains "127.0.0.1 " that part gets removed. Returns line.

* **remove_www(line)**: takes a line (string) of input and if it contains "www." that part gets removed. Returns line.

* **remove_line_comment(line)**: takes a line (string) of input and if it starts with "#" it **returns True/False**, so you can skip this line. In the host file anything right to a "#" is a comment.

* **delete_comment(line)**: takes a line (string) of input and if it has a side comment (e.g. "www.google.com #blacklist google") the side comments gets removed. Returns line.

* **remove_space(line)**: takes a line (string) of input and if its an empty line, it **returns True/False** so you can skip it.

* **remove_http(line)**: takes a line (string) of input and if it contains "http://" or "https://" that part gets removed. Returns line.
* **remove_0000(line)**: takes a line of input and if it contains "0.0.0.0 " that part gets removed. Returns line.

* **format_for_host(line, option)**: take a line (string) as input and an option (either "www" or "none", as strings.)
With the option "www", "127.0.0.1 www." gets added to the input line, to get "127.0.0.1 www.somesite.com"
With the option "none", only "127.0.0.1 " gets added, to get "127.0.0.1 somesite.com"
It returns line (your now changed input string)

* **zero_or_broadcast(line, option)**: depending on the option (either "127" or "0000") "127.0.0.1"
gets swapped with "0.0.0.0" or the other ways around. You choose the option you want to get.
Returns line.

* **open_readfile(filename)**: opens a file for reading

* **open_writefile(filename)**: opens a file for writing ("w+")

* **get_uniques(list)**: takes the already correctly formatted list of strings and orders the unique
values in a list. It's done with the set(list) Python method. Returns a list.

* **my_default_formatter()**: it removes everything (0.0.0.0, 127.0.0.1, www., http, etc), then appends the line into list.
It two lines the following way:
"127.0.0.1 somesite.com"
"127.0.0.1 www.somesite.com"
I've found that you can still access some sites if you only use "127.0.0.1" but I might be wrong.
