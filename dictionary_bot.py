import pandas

dict = pandas.read_excel('dic.xlsx', index_col='B')
# print(dict[0])
print(dict['abebe'])