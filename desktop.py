from pywinauto import Desktop

dlgs = Desktop(backend="uia").windows()
for dlg in dlgs:
    print(dlg.window_text(), dlg.class_name())

# 检查是否有两个或更多的窗口标题包含 "QQ"
qq_windows = [dlg for dlg in dlgs if "QQ" in dlg.window_text()]
# 判断是否存在两个或更多的 "QQ" 窗口
if len(qq_windows) >= 2:
    print("存在两个或更多的 'QQ' 窗口")
else:
    print("不存在两个或更多的 'QQ' 窗口")




