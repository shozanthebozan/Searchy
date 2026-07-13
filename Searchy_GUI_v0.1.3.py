import subprocess
import tkinter as tk
# function to allow changing search directory
search_dir="/"
def change_dir():
    global dirread
    dirread=search_dir_entry.get()
    search_dir=dirread
    

# tk gui
root=tk.Tk()
root.title("Searchy")
root.geometry("400x350")
Search_prompt=tk.Label(root,text="What would you like to search for?",fg="grey",font=("Helvetica",12,"bold"))
Search_prompt.place(anchor="center", relx=0.5,rely=0.1)
query=tk.Entry(root)
query.place(anchor="center", relx=0.5,rely=0.2)
search_dir_label=tk.Label(root,text="Directory to search \nEnter here:",font=("arial",8))
search_dir_label.place(anchor='w', relx=0.01,rely=0.2)
search_dir_entry=tk.Entry(root,width=5)
search_dir_entry.place(anchor="center",relx=0.15,rely=0.3)
search_dir_entry.insert(0, f"{search_dir}")
search_dir_submit=tk.Button(root, text="Ok",width=1,command=change_dir)
search_dir_submit.place(anchor="center",relx=0.3,rely=0.3)

# Connecting python TK GUI to bash script with function
def bashcnct():
    search_data=query.get()
    bash=fr"""
    search_bash="{search_data}"
    search_result=$(find {dirread} \( -path "/tmp" -o -path "/proc" -o -path "/sys" -o \( -path "/run/*" -not -path "/run/media*" \) \) -prune -o -iname "$search_bash" -print 2> /dev/null)u
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
