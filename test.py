"""from tkinter import *
root=Tk()
frm1=Frame(root)
choice1 = Checkbutton(frm1, text=f"{1}").grid(row=0,sticky=W)
benefits1 = Text(frm1,width=100,height=10)
benefits1.grid(row=1,column=0)
benefits1.insert(END,f"Sum Insured :  \n" )
benefits1.config(state="disabled",bg='#%02x%02x%02x' % (240,240,240))

choice2 = Checkbutton(frm1, text=f"{2}.").grid(row=3,sticky=W)
benefits2 = Text(frm1,width=100,height=6)
benefits2.grid(row=4)
benefits2.insert(END,f"Sum Insured : \nBenefits: \n")
benefits2.config(state="disabled",bg='#%02x%02x%02x' % (240,240,240))

frm1.pack()
root.mainloop()
""""""var=IntVar()
    choice = Checkbutton(frm, text=f"{i+1}.{policies[i][1]}",variable=var).pack()
    print (var.get())
    benefits = Text(frm, width=100, height=11)
    benefits.pack(side=TOP)
    benefits.insert(END, f"Sum Insured : {policies[i][2]}\nBenefits: \n" + policies[i][3])
    benefits.config(state="disabled", bg='#%02x%02x%02x' % (240, 240, 240))"""

from datetime import date

from dateutil.relativedelta import relativedelta

print(date.today(),date.today()+relativedelta(years=+5))
