# Livegrade-X-DTG-Slate

一个用与比对Livegrade场记信息与DTG-Slate场记信息的Python
---

中文 | [English](./README_en.md) 

## 阅读理解

![SCR-20230928-cxqq](https://cdn.statically.io/gh/Ahua9527/picx-images-hosting@master/20231016/SCR-20230928-cxqq.3m0ekh6f4eg0.webp)

## 使用环境
`Python 3.9.6+`  
### 使用依赖
`Pandas`
```console
pip3 install pandas
```

## 如何使用
#### 方法一
```console
python3 livegradeXdtg-slate.py -t -s slate.csv -l livegrade.csv
```
`-s`  指定 `DTG-Slate CSV` 输入文件路径  
`-l`  指定 `Livegrade CSV` 输入文件路径  
`-c`  指定 `clip_identifier` 列进行排序   
`-t`  指定 `tags` 列进行排序  

#### 方法二
#### [懒人快捷指令](https://www.icloud.com/shortcuts/e2d6508b8c064e93aeefb7dd5d5bc5bf)
###### `👆点我需要MacOS 12 Monterey +`
###### `第一次使用需要联网安装相应的依赖和脚本文件，可能会比较慢请耐心等待`
         
## 快捷指令如何更新`livegradeXdtg-slate.py`
#### 打开`Finder`在当前用户根目录下显示隐藏文件后删除`.Script`文件夹
#### 或在终端输入下方命令
```console
rm -rf ~/.Script
```
## Livegrade注意事项
- ### 在Livegrade中需要使用Rating来标记“过条”，“保条”，“废条”
- #### 使用🌟🌟🌟🌟🌟来表示过条 Circle
- #### 使用🌟🌟🌟来表示保条 KEEP
- #### 使用🌟来表示废条 NG

## 特别感谢
> [@WheheoHu](https://github.com/WheheoHu)·[@a12910](https://github.com/a12910)