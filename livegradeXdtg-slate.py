# 导入pandas库并将其重命名为pd
import pandas as pd
# 导入re模块，用于正则表达式操作
import re
# 导入argparse模块
import argparse





parser = argparse.ArgumentParser(description='指定输入文件路径')

# 添加命令行参数
parser.add_argument('-fs', '--slate_file', type=str, help='指定 slate 文件路径')
parser.add_argument('-fl', '--livegrade_file', type=str, help='指定 livegrade 文件路径')

# 解析命令行参数
args = parser.parse_args()

# 获取文件路径
slate_file = args.slate_file
livegrade_file = args.livegrade_file





# 指定输出文件
livegrade_convert = "~/.Script/livegrade_convert.csv"

# 指定输出文件的路径和文件名为”~/output.csv”
output_file = "~/Desktop/output.csv"





#定义一个输入函数和一个输出函数
def slate_csv(slate_file, slate_convert):
    # 读取CSV文件并将分隔符从;修改为,
    # 只保留指定的列名
    df = pd.read_csv(slate_file, delimiter=";", skiprows=[0, 1], usecols=["filenameBase", "scenes", "shot", "take", "tags"])
    
    # 重命名"filenameBase"列为"文件名"
    df.rename(columns={"filenameBase": "Name / Clip Identifier"}, inplace=True)
    
    # 重命名"scenes"列为"场"
    df.rename(columns={"scenes": "Scene"}, inplace=True)
    
    # 重命名"shot"列为"镜"
    df.rename(columns={"shot": "Shot"}, inplace=True)
    
    # 重命名"take"列为"次"
    df.rename(columns={"take": "Take"}, inplace=True)

    #将空值替换为哆啦Ahua
    df = df.fillna("nan")
    
    # 对"tags"列应用正则表达式，并只保留匹配到的"KEEP"、"NG"和"Circle"
    df["tags"] = df["tags"].apply(lambda x: ','.join(re.findall(r'\b(KEEP|nan|NG|Circle)\b', str(x))))
    
    # 过滤只包含匹配结果的数据行
    df = df[df["tags"].apply(lambda x: bool(x))]
    
    # 将DataFrame写入到新的CSV文件中
    df.to_csv(slate_convert, index=False)

# 指定输出文件
slate_convert = "~/.Script/slate_convert.csv"

# 调用slate_csv函数进行转换
slate_csv(slate_file, slate_convert)




#定义一个输入函数和一个输出函数
def livegrade_csv(livegrade_file, livegrade_convert):

    # 读取第二个CSV文件
    df = pd.read_csv(livegrade_file, usecols=["Name / Clip Identifier", "Scene", "Shot", "Take", "Rating"])
    
    # 将Rating列的值进行转换
    df["Rating"] = df["Rating"].map({3: "KEEP", 5: "Circle"})
    
    # 将DataFrame写入到输出文件中
    df.to_csv(livegrade_convert, index=False)

# 指定输出文件
livegrade_convert = "~/.Script/livegrade_convert.csv"

# 调用livegrade_csv函数处理第二个CSV文件
livegrade_csv(livegrade_file, livegrade_convert)





#读取slate_convert.csv
df_slate = pd.read_csv("~/.Script/slate_convert.csv")

# 读取livegrade_convert.csv
df_livegrade = pd.read_csv("~/.Script/livegrade_convert.csv")

#使用”Name / Clip Identifier”列进行外连接
df = pd.merge(df_slate, df_livegrade,  how="outer", on="Name / Clip Identifier")




# 对Scene_x列中所有以.0结尾的字符串进行删除操作
df['Scene_x'] = df['Scene_x'].astype(str).str.replace(r'\.0$', '', regex=True)
# 对Scene_y列中所有以.0结尾的字符串进行删除操作
df['Scene_y'] = df['Scene_y'].astype(str).str.replace(r'\.0$', '', regex=True)
# 对Shot_x列中所有以.0结尾的字符串进行删除操作
df['Shot_x'] = df['Shot_x'].astype(str).str.replace(r'\.0$', '', regex=True)
# 对Shot_y列中所有以.0结尾的字符串进行删除操作
df['Shot_y'] = df['Shot_y'].astype(str).str.replace(r'\.0$', '', regex=True)
# 对Take_x列中所有以.0结尾的字符串进行删除操作
df['Take_x'] = df['Take_x'].astype(str).str.replace(r'\.0$', '', regex=True)
# 对Take_y列中所有以.0结尾的字符串进行删除操作
df['Take_y'] = df['Take_y'].astype(str).str.replace(r'\.0$', '', regex=True)


# # #缺失值填充为”“空字符串
df = df.fillna("")

# 筛选tags列为空的行
# 筛选Scene_x列为空的行,筛选Scene_y列为空的行
# 筛选Shot_x列为空的行.筛选Shot_y列为空的行
# 筛选take_x列为空的行,筛选take_y列为空的行
# 筛选tags列与Rating列不相等的行
# 筛选Scene_x列与Scene_y列不相等的行
# 筛选take_x列与Take_y列不相等的行
df = df[(df["tags"] == "") | (df["Scene_x"] == "") | (df["Scene_y"] == "") | (df["Shot_x"] == "") | (df["Shot_y"] == "") | (df["Take_x"] == "")| (df["Take_y"] == "") | (df["tags"] != df["Rating"]) | (df["Scene_x"] != df["Scene_y"]) | (df["Shot_x"] != df["Shot_y"]) | (df["Take_x"] != df["Take_y"])]

# 将”tags”列中的值为”nan”的行替换为空字符串
df.loc[df["tags"] == "nan", ["tags"]] = ""
# 将”Scene_x”列中的值为”nan”的行替换为空字符串
df.loc[df["Scene_x"] == "nan", ["Scene_x"]] = ""
# 将”Scene_y”列中的值为”nan”的行替换为空字符串v
df.loc[df["Scene_y"] == "nan", ["Scene_y"]] = ""
# 将”Shot_x”列中的值为”nan”的行替换为空字符串
df.loc[df["Shot_x"] == "nan", ["Shot_x"]] = ""
# 将”Shot_y”列中的值为”nan”的行替换为空字符串
df.loc[df["Shot_y"] == "nan", ["Shot_y"]] = ""
# 将”Take_x”列中的值为”nan”的行替换为空字符串
df.loc[df["Take_x"] == "nan", ["Take_x"]] = ""
# 将”Take_y”列中的值为”nan”的行替换为空字符串
df.loc[df["Take_y"] == "nan", ["Take_y"]] = ""
# 将”tags”和”Rating”列中值相同的行替换为空值
df.loc[df["tags"] == df["Rating"], ["tags", "Rating"]] = ""
# 将”Scene_x”和”Scene_y”列中值相同的行替换为空值
df.loc[df["Scene_x"] == df["Scene_y"], ["Scene_x", "Scene_y"]] = ""
# 将”Shot_x”和”Shot_y”列中值相同的行替换为空值
df.loc[df["Shot_x"] == df["Shot_y"], ["Shot_x", "Shot_y"]] = ""
# 将”Take_x”和”Take_y”列中值相同的行替换为空值
df.loc[df["Take_x"] == df["Take_y"], ["Take_x", "Take_y"]] = ""




# 将DataFrame保存为CSV文件，去除索引列
df.to_csv(output_file, index=False)

# 指定输出文件的路径和文件名为”~/output.csv”
output_file = "~/Desktop/output.csv"