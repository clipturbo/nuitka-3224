import cairo
import tkinter.messagebox as messagebox

def main():
    messagebox.showerror("提示", message=f"{cairo.cairo_version()}", icon='error')

if __name__ == "__main__":
    main()
