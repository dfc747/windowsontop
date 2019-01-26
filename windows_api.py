import win32gui
import ctypes

user32 = ctypes.windll.user32
exclude_hwnds = (user32.GetShellWindow(), win32gui.FindWindow('Shell_TrayWnd', None))


def enumHandler(hwnd, lParams):
    if win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd) and hwnd not in exclude_hwnds:
        title = win32gui.GetWindowText(hwnd).strip()
        if title != '':
            print('-' + title)


def main():
    win32gui.EnumWindows(enumHandler, None)


if __name__ == '__main__':
    main()
