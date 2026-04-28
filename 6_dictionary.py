slang_dict = {"觉醒时刻":"1945",
              "yyds":"2025"}
slang_dict["疫情"] = "2019"
slang_dict["元宇宙"] = "2077"
slang_dict["毕业"] = "2027"
query = input("请输入你要查询的流行语：")
if query in slang_dict:
    print("你查询的"+query+"所在年份:")
    print(slang_dict[query])
else:
    print("你查询的流行语未收录")
    print("当前本词典获取的长度为："+str(len(slang_dict))+"条")
