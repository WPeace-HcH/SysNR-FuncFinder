import idc
import idaapi
import sys, os
path = os.path.dirname(os.path.abspath(__file__)) + "\\LffPlugDir_WPeace\\"
sys.path.append(path)
import LinuxFuncFinder_x64
import LinuxFuncFinder_x86
import LinuxFuncFinder_Mips32
import LinuxFuncFinder_Arm32


class myplugin_t(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = "SysNR-FuncFinder Plugin for IDA"
    help = "Find more information at https://github.com/wpeace-hch"
    wanted_name = "SysNR-FuncFinder"
    wanted_hotkey = "Ctrl-Alt-F"
    def init(self):
        print("\nSysNR-FuncFinder By WPeace.")
        try:
            WPe_Patcher.register(self, "SysNR-FuncFinder    (Ctrl-Alt-F)")
            WPe_About.register(self, "About")
        except:
            pass
        if idaapi.IDA_SDK_VERSION >= 740:
            idaapi.attach_action_to_menu("Edit/WPeace_Plugins/SysNR-FuncFinder    (Ctrl-Alt-F)", WPe_Patcher.get_name(), idaapi.SETMENU_APP)
            idaapi.attach_action_to_menu("Edit/WPeace_Plugins/About", WPe_About.get_name(), idaapi.SETMENU_APP)
        else:
            print("Your IDA version needs to be greater than 7.4! :(@WPeace")
        return idaapi.PLUGIN_OK
    def run(self, arg):
        self.patcher()
    def term(self):
        print("SysNR-FuncFinder works fine! :)@WPeace\n")
    def patcher(self):
        elf_magic = idc.Dword(idc.FirstSeg())
        if elf_magic == 0x464c457f or elf_magic == 0x7f454c46:
            e_machine = idc.Word(idc.FirstSeg() + 0x12)
            # AMD x86-64 architecture
            if e_machine == 62:
                LinuxFuncFinder_x64.main()
            # Intel 80386
            elif e_machine == 3:
                LinuxFuncFinder_x86.main()
            # MIPS I Architecture
            elif e_machine == 8:
                LinuxFuncFinder_Mips32.main()
            # Advanced RISC Machines ARM
            elif e_machine == 40:
                LinuxFuncFinder_Arm32.main()
            else:
                print("请确认插件版本是否支持当前文件架构。")
        else:
            print("当前插件仅支持ELF文件格式。")
    def about(self):
        f = About_Form()
        f.Execute()
        f.Free()


class Menu_Context(idaapi.action_handler_t):
        @classmethod
        def get_name(self):
            return self.__name__
            
        @classmethod
        def get_label(self):
            return self.label
            
        @classmethod
        def register(self, plugin, label):
            self.plugin = plugin
            self.label = label
            instance = self()
            return idaapi.register_action(idaapi.action_desc_t(
                self.get_name(),
                instance.get_label(),
                instance
            ))
            
        @classmethod
        def unregister(self):
            """Unregister the action.
            After unregistering the class cannot be used.
            """
            idaapi.unregister_action(self.get_name())
            
        @classmethod
        def activate(self, ctx):
            return 1
            
        @classmethod
        def update(self, ctx):
            try:
                return idaapi.AST_ENABLE_FOR_FORM if ctx.form_type == idaapi.BWN_DISASM else idaapi.AST_DISABLE_FOR_FORM
            except Exception as e:
                return idaapi.AST_ENABLE_ALWAYS


class About_Form(idaapi.Form):
    def __init__(self):
        super(About_Form, self).__init__(
            r"""STARTITEM 0
BUTTON YES* Open author's github
ABOUT（v1.0）
            {FormChangeCb}
            SysNR-FuncFinder Plugin for IDA.
            Written BY WPeace.
            """, {
            'FormChangeCb': self.FormChangeCb(self.OnFormChange),
            })

        self.Compile()

    def OnFormChange(self, fid):
        if fid == -2:
            import webbrowser
            webbrowser.open("https://github.com/wpeace-hch", new = 2)
        return 1


class WPe_Patcher(Menu_Context):
        def activate(self, ctx):
            self.plugin.patcher()
            return 1


class WPe_About(Menu_Context):
    def activate(self, ctx):
        self.plugin.about()
        return 1


def PLUGIN_ENTRY():
    return myplugin_t()