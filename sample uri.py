with open('file.txt') as fa:
    for line_aa in fa.readlines()[3:11]:
        line_aa = line_aa.strip()
        print
        line_aa
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = line_aa.split('\t', 9)