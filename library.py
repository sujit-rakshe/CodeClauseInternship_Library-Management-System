import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class LMS_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1000x400")  # Increase the width of the window

        self.library = LMS()

        self.label = tk.Label(root, text="Welcome to Library Management System", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=6, pady=20)

        self.tree = ttk.Treeview(root, columns=("Book ID", "Title", "Status", "Borrower", "Issue Date"), show="headings")
        self.tree.heading("Book ID", text="Book ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Borrower", text="Borrower")
        self.tree.heading("Issue Date", text="Issue Date")
        self.tree.column("Book ID", width=100)  # Adjust column widths
        self.tree.column("Title", width=200)
        self.tree.column("Status", width=100)
        self.tree.column("Borrower", width=150)
        self.tree.column("Issue Date", width=150)
        self.tree.grid(row=1, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

        self.issue_button = tk.Button(root, text="Issue Book", command=self.issue_book)
        self.issue_button.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

        self.return_button = tk.Button(root, text="Return Book", command=self.return_book)
        self.return_button.grid(row=2, column=4, padx=10, pady=10, sticky="nsew")

        self.display_books()  # Display books when the GUI is launched

        # Configure row and column weights to make the Treeview expand with the window
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)
        root.grid_columnconfigure(3, weight=1)
        root.grid_columnconfigure(4, weight=1)
        root.grid_columnconfigure(5, weight=1)

    def display_books(self):
        self.tree.delete(*self.tree.get_children())  # Clear existing entries
        books = self.library.get_books()
        for book_id, title, status, borrower, issue_date in books:
            self.tree.insert("", "end", values=(book_id, title, status, borrower, issue_date))

    def issue_book(self):
        self.issue_window = tk.Toplevel(self.root)
        self.issue_window.title("Issue Book")
        self.issue_window.geometry("300x150")

        self.issue_label = tk.Label(self.issue_window, text="Enter Book ID:")
        self.issue_label.pack(pady=5)

        self.issue_entry = tk.Entry(self.issue_window)
        self.issue_entry.pack(pady=5)

        self.borrower_label = tk.Label(self.issue_window, text="Enter Your Name:")
        self.borrower_label.pack(pady=5)

        self.borrower_entry = tk.Entry(self.issue_window)
        self.borrower_entry.pack(pady=5)

        self.issue_button = tk.Button(self.issue_window, text="Issue", command=self.issue_book_action)
        self.issue_button.pack(pady=5)

    def issue_book_action(self):
        book_id = self.issue_entry.get()
        borrower_name = self.borrower_entry.get()
        if book_id and borrower_name:
            result = self.library.issue_book(book_id, borrower_name)
            messagebox.showinfo("Issue Book Result", result)
            self.issue_window.destroy()
            self.display_books()

    def add_book(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add Book")
        self.add_window.geometry("300x100")

        self.add_label = tk.Label(self.add_window, text="Enter Book Title:")
        self.add_label.pack(pady=5)

        self.add_entry = tk.Entry(self.add_window)
        self.add_entry.pack(pady=5)

        self.add_button = tk.Button(self.add_window, text="Add", command=self.add_book_action)
        self.add_button.pack(pady=5)

    def add_book_action(self):
        book_title = self.add_entry.get()
        if book_title:
            result = self.library.add_book(book_title)
            messagebox.showinfo("Add Book Result", result)
            self.add_window.destroy()
            self.display_books()

    def return_book(self):
        self.return_window = tk.Toplevel(self.root)
        self.return_window.title("Return Book")
        self.return_window.geometry("300x100")

        self.return_label = tk.Label(self.return_window, text="Enter Book ID:")
        self.return_label.pack(pady=5)

        self.return_entry = tk.Entry(self.return_window)
        self.return_entry.pack(pady=5)

        self.return_button = tk.Button(self.return_window, text="Return", command=self.return_book_action)
        self.return_button.pack(pady=5)

    def return_book_action(self):
        book_id = self.return_entry.get()
        if book_id:
            result = self.library.return_book(book_id)
            messagebox.showinfo("Return Book Result", result)
            self.return_window.destroy()
            self.display_books()

class LMS:
    def __init__(self):
        self.books = {
            '101': {'title': 'Python Programming', 'status': 'Available', 'borrower': None, 'issue_date': None},
            '102': {'title': 'Introduction to Java', 'status': 'Available', 'borrower': None, 'issue_date': None},
            '103': {'title': 'Web Development Basics', 'status': 'Available', 'borrower': None, 'issue_date': None},
            '104': {'title': 'Data Structures in C', 'status': 'Issued', 'borrower': 'John', 'issue_date': '2023-09-10 14:30:00'},
            '105': {'title': 'Algorithms in Python', 'status': 'Issued', 'borrower': 'Alice', 'issue_date': '2023-09-09 10:15:00'},
            '106': {'title': 'Machine Learning Basics', 'status': 'Available', 'borrower': None, 'issue_date': None},
            '107': {'title': 'Database Management', 'status': 'Issued', 'borrower': 'Bob', 'issue_date': '2023-09-08 16:45:00'},
            '108': {'title': 'Web Design Fundamentals', 'status': 'Available', 'borrower': None, 'issue_date': None},
            '109': {'title': 'Networking Essentials', 'status': 'Issued', 'borrower': 'Eve', 'issue_date': '2023-09-07 09:30:00'},
            '110': {'title': 'Software Engineering', 'status': 'Available', 'borrower': None, 'issue_date': None},
        }
        self.current_id = 111

    def get_books(self):
        books = []
        for book_id, book in self.books.items():
            title = book['title']
            status = book['status']
            borrower = book['borrower'] if status == 'Issued' else ''
            issue_date = book['issue_date'] if status == 'Issued' else ''
            books.append((book_id, title, status, borrower, issue_date))
        return books

    def issue_book(self, book_id, borrower_name):
        if book_id in self.books:
            book = self.books[book_id]
            if book['status'] == 'Available':
                book['status'] = 'Issued'
                book['borrower'] = borrower_name
                book['issue_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return f"Book '{book['title']}' has been issued to {borrower_name}."
            else:
                return f"Book '{book['title']}' is already issued to {book['borrower']} on {book['issue_date']}."
        else:
            return "Book not found."

    def add_book(self, book_title):
        book_id = str(self.current_id)
        self.books[book_id] = {'title': book_title, 'status': 'Available', 'borrower': None, 'issue_date': None}
        self.current_id += 1
        return f"Book '{book_title}' has been added successfully."

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book['status'] == 'Issued':
                book['status'] = 'Available'
                borrower_name = book['borrower']
                book['borrower'] = None
                book['issue_date'] = None
                return f"Book '{book['title']}' has been returned by {borrower_name}."
            else:
                return f"Book '{book['title']}' is already available in the library."
        else:
            return "Book not found."

if __name__ == "__main__":
    root = tk.Tk()
    app = LMS_GUI(root)
    root.mainloop()
