# secret-santa

A simple to use Secret Santa generator _without_ having to give your email(s) to random websites online.
This is done by having the script output text files, which you can then send your friends.
The name on each outputted file is the person you should send that file to.

🎁🎄🎁

## How to use

1. `python santa.py`
2. Follow the given instructions.
3. Buy a gift for your assigned person.
4. Give that person the gift.
5. Have a Merry Christmas! ☃️

Alternatively, you can prepare a file to pipe in the necessary information, e.g.

```
4
Person1
Person2
Person3
Person4
```

and then `python santa.py < file.txt`.

If you want to introduce a blacklist, e.g. `Person1` cannot get `Person2` or `Person3`, you can modify the file like so:

```
4
Person1: Person2, Person3
Person2
Person3
Person4
```
