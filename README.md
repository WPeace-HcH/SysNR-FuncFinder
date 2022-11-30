# SysNR-FuncFinder
**A plugin for IDA** that renames functions by system call numbers.
## Background
In my daily analysis, many ELF files are stripped, so IDA won't provide any function name, when this happens, analyzing the sample becomes difficult. So I write a plugin that can rename functions by system call numbers.
## Install
- Just copy the file `SysNR-FuncFinder_WPeace.py` and the folder `LffPlugDir_WPeace` to IDA Plugins folder, then restart IDA Pro to use SysNR-FuncFinder.

`NOTE`: You need python3 and IDA >= 7.4.
## Usage
- **Edit $\Rightarrow$ WPeace_Plugins $\Rightarrow$ SysNR-FuncFinder**  
`(Or hotkey = "Ctrl-Alt-F")`
## Example

## Contact
Email hackinwpeace@gmail.com or leave a message for any questions.
