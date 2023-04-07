# SysNR-FuncFinder
**A plugin for IDA** that renames functions by system call numbers.
## Update History
|Version|Date|Supported Arch|Comment|
|----|----|----|----|
|1.0|2022-11-30|AMD x86-64 architecture、Intel 80386、MIPS I Architecture、Advanced RISC Machines ARM|
|1.1|2022-12-01|AMD x86-64 architecture、Intel 80386、MIPS I Architecture、Advanced RISC Machines ARM|Fix bug for IDA API version.|
|1.3|2022-12-27|ARM32 for EABI、AMD x86-64 architecture、Intel 80386、MIPS I Architecture、Advanced RISC Machines ARM|Add support for EABI ARM32 and Bug fixes.|
|1.5|2023-02-10|ARM32 for EABI、AMD x86-64 architecture、Intel 80386、MIPS I Architecture、Advanced RISC Machines ARM|Support finding main function for all architecture.|
|1.6|2023-02-14|ARM32 for EABI、AMD x86-64 architecture、Intel 80386、MIPS I Architecture、Advanced RISC Machines ARM|Fix bugs when finding main function.|
|1.7|2023-03-22|ARM32 for EABI、AMD x86-64 architecture、Intel 80386、MIPS I Architecture、Advanced RISC Machines ARM|Fix a bug and change some details.<br>(You need to delete old `SysNR-FuncFinder_WPeace.py` because the py-name have changed)|
|2.0|2023-04-07|ARM32 for EABI、AMD x86-64 architecture、Intel 80386、MIPS I Architecture、Advanced RISC Machines ARM、PowerPC32|- Add support for PowerPC32 and support finding main function for PowerPC32.<br>- Add support for Indirect-call MIPS|
## Background
In my daily analysis, many ELF files are stripped, in this condition IDA won't provide any function name, when this happens, analyzing the sample becomes difficult. So I write a plugin that can rename functions by system call numbers.
## Install
- Just copy the file `SysNR-FuncFinder.py` and the folder `LffPlugDir_WPeace` to IDA Plugins folder, then restart IDA Pro to use SysNR-FuncFinder.  
- `NOTE`: You need python3 and IDA >= 7.4.
## Usage
![image](https://github.com/WPeace-HcH/SysNR-FuncFinder/blob/main/IMG/menu.png)
- **Edit $\Rightarrow$ WPeace_Plugins $\Rightarrow$ SysNR-FuncFinder**  
`(Or hotkey = "Ctrl-Alt-F")`
## Example
![image](https://github.com/WPeace-HcH/SysNR-FuncFinder/blob/main/IMG/example.gif)
## Contact
You can leave a message for any questions.
