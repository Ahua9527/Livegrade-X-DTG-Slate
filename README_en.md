# Livegrade-X-DTG-Slate

A Python for Comparing Livegrade Field Recording Information with DTG-Slate Field Recording Information
---

English | [中文](./README.md) 

## Reading comprehension

![SCR-20230928-cxqq](https://cdn.statically.io/gh/Ahua9527/picx-images-hosting@master/20231016/SCR-20230928-cxqq.3m0ekh6f4eg0.webp)

## Prerequisites
`Python 3.9.6+`  
### Use dependency
`Pandas`
```console
pip3 install pandas
```

## How to use
#### Method one
```console
python3 livegradeXdtg-slate.py -t -s slate.csv -l livegrade.csv
```
`-s`  Specify the `DTG-Slate CSV` input file path  
`-l`  Specify the `Livegrade CSV` input file path  
`-c`  Specify the `clip_identifier` column to sort     
`-t`  Specify the `tags` column to sort  

#### Method two
#### [Lazy Shortcuts](https://www.icloud.com/shortcuts/e2d6508b8c064e93aeefb7dd5d5bc5bf)
###### `👆Click I need MacOS 12 Monterey +`
###### `The first use requires online installation of the corresponding dependencies and script files, which may be slow. Please wait patiently.`       
## How to update shortcuts`livegradeXdtg-slate.py`
#### Open`Finder`Display hidden files in the current user's root directory and delete them.`.Script`Folder
#### Or enter the command below at the terminal.
```console
rm -rf ~/.Script
```
## Livegrade considerations
- ### In livegrade, you need to use rating to mark "pass", "guarantee", and "waste"
- #### Use 🌟🌟🌟🌟🌟 to indicate passing bars (Circle)
- #### Use 🌟🌟🌟 to indicate KEEP (KEEP)
- #### Use 🌟 to represent waste (NG)


## Special thanks
> [@WheheoHu](https://github.com/WheheoHu)·[@a12910](https://github.com/a12910)