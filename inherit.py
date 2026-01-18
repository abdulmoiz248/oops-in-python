class A:
    varA='I am from class A'

class B:
    varB='I am from class B'

class C(A,B):
    varC='I am from class C'

if __name__ == "__main__":
    objC=C()
    print(C.mro())
    print(objC.varA)
    print(objC.varB)
    print(objC.varC)


"""
Straight talk: **this is multiple inheritance**, and Python handles conflicts using **MRO (Method Resolution Order)**.

If **both `A` and `B` have the same variable name**, Python picks **whichever class comes first in the inheritance list**.

Example 👇

```python
class A:
    var='from A'

class B:
    var='from B'

class C(A,B):
    pass

obj=C()
print(obj.var)
```

Output:

```
from A
```

Why?
Because Python checks classes **left to right** → `C → A → B → object`

If you flip the order:

```python
class C(B,A):
    pass
```

Now output:

```
from B
```

Want proof? Print the MRO:

```python
print(C.mro())
```

Key takeaway (no sugarcoating):

* Same variable/method name in multiple parents = **first parent wins**
* Order in `class C(A,B)` **matters**
* This applies to **methods AND variables**

Hot take 🔥:
If two parent classes share names, your design is already sus. Use composition or rename things unless you *really* want this behavior.

Want me to show how `super()` behaves in this case?

"""