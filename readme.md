## Truth Table Builder

I needed a way to build truth tables for class, and I really didn't want to solve them manually. So I did what most programming nerds would do and kick out a quick script.

### Usage
From the command line run the script with the boolean expression as an command line option.

```
python build.py "A && B || C"
```

If you're a python person, you can also use `and` instead of `&&` and `or` instead of `||`. 

A couple of notes. 

The variables need to be single capital letters. Lower cased letters will cause issues.

And the expression should be wrapped in double quotes. 

### Output
Running the example above will produce the following output.

```
A       B       C       A && B || C
True    True    True    True
True    True    False   True
True    False   True    True
True    False   False   False
False   True    True    True
False   True    False   False
False   False   True    True
False   False   False   False
```