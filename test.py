import tpandas as td
# 引入此模板可以不再引入pandas
# 实例
table = td.DataFrame([1,2,3],[1,3],[1],name = ['contents2','contents3','contents4'])

#设置索引 不出现多余列，设不设看自己情况
table.set_index('contents3',inplace=True)

# 如果保存中文出乱码可以加上编码utf-8-sig
table.to_excel('2.xlsx',encoding='utf-8-sig')
table.to_csv('2.csv',encoding='utf-8-sig')

# 读取更加简单只需要一个路径名即可，默认表单为1，编码为utf8，可以使用sheet_name与encoding更改
df =td.read_excel(r'2.xlsx')
q = td.tolist(df.contents3)
print('excel is ',q)
#同上，返回值为列表
df = td.read_csv(r'2.csv')
q= td.tolist(df.contents2,df.contents3)
print('csv is ',q)
#
# 一个文件添加多个表单，注意已经写入数据的文件会被重写
DF1 = td.DataFrame([1,2,3],['4','5'],name = ['contents2','contents3'])
DF2 = td.DataFrame([11,22,33],['44','55'],name = ['contents2','contents3'])
DF1.set_index('contents3',inplace=True)
DF2.set_index('contents3',inplace=True)

td.add_sheet(r'3.xlsx',DF1,DF2,sheet_name=['col1','col2'])






















