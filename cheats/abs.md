### var p30
The only times a variable appears "naked" -- without the $ prefix -- is when declared or assigned,
when unset, when exported, in an arithmetic expression within double parentheses (( ... )), or in the
special case of a variable representing a signal (see Example 32-5). Assignment may be with an = (as
in var1=27), in a read statement, and at the head of a loop (for var2 in 1 2 3).

```bash
hello="A B C  D"
echo $hello # A B C D
echo "$hello" # A B C  D
```
* space
  * var =num
  * CMD ARG
  * var= num
  * ENV  CMD

### var p36
explain
```bash
eval "`seq 10000 | sed -e 's/.*/export var&=ZZZZZZZZZZZZZZ/'`"
&& du
```
