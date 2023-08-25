from logger import Logger


# log = Logger(Logger.Error, file='myapp.log')
# log = Logger(Logger.Info, file='myapp.log')
# log = Logger(Logger.Warning, file='myapp.log')
# log = Logger(Logger.Debug, file='myapp.log')
log = Logger(Logger.Trace, file='myapp.log')

log.E("Это error сообщение",1,2,3)
log.I("Это info сообщение",4,5,6)
log.W("Это warning сообщение",7,8,9)
log.D("Это debug сообщение", 10, 11, 12)
log.T("Это trace сообщение ",13,14,15)

# VN: В приложении практически всегда только один экземпляр Логгера, и все логи выводятся через него.

# log_error = Logger(Logger.Error, file='myapp.log')
# log_info = Logger(Logger.Info, file='myapp.log')
# log_warning = Logger(Logger.Warning, file='myapp.log')
# log_debug = Logger(Logger.Debug, file='myapp.log')
# log_trace = Logger(Logger.Trace, file='myapp.log')

# log_error.E("Это error сообщение", 1, 2, 3)
# log_info.I("Это info сообщение", 4, 5, 6)
# log_warning.W("Это warning сообщение", 7, 8, 9)
# log_debug.D("Это debug сообщение", 10, 11, 12)
# log_trace.T("Это trace сообщение", 13, 14, 15)


