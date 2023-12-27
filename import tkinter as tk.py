import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DataAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Analyzer")

        self.file_path_label = tk.Label(root, text="File Path:")
        self.file_path_label.pack()

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.analyze_button = tk.Button(root, text="Analyze Data", command=self.analyze_data)
        self.analyze_button.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"),
                                                           ("Text Files", "*.txt"),
                                                           ("All Files", "*.*")])
        self.file_path_label.config(text=f"File Path: {file_path}")
        self.file_path = file_path

    def analyze_data(self):
        if not hasattr(self, 'file_path') or not self.file_path:
            self.file_path_label.config(text="Please select a file first.")
            return

        try:
            df = pd.read_csv(self.file_path)
            plt.scatter(df['X'], df['Y'])
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Scatter Plot')
            plt.show()

        except Exception as e:
            self.file_path_label.config(text=f"Error: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()
