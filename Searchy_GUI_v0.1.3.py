import subprocess
import tkinter as tk
search_dir="/"
# tk gui
root=tk.Tk()
root.title("Searchy")
root.geometry("400x350")
Search_prompt=tk.Label(root,text="What would you like to search for?",fg="grey",font=("Helvetica",12,"bold"))
Search_prompt.place(anchor="center", relx=0.5,rely=0.1)
query=tk.Entry(root)
query.place(anchor="center", relx=0.5,rely=0.2)

# Connecting python TK GUI to bash script with function
def bashcnct():
    search_data=query.get()
    bash=fr"""
    search_bash="{search_data}"
    search_result=$(find / \( -path "/tmp" -o -path "/proc" -o -path "/sys" -o \( -path "/run/*" -not -path "/run/media*" \) \) -prune -o -iname "$search_bash" -print 2> /dev/null)u
    if [ -z "$search_result" ]; then
        echo "File not found: 404"
    else
        echo "$search_result"
    fi
    """
    global result
    result=subprocess.run(bash, shell=True, capture_output=True,text=True)
    result_display.config(text=result.stdout)
#search results tk gui
result_frame=tk.Frame(root,borderwidth=4, relief="groove",height=250,width=400)
result_frame.place(anchor="center", relx=0.5, rely=0.68, relwidth=1.0, relheight=0.67)
result_display=tk.Label(result_frame)
result_display.place(anchor="center",relx=0.5,rely=0.5)
#tk gui
find=tk.Button(root,text="Search",fg="green",font=("Comic Sans MS",8,"italic"),command=bashcnct)
find.place(anchor="center",relx=0.5,rely=0.3)




if __name__ == "__main__":
    root.mainloop()
