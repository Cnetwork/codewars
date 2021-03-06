#!/usr/bin/python
#-*- coding:utf-8 -*-

# for 022
import chardet
# for 023
import copy
# for 025
import re

print 'Let\'s Say : '
print "'Hello World'"
print '"Hello world"'
print 'string1 + ',"String2 + " "'string3'"

print u"""Multilines
can be written
using three \"\"\"
"""

print 'C:\nowhere'
print 'C:\\nowhere'
print r'C:\nowhere'

print r'"<r>" means origin string and its \' useful for the \' '
print r'Let' '\'s ' r'go(Use combine)'

print u"The default for Python 2 is ASCII(for Python 3 it's utf-8)."
print u"This just effect how the interpreter reads the characters in the file."
print u"When you declare a string with a u in front, like u'This is a string', it tells the Python compiler that the string is Unicode, not bytes. The most different is that you can no embed unicode in the string(that is, u'\u2664' is now legal, you can use from __future__ import unicode literals to make it default."
print b'\u2665' u'\u2665'

string_1_utf8 = "Flügel"
print string_1_utf8
print "If no coding:utf-8 there is an error because ASCII has no ü"
print "u'' means this is a unicode string"

string_2_unicode = string_1_utf8.decode('utf-8')
print u"other_encode.decode('other_type') means turn the other string which use other type into the unicode"
print string_2_unicode

string_3_latin = string_2_unicode.encode('latin_1')
print u"unicode_string.encode('other') means turn unicode string into other encoding such as utf-8 or latin_1" 
print string_3_latin

string_3_chinese = '字瀛'
print "string_3_chinese : ",string_3_chinese

string_4_unicode = u'字å­å字瀛'
print "string_4_unicode",string_4_unicode

string_5_utf8 = string_4_unicode.encode('utf-8')
print "string_5_utf8",string_5_utf8

list_1_null = []

def whatisthis(s):
    if isinstance(s,str):
        print "Ordinary string : ", chardet.detect(s)
    elif isinstance(s,unicode):
        print "Unicode string, chardet Expected a bytes object, not a unicode object"
    else:
        print "Not a string : ",chardet.detect(s)

def whatisthis_2(s):
    if type(s).__name__ != 'unicode':
        print chardet.detect(s)
    else: print "unicode"

whatisthis(string_4_unicode)
whatisthis(string_5_utf8)
whatisthis(string_3_chinese)
whatisthis(string_3_latin)
whatisthis(list_1_null)

whatisthis_2(string_4_unicode)
whatisthis_2(string_5_utf8)
whatisthis_2(string_3_chinese)
whatisthis_2(string_3_latin)
whatisthis_2(list_1_null)
print "type can determin is unicode or string"
print "type(str).__name__ : ",type(string_2_unicode).__name__
print "type(str).__name__ : ",type(string_3_chinese).__name__

string_6 = "This is a string!"
a = str(string_6)
b = string_6[:]
c = string_6 + ""
d = copy.copy(string_6)
e = string_6
f = (string_6 + '.')[:-1]
print map(id,[string_6, a, b, c, d, e, f])
string_6 = "this is a new string!"
print map(id,[string_6, a, b, c, d, e, f])

print string_6[:6]*2
print 2*string_6
print "markline"
print ' '.join((string_6[:]) * 2)
print " ".join([string_6[:]] * 2)

print string_4_unicode
print "String Length : " + str(len(string_4_unicode))

list_2_s4u = list(string_4_unicode)
print len(list_2_s4u)

tuple_1_s4u = tuple(string_4_unicode)
tuple_2_l2s = tuple(list_2_s4u)

print "+ means connect but , not connect just print in turn"
print "tuple_1_s4u : ",tuple_1_s4u,len(tuple_1_s4u)
print "tuple_2_l2s : " ,tuple_2_l2s,len(tuple_2_l2s)


set_1_s4u = set(string_4_unicode)
set_2_l2s = set(list_2_s4u)
set_3_t1s = set(tuple_1_s4u)
print set_1_s4u
print set_2_l2s
print set_3_t1s

string_7 = "A1B2C3C3D4G5J88I9870897\n C1N200J1\n a1B2\n A10B\n"
pattern_1 = re.compile(r'([A-Z]\d+)+')

print "determine have pattern or not"
if pattern_1.match(string_7):
    print "matched"
else:
    print "not match"

string_8 = u'A1B2C3C3D4G5J88I9870897'
pattern_2 = re.compile('([A-Z]\d)+')

print "the first location of the pattern_2"
for m in re.finditer(pattern_2,string_7):
    print m.group()
print "the span of the pattern_2"
for m in pattern_2.finditer(string_7):
    print m.span(), m.start(), m.end(), m.group(), m.group(1),m.groups()

callable_iterator_object = pattern_2.finditer(string_7)
print callable_iterator_object
print list(callable_iterator_object)[2].group()


re_match_object = pattern_2.search(string_8)
print "only the first span [0,14)"
print re_match_object
print re_match_object.group(),re_match_object.span(),re_match_object.start(),re_match_object.end()

print "The last location of the pattern can use the finiter to create a new list and use the list[-1], just use the finditer"

print "Get more information"
print "use m.span(),m.start(),m.end(),m.group()"

print "One difference between finditer and findall is that former returns regex match objects wherears the other returns a tuple of the matched capturing groups"

print "Porcess the target lines"
f = open('/home/wsg/Code/python_project/268_skill/020_text_encoding.py') 
for line in f:
    print line
    print pattern_2.findall(line)
f.close()
