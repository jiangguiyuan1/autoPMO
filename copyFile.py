import os
import win32clipboard
import win32con
import ctypes
import time

class DROPFILES(ctypes.Structure):
    _fields_ = [
    ("pFiles", ctypes.c_uint),
    ("x", ctypes.c_long),
    ("y", ctypes.c_long),
    ("fNC", ctypes.c_int),
    ("fWide", ctypes.c_bool),
    ]
pDropFiles = DROPFILES()
pDropFiles.pFiles = ctypes.sizeof(DROPFILES)
pDropFiles.fWide = True
matedata = bytes(pDropFiles)


def SetClipboardFiles(paths):
    paths = [paths]
    for file in paths:
        if not os.path.exists(file):
            raise FileNotFoundError(f"file ({file}) not exists!")
    files = ("\0".join(paths)).replace("/", "\\")
    data = files.encode("U16")[2:]+b"\0\0"
    t0 = time.time()
    while True:
        if time.time() - t0 > 10:
            raise TimeoutError(f"设置剪贴板文件超时！ --> {paths}")
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_HDROP,matedata+data)
            break
        except:
            pass
        finally:
            try:
                win32clipboard.CloseClipboard()
            except:
                pass


file_path ="D:\\PMO-测试-1\\测试_测试3_测试.xlsx"
SetClipboardFiles(file_path)