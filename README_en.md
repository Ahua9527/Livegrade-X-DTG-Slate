# Livegrade-X-DTG-Slate

A Python for Comparing Livegrade Field Recording Information with DTG-Slate Field Recording Information
---

English | [中文](./README.md) 


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
- `-s`  Specify the `DTG-Slate CSV` input file path  
- `-l`  Specify the `Livegrade CSV` input file path  
- `-c`  Specify the `clip_identifier` column to sort     
- `-t`  Specify the `tags` column to sort  

#### Method two
#### [Lazy Shortcuts](https://www.icloud.com/shortcuts/0f372bfca14f4f2ab54e81ce25e77d0b)
###### `👆Click I need MacOS 12 Monterey +`
###### `The first use requires online installation of the corresponding dependencies and script files, which may be slow. Please wait patiently.`       

## Livegrade considerations
- ### In livegrade, you need to use rating to mark "pass", "guarantee", and "waste"
- #### Use 🌟🌟🌟🌟🌟 to indicate passing bars (Circle)
- #### Use 🌟🌟🌟 to indicate KEEP (KEEP)
- #### Use 🌟 to represent waste (NG)

## Reading comprehension

![Image.png](https://res.craft.do/user/full/69e79654-3209-1fb2-a0b1-6e6353d11c7f/doc/F754BB7C-893F-4F4F-A544-2B31F659DD86/FC20AE30-06F7-45DD-8D89-60AE7284EF0E_2/vxRPf1pbP0zpsa82vPrvBDDNqwpZT3Hkxe39xwTTDfAz/Image.png)

## Special thanks
> [@WheheoHu](https://github.com/WheheoHu)·[@a12910](https://github.com/a12910)