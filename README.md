# SysNR-FuncFinder
**A plugin for IDA** that renames functions by system call numbers.
## Update History
|Version|Date|Supported Arch|Comment|
|----|----|----|----|
|1.0|2022-11-30|AMD x86-64 architecture、Intel 80386、MIPS I Architecture、Advanced RISC Machines ARM|
|1.1|2022-12-01|AMD x86-64 architecture、Intel 80386、MIPS I Architecture、Advanced RISC Machines ARM|Fix bug for IDA API version|
|1.3|2022-12-27|ARM32 for EABI、AMD x86-64 architecture、Intel 80386、MIPS I Architecture、Advanced RISC Machines ARM|Bug fixes|
## Background
In my daily analysis, many ELF files are stripped, in this condition IDA won't provide any function name, when this happens, analyzing the sample becomes difficult. So I write a plugin that can rename functions by system call numbers.
## Install
- Just copy the file `SysNR-FuncFinder_WPeace.py` and the folder `LffPlugDir_WPeace` to IDA Plugins folder, then restart IDA Pro to use SysNR-FuncFinder.  
`NOTE`: You need python3 and IDA >= 7.4.
## Usage
![image](https://github.com/WPeace-HcH/SysNR-FuncFinder/blob/main/IMG/menu.png)
- **Edit $\Rightarrow$ WPeace_Plugins $\Rightarrow$ SysNR-FuncFinder**  
`(Or hotkey = "Ctrl-Alt-F")`
## Example
![image](https://github.com/WPeace-HcH/SysNR-FuncFinder/blob/main/IMG/example.gif)
## Contact
You can leave a message for any questions.
