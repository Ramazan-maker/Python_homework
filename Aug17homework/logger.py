

class Logger:
    Error = 0
    Warning = 1
    Info = 2
    Debug = 3
    Trace = 4
    names = ["[E]", "[W]", "[I]", "[D]", "[T]"]

    Colors={
        Error:'\033[91m',
        Warning:'\033[33m',
        Info:'\033[37m',
        Debug:'\033[32m',
        Trace:'\033[35m'
    }
    Reset_colors = '\033[0m'

    def __init__(self,levels,stdout=True,file=None):
        self.levels = levels
        self.stdout = stdout
        self.file = file

    def set_log_level(self,levels):
        self.levels = levels

    def _log(self,levels,*args,**kwargs):
        color = self.Colors.get(levels,'')

        if self.stdout:
            print(f'{color}{Logger.names[self.levels]}', *args, self.Reset_colors, **kwargs)
        if self.file:
            with open(self.file, 'a',encoding='utf-8') as f:
                f.write(f"[{levels}]" + ' '.join(map(str, args)) + '\n')
    def E(self, *args, **kwargs):
        if self.levels >= self.Error:
            self._log(self.Error, *args, **kwargs)
    def W(self,*args,**kwargs):
        if self.levels >= self.Warning:
            self._log(self.Warning, *args, **kwargs)
    def I(self,*args,**kwargs):
        if self.levels >= self.Info:
            self._log(self.Info, *args, **kwargs)
    def D(self,*args,**kwargs):
        if self.levels >= self.Debug:
            self._log(self.Debug, *args, **kwargs)
    def T(self,*args,**kwargs):
        if self.levels >= self.Trace:
            self._log(self.Trace, *args, **kwargs)