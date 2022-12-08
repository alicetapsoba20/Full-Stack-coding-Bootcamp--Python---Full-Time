Feuille De Triche Python Complète
Aide-mémoire Python

Téléchargez le fichier texte , forkez-moi sur GitHub ou consultez la FAQ .



Contenu
    1. Collections : , , , , , , , . 2. Types : , , , , , , . 3. Syntaxe : , , , , , , , . 4. Système : , , , , , , . 5. Données : , , , , , , , , . 6. Avancé : , , , , , . 7. Bibliothèques : , , , ,  List Dictionary Set Tuple Range Enumerate Iterator Generator
               Type String Regular_Exp Format Numbers Combinatorics Datetime
              Args Inline Closure Decorator Class Duck_Type Enum Exception
             Exit Print Input Command_Line_Arguments Open Path OS_Commands
                  JSON Pickle CSV SQLite Bytes Struct Array Memory_View Deque
        Threading Operator Introspection Metaprograming Eval Coroutines
           Progress_Bar Plot Table Curses Logging, , , , , , , , , .Scraping Web Profile
                                  NumPy Image Audio Games Data Cython

Principal
if __name__ == '__main__':     # Runs main() if file wasn't imported.
    main()
Liste
<list> = <list>[from_inclusive : to_exclusive : ±step_size]
<list>.append(<el>)            # Or: <list> += [<el>]
<list>.extend(<collection>)    # Or: <list> += <collection>
<list>.sort()
<list>.reverse()
<list> = sorted(<collection>)
<iter> = reversed(<list>)
sum_of_elements  = sum(<collection>)
elementwise_sum  = [sum(pair) for pair in zip(list_a, list_b)]
sorted_by_second = sorted(<collection>, key=lambda el: el[1])
sorted_by_both   = sorted(<collection>, key=lambda el: (el[1], el[0]))
flatter_list     = list(itertools.chain.from_iterable(<list>))
product_of_elems = functools.reduce(lambda out, el: out * el, <collection>)
list_of_chars    = list(<str>)
L' opérateur de module fournit les fonctions itemgetter() et mul() qui offrent les mêmes fonctionnalités que les expressions lambda ci-dessus.
<int> = <list>.count(<el>)     # Returns number of occurrences. Also works on strings.
index = <list>.index(<el>)     # Returns index of first occurrence or raises ValueError.
<list>.insert(index, <el>)     # Inserts item at index and moves the rest to the right.
<el> = <list>.pop([index])     # Removes and returns item at index or from the end.
<list>.remove(<el>)            # Removes first occurrence of item or raises ValueError.
<list>.clear()                 # Removes all items. Also works on dictionary and set.
Dictionnaire
<view> = <dict>.keys()                          # Coll. of keys that reflects changes.
<view> = <dict>.values()                        # Coll. of values that reflects changes.
<view> = <dict>.items()                         # Coll. of key-value tuples that reflects chgs.
value  = <dict>.get(key, default=None)          # Returns default if key is missing.
value  = <dict>.setdefault(key, default=None)   # Returns and writes default if key is missing.
<dict> = collections.defaultdict(<type>)        # Creates a dict with default value of type.
<dict> = collections.defaultdict(lambda: 1)     # Creates a dict with default value 1.
<dict> = dict(<collection>)                     # Creates a dict from coll. of key-value pairs.
<dict> = dict(zip(keys, values))                # Creates a dict from two collections.
<dict> = dict.fromkeys(keys [, value])          # Creates a dict from collection of keys.
<dict>.update(<dict>)                           # Adds items. Replaces ones with matching keys.
value = <dict>.pop(key)                         # Removes item or raises KeyError.
{k for k, v in <dict>.items() if v == value}    # Returns set of keys that point to the value.
{k: v for k, v in <dict>.items() if k in keys}  # Returns a dictionary, filtered by keys.
Compteur
>>> from collections import Counter
>>> colors = ['blue', 'blue', 'blue', 'red', 'red']
>>> counter = Counter(colors)
>>> counter['yellow'] += 1
Counter({'blue': 3, 'red': 2, 'yellow': 1})
>>> counter.most_common()[0]
('blue', 3)
Régler
<set> = set()
<set>.add(<el>)                                 # Or: <set> |= {<el>}
<set>.update(<collection>)                      # Or: <set> |= <set>
<set>  = <set>.union(<coll.>)                   # Or: <set> | <set>
<set>  = <set>.intersection(<coll.>)            # Or: <set> & <set>
<set>  = <set>.difference(<coll.>)              # Or: <set> - <set>
<set>  = <set>.symmetric_difference(<coll.>)    # Or: <set> ^ <set>
<bool> = <set>.issubset(<coll.>)                # Or: <set> <= <set>
<bool> = <set>.issuperset(<coll.>)              # Or: <set> >= <set>
<el> = <set>.pop()                              # Raises KeyError if empty.
<set>.remove(<el>)                              # Raises KeyError if missing.
<set>.discard(<el>)                             # Doesn't raise an error.
Ensemble Congelé
Est immuable et hachable.
Cela signifie qu'il peut être utilisé comme clé dans un dictionnaire ou comme élément dans un ensemble.
<frozenset> = frozenset(<collection>)
Tuple
Tuple est une liste immuable et hachable.

<tuple> = ()
<tuple> = (<el>, )
<tuple> = (<el_1>, <el_2> [, ...])
Tuple Nommé
Sous-classe de Tuple avec des éléments nommés.

>>> from collections import namedtuple
>>> Point = namedtuple('Point', 'x y')
>>> p = Point(1, y=2)
Point(x=1, y=2)
>>> p[0]
1
>>> p.x
1
>>> getattr(p, 'y')
2
>>> p._fields  # Or: Point._fields
('x', 'y')
Intervalle
<range> = range(to_exclusive)
<range> = range(from_inclusive, to_exclusive)
<range> = range(from_inclusive, to_exclusive, ±step_size)
from_inclusive = <range>.start
to_exclusive   = <range>.stop
Énumérer
for i, el in enumerate(<collection> [, i_start]):
    ...
Itérateur
<iter> = iter(<collection>)                 # `iter(<iter>)` returns unmodified iterator.
<iter> = iter(<function>, to_exclusive)     # A sequence of return values until 'to_exclusive'.
<el>   = next(<iter> [, default])           # Raises StopIteration or returns 'default' on end.
<list> = list(<iter>)                       # Returns a list of iterator's remaining elements.
Itertools
from itertools import count, repeat, cycle, chain, islice
<iter> = count(start=0, step=1)             # Returns updated value endlessly. Accepts floats.
<iter> = repeat(<el> [, times])             # Returns element endlessly or 'times' times.
<iter> = cycle(<collection>)                # Repeats the sequence endlessly.
<iter> = chain(<coll_1>, <coll_2> [, ...])  # Empties collections in order.
<iter> = chain.from_iterable(<collection>)  # Empties collections inside a collection in order.
<iter> = islice(<collection>, to_exclusive)
<iter> = islice(<collection>, from_inclusive, to_exclusive [, +step_size])
Générateur
Toute fonction contenant une instruction yield renvoie un générateur.
Les générateurs et les itérateurs sont interchangeables.
def count(start, step):
    while True:
        yield start
        start += step
>>> counter = count(10, 2)
>>> next(counter), next(counter), next(counter)
(10, 12, 14)
Taper
Tout est objet.
Chaque objet a un type.
Type et classe sont synonymes.
<type> = type(<el>)                          # Or: <el>.__class__
<bool> = isinstance(<el>, <type>)            # Or: issubclass(type(<el>), <type>)
>>> type('a'), 'a'.__class__, str
(<class 'str'>, <class 'str'>, <class 'str'>)
Certains Types N'ont Pas De Nom Intégré, Ils Doivent Donc Être Importés :
from types import FunctionType, MethodType, LambdaType, GeneratorType
Classes De Base Abstraites
Chaque classe de base abstraite spécifie un ensemble de sous-classes virtuelles. Ces classes sont alors reconnues par isinstance() et issubclass() comme des sous-classes de l'ABC, bien qu'elles ne le soient pas vraiment.

>>> from collections.abc import Sequence, Collection, Iterable
>>> isinstance([1, 2, 3], Iterable)
True
+------------------+------------+------------+------------+
|                  |  Sequence  | Collection |  Iterable  |
+------------------+------------+------------+------------+
| list, range, str |    yes     |    yes     |    yes     |
| dict, set        |            |    yes     |    yes     |
| iter             |            |            |    yes     |
+------------------+------------+------------+------------+
>>> from numbers import Integral, Rational, Real, Complex, Number
>>> isinstance(123, Number)
True
+--------------------+----------+----------+----------+----------+----------+
|                    | Integral | Rational |   Real   | Complex  |  Number  |
+--------------------+----------+----------+----------+----------+----------+
| int                |   yes    |   yes    |   yes    |   yes    |   yes    |
| fractions.Fraction |          |   yes    |   yes    |   yes    |   yes    |
| float              |          |          |   yes    |   yes    |   yes    |
| complex            |          |          |          |   yes    |   yes    |
| decimal.Decimal    |          |          |          |          |   yes    |
+--------------------+----------+----------+----------+----------+----------+
Chaîne De Caractères
<str>  = <str>.strip()                       # Strips all whitespace characters from both ends.
<str>  = <str>.strip('<chars>')              # Strips all passed characters from both ends.
<list> = <str>.split()                       # Splits on one or more whitespace characters.
<list> = <str>.split(sep=None, maxsplit=-1)  # Splits on 'sep' str at most 'maxsplit' times.
<list> = <str>.splitlines(keepends=False)    # Splits on \n,\r,\r\n. Keeps them if 'keepends'.
<str>  = <str>.join(<coll_of_strings>)       # Joins elements using string as separator.
<bool> = <sub_str> in <str>                  # Checks if string contains a substring.
<bool> = <str>.startswith(<sub_str>)         # Pass tuple of strings for multiple options.
<bool> = <str>.endswith(<sub_str>)           # Pass tuple of strings for multiple options.
<int>  = <str>.find(<sub_str>)               # Returns start index of first match or -1.
<int>  = <str>.index(<sub_str>)              # Same but raises ValueError if missing.
<str>  = <str>.replace(old, new [, count])   # Replaces 'old' with 'new' at most 'count' times.
<str>  = <str>.translate(<table>)            # Use `str.maketrans(<dict>)` to generate table.
<str>  = chr(<int>)                          # Converts int to Unicode char.
<int>  = ord(<str>)                          # Converts Unicode char to int.
Aussi : 'lstrip()', 'rstrip()'.
Aussi : 'lower()', 'upper()', 'capitalize()'et 'title()'.
Méthodes De Propriété
+---------------+----------+----------+----------+----------+----------+
|               | [ !#$%…] | [a-zA-Z] |  [¼½¾]   |  [²³¹]   |  [0-9]   |
+---------------+----------+----------+----------+----------+----------+
| isprintable() |   yes    |   yes    |   yes    |   yes    |   yes    |
| isalnum()     |          |   yes    |   yes    |   yes    |   yes    |
| isnumeric()   |          |          |   yes    |   yes    |   yes    |
| isdigit()     |          |          |          |   yes    |   yes    |
| isdecimal()   |          |          |          |          |   yes    |
+---------------+----------+----------+----------+----------+----------+
Aussi : 'isspace()'recherche '[ \t\n\r\f\v…]'.
Regex
import re
<str>   = re.sub(<regex>, new, text, count=0)  # Substitutes all occurrences with 'new'.
<list>  = re.findall(<regex>, text)            # Returns all occurrences as strings.
<list>  = re.split(<regex>, text, maxsplit=0)  # Use brackets in regex to include the matches.
<Match> = re.search(<regex>, text)             # Searches for first occurrence of the pattern.
<Match> = re.match(<regex>, text)              # Searches only at the beginning of the text.
<iter>  = re.finditer(<regex>, text)           # Returns all occurrences as match objects.
Search() et match() renvoient None s'ils ne trouvent pas de correspondance.
L'argument 'flags=re.IGNORECASE'peut être utilisé avec toutes les fonctions.
L' argument 'flags=re.MULTILINE'fait '^'et '$'correspond au début/à la fin de chaque ligne.
L' argument 'flags=re.DOTALL'fait que point accepte également le '\n'.
Utilisez r'\1'ou '\\1'pour la référence arrière.
Ajouter '?'après un opérateur pour le rendre non gourmand.
Faire Correspondre L'objet
<str>   = <Match>.group()                      # Returns the whole match. Also group(0).
<str>   = <Match>.group(1)                     # Returns part in the first bracket.
<tuple> = <Match>.groups()                     # Returns all bracketed parts.
<int>   = <Match>.start()                      # Returns start index of the match.
<int>   = <Match>.end()                        # Returns exclusive end index of the match.
Séquences Spéciales
Par défaut, les chiffres, les caractères alphanumériques et les espaces blancs de tous les alphabets sont mis en correspondance, sauf si un 'flags=re.ASCII'argument est utilisé.
Utilisez une majuscule pour la négation.
'\d' == '[0-9]'                                # Matches any digit.
'\w' == '[a-zA-Z0-9_]'                         # Matches any alphanumeric.
'\s' == '[ \t\n\r\f\v]'                        # Matches any whitespace.
Format
<str> = f'{<el_1>}, {<el_2>}'
<str> = '{}, {}'.format(<el_1>, <el_2>)
Les Attributs
>>> from collections import namedtuple
>>> Person = namedtuple('Person', 'name height')
>>> person = Person('Jean-Luc', 187)
>>> f'{person.height}'
'187'
>>> '{p.height}'.format(p=person)
'187'
Options Générales
{<el>:<10}                                     # '<el>      '
{<el>:^10}                                     # '   <el>   '
{<el>:>10}                                     # '      <el>'
{<el>:.<10}                                    # '<el>......'
{<el>:<0}                                      # '<el>'
Cordes
'!r'appelle la méthode repr() de l'objet , au lieu de str() , pour obtenir une chaîne.

{'abcde'!r:10}                                 # "'abcde'   "
{'abcde':10.3}                                 # 'abc       '
{'abcde':.3}                                   # 'abc'
Nombres
{ 123456:10,}                                  # '   123,456'
{ 123456:10_}                                  # '   123_456'
{ 123456:+10}                                  # '   +123456'
{-123456:=10}                                  # '-   123456'
{ 123456: }                                    # ' 123456'
{-123456: }                                    # '-123456'
Flotteurs
{1.23456:10.3}                                 # '      1.23'
{1.23456:10.3f}                                # '     1.235'
{1.23456:10.3e}                                # ' 1.235e+00'
{1.23456:10.3%}                                # '  123.456%'
Comparaison Des Types De Présentation :
+---------------+-----------------+-----------------+-----------------+-----------------+
|               |    {<float>}    |   {<float>:f}   |   {<float>:e}   |   {<float>:%}   |
+---------------+-----------------+-----------------+-----------------+-----------------+
|   0.000056789 |    '5.6789e-05' |     '0.000057'  |  '5.678900e-05' |     '0.005679%' |
|   0.00056789  |    '0.00056789' |     '0.000568'  |  '5.678900e-04' |     '0.056789%' |
|   0.0056789   |    '0.0056789'  |     '0.005679'  |  '5.678900e-03' |     '0.567890%' |
|   0.056789    |    '0.056789'   |     '0.056789'  |  '5.678900e-02' |     '5.678900%' |
|   0.56789     |    '0.56789'    |     '0.567890'  |  '5.678900e-01' |    '56.789000%' |
|   5.6789      |    '5.6789'     |     '5.678900'  |  '5.678900e+00' |   '567.890000%' |
|  56.789       |   '56.789'      |    '56.789000'  |  '5.678900e+01' |  '5678.900000%' |
| 567.89        |  '567.89'       |   '567.890000'  |  '5.678900e+02' | '56789.000000%' |
+---------------+-----------------+-----------------+-----------------+-----------------+
+---------------+-----------------+-----------------+-----------------+-----------------+
|               |   {<float>:.2}  |  {<float>:.2f}  |  {<float>:.2e}  |  {<float>:.2%}  |
+---------------+-----------------+-----------------+-----------------+-----------------+
|   0.000056789 |    '5.7e-05'    |       '0.00'    |    '5.68e-05'   |       '0.01%'   |
|   0.00056789  |    '0.00057'    |       '0.00'    |    '5.68e-04'   |       '0.06%'   |
|   0.0056789   |    '0.0057'     |       '0.01'    |    '5.68e-03'   |       '0.57%'   |
|   0.056789    |    '0.057'      |       '0.06'    |    '5.68e-02'   |       '5.68%'   |
|   0.56789     |    '0.57'       |       '0.57'    |    '5.68e-01'   |      '56.79%'   |
|   5.6789      |    '5.7'        |       '5.68'    |    '5.68e+00'   |     '567.89%'   |
|  56.789       |    '5.7e+01'    |      '56.79'    |    '5.68e+01'   |    '5678.90%'   |
| 567.89        |    '5.7e+02'    |     '567.89'    |    '5.68e+02'   |   '56789.00%'   |
+---------------+-----------------+-----------------+-----------------+-----------------+
Ints
{90:c}                                   # 'Z'
{90:b}                                   # '1011010'
{90:X}                                   # '5A'
Nombres
Les Types
<int>      = int(<float/str/bool>)       # Or: math.floor(<float>)
<float>    = float(<int/str/bool>)       # Or: <real>e±<int>
<complex>  = complex(real=0, imag=0)     # Or: <real> ± <real>j
<Fraction> = fractions.Fraction(0, 1)    # Or: Fraction(numerator=0, denominator=1)
<Decimal>  = decimal.Decimal(<str/int>)  # Or: Decimal((sign, digits, exponent))
'int(<str>)'et 'float(<str>)'lève ValueError sur les chaînes mal formées.
Les nombres décimaux peuvent être représentés exactement, contrairement aux flottants où '1.1 + 2.2 != 3.3'.
La précision des opérations décimales est définie avec : 'decimal.getcontext().prec = <int>'.
Les Fonctions De Base
<num> = pow(<num>, <num>)                # Or: <num> ** <num>
<num> = abs(<num>)                       # <float> = abs(<complex>)
<num> = round(<num> [, ±ndigits])        # `round(126, -1) == 130`
Math
from math import e, pi, inf, nan, isinf, isnan
from math import cos, acos, sin, asin, tan, atan, degrees, radians
from math import log, log10, log2
Statistiques
from statistics import mean, median, variance, stdev, pvariance, pstdev
Aléatoire
from random import random, randint, choice, shuffle
<float> = random()
<int>   = randint(from_inclusive, to_inclusive)
<el>    = choice(<list>)
shuffle(<list>)
Bac, Hexagonal
<int>        = ±0b<bin>                  # Or: ±0x<hex>
<int>        = int('±<bin>', 2)          # Or: int('±<hex>', 16)
<int>        = int('±0b<bin>', 0)        # Or: int('±0x<hex>', 0)
'[-]0b<bin>' = bin(<int>)                # Or: hex(<int>)
Opérateurs Au Niveau Du Bit
<int>        = <int> & <int>             # And
<int>        = <int> | <int>             # Or
<int>        = <int> ^ <int>             # Xor (0 if both bits equal)
<int>        = <int> << n_bits           # Shift left (>> for right)
<int>        = ~<int>                    # Not (also: -<int> - 1)
Combinatoire
Chaque fonction renvoie un itérateur.
Si vous voulez imprimer l'itérateur, vous devez d'abord le passer à la fonction list() !
from itertools import product, combinations, combinations_with_replacement, permutations
>>> product([0, 1], repeat=3)
[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
 (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
>>> product('ab', '12')
[('a', '1'), ('a', '2'),
 ('b', '1'), ('b', '2')]
>>> combinations('abc', 2)
[('a', 'b'), ('a', 'c'),
 ('b', 'c')]
>>> combinations_with_replacement('abc', 2)
[('a', 'a'), ('a', 'b'), ('a', 'c'),
 ('b', 'b'), ('b', 'c'),
 ('c', 'c')]
>>> permutations('abc', 2)
[('a', 'b'), ('a', 'c'),
 ('b', 'a'), ('b', 'c'),
 ('c', 'a'), ('c', 'b')]
Dateheure
Le module 'datetime' fournit les classes 'date' <D>, 'time' <T>, 'datetime' <DT>et 'timedelta' <TD>. Tous sont immuables et hachables.
Les objets time et datetime peuvent être 'aware' <a>, ce qui signifie qu'ils ont défini un fuseau horaire, ou 'naive' <n>, ce qui signifie qu'ils ne le font pas.
Si l'objet est naïf, il est supposé être dans le fuseau horaire du système.
from datetime import date, time, datetime, timedelta
from dateutil.tz import UTC, tzlocal, gettz, resolve_imaginary
Constructeurs
<D>  = date(year, month, day)
<T>  = time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, fold=0)
<DT> = datetime(year, month, day, hour=0, minute=0, second=0, ...)
<TD> = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0,
                 minutes=0, hours=0, weeks=0)
Utilisez '<D/DT>.weekday()'pour obtenir le jour de la semaine (Mon == 0).
'fold=1'désigne le deuxième passage en cas de saut de temps d'une heure.
'<DTa> = resolve_imaginary(<DTa>)'corrige les DT qui tombent dans l'heure manquante.
À Présent
<D/DTn>  = D/DT.today()                     # Current local date or naive datetime.
<DTn>    = DT.utcnow()                      # Naive datetime from current UTC time.
<DTa>    = DT.now(<tzinfo>)                 # Aware datetime from current tz time.
Pour extraire le temps, utilisez '<DTn>.time()', '<DTa>.time()'ou '<DTa>.timetz()'.
Fuseau Horaire
<tzinfo> = UTC                              # UTC timezone. London without DST.
<tzinfo> = tzlocal()                        # Local timezone. Also gettz().
<tzinfo> = gettz('<Continent>/<City>')      # 'Continent/City_Name' timezone or None.
<DTa>    = <DT>.astimezone(<tzinfo>)        # Datetime, converted to passed timezone.
<Ta/DTa> = <T/DT>.replace(tzinfo=<tzinfo>)  # Unconverted object with new timezone.
Encoder
<D/T/DT> = D/T/DT.fromisoformat('<iso>')    # Object from ISO string. Raises ValueError.
<DT>     = DT.strptime(<str>, '<format>')   # Datetime from str, according to format.
<D/DTn>  = D/DT.fromordinal(<int>)          # D/DTn from days since Christ, at midnight.
<DTn>    = DT.fromtimestamp(<real>)         # Local time DTn from seconds since Epoch.
<DTa>    = DT.fromtimestamp(<real>, <tz.>)  # Aware datetime from seconds since Epoch.
Les chaînes ISO se présentent sous les formes suivantes : 'YYYY-MM-DD', 'HH:MM:SS.ffffff[±<offset>]', ou les deux séparés par un caractère arbitraire. Le décalage est formaté comme suit : 'HH:MM'.
L'époque sur les systèmes Unix est : '1970-01-01 00:00 UTC', '1970-01-01 01:00 CET', …
Décoder
<str>    = <D/T/DT>.isoformat(sep='T')      # Also timespec='auto/hours/minutes/seconds'.
<str>    = <D/T/DT>.strftime('<format>')    # Custom string representation.
<int>    = <D/DT>.toordinal()               # Days since Christ, ignoring time and tz.
<float>  = <DTn>.timestamp()                # Seconds since Epoch, from DTn in local tz.
<float>  = <DTa>.timestamp()                # Seconds since Epoch, from DTa.
Format
>>> from datetime import datetime
>>> dt = datetime.strptime('2015-05-14 23:39:00.00 +0200', '%Y-%m-%d %H:%M:%S.%f %z')
>>> dt.strftime("%A, %dth of %B '%y, %I:%M%p %Z")
"Thursday, 14th of May '15, 11:39PM UTC+02:00"
Lors de l'analyse, '%z'accepte également '±HH:MM'.
Pour une utilisation abrégée du jour de la semaine et du mois '%a'et '%b'.
Arithmétique
<D/DT>   = <D/DT>   ± <TD>                  # Returned datetime can fall into missing hour.
<TD>     = <D/DTn>  - <D/DTn>               # Returns the difference, ignoring time jumps.
<TD>     = <DTa>    - <DTa>                 # Ignores time jumps if they share tzinfo object.
<TD>     = <DT_UTC> - <DT_UTC>              # Convert DTs to UTC to get the actual delta.
Arguments
Appel De Fonction Interne
<function>(<positional_args>)                  # f(0, 0)
<function>(<keyword_args>)                     # f(x=0, y=0)
<function>(<positional_args>, <keyword_args>)  # f(0, y=0)
À L'intérieur De La Définition De La Fonction
def f(<nondefault_args>):                      # def f(x, y):
def f(<default_args>):                         # def f(x=0, y=0):
def f(<nondefault_args>, <default_args>):      # def f(x, y=0):
Opérateur Splat
Appel De Fonction Interne
Splat développe une collection en arguments de position, tandis que splatty-splat développe un dictionnaire en arguments de mots clés.

args   = (1, 2)
kwargs = {'x': 3, 'y': 4, 'z': 5}
func(*args, **kwargs)
Est Le Même Que:
func(1, 2, x=3, y=4, z=5)
À L'intérieur De La Définition De La Fonction
Splat combine zéro ou plusieurs arguments de position dans un tuple, tandis que splatty-splat combine zéro ou plusieurs arguments de mots clés dans un dictionnaire.

def add(*a):
    return sum(a)
>>> add(1, 2, 3)
6
Combinaisons D'arguments Juridiques :
def f(x, y, z):                # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
def f(*, x, y, z):             # f(x=1, y=2, z=3)
def f(x, *, y, z):             # f(x=1, y=2, z=3) | f(1, y=2, z=3)
def f(x, y, *, z):             # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3)
def f(*args):                  # f(1, 2, 3)
def f(x, *args):               # f(1, 2, 3)
def f(*args, z):               # f(1, 2, z=3)
def f(x, *args, z):            # f(1, 2, z=3)
def f(**kwargs):               # f(x=1, y=2, z=3)
def f(x, **kwargs):            # f(x=1, y=2, z=3) | f(1, y=2, z=3)
def f(*, x, **kwargs):         # f(x=1, y=2, z=3)
def f(*args, **kwargs):        # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
def f(x, *args, **kwargs):     # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
def f(*args, y, **kwargs):     # f(x=1, y=2, z=3) | f(1, y=2, z=3)
def f(x, *args, z, **kwargs):  # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3)
Autres Utilisations
<list>  = [*<collection> [, ...]]
<set>   = {*<collection> [, ...]}
<tuple> = (*<collection>, [...])
<dict>  = {**<dict> [, ...]}
head, *body, tail = <collection>
En Ligne
Lambda
<function> = lambda: <return_value>
<function> = lambda <argument_1>, <argument_2>: <return_value>
Compréhensions
<list> = [i+1 for i in range(10)]                   # [1, 2, ..., 10]
<set>  = {i for i in range(10) if i > 5}            # {6, 7, 8, 9}
<iter> = (i+5 for i in range(10))                   # (5, 6, ..., 14)
<dict> = {i: i*2 for i in range(10)}                # {0: 0, 1: 2, ..., 9: 18}
out = [i+j for i in range(10) for j in range(10)]
Est Le Même Que:
out = []
for i in range(10):
    for j in range(10):
        out.append(i+j)
Cartographier, Filtrer, Réduire
from functools import reduce
<iter> = map(lambda x: x + 1, range(10))            # (1, 2, ..., 10)
<iter> = filter(lambda x: x > 5, range(10))         # (6, 7, 8, 9)
<obj>  = reduce(lambda out, x: out + x, range(10))  # 45
N'importe Lequel, Tous
<bool> = any(<collection>)                          # False if empty.
<bool> = all(el[1] for el in <collection>)          # True if empty.
Sinon
<obj> = <expression_if_true> if <condition> else <expression_if_false>
>>> [a if a else 'zero' for a in (0, 1, 2, 3)]
['zero', 1, 2, 3]
Namedtuple, Enum, Dataclass
from collections import namedtuple
Point     = namedtuple('Point', 'x y')
point     = Point(0, 0)
from enum import Enum
Direction = Enum('Direction', 'n e s w')
direction = Direction.n
from dataclasses import make_dataclass
Creature  = make_dataclass('Creature', ['location', 'direction'])
creature  = Creature(Point(0, 0), Direction.n)
Fermeture
Nous avons une fermeture en Python lorsque : * Une fonction imbriquée fait référence à une valeur de sa fonction englobante, puis * la fonction englobante renvoie la fonction imbriquée.

def get_multiplier(a):
    def out(b):
        return a * b
    return out
>>> multiply_by_3 = get_multiplier(3)
>>> multiply_by_3(10)
30
Si plusieurs fonctions imbriquées dans la fonction englobante font référence à la même valeur, cette valeur est partagée.
Pour accéder dynamiquement à la première variable libre de la fonction, utilisez '<function>.__closure__[0].cell_contents'.
Partiel
from functools import partial
<function> = partial(<function> [, <arg_1>, <arg_2>, ...])
>>> import operator as op
>>> multiply_by_3 = partial(op.mul, 3)
>>> multiply_by_3(10)
30
Partial est également utile dans les cas où la fonction doit être passée en argument, car elle nous permet de définir ses arguments à l'avance.
Quelques exemples étant : 'defaultdict(<function>)', 'iter(<function>, to_exclusive)'et dataclass's 'field(default_factory=<function>)'.
Non Local
Si la variable est assignée n'importe où dans la portée, elle est considérée comme une variable locale, à moins qu'elle ne soit déclarée comme 'globale' ou 'non locale'.

def get_counter():
    i = 0
    def out():
        nonlocal i
        i += 1
        return i
    return out
>>> counter = get_counter()
>>> counter(), counter(), counter()
(1, 2, 3)
Décorateur
Un décorateur prend une fonction, ajoute des fonctionnalités et la renvoie.

@decorator_name
def function_that_gets_passed_to_decorator():
    ...
Exemple De Débogueur
Décorateur qui imprime le nom de la fonction à chaque fois qu'elle est appelée.

from functools import wraps

def debug(func):
    @wraps(func)
    def out(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return out

@debug
def add(x, y):
    return x + y
Wraps est un décorateur d'assistance qui copie les métadonnées de la fonction passée (func) vers la fonction qu'elle enveloppe (out).
Sans elle 'add.__name__'reviendrait 'out'.
Cache LRU
Décorateur qui met en cache les valeurs de retour de la fonction. Tous les arguments de la fonction doivent être hachables.

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)
L'interpréteur CPython limite la profondeur de récursivité à 1000 par défaut. Pour l'augmenter, utilisez 'sys.setrecursionlimit(<depth>)'.
Décorateur Paramétré
Un décorateur qui accepte des arguments et renvoie un décorateur normal qui accepte une fonction.

from functools import wraps

def debug(print_result=False):
    def decorator(func):
        @wraps(func)
        def out(*args, **kwargs):
            result = func(*args, **kwargs)
            print(func.__name__, result if print_result else '')
            return result
        return out
    return decorator

@debug(print_result=True)
def add(x, y):
    return x + y
Classer
class <name>:
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.a!r})'
    def __str__(self):
        return str(self.a)

    @classmethod
    def get_class_name(cls):
        return cls.__name__
La valeur de retour de repr() doit être sans ambiguïté et de str() lisible.
Si seul repr() est défini, il sera également utilisé pour str().
Cas D'utilisation De Str() :
print(<el>)
print(f'{<el>}')
raise Exception(<el>)
loguru.logger.debug(<el>)
csv.writer(<file>).writerow([<el>])
Cas D'utilisation De Repr() :
print([<el>])
print(f'{<el>!r}')
>>> <el>
loguru.logger.exception()
Z = dataclasses.make_dataclass('Z', ['a']); print(Z(<el>))
Surcharge Du Constructeur
class <name>:
    def __init__(self, a=None):
        self.a = a
Héritage
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

class Employee(Person):
    def __init__(self, name, age, staff_num):
        super().__init__(name, age)
        self.staff_num = staff_num
Héritage Multiple
class A: pass
class B: pass
class C(A, B): pass
MRO détermine l'ordre dans lequel les classes parentes sont parcourues lors de la recherche d'une méthode :

>>> C.mro()
[<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>]
Propriété
Manière pythonique d'implémenter les getters et les setters.

class MyClass:
    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value
>>> el = MyClass()
>>> el.a = 123
>>> el.a
123
Classe De Données
Décorateur qui génère automatiquement les méthodes spéciales init(), repr() et eq().

from dataclasses import dataclass, field

@dataclass(order=False, frozen=False)
class <class_name>:
    <attr_name_1>: <type>
    <attr_name_2>: <type> = <default_value>
    <attr_name_3>: list/dict/set = field(default_factory=list/dict/set)
Les objets peuvent être rendus triables avec 'order=True'et/ou immuables et hachables avec 'frozen=True'.
La fonction field() est nécessaire car '<attr_name>: list = []'elle créerait une liste partagée par toutes les instances.
Default_factory peut être n'importe quel callable .
En Ligne:
from dataclasses import make_dataclass
<class> = make_dataclass('<class_name>', <coll_of_attribute_names>)
<class> = make_dataclass('<class_name>', <coll_of_tuples>)
<tuple> = ('<attr_name>', <type> [, <default_value>])
Machines À Sous
Mécanisme qui limite les objets aux attributs répertoriés dans les « emplacements » et réduit considérablement leur empreinte mémoire.

class MyClassWithSlots:
    __slots__ = ['a']
    def __init__(self):
        self.a = 1
Copie
from copy import copy, deepcopy
<object> = copy(<object>)
<object> = deepcopy(<object>)
Types De Canard
Un type de canard est un type implicite qui prescrit un ensemble de méthodes spéciales. Tout objet pour lequel ces méthodes sont définies est considéré comme un membre de ce type de canard.

Comparable
Si la méthode eq() n'est pas remplacée, elle renvoie 'id(self) == id(other)', qui est identique à 'self is other'.
Cela signifie que tous les objets ne sont pas égaux par défaut.
Seul l'objet de gauche a la méthode eq() appelée, à moins qu'il ne renvoie NotImplemented, auquel cas l'objet de droite est consulté.
class MyComparable:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.a == other.a
        return NotImplemented
Hachable
L'objet hachable nécessite à la fois les méthodes hash() et eq() et sa valeur de hachage ne doit jamais changer.
Les objets hachables qui se comparent égaux doivent avoir la même valeur de hachage, ce qui signifie que le hash() par défaut qui renvoie 'id(self)'ne le fera pas.
C'est pourquoi Python rend automatiquement les classes non hachables si vous n'implémentez que eq().
class MyHashable:
    def __init__(self, a):
        self._a = a
    @property
    def a(self):
        return self._a
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.a == other.a
        return NotImplemented
    def __hash__(self):
        return hash(self.a)
Triable
Avec le décorateur total_ordering, il vous suffit de fournir eq() et l'une des méthodes spéciales lt(), gt(), le() ou ge().
from functools import total_ordering

@total_ordering
class MySortable:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.a == other.a
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.a < other.a
        return NotImplemented
Itérateur
Tout objet qui a les méthodes next() et iter() est un itérateur.
Next() doit renvoyer l'élément suivant ou déclencher StopIteration.
Iter() doit renvoyer 'self'.
class Counter:
    def __init__(self):
        self.i = 0
    def __next__(self):
        self.i += 1
        return self.i
    def __iter__(self):
        return self
>>> counter = Counter()
>>> next(counter), next(counter), next(counter)
(1, 2, 3)
Python A De Nombreux Objets Itérateurs Différents :
Itérateurs renvoyés par la fonction iter() , tels que list_iterator et set_iterator.
Objets renvoyés par le module itertools , tels que count, repeat et cycle.
Générateurs renvoyés par les fonctions de générateur et les expressions de générateur .
Les objets fichier renvoyés par la fonction open() , etc.
Appelable
Toutes les fonctions et classes ont une méthode call(), elles sont donc appelables.
Lorsque cette feuille de triche utilise '<function>'comme argument, cela signifie en fait '<callable>'.
class Counter:
    def __init__(self):
        self.i = 0
    def __call__(self):
        self.i += 1
        return self.i
>>> counter = Counter()
>>> counter(), counter(), counter()
(1, 2, 3)
Gestionnaire De Contexte
Enter() doit verrouiller les ressources et éventuellement renvoyer un objet.
Exit() devrait libérer les ressources.
Toute exception qui se produit à l'intérieur du bloc with est transmise à la méthode exit().
S'il souhaite supprimer l'exception, il doit renvoyer une valeur vraie.
class MyOpen:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename)
        return self.file
    def __exit__(self, exc_type, exception, traceback):
        self.file.close()
>>> with open('test.txt', 'w') as file:
...     file.write('Hello World!')
>>> with MyOpen('test.txt') as file:
...     print(file.read())
Hello World!
Types De Canards Itérables
Itérable
La seule méthode requise est iter(). Il doit retourner un itérateur des éléments de l'objet.
Contient() fonctionne automatiquement sur tout objet pour lequel iter() est défini.
class MyIterable:
    def __init__(self, a):
        self.a = a
    def __iter__(self):
        return iter(self.a)
    def __contains__(self, el):
        return el in self.a
>>> obj = MyIterable([1, 2, 3])
>>> [el for el in obj]
[1, 2, 3]
>>> 1 in obj
True
Le Recueil
Les seules méthodes requises sont iter() et len().
Cette feuille de triche signifie en fait '<iterable>'quand elle utilise '<collection>'.
J'ai choisi de ne pas utiliser le nom "itérable" car il semble plus effrayant et plus vague que "collection".
class MyCollection:
    def __init__(self, a):
        self.a = a
    def __iter__(self):
        return iter(self.a)
    def __contains__(self, el):
        return el in self.a
    def __len__(self):
        return len(self.a)
Séquence
Les seules méthodes requises sont len() et getitem().
Getitem() doit renvoyer un élément à l'index ou déclencher IndexError.
Iter() et contains() fonctionnent automatiquement sur tout objet pour lequel getitem() est défini.
Reversed() fonctionne automatiquement sur tout objet pour lequel getitem() et len() sont définis.
class MySequence:
    def __init__(self, a):
        self.a = a
    def __iter__(self):
        return iter(self.a)
    def __contains__(self, el):
        return el in self.a
    def __len__(self):
        return len(self.a)
    def __getitem__(self, i):
        return self.a[i]
    def __reversed__(self):
        return reversed(self.a)
Séquence ABC
C'est une interface plus riche que la séquence de base.
Son extension génère iter(), contains(), reversed(), index() et count().
Contrairement à 'abc.Iterable'et 'abc.Collection', ce n'est pas un type de canard. C'est pourquoi 'issubclass(MySequence, abc.Sequence)'renverrait False même si MySequence avait toutes les méthodes définies.
from collections import abc

class MyAbcSequence(abc.Sequence):
    def __init__(self, a):
        self.a = a
    def __len__(self):
        return len(self.a)
    def __getitem__(self, i):
        return self.a[i]
Tableau Des Méthodes Spéciales Requises Et Disponibles Automatiquement :
+------------+------------+------------+------------+--------------+
|            |  Iterable  | Collection |  Sequence  | abc.Sequence |
+------------+------------+------------+------------+--------------+
| iter()     |    REQ     |    REQ     |    Yes     |     Yes      |
| contains() |    Yes     |    Yes     |    Yes     |     Yes      |
| len()      |            |    REQ     |    REQ     |     REQ      |
| getitem()  |            |            |    REQ     |     REQ      |
| reversed() |            |            |    Yes     |     Yes      |
| index()    |            |            |            |     Yes      |
| count()    |            |            |            |     Yes      |
+------------+------------+------------+------------+--------------+
Les autres ABC qui génèrent des méthodes manquantes sont : MutableSequence, Set, MutableSet, Mapping et MutableMapping.
Les noms de leurs méthodes requises sont stockés dans '<abc>.__abstractmethods__'.
Énumération
from enum import Enum, auto

class <enum_name>(Enum):
    <member_name_1> = <value_1>
    <member_name_2> = <value_2_a>, <value_2_b>
    <member_name_3> = auto()
S'il n'y a pas de valeurs numériques avant auto(), il renvoie 1.
Sinon, il renvoie un incrément de la dernière valeur numérique.
<member> = <enum>.<member_name>                 # Returns a member.
<member> = <enum>['<member_name>']              # Returns a member or raises KeyError.
<member> = <enum>(<value>)                      # Returns a member or raises ValueError.
<str>    = <member>.name                        # Returns member's name.
<obj>    = <member>.value                       # Returns member's value.
list_of_members = list(<enum>)
member_names    = [a.name for a in <enum>]
member_values   = [a.value for a in <enum>]
random_member   = random.choice(list(<enum>))
def get_next_member(member):
    members = list(member.__class__)
    index   = (members.index(member) + 1) % len(members)
    return members[index]
En Ligne
Cutlery = Enum('Cutlery', 'fork knife spoon')
Cutlery = Enum('Cutlery', ['fork', 'knife', 'spoon'])
Cutlery = Enum('Cutlery', {'fork': 1, 'knife': 2, 'spoon': 3})
Les Fonctions Définies Par L'utilisateur Ne Peuvent Pas Être Des Valeurs, Elles Doivent Donc Être Encapsulées :
from functools import partial
LogicOp = Enum('LogicOp', {'AND': partial(lambda l, r: l and r),
                           'OR' : partial(lambda l, r: l or r)})
Une autre solution dans ce cas particulier consiste à utiliser les fonctions intégrées and_() et or_() du module operator .
Exceptions
Exemple De Base
try:
    <code>
except <exception>:
    <code>
Exemple Complexe
try:
    <code_1>
except <exception_a>:
    <code_2_a>
except <exception_b>:
    <code_2_b>
else:
    <code_2_c>
finally:
    <code_3>
Le code à l'intérieur du 'else'bloc ne sera exécuté que si 'try'le bloc n'a pas d'exception.
Le code à l'intérieur du 'finally'bloc sera toujours exécuté.
Attraper Les Exceptions
except <exception>:
except <exception> as <name>:
except (<exception>, ...):
except (<exception>, ...) as <name>:
Intercepte également les sous-classes de l'exception.
Utilisez 'traceback.print_exc()'pour imprimer le message d'erreur sur stderr.
Lever Des Exceptions
raise <exception>
raise <exception>()
raise <exception>(<el> [, ...])
Relance De L'exception Interceptée :
except <exception> as <name>:
    ...
    raise
Objet D'exception
arguments = <name>.args
exc_type  = <name>.__class__
filename  = <name>.__traceback__.tb_frame.f_code.co_filename
func_name = <name>.__traceback__.tb_frame.f_code.co_name
line      = linecache.getline(filename, <name>.__traceback__.tb_lineno)
error_msg = traceback.format_exception(exc_type, <name>, <name>.__traceback__)
Exceptions Intégrées
BaseException
 +-- SystemExit                   # Raised by the sys.exit() function.
 +-- KeyboardInterrupt            # Raised when the user hits the interrupt key (ctrl-c).
 +-- Exception                    # User-defined exceptions should be derived from this class.
      +-- ArithmeticError         # Base class for arithmetic errors.
      |    +-- ZeroDivisionError  # Raised when dividing by zero.
      +-- AttributeError          # Raised when an attribute is missing.
      +-- EOFError                # Raised by input() when it hits end-of-file condition.
      +-- LookupError             # Raised when a look-up on a collection fails.
      |    +-- IndexError         # Raised when a sequence index is out of range.
      |    +-- KeyError           # Raised when a dictionary key or set element is not found.
      +-- NameError               # Raised when a variable name is not found.
      +-- OSError                 # Failures such as “file not found” or “disk full”.
      |    +-- FileNotFoundError  # When a file or directory is requested but doesn't exist.
      +-- RuntimeError            # Raised by errors that don't fall into other categories.
      |    +-- RecursionError     # Raised when the maximum recursion depth is exceeded.
      +-- StopIteration           # Raised by next() when run on an empty iterator.
      +-- TypeError               # Raised when an argument is of wrong type.
      +-- ValueError              # When an argument is of right type but inappropriate value.
           +-- UnicodeError       # Raised when encoding/decoding strings to/from bytes fails.
Collections Et Leurs Exceptions :
+-----------+------------+------------+------------+
|           |    list    |    dict    |    set     |
+-----------+------------+------------+------------+
| getitem() | IndexError |  KeyError  |            |
| pop()     | IndexError |  KeyError  |  KeyError  |
| remove()  | ValueError |            |  KeyError  |
| index()   | ValueError |            |            |
+-----------+------------+------------+------------+
Exceptions Intégrées Utiles :
raise TypeError('Argument is of wrong type!')
raise ValueError('Argument is of right type but inappropriate value!')
raise RuntimeError('None of above!')
Exceptions Définies Par L'utilisateur
class MyError(Exception):
    pass

class MyInputError(MyError):
    pass
Sortir
Quitte l'interpréteur en levant l'exception SystemExit.

import sys
sys.exit()                        # Exits with exit code 0 (success).
sys.exit(<el>)                    # Prints to stderr and exits with 1.
sys.exit(<int>)                   # Exits with passed exit code.
Imprimer
print(<el_1>, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
À utiliser 'file=sys.stderr'pour les messages d'erreurs.
Utilisez 'flush=True'pour rincer le flux de force.
Jolie Impression
from pprint import pprint
pprint(<collection>, width=80, depth=None, compact=False, sort_dicts=True)
Les niveaux plus profonds que 'profondeur' sont remplacés par '…'.
Saisir
Lit une ligne à partir d'une entrée utilisateur ou d'un tube s'il est présent.

<str> = input(prompt=None)
La nouvelle ligne de fin est supprimée.
La chaîne d'invite est imprimée sur la sortie standard avant de lire l'entrée.
Lève EOFError lorsque l'utilisateur appuie sur EOF (ctrl-d/z) ou que le flux d'entrée est épuisé.
Arguments De La Ligne De Commande
import sys
script_name = sys.argv[0]
arguments   = sys.argv[1:]
Analyseur D'arguments
from argparse import ArgumentParser, FileType
p = ArgumentParser(description=<str>)
p.add_argument('-<short_name>', '--<name>', action='store_true')  # Flag
p.add_argument('-<short_name>', '--<name>', type=<type>)          # Option
p.add_argument('<name>', type=<type>, nargs=1)                    # First argument
p.add_argument('<name>', type=<type>, nargs='+')                  # Remaining arguments
p.add_argument('<name>', type=<type>, nargs='*')                  # Optional arguments
args  = p.parse_args()                                            # Exits on error.
value = args.<name>
Utilisez 'help=<str>'pour définir la description de l'argument.
Utilisez 'default=<el>'pour définir la valeur par défaut.
Utiliser 'type=FileType(<mode>)'pour les fichiers.
Ouvert
Ouvre le fichier et renvoie un objet fichier correspondant.

<file> = open('<path>', mode='r', encoding=None, newline=None)
'encoding=None'signifie que l'encodage par défaut est utilisé, qui dépend de la plate-forme. La meilleure pratique consiste à utiliser 'encoding="utf-8"'chaque fois que possible.
'newline=None'signifie que toutes les différentes combinaisons de fin de ligne sont converties en '\n' en lecture, tandis qu'en écriture, tous les caractères '\n' sont convertis en séparateur de ligne par défaut du système.
'newline=""'signifie qu'aucune conversion n'a lieu, mais que l'entrée est toujours divisée en morceaux par readline() et readlines() sur '\n', '\r' ou '\r\n'.
Modes
'r' - Lire (par défaut).
'w' - Ecrire (tronquer).
'x' - Écrire ou échouer si le fichier existe déjà.
'a' - Appendre.
'w+'- Lire et écrire (tronquer).
'r+'- Lire et écrire depuis le début.
'a+'- Lire et écrire à partir de la fin.
't' - Mode texte (par défaut).
'b' - Mode binaire.
Exceptions
'FileNotFoundError'peut être relevé lors de la lecture avec 'r'ou 'r+'.
'FileExistsError'peut être augmenté lors de l'écriture avec 'x'.
'IsADirectoryError'et 'PermissionError'peut être augmenté par n'importe qui.
'OSError'est la classe parent de toutes les exceptions listées.
Objet Fichier
<file>.seek(0)                      # Moves to the start of the file.
<file>.seek(offset)                 # Moves 'offset' chars/bytes from the start.
<file>.seek(0, 2)                   # Moves to the end of the file.
<bin_file>.seek(±offset, <anchor>)  # Anchor: 0 start, 1 current position, 2 end.
<str/bytes> = <file>.read(size=-1)  # Reads 'size' chars/bytes or until EOF.
<str/bytes> = <file>.readline()     # Returns a line or empty string/bytes on EOF.
<list>      = <file>.readlines()    # Returns a list of remaining lines.
<str/bytes> = next(<file>)          # Returns a line using buffer. Do not mix.
<file>.write(<str/bytes>)           # Writes a string or bytes object.
<file>.writelines(<collection>)     # Writes a coll. of strings or bytes objects.
<file>.flush()                      # Flushes write buffer.
Les méthodes n'ajoutent ni ne suppriment les nouvelles lignes de fin, même writelines().
Lire Le Texte Du Fichier
def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()
Écrire Du Texte Dans Un Fichier
def write_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
Chemin
from os import getcwd, path, listdir
from glob import glob
<str>  = getcwd()                   # Returns the current working directory.
<str>  = path.join(<path>, ...)     # Joins two or more pathname components.
<str>  = path.abspath(<path>)       # Returns absolute path.
<str>  = path.basename(<path>)      # Returns final component of the path.
<str>  = path.dirname(<path>)       # Returns path without the final component.
<tup.> = path.splitext(<path>)      # Splits on last period of the final component.
<list> = listdir(path='.')          # Returns filenames located at path.
<list> = glob('<pattern>')          # Returns paths matching the wildcard pattern.
<bool> = path.exists(<path>)        # Or: <Path>.exists()
<bool> = path.isfile(<path>)        # Or: <DirEntry/Path>.is_file()
<bool> = path.isdir(<path>)         # Or: <DirEntry/Path>.is_dir()
EntréeRépertoire
L'utilisation de scandir() au lieu de listdir() peut augmenter considérablement les performances du code qui a également besoin d'informations sur le type de fichier.

from os import scandir
<iter> = scandir(path='.')          # Returns DirEntry objects located at path.
<str>  = <DirEntry>.path            # Returns path as a string.
<str>  = <DirEntry>.name            # Returns final component as a string.
<file> = open(<DirEntry>)           # Opens the file and returns file object.
Objet De Chemin
from pathlib import Path
<Path> = Path(<path> [, ...])       # Accepts strings, Paths and DirEntry objects.
<Path> = <path> / <path> [/ ...]    # One of the paths must be a Path object.
<Path> = Path()                     # Returns relative cwd. Also Path('.').
<Path> = Path.cwd()                 # Returns absolute cwd. Also Path().resolve().
<Path> = <Path>.resolve()           # Returns absolute Path without symlinks.
<Path> = <Path>.parent              # Returns Path without final component.
<str>  = <Path>.name                # Returns final component as a string.
<str>  = <Path>.stem                # Returns final component without extension.
<str>  = <Path>.suffix              # Returns final component's extension.
<tup.> = <Path>.parts               # Returns all components as strings.
<iter> = <Path>.iterdir()           # Returns dir contents as Path objects.
<iter> = <Path>.glob('<pattern>')   # Returns Paths matching the wildcard pattern.
<str>  = str(<Path>)                # Returns path as a string.
<file> = open(<Path>)               # Opens the file and returns file object.
Commandes Du Système D'exploitation
Fichiers Et Répertoires
Les chemins peuvent être des chaînes, des objets Paths ou DirEntry.
Les fonctions signalent les erreurs liées au système d'exploitation en levant OSError ou l'une de ses sous- classes .
import os, shutil
os.chdir(<path>)                    # Changes the current working directory.
os.mkdir(<path>, mode=0o777)        # Creates a directory. Mode is in octal.
shutil.copy(from, to)               # Copies the file. 'to' can exist or be a dir.
shutil.copytree(from, to)           # Copies the directory. 'to' must not exist.
os.rename(from, to)                 # Renames/moves the file or directory.
os.replace(from, to)                # Same, but overwrites 'to' if it exists.
os.remove(<path>)                   # Deletes the file.
os.rmdir(<path>)                    # Deletes the empty directory.
shutil.rmtree(<path>)               # Deletes the directory.
Commandes Du Shell
import os
<str> = os.popen('<shell_command>').read()
Envoie '1 + 1' À La Calculatrice De Base Et Capture Sa Sortie :
>>> from subprocess import run
>>> run('bc', input='1 + 1\n', capture_output=True, encoding='utf-8')
CompletedProcess(args='bc', returncode=0, stdout='2\n', stderr='')
Envoie Test.In À La Calculatrice De Base Exécutée En Mode Standard Et Enregistre Sa Sortie Dans Test.Out :
>>> from shlex import split
>>> os.popen('echo 1 + 1 > test.in')
>>> run(split('bc -s'), stdin=open('test.in'), stdout=open('test.out', 'w'))
CompletedProcess(args=['bc', '-s'], returncode=0)
>>> open('test.out').read()
'2\n'
JSON
Format de fichier texte pour stocker des collections de chaînes et de nombres.

import json
<str>    = json.dumps(<object>, ensure_ascii=True, indent=None)
<object> = json.loads(<str>)
Lire L'objet À Partir Du Fichier JSON
def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
Écrire Un Objet Dans Un Fichier JSON
def write_to_json_file(filename, an_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)
Cornichon
Format de fichier binaire pour stocker des objets.

import pickle
<bytes>  = pickle.dumps(<object>)
<object> = pickle.loads(<bytes>)
Lire L'objet À Partir Du Fichier
def read_pickle_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
Écrire Un Objet Dans Un Fichier
def write_to_pickle_file(filename, an_object):
    with open(filename, 'wb') as file:
        pickle.dump(an_object, file)
CSV
Format de fichier texte pour stocker des feuilles de calcul.

import csv
Lis
<reader> = csv.reader(<file>)       # Also: `dialect='excel', delimiter=','`.
<list>   = next(<reader>)           # Returns next row as a list of strings.
<list>   = list(<reader>)           # Returns list of remaining rows.
Le fichier doit être ouvert avec un 'newline=""'argument, sinon les sauts de ligne intégrés à l'intérieur des champs entre guillemets ne seront pas interprétés correctement !
Écrire
<writer> = csv.writer(<file>)       # Also: `dialect='excel', delimiter=','`.
<writer>.writerow(<collection>)     # Encodes objects using `str(<el>)`.
<writer>.writerows(<coll_of_coll>)  # Appends multiple rows.
Le fichier doit être ouvert avec un 'newline=""'argument, sinon '\r' sera ajouté devant chaque '\n' sur les plates-formes qui utilisent les fins de ligne '\r\n' !
Paramètres
'dialect'- Paramètre maître qui définit les valeurs par défaut.
'delimiter'- Une chaîne d'un caractère utilisée pour séparer les champs.
'quotechar'- Caractère pour citer les champs contenant des caractères spéciaux.
'doublequote'- Si les guillemets à l'intérieur des champs sont doublés ou échappés.
'skipinitialspace'- Si les espaces après le délimiteur sont supprimés.
'lineterminator'- Spécifie comment le rédacteur termine les lignes.
'quoting'- Contrôle le nombre de citations : 0 - si nécessaire, 1 - tous.
'escapechar'- Caractère d'échappement de 'quotechar' si 'doublequote' vaut False.
Dialectes
+------------------+--------------+--------------+--------------+
|                  |     excel    |   excel-tab  |     unix     |
+------------------+--------------+--------------+--------------+
| delimiter        |       ','    |      '\t'    |       ','    |
| quotechar        |       '"'    |       '"'    |       '"'    |
| doublequote      |      True    |      True    |      True    |
| skipinitialspace |     False    |     False    |     False    |
| lineterminator   |    '\r\n'    |    '\r\n'    |      '\n'    |
| quoting          |         0    |         0    |         1    |
| escapechar       |      None    |      None    |      None    |
+------------------+--------------+--------------+--------------+
Lire Les Lignes Du Fichier CSV
def read_csv_file(filename):
    with open(filename, encoding='utf-8', newline='') as file:
        return list(csv.reader(file))
Écrire Des Lignes Dans Un Fichier CSV
def write_to_csv_file(filename, rows):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
SQLiteName
Moteur de base de données sans serveur qui stocke chaque base de données dans un fichier séparé.

Relier
Ouvre une connexion au fichier de base de données. Crée un nouveau fichier si le chemin n'existe pas.

import sqlite3
<con> = sqlite3.connect('<path>')               # Also ':memory:'.
<con>.close()
Lis
Les valeurs renvoyées peuvent être de type str, int, float, bytes ou None.

<cursor> = <con>.execute('<query>')             # Can raise a subclass of sqlite3.Error.
<tuple>  = <cursor>.fetchone()                  # Returns next row. Also next(<cursor>).
<list>   = <cursor>.fetchall()                  # Returns remaining rows. Also list(<cursor>).
Écrire
<con>.execute('<query>')
<con>.commit()
Ou:
with <con>:
    <con>.execute('<query>')
Espaces Réservés
Les valeurs transmises peuvent être de type str, int, float, bytes, None, bool, datetime.date ou datetime.datetme.
Les booléens seront stockés et renvoyés sous forme d'entiers et de dates sous forme de chaînes au format ISO .
<con>.execute('<query>', <list/tuple>)          # Replaces '?'s in query with values.
<con>.execute('<query>', <dict/namedtuple>)     # Replaces ':<key>'s with values.
<con>.executemany('<query>', <coll_of_above>)   # Runs execute() many times.
Exemple
Dans cet exemple, les valeurs ne sont pas réellement enregistrées car elles 'con.commit()'sont omises !

>>> con = sqlite3.connect('test.db')
>>> con.execute('create table person (person_id integer primary key, name, height)')
>>> con.execute('insert into person values (null, ?, ?)', ('Jean-Luc', 187)).lastrowid
1
>>> con.execute('select * from person').fetchall()
[(1, 'Jean-Luc', 187)]
MySQL
A une interface très similaire, avec les différences énumérées ci-dessous.

# $ pip3 install mysql-connector
from mysql import connector
<con> = connector.connect(host=<str>, …)        # `user=<str>, password=<str>, database=<str>`.
<cursor> = <con>.cursor()                       # Only cursor has execute method.
<cursor>.execute('<query>')                     # Can raise a subclass of connector.Error.
<cursor>.execute('<query>', <list/tuple>)       # Replaces '%s's in query with values.
<cursor>.execute('<query>', <dict/namedtuple>)  # Replaces '%(<key>)s's with values.
Octets
L'objet Bytes est une séquence immuable d'octets uniques. La version mutable est appelée bytearray.

<bytes> = b'<str>'                       # Only accepts ASCII characters and \x00 - \xff.
<int>   = <bytes>[<index>]               # Returns int in range from 0 to 255.
<bytes> = <bytes>[<slice>]               # Returns bytes even if it has only one element.
<bytes> = <bytes>.join(<coll_of_bytes>)  # Joins elements using bytes object as separator.
Encoder
<bytes> = bytes(<coll_of_ints>)          # Ints must be in range from 0 to 255.
<bytes> = bytes(<str>, 'utf-8')          # Or: <str>.encode('utf-8')
<bytes> = <int>.to_bytes(n_bytes, …)     # `byteorder='big/little', signed=False`.
<bytes> = bytes.fromhex('<hex>')         # Hex numbers can be separated by spaces.
Décoder
<list>  = list(<bytes>)                  # Returns ints in range from 0 to 255.
<str>   = str(<bytes>, 'utf-8')          # Or: <bytes>.decode('utf-8')
<int>   = int.from_bytes(<bytes>, …)     # `byteorder='big/little', signed=False`.
'<hex>' = <bytes>.hex()                  # Returns a string of hexadecimal numbers.
Lire Les Octets Du Fichier
def read_bytes(filename):
    with open(filename, 'rb') as file:
        return file.read()
Écrire Des Octets Dans Le Fichier
def write_bytes(filename, bytes_obj):
    with open(filename, 'wb') as file:
        file.write(bytes_obj)
Structure
Module qui effectue des conversions entre une suite de nombres et un objet bytes.
Les tailles de type et l'ordre des octets natifs de la machine sont utilisés par défaut.
from struct import pack, unpack, iter_unpack
<bytes>  = pack('<format>', <num_1> [, <num_2>, ...])
<tuple>  = unpack('<format>', <bytes>)
<tuples> = iter_unpack('<format>', <bytes>)
Exemple
>>> pack('>hhl', 1, 2, 3)
b'\x00\x01\x00\x02\x00\x00\x00\x03'
>>> unpack('>hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03')
(1, 2, 3)
Format
Pour Les Tailles De Caractères Standard, Commencez La Chaîne De Format Par :
'='- ordre natif des octets
'<'- petit endian
'>'- big-endian (aussi '!')
Types Entiers. Utilisez Une Majuscule Pour Les Caractères Non Signés. Les Tailles Standard Sont Entre Parenthèses :
'x'- octet de remplissage
'b'- char (1)
'h'- court (2)
'i'- entier (4)
'l'- longue (4)
'q'- long long (8)
Types À Virgule Flottante :
'f'- flotteur (4)
'd'- double (8)
Déployer
Liste qui ne peut contenir que des nombres d'un type prédéfini. Les types disponibles et leurs tailles en octets sont répertoriés ci-dessus.

from array import array
<array> = array('<typecode>', <collection>)    # Array from collection of numbers.
<array> = array('<typecode>', <bytes>)         # Array from bytes object.
<array> = array('<typecode>', <array>)         # Treats array as a sequence of numbers.
<bytes> = bytes(<array>)                       # Or: <array>.tobytes()
Mémoire Visuelle
Un objet séquence qui pointe vers la mémoire d'un autre objet.
Chaque élément peut référencer un ou plusieurs octets consécutifs, selon le format.
L'ordre et le nombre d'éléments peuvent être modifiés avec le découpage en tranches.
<mview> = memoryview(<bytes/bytearray/array>)  # Immutable if bytes, else mutable.
<real>  = <mview>[<index>]                     # Returns an int or a float.
<mview> = <mview>[<slice>]                     # Mview with rearranged elements.
<mview> = <mview>.cast('<typecode>')           # Casts memoryview to the new format.
<mview>.release()                              # Releases the object's memory buffer.
Décoder
<bin_file>.write(<mview>)                      # Writes mview to the binary file.
<bytes> = bytes(<mview>)                       # Creates a new bytes object.
<bytes> = <bytes>.join(<coll_of_mviews>)       # Joins mviews using bytes object as sep.
<array> = array('<typecode>', <mview>)         # Treats mview as a sequence of numbers.
<list>  = list(<mview>)                        # Returns list of ints or floats.
<str>   = str(<mview>, 'utf-8')                # Treats mview as a bytes object.
<int>   = int.from_bytes(<mview>, …)           # `byteorder='big/little', signed=False`.
'<hex>' = <mview>.hex()                        # Treats mview as a bytes object.
Deque
Une liste thread-safe avec des ajouts et des pops efficaces de chaque côté. Prononcé "pont".

from collections import deque
<deque> = deque(<collection>, maxlen=None)
<deque>.appendleft(<el>)                       # Opposite element is dropped if full.
<deque>.extendleft(<collection>)               # Collection gets reversed.
<el> = <deque>.popleft()                       # Raises IndexError if empty.
<deque>.rotate(n=1)                            # Rotates elements to the right.
Enfilage
L'interpréteur CPython ne peut exécuter qu'un seul thread à la fois.
C'est pourquoi l'utilisation de plusieurs threads n'entraînera pas une exécution plus rapide, à moins qu'au moins l'un des threads ne contienne une opération d'E/S.
from threading import Thread, RLock, Semaphore, Event, Barrier
Fil De Discussion
<Thread> = Thread(target=<function>)  # Use `args=<collection>` to set arguments.
<Thread>.start()                      # Starts the thread.
<bool> = <Thread>.is_alive()          # Checks if thread has finished executing.
<Thread>.join()                       # Waits for thread to finish.
Utilisez 'kwargs=<dict>'pour passer des arguments de mots-clés à la fonction.
Utilisez 'daemon=True', sinon le programme ne pourra pas se fermer tant que le thread est actif.
Bloquer
<lock> = RLock()
<lock>.acquire()                      # Waits for lock to be available.
<lock>.release()                      # Makes the lock available again.
Ou:
lock = RLock()
with lock:
    ...
Sémaphore, Événement, Barrière
<Semaphore> = Semaphore(value=1)      # Lock that can be acquired 'value' times.
<Event>     = Event()                 # Method wait() blocks until set() is called.
<Barrier>   = Barrier(n_times)        # Method wait() blocks until it's called 'n_times'.
Exécuteur De Pool De Threads
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=None) as executor:         # Does not exit until done.
    <iter>   = executor.map(lambda x: x + 1, range(3))         # (1, 2, 3)
    <iter>   = executor.map(lambda x, y: x + y, 'abc', '123')  # ('a1', 'b2', 'c3')
    <Future> = executor.submit(<function> [, <arg_1>, ...])    # Also visible outside block.
Avenir:
<bool> = <Future>.done()              # Checks if thread has finished executing.
<obj>  = <Future>.result()            # Waits for thread to finish and returns result.
File D'attente
Une file d'attente FIFO thread-safe. Pour la file d'attente LIFO, utilisez LifoQueue.

from queue import Queue
<Queue> = Queue(maxsize=0)
<Queue>.put(<el>)                     # Blocks until queue stops being full.
<Queue>.put_nowait(<el>)              # Raises queue.Full exception if full.
<el> = <Queue>.get()                  # Blocks until queue stops being empty.
<el> = <Queue>.get_nowait()           # Raises queue.Empty exception if empty.
Opérateur
Module de fonctions qui fournit la fonctionnalité des opérateurs.

from operator import add, sub, mul, truediv, floordiv, mod, pow, neg, abs
from operator import eq, ne, lt, le, gt, ge
from operator import and_, or_, not_
from operator import itemgetter, attrgetter, methodcaller
import operator as op
elementwise_sum  = map(op.add, list_a, list_b)
sorted_by_second = sorted(<collection>, key=op.itemgetter(1))
sorted_by_both   = sorted(<collection>, key=op.itemgetter(1, 0))
product_of_elems = functools.reduce(op.mul, <collection>)
LogicOp          = enum.Enum('LogicOp', {'AND': op.and_, 'OR' : op.or_})
last_el          = op.methodcaller('pop')(<list>)
Introspection
Inspecter le code à l'exécution.

Variables
<list> = dir()                             # Names of local variables (incl. functions).
<dict> = vars()                            # Dict of local variables. Also locals().
<dict> = globals()                         # Dict of global variables.
Les Attributs
<list> = dir(<object>)                     # Names of object's attributes (incl. methods).
<dict> = vars(<object>)                    # Dict of object's fields. Also <obj>.__dict__.
<bool> = hasattr(<object>, '<attr_name>')  # Checks if getattr() raises an error.
value  = getattr(<object>, '<attr_name>')  # Raises AttributeError if attribute is missing.
setattr(<object>, '<attr_name>', value)    # Only works on objects with __dict__ attribute.
delattr(<object>, '<attr_name>')           # Equivalent to `del <object>.<attr_name>`.
Paramètres
from inspect import signature
<sig>        = signature(<function>)
no_of_params = len(<sig>.parameters)
param_names  = list(<sig>.parameters.keys())
param_kinds  = [a.kind for a in <sig>.parameters.values()]
Métaprogrammation
Code qui génère du code.

Taper
Type est la classe racine. S'il ne passe qu'un objet, il renvoie son type (classe). Sinon, il crée une nouvelle classe.

<class> = type('<class_name>', <parents_tuple>, <attributes_dict>)
>>> Z = type('Z', (), {'a': 'abcde', 'b': 12345})
>>> z = Z()
Méta Classe
Une classe qui crée des classes.

def my_meta_class(name, parents, attrs):
    attrs['a'] = 'abcde'
    return type(name, parents, attrs)
Ou:
class MyMetaClass(type):
    def __new__(cls, name, parents, attrs):
        attrs['a'] = 'abcde'
        return type.__new__(cls, name, parents, attrs)
New() est une méthode de classe qui est appelée avant init(). S'il renvoie une instance de sa classe, cette instance est transmise à init() en tant qu'argument 'self'.
Il reçoit les mêmes arguments que init(), à l'exception du premier qui spécifie le type souhaité de l'instance renvoyée (MyMetaClass dans notre cas).
Comme dans notre cas, new() peut également être appelé directement, généralement à partir d'une méthode new() d'une classe enfant ( def __new__(cls): return super().__new__(cls)).
La seule différence entre les exemples ci-dessus est que my_meta_class() renvoie une classe de type type, tandis que MyMetaClass() renvoie une classe de type MyMetaClass.
Attribut De Métaclasse
Juste avant qu'une classe ne soit créée, elle vérifie si l'attribut 'metaclass' est défini. Si ce n'est pas le cas, il vérifie récursivement si l'un de ses parents l'a défini et en vient finalement à type().

class MyClass(metaclass=MyMetaClass):
    b = 12345
>>> MyClass.a, MyClass.b
('abcde', 12345)
Diagramme De Types
type(MyClass)     == MyMetaClass     # MyClass is an instance of MyMetaClass.
type(MyMetaClass) == type            # MyMetaClass is an instance of type.
+-------------+-------------+
|   Classes   | Metaclasses |
+-------------+-------------|
|   MyClass --> MyMetaClass |
|             |     v       |
|    object -----> type <+  |
|             |     ^ +--+  |
|     str ----------+       |
+-------------+-------------+
Diagramme D'héritage
MyClass.__base__     == object       # MyClass is a subclass of object.
MyMetaClass.__base__ == type         # MyMetaClass is a subclass of type.
+-------------+-------------+
|   Classes   | Metaclasses |
+-------------+-------------|
|   MyClass   | MyMetaClass |
|      v      |     v       |
|    object <----- type     |
|      ^      |             |
|     str     |             |
+-------------+-------------+
Éval
>>> from ast import literal_eval
>>> literal_eval('1 + 2')
3
>>> literal_eval('[1, 2, 3]')
[1, 2, 3]
>>> literal_eval('abs(1)')
ValueError: malformed node or string
Coroutines
Les coroutines ont beaucoup en commun avec les threads, mais contrairement aux threads, elles n'abandonnent le contrôle que lorsqu'elles appellent une autre coroutine et elles n'utilisent pas autant de mémoire.
La définition de la coroutine commence par 'async'et son appel par 'await'.
'asyncio.run(<coroutine>)'est le point d'entrée principal des programmes asynchrones.
Les fonctions wait (), rassemble () et as_completed () peuvent être utilisées lorsque plusieurs coroutines doivent être démarrées en même temps.
Le module Asyncio fournit également ses propres classes Queue , Event , Lock et Semaphore .
Exécute Un Jeu De Terminal Où Vous Contrôlez Un Astérisque Qui Doit Éviter Les Nombres :
import asyncio, collections, curses, enum, random

P = collections.namedtuple('P', 'x y')         # Position
D = enum.Enum('D', 'n e s w')                  # Direction

def main(screen):
    curses.curs_set(0)                         # Makes cursor invisible.
    screen.nodelay(True)                       # Makes getch() non-blocking.
    asyncio.run(main_coroutine(screen))        # Starts running asyncio code.

async def main_coroutine(screen):
    state = {'*': P(0, 0), **{id_: P(30, 10) for id_ in range(10)}}
    moves = asyncio.Queue()
    coros = (*(random_controller(id_, moves) for id_ in range(10)),
             human_controller(screen, moves),
             model(moves, state, *screen.getmaxyx()),
             view(state, screen))
    await asyncio.wait(coros, return_when=asyncio.FIRST_COMPLETED)

async def random_controller(id_, moves):
    while True:
        moves.put_nowait((id_, random.choice(list(D))))
        await asyncio.sleep(random.random() / 2)

async def human_controller(screen, moves):
    while True:
        ch = screen.getch()
        key_mappings = {259: D.n, 261: D.e, 258: D.s, 260: D.w}
        if ch in key_mappings:
            moves.put_nowait(('*', key_mappings[ch]))
        await asyncio.sleep(0.01)  

async def model(moves, state, height, width):
    while state['*'] not in {p for id_, p in state.items() if id_ != '*'}:
        id_, d = await moves.get()
        p      = state[id_]
        deltas = {D.n: P(0, -1), D.e: P(1, 0), D.s: P(0, 1), D.w: P(-1, 0)}
        new_p  = P(*[sum(a) for a in zip(p, deltas[d])])
        if 0 <= new_p.x < width-1 and 0 <= new_p.y < height:
            state[id_] = new_p

async def view(state, screen):
    while True:
        screen.clear()
        for id_, p in state.items():
            screen.addstr(p.y, p.x, str(id_))
        await asyncio.sleep(0.01)  

curses.wrapper(main)


Bibliothèques
Barre De Progression
# $ pip3 install tqdm
from tqdm import tqdm
from time import sleep
for el in tqdm([1, 2, 3]):
    sleep(0.2)
Terrain
# $ pip3 install matplotlib
from matplotlib import pyplot
pyplot.plot(<y_data> [, label=<str>])
pyplot.plot(<x_data>, <y_data>)
pyplot.legend()                                # Adds a legend.
pyplot.savefig('<path>')                       # Saves the figure.
pyplot.show()                                  # Displays the figure.
pyplot.clf()                                   # Clears the figure.
Table
Imprime Un Fichier CSV Sous Forme De Tableau ASCII :
# $ pip3 install tabulate
import csv, tabulate
with open('test.csv', encoding='utf-8', newline='') as file:
    rows   = csv.reader(file)
    header = [a.title() for a in next(rows)]
    table  = tabulate.tabulate(rows, header)
    print(table)
Malédictions
Efface Le Terminal, Imprime Un Message Et Attend L'appui Sur La Touche ESC :
from curses import wrapper, curs_set, ascii
from curses import KEY_UP, KEY_RIGHT, KEY_DOWN, KEY_LEFT

def main():
    wrapper(draw)

def draw(screen):
    curs_set(0)                                # Makes cursor invisible.
    screen.nodelay(True)                       # Makes getch() non-blocking.
    screen.clear()
    screen.addstr(0, 0, 'Press ESC to quit.')  # Coordinates are y, x.
    while screen.getch() != ascii.ESC:
        pass

def get_border(screen):
    from collections import namedtuple
    P = namedtuple('P', 'x y')
    height, width = screen.getmaxyx()
    return P(width-1, height-1)

if __name__ == '__main__':
    main()
Enregistrement
# $ pip3 install loguru
from loguru import logger
logger.add('debug_{time}.log', colorize=True)  # Connects a log file.
logger.add('error_{time}.log', level='ERROR')  # Another file for errors or higher.
logger.<level>('A logging message.')
Niveaux : 'debug', 'info', 'success', 'warning', 'error', 'critical'.
Exceptions
La description de l'exception, la trace de la pile et les valeurs des variables sont ajoutées automatiquement.

try:
    ...
except <exception>:
    logger.exception('An error happened.')
Rotation
Argument qui définit une condition lorsqu'un nouveau fichier journal est créé.

rotation=<int>|<datetime.timedelta>|<datetime.time>|<str>
'<int>'- Taille maximale du fichier en octets.
'<timedelta>'- Âge maximum d'un fichier.
'<time>'- Moment de la journée.
'<str>'- Tout ce qui précède sous forme de chaîne : '100 MB', '1 month', 'monday at 12:00', …
Rétention
Définit une condition selon laquelle les anciens fichiers journaux sont supprimés.

retention=<int>|<datetime.timedelta>|<str>
'<int>'- Nombre maximum de fichiers.
'<timedelta>'- Âge maximum d'un fichier.
'<str>'- Âge max sous forme de chaîne : '1 week, 3 days', '2 months', …
Grattage
Extrait L'URL, Le Numéro De Version Et Le Logo De Python De La Page Wikipedia :
# $ pip3 install requests beautifulsoup4
import requests, sys
from bs4 import BeautifulSoup
URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
try:
    html  = requests.get(URL).text
    doc   = BeautifulSoup(html, 'html.parser')
    table = doc.find('table', class_='infobox vevent')
    rows  = table.find_all('tr')
    link  = rows[11].find('a')['href']
    ver   = rows[6].find('div').text.split()[0]
    url_i = rows[0].find('img')['src']
    image = requests.get(f'https:{url_i}').content
    with open('test.png', 'wb') as file:
        file.write(image)
    print(link, ver)
except requests.exceptions.ConnectionError:
    print("You've got problems with connection.", file=sys.stderr)
La Toile
# $ pip3 install bottle
from bottle import run, route, static_file, template, post, request, response
import json
Courir
run(host='localhost', port=8080)        # Runs locally.
run(host='0.0.0.0', port=80)            # Runs globally.
Demande Statique
@route('/img/<image>')
def send_image(image):
    return static_file(image, 'img_dir/', mimetype='image/png')
Demande Dynamique
@route('/<sport>')
def send_page(sport):
    return template('<h1>{{title}}</h1>', title=sport)
Requête REST
@post('/odds/<sport>')
def odds_handler(sport):
    team = request.forms.get('team')
    home_odds, away_odds = 2.44, 3.29
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps([team, home_odds, away_odds])
Test:
# $ pip3 install requests
>>> import requests
>>> url  = 'http://localhost:8080/odds/football'
>>> data = {'team': 'arsenal f.c.'}
>>> response = requests.post(url, data=data)
>>> response.json()
['arsenal f.c.', 2.44, 3.29]
Profilage
Chronomètre
from time import time
start_time = time()                     # Seconds since the Epoch.
...
duration = time() - start_time
Haute Performance:
from time import perf_counter
start_time = perf_counter()             # Seconds since restart.
...
duration = perf_counter() - start_time
Chronométrer Un Extrait
>>> from timeit import timeit
>>> timeit('"-".join(str(a) for a in range(100))',
...        number=10000, globals=globals(), setup='pass')
0.34986
Profilage Par Ligne
# $ pip3 install line_profiler memory_profiler
@profile
def main():
    a = [*range(10000)]
    b = {*range(10000)}
main()
$ kernprof -lv test.py
Line #   Hits     Time  Per Hit   % Time  Line Contents
=======================================================
     1                                    @profile
     2                                    def main():
     3      1   1128.0   1128.0     27.4      a = [*range(10000)]
     4      1   2994.0   2994.0     72.6      b = {*range(10000)}
$ python3 -m memory_profiler test.py
Line #         Mem usage      Increment   Line Contents
=======================================================
     1        35.387 MiB     35.387 MiB   @profile
     2                                    def main():
     3        35.734 MiB      0.348 MiB       a = [*range(10000)]
     4        36.160 MiB      0.426 MiB       b = {*range(10000)}
Graphique D'appel
Génère Une Image PNG D'un Graphique D'appels Avec Les Goulots D'étranglement Mis En Évidence :
# $ pip3 install pycallgraph
from pycallgraph import output, PyCallGraph
from datetime import datetime
time_str = datetime.now().strftime('%Y%m%d%H%M%S')
filename = f'profile-{time_str}.png'
drawer = output.GraphvizOutput(output_file=filename)
with PyCallGraph(drawer):
    <code_to_be_profiled>
NumPy
Mini-langage de manipulation de tableaux. Il peut s'exécuter jusqu'à cent fois plus vite que le code Python équivalent.

# $ pip3 install numpy
import numpy as np
<array> = np.array(<list>)
<array> = np.arange(from_inclusive, to_exclusive, ±step_size)
<array> = np.ones(<shape>)
<array> = np.random.randint(from_inclusive, to_exclusive, <shape>)
<array>.shape = <shape>
<view>  = <array>.reshape(<shape>)
<view>  = np.broadcast_to(<array>, <shape>)
<array> = <array>.sum(axis)
indexes = <array>.argmin(axis)
La forme est un tuple de tailles de dimension.
L'axe est l'indice d'une dimension qui est réduite. La dimension la plus à gauche a l'index 0.
Indexage
<el>       = <2d_array>[0, 0]        # First element.
<1d_view>  = <2d_array>[0]           # First row.
<1d_view>  = <2d_array>[:, 0]        # First column. Also [..., 0].
<3d_view>  = <2d_array>[None, :, :]  # Expanded by dimension of size 1.
<1d_array> = <2d_array>[<1d_row_indexes>, <1d_column_indexes>]
<2d_array> = <2d_array>[<2d_row_indexes>, <2d_column_indexes>]
<2d_bools> = <2d_array> > 0
<1d_array> = <2d_array>[<2d_bools>]
Si les index de ligne et de colonne diffèrent par leur forme, ils sont combinés avec la diffusion.
Diffusion
La diffusion est un ensemble de règles selon lesquelles les fonctions NumPy fonctionnent sur des tableaux de différentes tailles et/ou dimensions.

left  = [[0.1], [0.6], [0.8]]        # Shape: (3, 1)
right = [ 0.1 ,  0.6 ,  0.8 ]        # Shape: (3)
1. Si Les Formes De Tableau Diffèrent En Longueur, Remplissez À Gauche La Forme La Plus Courte Avec Des Uns :
left  = [[0.1], [0.6], [0.8]]        # Shape: (3, 1)
right = [[0.1 ,  0.6 ,  0.8]]        # Shape: (1, 3) <- !
2. Si Des Dimensions Diffèrent En Taille, Développez Celles Qui Ont La Taille 1 En Dupliquant Leurs Éléments :
left  = [[0.1, 0.1, 0.1], [0.6, 0.6, 0.6], [0.8, 0.8, 0.8]]  # Shape: (3, 3) <- !
right = [[0.1, 0.6, 0.8], [0.1, 0.6, 0.8], [0.1, 0.6, 0.8]]  # Shape: (3, 3) <- !
3. Si Aucune Dimension Non Concordante N'a La Taille 1, Génère Une Erreur.
Exemple
Pour Chaque Point Renvoie L'index De Son Point Le Plus Proche ( [0.1, 0.6, 0.8] => [1, 2, 1]):
>>> points = np.array([0.1, 0.6, 0.8])
 [ 0.1,  0.6,  0.8]
>>> wrapped_points = points.reshape(3, 1)
[[ 0.1],
 [ 0.6],
 [ 0.8]]
>>> distances = wrapped_points - points
[[ 0. , -0.5, -0.7],
 [ 0.5,  0. , -0.2],
 [ 0.7,  0.2,  0. ]]
>>> distances = np.abs(distances)
[[ 0. ,  0.5,  0.7],
 [ 0.5,  0. ,  0.2],
 [ 0.7,  0.2,  0. ]]
>>> i = np.arange(3)
[0, 1, 2]
>>> distances[i, i] = np.inf
[[ inf,  0.5,  0.7],
 [ 0.5,  inf,  0.2],
 [ 0.7,  0.2,  inf]]
>>> distances.argmin(1)
[1, 2, 1]
Image
# $ pip3 install pillow
from PIL import Image
<Image> = Image.new('<mode>', (width, height))
<Image> = Image.open('<path>')
<Image> = <Image>.convert('<mode>')
<Image>.save('<path>')
<Image>.show()
<tuple/int> = <Image>.getpixel((x, y))          # Returns a pixel.
<Image>.putpixel((x, y), <tuple/int>)           # Writes a pixel to the image.
<ImagingCore> = <Image>.getdata()               # Returns a sequence of pixels.
<Image>.putdata(<list/ImagingCore>)             # Writes a sequence of pixels.
<Image>.paste(<Image>, (x, y))                  # Writes an image to the image.
<2d_array> = np.array(<Image>)                  # Creates NumPy array from greyscale image.
<3d_array> = np.array(<Image>)                  # Creates NumPy array from color image.
<Image>    = Image.fromarray(<array>)           # Creates image from NumPy array of floats.
Modes
'1'- Pixels 1 bit, noir et blanc, stockés à raison d'un pixel par octet.
'L'- Pixels 8 bits, niveaux de gris.
'RGB'- Pixels 3x8 bits, couleurs vraies.
'RGBA'- Pixels 4x8 bits, couleurs vraies avec masque de transparence.
'HSV'- Pixels 3x8 bits, teinte, saturation, espace colorimétrique de valeur.
Exemples
Crée Une Image PNG D'un Dégradé Arc-En-Ciel :
WIDTH, HEIGHT = 100, 100
size = WIDTH * HEIGHT
hues = [255 * i/size for i in range(size)]
img = Image.new('HSV', (WIDTH, HEIGHT))
img.putdata([(int(h), 255, 255) for h in hues])
img.convert('RGB').save('test.png')
Ajoute Du Bruit À Une Image PNG :
from random import randint
add_noise = lambda value: max(0, min(255, value + randint(-20, 20)))
img = Image.open('test.png').convert('HSV')
img.putdata([(add_noise(h), s, v) for h, s, v in img.getdata()])
img.convert('RGB').save('test.png')
Dessin
from PIL import ImageDraw
<ImageDraw> = ImageDraw.Draw(<Image>)
<ImageDraw>.point((x, y), fill=None)
<ImageDraw>.line((x1, y1, x2, y2 [, ...]), fill=None, width=0, joint=None) 
<ImageDraw>.arc((x1, y1, x2, y2), from_deg, to_deg, fill=None, width=0)
<ImageDraw>.rectangle((x1, y1, x2, y2), fill=None, outline=None, width=0)
<ImageDraw>.polygon((x1, y1, x2, y2 [, ...]), fill=None, outline=None)
<ImageDraw>.ellipse((x1, y1, x2, y2), fill=None, outline=None, width=0)
Utilisez 'fill=<color>'pour définir la couleur primaire.
Utilisez 'outline=<color>'pour définir la couleur secondaire.
La couleur peut être spécifiée sous la forme d'un tuple, d'un entier, d' '#rrggbb'une chaîne ou d'un nom de couleur.
Animation
Crée Un GIF D'une Balle Qui Rebondit :
# $ pip3 install pillow imageio
from PIL import Image, ImageDraw
import imageio
WIDTH, R = 126, 10
frames = []
for velocity in range(15):
    y = sum(range(velocity+1))
    frame = Image.new('L', (WIDTH, WIDTH))
    draw  = ImageDraw.Draw(frame)
    draw.ellipse((WIDTH/2-R, y, WIDTH/2+R, y+R*2), fill='white')
    frames.append(frame)
frames += reversed(frames[1:-1])
imageio.mimsave('test.gif', frames, duration=0.03)
L'audio
import wave
<Wave_read>  = wave.open('<path>', 'rb')        # Opens the WAV file.
framerate    = <Wave_read>.getframerate()       # Number of frames per second.
nchannels    = <Wave_read>.getnchannels()       # Number of samples per frame.
sampwidth    = <Wave_read>.getsampwidth()       # Sample size in bytes.
nframes      = <Wave_read>.getnframes()         # Number of frames.
<params>     = <Wave_read>.getparams()          # Immutable collection of above.
<bytes>      = <Wave_read>.readframes(nframes)  # Returns next 'nframes' frames.
<Wave_write> = wave.open('<path>', 'wb')        # Truncates existing file.
<Wave_write>.setframerate(<int>)                # 44100 for CD, 48000 for video.
<Wave_write>.setnchannels(<int>)                # 1 for mono, 2 for stereo.
<Wave_write>.setsampwidth(<int>)                # 2 for CD quality sound.
<Wave_write>.setparams(<params>)                # Sets all parameters.
<Wave_write>.writeframes(<bytes>)               # Appends frames to the file.
L'objet Bytes contient une séquence de trames, chacune constituée d'un ou plusieurs échantillons.
Dans un signal stéréo, le premier échantillon d'une trame appartient au canal gauche.
Chaque échantillon est constitué d'un ou plusieurs octets qui, convertis en nombre entier, indiquent le déplacement d'une membrane de haut-parleur à un instant donné.
Si la largeur de l'échantillon est un, alors l'entier doit être codé sans signe.
Pour toutes les autres tailles, l'entier doit être codé signé avec l'ordre des octets petit boutien.
Exemples De Valeurs
+-----------+-------------+------+-------------+
| sampwidth |     min     | zero |     max     |
+-----------+-------------+------+-------------+
|     1     |           0 |  128 |         255 |
|     2     |      -32768 |    0 |       32767 |
|     3     |    -8388608 |    0 |     8388607 |
|     4     | -2147483648 |    0 |  2147483647 |
+-----------+-------------+------+-------------+
Lire Des Échantillons Flottants À Partir D'un Fichier WAV
def read_wav_file(filename):
    def get_int(a_bytes):
        an_int = int.from_bytes(a_bytes, 'little', signed=width!=1)
        return an_int - 128 * (width == 1)
    with wave.open(filename, 'rb') as file:
        width  = file.getsampwidth()
        frames = file.readframes(-1)
    byte_samples = (frames[i: i + width] for i in range(0, len(frames), width))
    return [get_int(b) / pow(2, width * 8 - 1) for b in byte_samples]
Écrire Des Échantillons Flottants Dans Un Fichier WAV
def write_to_wav_file(filename, float_samples, nchannels=1, sampwidth=2, framerate=44100):
    def get_bytes(a_float):
        a_float = max(-1, min(1 - 2e-16, a_float))
        a_float += sampwidth == 1
        a_float *= pow(2, sampwidth * 8 - 1)
        return int(a_float).to_bytes(sampwidth, 'little', signed=sampwidth!=1) 
    with wave.open(filename, 'wb') as file:
        file.setnchannels(nchannels)
        file.setsampwidth(sampwidth)
        file.setframerate(framerate)
        file.writeframes(b''.join(get_bytes(f) for f in float_samples))
Exemples
Enregistre Une Onde Sinusoïdale Dans Un Fichier WAV Mono :
from math import pi, sin
samples_f = (sin(i * 2 * pi * 440 / 44100) for i in range(100000))
write_to_wav_file('test.wav', samples_f)
Ajoute Du Bruit À Un Fichier WAV Mono :
from random import random
add_noise = lambda value: value + (random() - 0.5) * 0.03
samples_f = (add_noise(f) for f in read_wav_file('test.wav'))
write_to_wav_file('test.wav', samples_f)
Lit Un Fichier WAV :
# $ pip3 install simpleaudio
from simpleaudio import play_buffer
with wave.open('test.wav', 'rb') as file:
    p = file.getparams()
    frames = file.readframes(-1)
    play_buffer(frames, p.nchannels, p.sampwidth, p.framerate)
Texte Pour Parler
# $ pip3 install pyttsx3
import pyttsx3
engine = pyttsx3.init()
engine.say('Sally sells seashells by the seashore.')
engine.runAndWait()
Synthétiseur
Joue Popcorn De Gershon Kingsley :
# $ pip3 install simpleaudio
import simpleaudio, math, struct
from itertools import chain, repeat
F  = 44100
P1 = '71♪,69,,71♪,66,,62♪,66,,59♪,,,'
P2 = '71♪,73,,74♪,73,,74,,71,,73♪,71,,73,,69,,71♪,69,,71,,67,,71♪,,,'
get_pause   = lambda seconds: repeat(0, int(seconds * F))
sin_f       = lambda i, hz: math.sin(i * 2 * math.pi * hz / F)
get_wave    = lambda hz, seconds: (sin_f(i, hz) for i in range(int(seconds * F)))
get_hz      = lambda key: 8.176 * 2 ** (int(key) / 12)
parse_note  = lambda note: (get_hz(note[:2]), 0.25 if '♪' in note else 0.125)
get_samples = lambda note: get_wave(*parse_note(note)) if note else get_pause(0.125)
samples_f   = chain.from_iterable(get_samples(n) for n in f'{P1}{P1}{P2}'.split(','))
samples_b   = b''.join(struct.pack('<h', int(f * 30000)) for f in samples_f)
simpleaudio.play_buffer(samples_b, 1, 2, F)
Pygame
Exemple De Base
# $ pip3 install pygame
import pygame as pg
pg.init()
screen = pg.display.set_mode((500, 500))
rect = pg.Rect(240, 240, 20, 20)
while all(event.type != pg.QUIT for event in pg.event.get()):
    deltas = {pg.K_UP: (0, -3), pg.K_RIGHT: (3, 0), pg.K_DOWN: (0, 3), pg.K_LEFT: (-3, 0)}
    for delta in (deltas.get(i) for i, on in enumerate(pg.key.get_pressed()) if on):
        rect = rect.move(delta) if delta else rect
    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (255, 255, 255), rect)
    pg.display.flip()
Rectangle
Objet pour stocker des coordonnées rectangulaires.

<Rect> = pg.Rect(x, y, width, height)           # X and y are coordinates of topleft corner.
<int>  = <Rect>.x/y/centerx/centery/…           # Top, right, bottom, left.
<tup.> = <Rect>.topleft/center/…                # Topright, bottomright, bottomleft.
<Rect> = <Rect>.move((x, y))                    # Use move_ip() to move in place.
<bool> = <Rect>.collidepoint((x, y))            # Tests if a point is inside a rectangle.
<bool> = <Rect>.colliderect(<Rect>)             # Tests if two rectangles overlap.
<int>  = <Rect>.collidelist(<list_of_Rect>)     # Returns index of first colliding Rect or -1.
<list> = <Rect>.collidelistall(<list_of_Rect>)  # Returns indexes of all colliding Rects.
Surface
Objet de représentation d'images.

<Surf> = pg.display.set_mode((width, height))   # Returns the display surface.
<Surf> = pg.Surface((width, height))            # Creates a new surface.
<Surf> = pg.image.load('<path>')                # Loads the image.
<Surf> = <Surf>.subsurface(<Rect>)              # Returns a subsurface.
<Surf>.fill(color)                              # Fills the whole surface.
<Surf>.set_at((x, y), color)                    # Updates pixel.
<Surf>.blit(<Surface>, (x, y))                  # Draws passed surface to the surface.
<Surf> = pg.transform.flip(<Surf>, xbool, ybool)
<Surf> = pg.transform.rotate(<Surf>, degrees)
<Surf> = pg.transform.scale(<Surf>, (width, height))
pg.draw.line(<Surf>, color, (x1, y1), (x2, y2), width)
pg.draw.arc(<Surf>, color, <Rect>, from_radians, to_radians)
pg.draw.rect(<Surf>, color, <Rect>)
pg.draw.polygon(<Surf>, color, points)
pg.draw.ellipse(<Surf>, color, <Rect>)
Police De Caractère
<Font> = pg.font.SysFont('<name>', size, bold=False, italic=False)
<Font> = pg.font.Font('<path>', size)
<Surf> = <Font>.render(text, antialias, color [, background])
Du Son
<Sound> = pg.mixer.Sound('<path>')              # Loads the WAV file.
<Sound>.play()                                  # Starts playing the sound.
Exemple De Base De Mario Brothers
import collections, dataclasses, enum, io, pygame, urllib.request, itertools as it
from random import randint

P = collections.namedtuple('P', 'x y')          # Position
D = enum.Enum('D', 'n e s w')                   # Direction
SIZE, MAX_SPEED = 50, P(5, 10)                  # Screen size, Speed limit

def main():
    def get_screen():
        pygame.init()
        return pygame.display.set_mode(2 * [SIZE*16])
    def get_images():
        url = 'https://gto76.github.io/python-cheatsheet/web/mario_bros.png'
        img = pygame.image.load(io.BytesIO(urllib.request.urlopen(url).read()))
        return [img.subsurface(get_rect(x, 0)) for x in range(img.get_width() // 16)]
    def get_mario():
        Mario = dataclasses.make_dataclass('Mario', 'rect spd facing_left frame_cycle'.split())
        return Mario(get_rect(1, 1), P(0, 0), False, it.cycle(range(3)))
    def get_tiles():
        positions = [p for p in it.product(range(SIZE), repeat=2) if {*p} & {0, SIZE-1}] + \
            [(randint(1, SIZE-2), randint(2, SIZE-2)) for _ in range(SIZE**2 // 10)]
        return [get_rect(*p) for p in positions]
    def get_rect(x, y):
        return pygame.Rect(x*16, y*16, 16, 16)
    run(get_screen(), get_images(), get_mario(), get_tiles())

def run(screen, images, mario, tiles):
    clock = pygame.time.Clock()
    while all(event.type != pygame.QUIT for event in pygame.event.get()):
        keys = {pygame.K_UP: D.n, pygame.K_RIGHT: D.e, pygame.K_DOWN: D.s, pygame.K_LEFT: D.w}
        pressed = {keys.get(i) for i, on in enumerate(pygame.key.get_pressed()) if on}
        update_speed(mario, tiles, pressed)
        update_position(mario, tiles)
        draw(screen, images, mario, tiles, pressed)
        clock.tick(28)

def update_speed(mario, tiles, pressed):
    x, y = mario.spd
    x += 2 * ((D.e in pressed) - (D.w in pressed))
    x -= x // abs(x) if x else 0
    y += 1 if D.s not in get_boundaries(mario.rect, tiles) else (D.n in pressed) * -10
    mario.spd = P(*[max(-limit, min(limit, s)) for limit, s in zip(MAX_SPEED, P(x, y))])

def update_position(mario, tiles):
    new_p = mario.rect.topleft
    larger_speed = max(abs(s) for s in mario.spd)
    for _ in range(larger_speed):
        mario.spd = stop_on_collision(mario.spd, get_boundaries(mario.rect, tiles))
        new_p = P(*[a + s/larger_speed for a, s in zip(new_p, mario.spd)])
        mario.rect.topleft = new_p

def get_boundaries(rect, tiles):
    deltas = {D.n: P(0, -1), D.e: P(1, 0), D.s: P(0, 1), D.w: P(-1, 0)}
    return {d for d, delta in deltas.items() if rect.move(delta).collidelist(tiles) != -1}

def stop_on_collision(spd, bounds):
    return P(x=0 if (D.w in bounds and spd.x < 0) or (D.e in bounds and spd.x > 0) else spd.x,
             y=0 if (D.n in bounds and spd.y < 0) or (D.s in bounds and spd.y > 0) else spd.y)

def draw(screen, images, mario, tiles, pressed):
    def get_frame_index():
        if D.s not in get_boundaries(mario.rect, tiles):
            return 4
        return next(mario.frame_cycle) if {D.w, D.e} & pressed else 6
    screen.fill((85, 168, 255))
    mario.facing_left = (D.w in pressed) if {D.w, D.e} & pressed else mario.facing_left
    screen.blit(images[get_frame_index() + mario.facing_left * 9], mario.rect)
    for rect in tiles:
        screen.blit(images[18 if {*rect.topleft} & {0, (SIZE-1)*16} else 19], rect)
    pygame.display.flip()

if __name__ == '__main__':
    main()
Pandas
# $ pip3 install pandas
import pandas as pd
from pandas import Series, DataFrame
Série
Dictionnaire ordonné avec un nom.

>>> Series([1, 2], index=['x', 'y'], name='a')
x    1
y    2
Name: a, dtype: int64
<Sr> = Series(<list>)                         # Assigns RangeIndex starting at 0.
<Sr> = Series(<dict>)                         # Takes dictionary's keys for index.
<Sr> = Series(<dict/Series>, index=<list>)    # Only keeps items with keys specified in index.
<el> = <Sr>.loc[key]                          # Or: <Sr>.iloc[index]
<Sr> = <Sr>.loc[keys]                         # Or: <Sr>.iloc[indexes]
<Sr> = <Sr>.loc[from_key : to_key_inclusive]  # Or: <Sr>.iloc[from_i : to_i_exclusive]
<el> = <Sr>[key/index]                        # Or: <Sr>.key
<Sr> = <Sr>[keys/indexes]                     # Or: <Sr>[<key_range/range>]
<Sr> = <Sr>[bools]                            # Or: <Sr>.i/loc[bools]
<Sr> = <Sr> ><== <el/Sr>                      # Returns a Series of bools.
<Sr> = <Sr> +-*/ <el/Sr>                      # Non-matching keys get value NaN.
<Sr> = <Sr>.append(<Sr>)                      # Or: pd.concat(<coll_of_Sr>)
<Sr> = <Sr>.combine_first(<Sr>)               # Adds items that are not yet present.
<Sr>.update(<Sr>)                             # Updates items that are already present.
Agréger, Transformer, Mapper :
<el> = <Sr>.sum/max/mean/idxmax/all()         # Or: <Sr>.aggregate(<agg_func>)
<Sr> = <Sr>.rank/diff/cumsum/ffill/interpl()  # Or: <Sr>.agg/transform(<trans_func>)
<Sr> = <Sr>.fillna(<el>)                      # Or: <Sr>.apply/agg/transform/map(<map_func>)
La façon 'aggregate()'de 'transform()'savoir si une fonction accepte un élément ou toute la série consiste à lui transmettre d'abord une valeur unique et si elle génère une erreur, elle lui transmet alors toute la série.
>>> sr = Series([1, 2], index=['x', 'y'])
x    1
y    2
+-------------+-------------+-------------+---------------+
|             |    'sum'    |   ['sum']   | {'s': 'sum'}  |
+-------------+-------------+-------------+---------------+
| sr.apply(…) |      3      |    sum  3   |     s  3      |
| sr.agg(…)   |             |             |               |
+-------------+-------------+-------------+---------------+
+-------------+-------------+-------------+---------------+
|             |    'rank'   |   ['rank']  | {'r': 'rank'} |
+-------------+-------------+-------------+---------------+
| sr.apply(…) |             |      rank   |               |
| sr.agg(…)   |     x  1    |   x     1   |    r  x  1    |
| sr.trans(…) |     y  2    |   y     2   |       y  2    |
+-------------+-------------+-------------+---------------+
Le dernier résultat a un index hiérarchique. Utilisez '<Sr>[key_1, key_2]'pour obtenir ses valeurs.
Trame De Données
Tableau avec des lignes et des colonnes étiquetées.

>>> DataFrame([[1, 2], [3, 4]], index=['a', 'b'], columns=['x', 'y'])
   x  y
a  1  2
b  3  4
<DF>    = DataFrame(<list_of_rows>)           # Rows can be either lists, dicts or series.
<DF>    = DataFrame(<dict_of_columns>)        # Columns can be either lists, dicts or series.
<el>    = <DF>.loc[row_key, column_key]       # Or: <DF>.iloc[row_index, column_index]
<Sr/DF> = <DF>.loc[row_key/s]                 # Or: <DF>.iloc[row_index/es]
<Sr/DF> = <DF>.loc[:, column_key/s]           # Or: <DF>.iloc[:, column_index/es]
<DF>    = <DF>.loc[row_bools, column_bools]   # Or: <DF>.iloc[row_bools, column_bools]
<Sr/DF> = <DF>[column_key/s]                  # Or: <DF>.column_key
<DF>    = <DF>[row_bools]                     # Keeps rows as specified by bools.
<DF>    = <DF>[<DF_of_bools>]                 # Assigns NaN to False values.
<DF>    = <DF> ><== <el/Sr/DF>                # Returns DataFrame of bools.
<DF>    = <DF> +-*/ <el/Sr/DF>                # Non-matching keys get value NaN.
<DF>    = <DF>.set_index(column_key)          # Replaces row keys with values from a column.
<DF>    = <DF>.reset_index()                  # Moves row keys to their own column.
<DF>    = <DF>.filter('<regex>', axis=1)      # Only keeps columns whose key matches the regex.
<DF>    = <DF>.melt(id_vars=column_key/s)     # Converts DF from wide to long format.
Fusionner, Joindre, Concat :
>>> l = DataFrame([[1, 2], [3, 4]], index=['a', 'b'], columns=['x', 'y'])
   x  y 
a  1  2 
b  3  4 
>>> r = DataFrame([[4, 5], [6, 7]], index=['b', 'c'], columns=['y', 'z'])
   y  z
b  4  5
c  6  7
+------------------------+---------------+------------+------------+--------------------------+
|        how/join        |    'outer'    |   'inner'  |   'left'   |       description        |
+------------------------+---------------+------------+------------+--------------------------+
| l.merge(r, on='y',     |    x   y   z  | x   y   z  | x   y   z  | Joins/merges on column.  |
|            how=…)      | 0  1   2   .  | 3   4   5  | 1   2   .  | Also accepts left_on and |
|                        | 1  3   4   5  |            | 3   4   5  | right_on parameters.     |
|                        | 2  .   6   7  |            |            | Uses 'inner' by default. |
+------------------------+---------------+------------+------------+--------------------------+
| l.join(r, lsuffix='l', |    x yl yr  z |            | x yl yr  z | Joins/merges on row keys.|
|           rsuffix='r', | a  1  2  .  . | x yl yr  z | 1  2  .  . | Uses 'left' by default.  |
|           how=…)       | b  3  4  4  5 | 3  4  4  5 | 3  4  4  5 |                          |
|                        | c  .  .  6  7 |            |            |                          |
+------------------------+---------------+------------+------------+--------------------------+
| pd.concat([l, r],      |    x   y   z  |     y      |            | Adds rows at the bottom. |
|           axis=0,      | a  1   2   .  |     2      |            | Uses 'outer' by default. |
|           join=…)      | b  3   4   .  |     4      |            | By default works the     |
|                        | b  .   4   5  |     4      |            | same as `l.append(r)`.   |
|                        | c  .   6   7  |     6      |            |                          |
+------------------------+---------------+------------+------------+--------------------------+
| pd.concat([l, r],      |    x  y  y  z |            |            | Adds columns at the      |
|           axis=1,      | a  1  2  .  . | x  y  y  z |            | right end.               |
|           join=…)      | b  3  4  4  5 | 3  4  4  5 |            | Uses 'outer' by default. |
|                        | c  .  .  6  7 |            |            |                          |
+------------------------+---------------+------------+------------+--------------------------+
| l.combine_first(r)     |    x   y   z  |            |            | Adds missing rows and    |
|                        | a  1   2   .  |            |            | columns.                 |
|                        | b  3   4   5  |            |            |                          |
|                        | c  .   6   7  |            |            |                          |
+------------------------+---------------+------------+------------+--------------------------+
Agréger, Transformer, Mapper :
<Sr> = <DF>.sum/max/mean/idxmax/all()         # Or: <DF>.apply/agg/transform(<agg_func>)
<DF> = <DF>.rank/diff/cumsum/ffill/interpl()  # Or: <DF>.apply/agg/transform(<trans_func>)
<DF> = <DF>.fillna(<el>)                      # Or: <DF>.applymap(<map_func>)
Toutes les opérations fonctionnent sur les colonnes par défaut. Utilisez 'axis=1'le paramètre pour traiter les lignes à la place.
>>> df = DataFrame([[1, 2], [3, 4]], index=['a', 'b'], columns=['x', 'y'])
   x  y
a  1  2
b  3  4
+-------------+-------------+-------------+---------------+
|             |    'sum'    |   ['sum']   | {'x': 'sum'}  |
+-------------+-------------+-------------+---------------+
| df.apply(…) |             |       x  y  |               |
| df.agg(…)   |     x  4    |  sum  4  6  |     x  4      |
|             |     y  6    |             |               |
+-------------+-------------+-------------+---------------+
+-------------+-------------+-------------+---------------+
|             |    'rank'   |   ['rank']  | {'x': 'rank'} |
+-------------+-------------+-------------+---------------+
| df.apply(…) |      x  y   |      x    y |        x      |
| df.agg(…)   |   a  1  1   |   rank rank |     a  1      |
| df.trans(…) |   b  2  2   | a    1    1 |     b  2      |
|             |             | b    2    2 |               |
+-------------+-------------+-------------+---------------+
Utilisez '<DF>[col_key_1, col_key_2][row_key]'pour obtenir les valeurs du cinquième résultat.
Encoder, Décoder :
<DF> = pd.read_json/html('<str/path/url>')
<DF> = pd.read_csv/pickle/excel('<path/url>')
<DF> = pd.read_sql('<query>', <connection>)
<DF> = pd.read_clipboard()
<dict> = <DF>.to_dict(['d/l/s/sp/r/i'])
<str>  = <DF>.to_json/html/csv/markdown/latex([<path>])
<DF>.to_pickle/excel(<path>)
<DF>.to_sql('<table_name>', <connection>)
Par Groupe
Objet qui regroupe les lignes d'un dataframe en fonction de la valeur de la colonne passée.

>>> df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 6]], index=list('abc'), columns=list('xyz'))
>>> df.groupby('z').get_group(3)
   x  y
a  1  2
>>> df.groupby('z').get_group(6)
   x  y
b  4  5
c  7  8
<GB> = <DF>.groupby(column_key/s)             # DF is split into groups based on passed column.
<DF> = <GB>.get_group(group_key)              # Selects a group by value of grouping column.
Agréger, Transformer, Mapper :
<DF> = <GB>.sum/max/mean/idxmax/all()         # Or: <GB>.apply/agg(<agg_func>)
<DF> = <GB>.rank/diff/cumsum/ffill()          # Or: <GB>.aggregate(<trans_func>)  
<DF> = <GB>.fillna(<el>)                      # Or: <GB>.transform(<map_func>)
>>> gb = df.groupby('z')
      x  y  z
3: a  1  2  3
6: b  4  5  6
   c  7  8  6
+-------------+-------------+-------------+-------------+---------------+
|             |    'sum'    |    'rank'   |   ['rank']  | {'x': 'rank'} |
+-------------+-------------+-------------+-------------+---------------+
| gb.agg(…)   |      x   y  |      x  y   |      x    y |        x      |
|             |  z          |   a  1  1   |   rank rank |     a  1      |
|             |  3   1   2  |   b  1  1   | a    1    1 |     b  1      |
|             |  6  11  13  |   c  2  2   | b    1    1 |     c  2      |
|             |             |             | c    2    2 |               |
+-------------+-------------+-------------+-------------+---------------+
| gb.trans(…) |      x   y  |      x  y   |             |               |
|             |  a   1   2  |   a  1  1   |             |               |
|             |  b  11  13  |   b  1  1   |             |               |
|             |  c  11  13  |   c  1  1   |             |               |
+-------------+-------------+-------------+-------------+---------------+
Roulant
Objet pour les calculs de fenêtre glissante.

<R_Sr/R_DF/R_GB> = <Sr/DF/GB>.rolling(window_size)  # Also: `min_periods=None, center=False`.
<R_Sr/R_DF>      = <R_DF/R_GB>[column_key/s]        # Or: <R>.column_key
<Sr/DF/DF>       = <R_Sr/R_DF/R_GB>.sum/max/mean()  # Or: <R>.apply/agg(<agg_func/str>)
Comploter
Décès De Covid Par Continent
Morts du covid
# $ pip3 install pandas plotly
import pandas as pd
import plotly.express

covid = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', 
                    usecols=['iso_code', 'date', 'total_deaths', 'population'])
continents = pd.read_csv('https://datahub.io/JohnSnowLabs/country-and-continent-codes-' + \
                         'list/r/country-and-continent-codes-list-csv.csv',
                         usecols=['Three_Letter_Country_Code', 'Continent_Name'])
df = pd.merge(covid, continents, left_on='iso_code', right_on='Three_Letter_Country_Code')
df = df.groupby(['Continent_Name', 'date']).sum().reset_index()
df['Total Deaths per Million'] = df.total_deaths * 1e6 / df.population
df = df[('2020-03-14' < df.date) & (df.date < '2020-06-25')]
df = df.rename({'date': 'Date', 'Continent_Name': 'Continent'}, axis='columns')
plotly.express.line(df, x='Date', y='Total Deaths per Million', color='Continent').show()
Cas Confirmés De Covid, Prix Du Dow Jones, De L'or Et Du Bitcoin
Cas de covid
# $ pip3 install pandas plotly
import pandas, datetime
import plotly.graph_objects as go

def main():
    display_data(wrangle_data(*scrape_data()))

def scrape_data():
    def scrape_yahoo(id_):
        BASE_URL = 'https://query1.finance.yahoo.com/v7/finance/download/'
        now  = int(datetime.datetime.now().timestamp())
        url  = f'{BASE_URL}{id_}?period1=1579651200&period2={now}&interval=1d&events=history'
        return pandas.read_csv(url, usecols=['Date', 'Close']).set_index('Date').Close 
    covid = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', 
                        usecols=['date', 'total_cases'])
    covid = covid.groupby('date').sum()
    dow, gold, bitcoin = [scrape_yahoo(id_) for id_ in ('^DJI', 'GC=F', 'BTC-USD')]
    dow.name, gold.name, bitcoin.name = 'Dow Jones', 'Gold', 'Bitcoin'
    return covid, dow, gold, bitcoin

def wrangle_data(covid, dow, gold, bitcoin):
    df = pandas.concat([covid, dow, gold, bitcoin], axis=1)
    df = df.loc['2020-02-23':].iloc[:-2]
    df = df.interpolate()
    df.iloc[:, 1:] = df.rolling(10, min_periods=1, center=True).mean().iloc[:, 1:]
    df.iloc[:, 1:] = df.iloc[:, 1:] / df.iloc[0, 1:] * 100
    return df

def display_data(df):
    def get_trace(col_name):
        return go.Scatter(x=df.index, y=df[col_name], name=col_name, yaxis='y2')
    traces = [get_trace(col_name) for col_name in df.columns[1:]]
    traces.append(go.Scatter(x=df.index, y=df.total_cases, name='Total Cases', yaxis='y1'))
    figure = go.Figure()
    figure.add_traces(traces)
    figure.update_layout(
        yaxis1=dict(title='Total Cases', rangemode='tozero'),
        yaxis2=dict(title='%', rangemode='tozero', overlaying='y', side='right'),
        legend=dict(x=1.1)
    ).show()

if __name__ == '__main__':
    main()
Cyton
Bibliothèque qui compile le code Python en C.

# $ pip3 install cython
import pyximport; pyximport.install()
import <cython_script>
<cython_script>.main()
Définitions
Toutes les 'cdef'définitions sont facultatives, mais elles contribuent à l'accélération.
Le script doit être enregistré avec une 'pyx'extension.
cdef <type> <var_name> = <el>
cdef <type>[n_elements] <var_name> = [<el_1>, <el_2>, ...]
cdef <type/void> <func_name>(<type> <arg_name_1>, ...):
cdef class <class_name>:
    cdef public <type> <attr_name>
    def __init__(self, <type> <arg_name>):
        self.<attr_name> = <arg_name>
cdef enum <enum_name>: <member_name_1>, <member_name_2>, ...
Annexe
PyInstaller
$ pip3 install pyinstaller
$ pyinstaller script.py                        # Compiles into './dist/script' directory.
$ pyinstaller script.py --onefile              # Compiles into './dist/script' console app.
$ pyinstaller script.py --windowed             # Compiles into './dist/script' windowed app.
$ pyinstaller script.py --add-data '<path>:.'  # Adds file to the root of the executable.
Les chemins d'accès aux fichiers doivent être mis à jour en 'os.path.join(sys._MEIPASS, <path>)'.
Modèle De Script De Base
#!/usr/bin/env python3
#
# Usage: .py
#

from collections import namedtuple
from dataclasses import make_dataclass
from enum import Enum
from sys import argv
import re


def main():
    pass


###
##  UTIL
#

def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()


if __name__ == '__main__':
    main()