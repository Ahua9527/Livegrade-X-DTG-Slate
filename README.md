# Livegrade-X-DTG-Slate

一个用与比对Livegrade场记信息与DTG-Slate场记信息的Python
---

中文 | [English](./README_en.md) 


## 使用环境
`Python 3.9.6+`  
`Pandas`

## 如何使用

#### 方法一
```console
python3 livegradeXdtg-slate.py -t -s slate.csv -l livegrade.csv
```
-`-s`  指定 `DTG-Slate CSV` 输入文件路径  
-`-l`  指定 `Livegrade CSV` 输入文件路径  
-`-c`  指定 `clip_identifier` 列进行排序   
-`-t`  指定 `tags` 列进行排序  

#### 方法二
#### [懒人快捷指令](https://www.icloud.com/shortcuts/0f372bfca14f4f2ab54e81ce25e77d0b)
###### `👆点我需MacOS 12 Monterey +`
###### `第一次使用需要联网安装相应的依赖和脚本文件，可能会比较慢请耐心等待`
         

## Livegrade注意事项
- ### 在Livegrade中需要使用Rating来标记“过条”，“保条”，“废条”
- #### 使用🌟🌟🌟🌟🌟来表示过条 Circle
- #### 使用🌟🌟🌟来表示保条 KEEP
- #### 使用🌟来表示废条 NG

## 阅读理解

![Image.png](https://res.craft.do/user/full/69e79654-3209-1fb2-a0b1-6e6353d11c7f/doc/F754BB7C-893F-4F4F-A544-2B31F659DD86/FC20AE30-06F7-45DD-8D89-60AE7284EF0E_2/vxRPf1pbP0zpsa82vPrvBDDNqwpZT3Hkxe39xwTTDfAz/Image.png)

## 特别感谢
> [@WheheoHu](https://github.com/WheheoHu)·[@a12910](https://github.com/a12910)