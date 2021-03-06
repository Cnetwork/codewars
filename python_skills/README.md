## Welcome to the Python 268 skills
###019_literal.py
* 学会使用“”以及'',了解他们两个的搭配用法以及两者与转义字符的配合
* 使用u""" text """ 显示多行内容
* 学习前缀 u,r


###020_text_encoding.py
* 了解python文件开头的 -\*- coding: utf-8 -\*-的具体含义，意思为该文件会以utf-8的文本格式内容存储在机器硬盘中。文件默认会以ADCII的形式存储。注意这里和文件内部的print输出并没有什么直接关系。这是interpreter读取python文件的方式。 [link](http://stackoverflow.com/questions/3170211/why-declare-unicode-by-string-in-python)
* 字符串前面加 u 表示该字符串会以unicode编码形式存在


###021_trans_encoding.py | 021_trans_encoding2.py
* 设想以unicode为中心，进行 encode 和 decode 过程，举例来说一个 utf-8 格式的字符串想要编程unicode字符串，使用 utf8_string.decode('utf-8'), 如果一个unicode字符串想转化为 utf-8 格式，使用unicode_string.encode('utf-8')   [link](http://pythoncentral.io/python-unicode-encode-decode-strings-python-2x/)


###022_detect_charset.py
* 使用内置函数 isinstance() 来判断是否为  str/unicode/others
* 使用type(string).__name__ 来判断是否为 unicode/str/others
* 使用chardet.detect(s)可以判断字符最大可能属于哪一个编码 (pip install chardet)


###023_copy_string.py
* 使用str(), s[:], s+'', copy.copy(), =, 加入再删减的方法 [link](http://stackoverflow.com/questions/24804453/how-can-i-copy-a-python-string)

###024_repeat_string.py
* 使用num * str 或者 str * num 或者 join

###025_get_string_length.py
* len(list/tuple/set/dict) 内置函数

###026_search_string.py
```
import re
pattern = re.compile()
for m in re.finditer(pattern,str)
	print m.group()
print pattern.search(str).group()/span()
这里的finditer 和 search 返回的都是object 但是findall 返回的是一个list
```

###027_begginning_patterns.py
* 使用r'^hello' r'\Ahello' h或者 re.match

###028_single_match.py
* 使用 r'\w+'


###029_specific_encode_regex_match.py
* 如果要在匹配字符串中非ASCII的字段时候，需要使用特殊的字符串编码去进行匹配， 这时候需要将unicode字符串进行编码，在re中加入相应的编码flag，如 re.findall(r"\w", string_2.decode('utf-8),flags=re.U) [link](http://stackoverflow.com/questions/10165102/how-do-i-get-a-regular-%20expression-to-recognize-non-ascii-characters-as-letters)


###030_point_match_newline_break.py
* use re.DOTALL 如：re.match(r".", "\n", re.DOTALL) [link]("http://stackoverflow.com/questions/8150745/regular-expression-how-to-match-a-string-containing-n-newline")

###031_get_the_regex_remnant.py
* 一次性匹配完毕，按列表进行存储findall
* 使用sub去找匹配剩余部分， 再用剩余部分进行匹配

###032_count_single_wordString_frenquency.py
* 使用findall (返回的是列表)，直接使用len()判断长度
* 对于非正则表达式可以表示的字段，直接使用string.count即可

###033_count_frenquency.py
* 使用dict 以及 sorted()函数 按照unicode进行匹配，匹配之后的输出需要编码为utf-8

###034_compare_string.py
* ==即可判断字符串是否相等，但是要忽略文字序列，可以构建一个字典类Counter进行比较 [link](http://www.pythoner.com/205.html)


###035_blank_match.py
* r" "可以匹配空格，最好使用re进行正则表达式匹配。

###036_blank_line_match.py
* 空行可以包括/t/s/n等等，可以使用line.strip()删去段前段后的空白，判断是否为False 即 not line.strip()

###037_string_of_integer.py
* 判断str是否是字符串使用str.isdigit()
* 转化为Int 或者 float 使用内置函数 int() 和 float()

###038_Parse_string_float_or_int.py
* format(1234,'b/x/o') binary/hex/oct
* 在os.chmod中使用0644 与 int("0644", 8)具有同样的效果

###039_determine_capitalize.py
* 字符串或者字符统一判断使用 string.isupper()/islower()
* 可以使用r'[a-z]' r'[A-Z]' 匹配判断

###040_string_upper_capitalize.py
* 使用 string.upper()/lower()/swapcase()
* 每个单词首字母大写使用string.title(), 段落首字母大写使用string.capitalize()


###041_partition_of_string.py
* 使用string[i:j]来进行取得字符串片段，如果是其他字符编码，最好字符串采用u''进行初始化，才可以不出现打断情况


###042_partition_of_matched_regex.py
* re.match 从字符串开头进行匹配并只匹配一次
* re.search 对所有匹配项进行匹配
* re.findall 也是对所有匹配项进行匹配
* 这里需要再次进行确认，每一个函数的具体返回值以及匹配内容（？）

###043_per_post_string_with_regex.py
* 取出正则表达式之前或者之后的内容
*  re.compile(ur"(.\*)PATTERN(.\*)") 然后通过groups() 以及group(n)来查看相应内容


###044_regex_match_length.py
* 使用re.finditer可以返回一个iterator的集合，每一个iterator都包含着一个匹配项的 start(), end(), span()


###045_split_line_to_section.py
* split("\n")

###046_split_string_into_line.py
* 使用 string.splitlines()
* 还可以通过readline 并进行行处理存储到列表

###047_split_string_into_word.y
* 使用split(r"xxx")进行分割
* 使用re.split(pattern_1, string_1)


###048_regex_split_string.py
* 使用 re.compile(r"pattern").split(string) 同047

###049_each_elem_of_string.py
* 将string 转化为List,再一一进行处理


###050_each_elem_as_number.py
* 将char 转化为 number使用ord(char)
* 将number转为 char 使用chr(number)
* 将number转化为unicode的char 使用unichr(number)


###051_combine_stirngs.py
* 使用str1+str2 str1,str2两种方法

###052_replace_part_of_string.py
* 使用re.sub进行字符串内容替换


###053_deal_with_caret_notation.py
* re中使用r"" +（） + \\1可以进行匹配内容抽取


###054_delete_part_of_string
* 使用\1 替换\1+来达到删除重复的目的
* 使用lstrip(‘xxx’)删除左侧内容 rstrip 删除右侧内容, strip删除双端内容


###055_chomp_the_string_end.py


###056_delete_bank_around_the_string.py
* 使用strip(" ")


###057_space_tab_translate.py
* 使用re.sub去替换 tab 和space 
* 如: re.compile(ur" "*tabstop_num) 替换为\t

###058_change_indent_wtc.py
* 使用re.sub变更缩进


###059_NULL

###060_add_string_in_the_end.py
* 使用str1 += str2即可

###061_delete_part_of_the_string.py
* use a[4:] 与 re.sub 进行删除

###062_























