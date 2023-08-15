import tkinter as tk
from tkinter import filedialog, messagebox

class 文本编辑器:
    def __init__(self, root):
        self.root = root
        self.root.title("Liyao专业文本编辑器 V8.0")  # 在标题中显示版本号

        self.text_widget = tk.Text(self.root)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        self.current_file = None  # 用于保存当前打开的文件路径

        self.open_mode_var = tk.StringVar()
        self.open_mode_var.set("normal")  # 默认打开方式为正常

        self.encoding_var = tk.StringVar()
        self.encoding_var.set("utf-8")  # 默认编码为UTF-8

        self.创建菜单()

    def 创建菜单(self):
        菜单栏 = tk.Menu(self.root)
        self.root.config(menu=菜单栏)

        文件菜单 = tk.Menu(菜单栏, tearoff=0)
        菜单栏.add_cascade(label="文件", menu=文件菜单)
        文件菜单.add_command(label="新建", command=self.新建文件)
        文件菜单.add_command(label="打开", command=self.打开文件)
        文件菜单.add_command(label="保存", command=self.保存文件)
        文件菜单.add_command(label="另存为", command=self.另存为文件)
        文件菜单.add_separator()
        文件菜单.add_command(label="退出", command=self.root.quit)

        编辑菜单 = tk.Menu(菜单栏, tearoff=0)
        菜单栏.add_cascade(label="编辑", menu=编辑菜单)
        编辑菜单.add_command(label="复制", command=self.复制文本)
        编辑菜单.add_command(label="粘贴", command=self.粘贴文本)

        打开方式菜单 = tk.Menu(菜单栏, tearoff=0)
        菜单栏.add_cascade(label="打开方式", menu=打开方式菜单)
        打开方式菜单.add_radiobutton(label="正常打开", variable=self.open_mode_var, value="normal")
        打开方式菜单.add_radiobutton(label="16进制打开", variable=self.open_mode_var, value="hex")
        打开方式菜单.add_radiobutton(label="2进制打开", variable=self.open_mode_var, value="binary")
        打开方式菜单.add_radiobutton(label="8进制打开", variable=self.open_mode_var, value="octal")

        编码菜单 = tk.Menu(菜单栏, tearoff=0)
        菜单栏.add_cascade(label="编码", menu=编码菜单)
        编码菜单.add_radiobutton(label="UTF-8", variable=self.encoding_var, value="utf-8")
        编码菜单.add_radiobutton(label="GBK", variable=self.encoding_var, value="gbk")
        编码菜单.add_radiobutton(label="UTF-16", variable=self.encoding_var, value="utf-16")

    def 新建文件(self):
        self.text_widget.delete("1.0", tk.END)
        self.current_file = None

    def 打开文件(self):
        文件路径 = filedialog.askopenfilename()  # 允许打开所有类型的文件
        if 文件路径:
            self.current_file = 文件路径
            打开方式 = self.open_mode_var.get()
            with open(文件路径, "rb") as 文件:
                内容 = 文件.read()
                if 打开方式 == "hex":
                    内容 = 内容.hex()
                elif 打开方式 == "binary":
                    内容 = " ".join(format(byte, '08b') for byte in 内容)
                elif 打开方式 == "octal":
                    内容 = " ".join(format(byte, 'o') for byte in 内容)
                else:
                    内容 = 内容.decode(self.encoding_var.get(), errors="replace")
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert(tk.END, 内容)

    def 保存文件(self):
        if self.current_file:  # 如果有打开的文件
            内容 = self.text_widget.get("1.0", tk.END)
           
            with open(self.current_file, "w", encoding=self.encoding_var.get()) as 文件:
                文件.write(内容)
        else:
            self.另存为文件()

    def 另存为文件(self):
        内容 = self.text_widget.get("1.0", tk.END)
        文件路径 = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
        if 文件路径:
            self.current_file = 文件路径
            with open(文件路径, "w", encoding=self.encoding_var.get()) as 文件:
                文件.write(内容)

    def 复制文本(self):
        try:
            选中文本 = self.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)
            self.root.clipboard_clear()
            self.root.clipboard_append(选中文本)
        except tk.TclError:
            pass

    def 粘贴文本(self):
        粘贴内容 = self.root.clipboard_get()
        self.text_widget.insert(tk.INSERT, 粘贴内容)

if __name__ == "__main__":
    root = tk.Tk()
    编辑器 = 文本编辑器(root)
    root.mainloop()
