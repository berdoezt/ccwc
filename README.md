# ccwc

- wc tools from scratch from [Coding Challenge](https://codingchallenges.fyi/challenges/challenge-wc/)
- https://en.wikipedia.org/wiki/Wc_(Unix)

## requirements
- python3

## available options
- -c, count bytes
- -l, count lines
- -w, count words
- -m, count chars
- generic, count line, word, bytes

## how to use
1. file name as argument
```bash
# count bytes
> python3 main.py -c test.txt
> 342190 test.txt

# count line, word, bytes respectively
> python3 main.py test.txt
> 7145 58164 342190 test.txt
```
2. file name as stdin
```bash
# count bytes
> cat test.txt | python3 main.py -c
> 342190

# count line, word, bytes respectively
> cat test.txt | python3 main.py
>   7145 58164 342190
```