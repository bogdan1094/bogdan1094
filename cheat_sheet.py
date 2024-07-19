---------------------------------------------------------------------------------------------//////////////////////PYTHON//////////////////////---------------------------------------------------------------------------------------------

1. Cererea unui input de la tastatura:
name=input('Care este numele tau:?')

2. Transformarea din litere mari in mici si invers
"HELLO WORLD".lower()
"hello world".upper()

3. Numarul de caractere al unui string:
len("HELLO WORLD")

4. Listeaza toate functiile valide pentru un anumit tip de data:
dir('HELLO WORLD')

5. Modul getpass: (exemplu de captare a parolei 'criptat') (Trebuie importat modulul mai intai: import getpass)
Password=getpass.getpass('Password=')

6. Concatenare variabile si stringuri:
print('Academia ' + val1 + ' ' + val2 + ' ' + str(b) + ' ' + val3 )

7. Newline:
m = "This string\nspans multiple\nlines"

8. TABS:
m = "test1 \t test2"

9. RAW string print:
print(r"C:\Users\KF86NI")

10. Catul impartirii:
print ("Citul impartiirii lui a la b este:", a // b )

11. Restul impartirii:
print ("Restul impartiirii lui a la b este:", a % b )

12. Formatted strings:
full_name= f" {} + {}"

13. Remove whitespaces from strings (input):
print(string.strip)

14. find vs in methods
print(string.find("abc")) vs print ("abc" in string)
find return the index and in retruns boolean (True or False)

//////////////////////////////////////////////////////////////////
All numeric types (except complex) support the following operations:
arithmetic operations:
x + y (addition)
x - y (substraction)
x * y (multiplication)
x / y (division)
x // y (division quotient)
x % y (division remainder)
x ** y (exponentiation)
-x (negation)
built-in functions:
abs(x) (absolute value)
int(x) (conversion to integer)
float(x) (conversion to floating point)
complex(x, y) (creation of a complex number where x is real part and y imaginary part)
divmod(x, y) (creation of (x // y, x % y) pair) !!!!!
pow(x, y) (x to the power y, the same as x ** y)
Types int and float also support:
round(x, [n]) (x rounded to n digits, n defaults to 0)
//////////////////////////////////////////////////////////////////

15. Logical operators (and / or / not)

16. Iteratori: range(x), strings, lists, tuples etc
                                                ------------------------------------------------/////IF,FOR,WHILE/////----------------------------------------------------
10. IF
a="curs 1"
if a!="curs 1":
    print("Stringul dat difera de conditie")
else :
    print("cele 2 stringuri sunt identice cu", a)
print("aici nu sunt in if")

11. ELIF
nr_kg=78
if nr_kg < 2:
    print("Numarul de kg al unui copil de o luna")
elif nr_kg < 40:
    print("Numarul de kg al unui adolescent")
else:
    print("Numarul de kg al unui adult")
print("aici nu sunt in if")

12. FOR
for i in range(10): # (0,1..9)
    print(i)
for i in range(1,11,2): #din 2 in 2
    print(i)

13. Nested loops:
for x in range (5):
    for y in range (3):
print(f"({x},{y})")

13. WHILE
c=6
while c>2:
    print(c)
    c-=1   # decrementare cu 1
    print("C dupa decerementare")
print("Am iesit din while")

14. BREAK & CONTINUE
c=6
while c>2:
    if c == 4:
        c-=1
        continue
        c=c-1  #nu o sa se decrementeze pt ca instr dupa continue nu se executa
    else:
        if c == 3:
            print("Am iesit din while cu break")
            break
    print(c)
    c-=1
    print("C dupa decerementare")
print("Am iesit din while")


------------------------------------------------/////LISTE,TUPLURI,SETURI, DICTIONARE/////----------------------------------------------------
15. LISTE []
l=["primul", 1, 1.5, "string", "ultimul"]
print("Elementele listei sunt:" ,l)
print("Primul element este:" , l[0])
print ("Toate elementele mai putin primul si ultimul sunt:", l[1:-1])
l.append("ultimul +1")
m=[1,"x", [1,2,3]]
for i in m:
    print(i)
for i in range(0,len(m)):
    print("m[%d]=%s" % (i,m[i])) #m[0]=1, m[1]=x, m[2]=[1,2,3]

-List unpacking:
first, second, last = l # first = primul, second=1, last = ultimul

-enumerate function creates indexes of the list elements
list = ["a", "b", "c"]
for index, value in enumerate(list):
    print(index, value)

-Lambda funcitions:
print (sort(key=lambda arguments:expression))

-List comprehension:
[expression for item in items]
prices = [item[1] for items in intems]   ([expression for item in list])
filtered = [item for item in list if item >=10]

-Zip function combines elements of lists (iterables) one by one and creates a list of tuples! [(a1,b1,c1), (a2,b2,c2), (a3,b3,c3)]

16. TUPLURI () -Tuplul este immutable! (read only)
t=(1, "Iasi", "Cluj", 2.8)
print("primul element al tuplului este:" ,t[0])
t+=("Bucuresti", "Nasi", 10)
print ("tuplu dupa concatenare", t)

17. SETURI {} # se folosesc pentru unicitate a elementelor!
s1={'abc', 8, 9, 10, 1.23}
s2={18,1,'abc',8,77,14,9.7}
i=s1.intersection(s2)
d=s1.difference(s2)
u=s1.union(s2)
print('uniunea s1 cu s2', u)

18. DICTIONAR
stoc={'becuri':100, 'lanterne':34, 'prize':23}
stoc.update({'becuri':58,'cabluri':19})
lista=[('caiete',35),('pixuri',11), ('creioane',7)]
d=dict(lista)
for k in d.keys():
    print(k)
for v in d.values():
    print(v)
for k,v in d.items():
    print("%s=%d" %(k,v))

-Dictonary comprehension:
values = {x: x*2 fror x in range(5)}

19. GENERATORI: #memory efficient !
values = (x*2 fror x in range(5))
Items of the generator can be accessed only by iterating over it!

--------------------------------------------------------/////FUNCTII/////---------------------------------------------------------
19. FUNCTII
def patrat(a):
    return a*a
b=patrat(4)

def printeaza_banner(mesaj,border='#'):
    line=border*len(mesaj)
    print(line)
    print(mesaj)
    print(line)
printeaza_banner("Python fundamentals")

*************************
if isinstance(s1,set):
    print("este set")
else:
    print("nu este set")
*************************
def printeaza_argumente(a1,a2,*args,k1,k2,**kwargs):
    print(a1)
    print(a2)
    print(args)
    print(k1)
    print(k2)
    print(kwargs)

*************************
def unlimit_param(*args): # functia permite un numar nedefinit/nelimitat de parametrii !!!
    This will create a tuple


--------------------------------------------------------/////VARIABILE LOCALE & GLOBALE/////---------------------------------------------------------
20. VARIABILE
count = 0
def show_count():
    print("count = ", count)
def set_count(c):
    count = c

>>> show_count()
count =  0
>>> set_count(5)
>>> show_count()
count =  0
*************************
def show_count():
    print("count = ", count)
def set_count(c):
    global count
    count = c
--------------------------------------------------------/////LUCRU CU FISIERE/////---------------------------------------------------------
21. Crearea si scrierea instr-un fisier:
with open("file1.txt", mode='at') as f:
    f.writelines(["\na 3-a linie","\na 4-a linie"])

22. Citirea din fisier:
with open("file1.txt", mode='rt') as f:
    #print(f.read())
    print(f.read(2)) #incp citirea de la al doilea element
    f.seek() #0 inceput, 1 pozitia curenta, 2 final
    print(f.read())

-Using the with statement the files always get closed!
--------------------------------------------------------/////MODULE/////---------------------------------------------------------
23. Modulul os:
import os
os.getcwd() #-> imi afiseaza directorul curent
os.chdir("C:\\Users\cr26cw\PycharmProjects") #-> imi schimba directorul curent
print(os.getcwd())
os.chdir("../../../") #-> pot sa folosesc si o cale relativa( ../ inseamna directorul parinte)
print(os.listdir(os.getcwd() + "/cr26cw/PycharmProjects")) #-> imi listeaza fisierele si directoarele din PycharmProjects
os.mkdir("./test1") #-> imi creeaza un director in folderul curent
os.makedirs("./test2/test3/test4") #-> creeaza recursiv foldere incepand din folderul curent
os.rmdir("./test2/test3/test4") #-> sterge folderul test4

24. Modulul shutil
import shutil
shutil.rmtree("./test2/test3") #-> stergem recursiv directoare
os.remove("./firstfile.txt") #-> cu remove stergem un fisier

25. Modulul random:
import random
print("un numar floar intre 0 si 1", random.random())
print("un numar floar intre 5 si 8", random.uniform(5,8))
print("un numar intreg intre 5 si 8", random.randint(5,8))
print("un numar impar intre 1 si 15", random.randrange(1,15,2))
print("un numar divizibil cu 3 intre 0 si 15", random.randrange(0,15,3))
print("un caracter din stringul meu", random.choice("Bogdan"))

items=["ana", "iuliana", "bogdan", "razvan"]
random.shuffle(items)
print("lista dupa shuffle este", items)

26. Modulul time/datetime:
import time
timpul_curent=time.time()  ##epoch
timpul_curent_frumos=time.ctime()
print(timpul_curent)
print("tipul lui time este:", type(timpul_curent))
print(timpul_curent_frumos)
print("tipul lui ctime este:", type(timpul_curent_frumos))

later=timpul_curent + 360
print("timpul peste 6 minute va fi", time.ctime(later))

timp_parsat=time.strptime(timpul_curent_frumos)
print("timp parsat este:", timp_parsat)

timpul_parsat_final=time.strftime("%a %b %d %H:%M:%S", timp_parsat)
print("timpul_parsat_final este:", timpul_parsat_final)

import datetime
ziua_curenta=datetime.date.today()
print("ziua curenta este:", ziua_curenta)
o_zi=datetime.timedelta(days=1)
print(o_zi)

ieri=ziua_curenta-o_zi
print("ieri", ieri)
--------------------------------------------------------/////EXCEPTIONS HANDLING / RAISING EXCEPTIONS/////---------------------------------------------------------
27. Exceptii (Handling):
try:
    age = int(input("Age:"))
except ValueError as ex:
    print("You didn/t enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")
print("Execution continues")
----------------------------
-You can specify multiple exception in the same except statement: # except (ValueError, ZeroDivisonError) as ex:

-FINALLY:
finally is used inside a program to always execute a command, even if exceptions are thrown or conditions are not met:

try:
    file.open("app.py")
    age = int(input("Age:"))
except ValueError as ex:
    print("You didn/t enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")
print("Execution continues")
finally:
file.close()

28.Raising exceptions:# !! Exception raising is a costly operation that would impact the performance of the program. Instead use if statemets to handle the situations or with "return None".
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/ age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

--------------------------------------------------------/////ARHIVARE/////---------------------------------------------------------
28. Arhivare/Dezarhivare
import gzip
text="Textul meu ce va fi arhivat"
with gzip.open("mygzip.txt.gz", mode='wt') as f:
    f.writelines(text)
with gzip.open("mygzip.txt.gz", mode='rb') as f:
    continut_arhiva=f.read()
--------------------------------------------------------/////CLASE, MOSTENIRI, INTERFETE, POLIMORFISM/////---------------------------------------------------------
29. Clase:
class Angajat:           # vreau sa stochez info de genul: nume, varsta, vechime,companie
    companie="ING"       # class level(based) attribute - it is shared with all objects/instances of the class!
    def __init__(self, name, age, experince ):
        self.nume = name
        self.varsta = age
        self.vechime = experince

    def schimba_varsta(self, new_age):
        self.varsta=new_age

    def info_angajat(self):
        print("Nume angajat", self.nume)
        print("Varsta", self.varsta)
        print("Vechime", self.vechime)
        print("Companie", self.companie)

ang1=Angajat("Bogdan",25,4)
ang2=Angajat("Vasile",43,20)
# ang1.info_angajat()
print("Varsta angajatului 2 este:", ang2.varsta)
ang2.schimba_varsta(33)
print("Varsta angajatului 2 este:", ang2.varsta)

30. Mosteniri
class ClasaDeBaza():
    def __init__(self):
        print("Init din Calasa de Baza")

    def fct(self):
        print("Functie din Clasa de Baza")

class SubClasa(ClasaDeBaza):
    def __init__(self):
        print("Init din Subclasa")
    def fct(self,var):
        super().__init__()  #chem initul din clasa de baza
        print("fct din subclasa")
        print("Variabila mea este:", var)

cb=ClasaDeBaza()
sb=SubClasa()
sb.fct(3)

31. Interfete & Polimorfism:
class Document():
    def __init__(self,nume):
        self.name=nume
    def show(self):
        raise NotImplementedError("Orice clasa care implementeaza interfata Document tre sa faca suprascriere la functia show")

class PDF(Document):
    def show(self):
        return "Acesta este un fisier PDF!"
class Excel(Document):
    def show(self):
        return "Acesta este un fisier Excel!"
class OnlineDoc(Document):
    def show(self):
        pass
        #return "Acesta este un fisier WEB!"

lista =[PDF("pdf1"), PDF("pdf2"), Excel("excel1"), OnlineDoc("ondoc1")]
for obj in lista:
    print(obj.show())
----------------------------------------------------///// RECURSIVITATE & REGEX /////-----------------------------------------------------



----------------------------------------------------///// Python Notes /////-----------------------------------------------------


VsCode Python extensions:
- Python
- Git Graph
- Docker
- Django
- Pylint

* Format on Save in VsCode -> Setting (search for format on save)!
* Install CodeRunner Extension in order to run python code !
-change from Python2 to Python3 for Code Runner -VsCode Settings -3 dots on the rigt -> Open setting.json and search o
for "code-runner.executorMap" - search for python on the right side (UserSettings) - change the python -u to python3
* Boolean values should be Camel case!
* Escape character ( \ )
* Formatted strings: full_name= f" {} + {}"
