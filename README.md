# NamePassGenerator
This script generates passwords based on the user's first name and last name.


```shell
❯ python3 NamePassGenerator.py
usage: NamePassGenerator.py [-h] [-w FILE] [-n NAME] [-s SURNAME]

Generate a list of users from a firts and last name

options:
  -h, --help            show this help message and exit
  -w FILE, --file FILE  file containning the list of users
  -n NAME, --name NAME  Name
  -s SURNAME, --surname SURNAME
                        Surname
                                                             
```

```shell
❯ cat users.txt
b0y seven
b0y four
            
```

In the script you can generate two types of word lists, one using a file and the other using a first and last name

# Use file

```shell
❯ python3 NamePassGenerator.py -w users.txt
[*] [🤔] Generating...
[←] Task completed and Saved in the file wordlist.txt
```

```shell
❯ cat wordlist.txt
b0yseven
b0y-seven
b0y.seven
bseven
b-seven
b.seven
sevenb0y
seven-b0y
seven.b0y
sevenb
seven-b
seven.b
b0ysev
b0y.sev
b0yfour
b0y-four
b0y.four
bfour
b-four
b.four
fourb0y
four-b0y
four.b0y
fourb
four-b
four.b
b0yfou
b0y.fou
```
# Use a name and surname

```shell
❯ python3 NamePassGenerator.py -n b0y -s seven
[*] [🤔] Generating...
[.] Task completed and Saved in the file wordlistUser.txt
```

```shell
❯ cat wordlistUser.txt
b0yseven
b0y-seven
b0y.seven
bseven
b-seven
b.seven
sevenb0y
seven-b0y
seven.b0y
sevenb
seven-b
seven.b
b0ysev
b0y.sev

```
