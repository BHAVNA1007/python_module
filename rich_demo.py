
from rich import print

print("[bold green]Hello Bhavna![/bold green]")
print("[bold red]This is Rich[/bold red]")

print("[yellow]Yellow[/yellow]")

print('[bold yellow]you know you are very bad, why... because you were not easylly installed in my lapppppp[/bold yellow]')




print("[cyan]Cyan[/cyan]")
print("[yellow underline]Now, I am at my home because of rakshabandhan.... yeeeeeeee ![/yellow underline]")




'''
Very useful for displaying structured data.

Rich's Table provides methods such as add_column() and add_row() for terminal tables.
'''



from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Employees")

table.add_column("ID")
table.add_column("Name")
table.add_column("Salary")

table.add_row("101", "Amit", "50000")
table.add_row("102", "Rahul", "60000")

console.print(table)





console = Console()

console.print("Hello")
console.log("Program started")

'''
Console provides advanced terminal features such as styling, markup, logging information, pretty printing and terminal-aware output, whereas print() provides basic text output.
'''





'''
Rich Progress Bar
Useful when a task takes time.
'''




from rich.progress import track
import time

for i in track(range(10), description="Processing..."):
    time.sleep(1)




'''
You get a progress indicator instead of staring at a blank terminal.

Rich also supports multiple simultaneous tasks through Progress.

Q: Where would you use Rich?

I would use Rich mainly in CLI applications, scripts, automation tools and development utilities where I want better terminal output, progress indicators, tables or debugging information.
'''



'''

py -m pip install rich



1. rich — Terminal/CLI Formatting Library
What is Rich?

Rich is a third-party Python library used to make terminal/console output more attractive, readable, and informative.

It supports:

Colored/styled text
Tables
Progress bars
Spinners
Markdown
Syntax highlighting
Pretty printing
Better logging
Better tracebacks
'''