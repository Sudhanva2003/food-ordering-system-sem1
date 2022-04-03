from tkinter import *
import random

from PIL import ImageTk,Image
root=Tk()
root.title('food ordering system')
root.geometry('1200x1200')
root.config(bg='darksalmon')
root.iconbitmap("beverage_7Eb_icon.ico")
myimg=ImageTk.PhotoImage(Image.open('pngwing.com.png'))
mylabel=Label(root,image=myimg,width=80,height=80)
mylabel.place(x=220,y=0)

topframe=Frame(root,bd=10,relief=RIDGE)
topframe.pack(side=TOP)
labeltitle=Label(topframe,text='SamZaiSah\'s ordering services',font=('jokerman',30,'italic','bold','underline'),fg='black',bd=9,bg='firebrick1')
labeltitle.grid(row=0,column=0)

def roti():
    if var1.get() == 1:
        textroti.config(state=NORMAL)
        textroti.delete(0, END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')


def daal():
    if var2.get() == 1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0, END)
        textdaal.focus()

    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')


def fish():
    if var3.get() == 1:
        textfish.config(state=NORMAL)
        textfish.delete(0, END)
        textfish.focus()

    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')


def sabji():
    if var4.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.focus()
        textsabji.delete(0, END)
    elif var4.get() == 0:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')


def kebab():
    if var5.get() == 1:
        textkebab.config(state=NORMAL)
        textkebab.focus()
        textkebab.delete(0, END)
    elif var5.get() == 0:
        textkebab.config(state=DISABLED)
        e_kebab.set('0')


def chawal():
    if var6.get() == 1:
        textchawal.config(state=NORMAL)
        textchawal.focus()
        textchawal.delete(0, END)
    elif var6.get() == 0:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')


def mutton():
    if var7.get() == 1:
        textmutton.config(state=NORMAL)
        textmutton.focus()
        textmutton.delete(0, END)
    elif var7.get() == 0:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')


def paneer():
    if var8.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.focus()
        textpaneer.delete(0, END)
    elif var8.get() == 0:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')


def chicken():
    if var9.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.focus()
        textchicken.delete(0, END)
    elif var9.get() == 0:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')


def lassi():
    if var10.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.focus()
        textlassi.delete(0, END)
    elif var10.get() == 0:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')


def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    elif var11.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')


def faluda():
    if var12.get() == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.focus()
        textfaluda.delete(0, END)
    elif var12.get() == 0:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')


def shikanji():
    if var13.get() == 1:
        textshikanji.config(state=NORMAL)
        textshikanji.focus()
        textshikanji.delete(0, END)
    elif var13.get() == 0:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')


def jaljeera():
    if var14.get() == 1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.focus()
        textjaljeera.delete(0, END)
    elif var14.get() == 0:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')

def roohafza():
    if var15.get() == 1:
        textroohafza.config(state=NORMAL)
        textroohafza.focus()
        textroohafza.delete(0, END)
    elif var15.get() == 0:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')


def masalatea():
    if var16.get() == 1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.focus()
        textmasalatea.delete(0, END)
    elif var16.get() == 0:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')


def badammilk():
    if var17.get() == 1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.focus()
        textbadammilk.delete(0, END)
    elif var17.get() == 0:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')


def colddrinks():
    if var18.get() == 1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.focus()
        textcolddrinks.delete(0, END)
    elif var18.get() == 0:
        textcolddrinks.config(state=DISABLED)
        e_coldrinks.set('0')


def oreo():
    if var19.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
    elif var19.get() == 0:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')


def apple():
    if var20.get() == 1:
        textapple.config(state=NORMAL)
        textapple.focus()
        textapple.delete(0, END)
    elif var20.get() == 0:
        textapple.config(state=DISABLED)
        e_apple.set('0')


def kitkat():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.focus()
        textkitkat.delete(0, END)
    elif var21.get() == 0:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')


def vanilla():
    if var22.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.focus()
        textvanilla.delete(0, END)
    elif var22.get() == 0:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')


def banana():
    if var23.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.focus()
        textbanana.delete(0, END)
    elif var23.get() == 0:
        textbanana.config(state=DISABLED)
        e_banana.set('0')


def brownie():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.focus()
        textbrownie.delete(0, END)
    elif var24.get() == 0:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')


def pineapple():
    if var25.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.focus()
        textpineapple.delete(0, END)
    elif var25.get() == 0:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')


def chocolate():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.focus()
        textchocolate.delete(0, END)
    elif var26.get() == 0:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')


def blackforest():
    if var27.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.focus()
        textblackforest.delete(0, END)
    elif var27.get() == 0:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')



menuFrame = Frame(root, bd=10, relief=RIDGE, bg='firebrick4')
menuFrame.pack(side=LEFT)

foodFrame = LabelFrame(menuFrame, text='Food', font=('algerian', 19, 'bold'), bd=10, relief=RIDGE, fg='red4', )
foodFrame.pack(side=LEFT)
drinksFrame = LabelFrame(menuFrame, text='Drinks', font=('algerian', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
drinksFrame.pack(side=LEFT)
cakesFrame = LabelFrame(menuFrame, text='Cakes', font=('algerian', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
cakesFrame.pack(side=RIGHT)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_roti = StringVar()
e_daal = StringVar()
e_sabji = StringVar()
e_chawal = StringVar()
e_fish = StringVar()
e_mutton = StringVar()
e_kebab = StringVar()
e_chicken = StringVar()
e_paneer = StringVar()

e_lassi = StringVar()
e_coffee = StringVar()
e_faluda = StringVar()
e_shikanji = StringVar()
e_roohafza = StringVar()
e_jaljeera = StringVar()
e_masalatea = StringVar()
e_badammilk = StringVar()
e_coldrinks = StringVar()

e_oreo = StringVar()
e_kitkat = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()

costoffoodvar = StringVar()
costofdrinksvar = StringVar()
costofcakesvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

e_roti.set('0')
e_daal.set('0')
e_sabji.set('0')
e_fish.set('0')
e_kebab.set('0')
e_chawal.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_paneer.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_roohafza.set('0')
e_shikanji.set('0')
e_jaljeera.set('0')
e_masalatea.set('0')
e_badammilk.set('0')
e_coldrinks.set('0')

e_kitkat.set('0')
e_banana.set('0')
e_pineapple.set('0')
e_apple.set('0')
e_chocolate.set('0')
e_oreo.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_vanilla.set('0')

roti = Checkbutton(foodFrame, text='Roti (Rs.20)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var1
                   , command=roti)
roti.grid(row=0, column=0, sticky=W)

daal = Checkbutton(foodFrame, text='Daal (Rs.50)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var2
                   , command=daal)
daal.grid(row=1, column=0, sticky=W)

fish = Checkbutton(foodFrame, text='Fish (Rs.120)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var3
                   , command=fish)
fish.grid(row=2, column=0, sticky=W)

sabji = Checkbutton(foodFrame, text='Sabji (Rs.80)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var4
                    , command=sabji)
sabji.grid(row=3, column=0, sticky=W)

kebab = Checkbutton(foodFrame, text='Kebab (Rs.180)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var5
                    , command=kebab)
kebab.grid(row=4, column=0, sticky=W)

chawal = Checkbutton(foodFrame, text='Chawal (Rs.80)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var6
                     , command=chawal)
chawal.grid(row=5, column=0, sticky=W)

mutton = Checkbutton(foodFrame, text='Mutton (Rs.165)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var7,
                     command=mutton)
mutton.grid(row=6, column=0, sticky=W)

paneer = Checkbutton(foodFrame, text='Paneer (Rs.150)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var8
                     , command=paneer)
paneer.grid(row=7, column=0, sticky=W)

chicken = Checkbutton(foodFrame, text='Chicken (Rs.140)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var9
                      , command=chicken)
chicken.grid(row=8, column=0, sticky=W)

# Entry Fields for Food Items

textroti = Entry(foodFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_roti)
textroti.grid(row=0, column=1)

textdaal = Entry(foodFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_daal)
textdaal.grid(row=1, column=1)

textfish = Entry(foodFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_fish)
textfish.grid(row=2, column=1)

textsabji = Entry(foodFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sabji)
textsabji.grid(row=3, column=1)

textkebab = Entry(foodFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kebab)
textkebab.grid(row=4, column=1)

textchawal = Entry(foodFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chawal)
textchawal.grid(row=5, column=1)

textmutton = Entry(foodFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mutton)
textmutton.grid(row=6, column=1)

textpaneer = Entry(foodFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_paneer)
textpaneer.grid(row=7, column=1)

textchicken = Entry(foodFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=8, column=1)

lassi = Checkbutton(drinksFrame, text='Lassi (Rs.65)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var10
                    , command=lassi)
lassi.grid(row=0, column=0, sticky=W)

coffee = Checkbutton(drinksFrame, text='Coffee (Rs.40)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var11
                     , command=coffee)
coffee.grid(row=1, column=0, sticky=W)

faluda = Checkbutton(drinksFrame, text='Faluda (Rs.75)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var12
                     , command=faluda)
faluda.grid(row=2, column=0, sticky=W)

shikanji = Checkbutton(drinksFrame, text='Shikanji (Rs.45)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var13
                       , command=shikanji)
shikanji.grid(row=3, column=0, sticky=W)

jaljeera = Checkbutton(drinksFrame, text='Jaljeera (Rs.35)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var14
                       , command=jaljeera)
jaljeera.grid(row=4, column=0, sticky=W)

roohafza = Checkbutton(drinksFrame, text='Roohafza (Rs.60)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var15
                       , command=roohafza)
roohafza.grid(row=5, column=0, sticky=W)

masalatea = Checkbutton(drinksFrame, text='Masala Tea (Rs.15)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0,
                        variable=var16
                        , command=masalatea)
masalatea.grid(row=6, column=0, sticky=W)

badammilk = Checkbutton(drinksFrame, text='Badam Milk (Rs.25)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0,
                        variable=var17
                        , command=badammilk)
badammilk.grid(row=7, column=0, sticky=W)

colddrinks = Checkbutton(drinksFrame, text='Cold Drinks (Rs.25)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0,
                         variable=var18
                         , command=colddrinks)
colddrinks.grid(row=8, column=0, sticky=W)

# entry fields for drink items

textlassi = Entry(drinksFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_lassi)
textlassi.grid(row=0, column=1)

textcoffee = Entry(drinksFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1, column=1)

textfaluda = Entry(drinksFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_faluda)
textfaluda.grid(row=2, column=1)

textshikanji = Entry(drinksFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_shikanji)
textshikanji.grid(row=3, column=1)

textjaljeera = Entry(drinksFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_jaljeera)
textjaljeera.grid(row=4, column=1)

textroohafza = Entry(drinksFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_roohafza)
textroohafza.grid(row=5, column=1)

textmasalatea = Entry(drinksFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_masalatea)
textmasalatea.grid(row=6, column=1)

textbadammilk = Entry(drinksFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_badammilk)
textbadammilk.grid(row=7, column=1)

textcolddrinks = Entry(drinksFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coldrinks)
textcolddrinks.grid(row=8, column=1)

# Cakes

oreocake = Checkbutton(cakesFrame, text='Oreo (Rs.220)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var19
                       , command=oreo)
oreocake.grid(row=0, column=0, sticky=W)

applecake = Checkbutton(cakesFrame, text='Apple (Rs.180)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var20
                        , command=apple)
applecake.grid(row=1, column=0, sticky=W)

kitkatcake = Checkbutton(cakesFrame, text='Kitkat (Rs.225)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var21
                         , command=kitkat)
kitkatcake.grid(row=2, column=0, sticky=W)

vanillacake = Checkbutton(cakesFrame, text='Vanilla (Rs.160)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var22
                          , command=vanilla)
vanillacake.grid(row=3, column=0, sticky=W)

bananacake = Checkbutton(cakesFrame, text='Banana (Rs.160)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var23
                         , command=banana)
bananacake.grid(row=4, column=0, sticky=W)

browniecake = Checkbutton(cakesFrame, text='Brownie (Rs.250)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0, variable=var24
                          , command=brownie)
browniecake.grid(row=5, column=0, sticky=W)

pineapplecake = Checkbutton(cakesFrame, text='Pineapple (Rs.190)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0,
                            variable=var25
                            , command=pineapple)
pineapplecake.grid(row=6, column=0, sticky=W)

chocolatecake = Checkbutton(cakesFrame, text='Chocolate (Rs.220)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0,
                            variable=var26
                            , command=chocolate)
chocolatecake.grid(row=7, column=0, sticky=W)

blackforestcake = Checkbutton(cakesFrame, text='BlackForest(Rs.300)', font=('Script MT Bold', 18, 'bold'), onvalue=1, offvalue=0,
                              variable=var27
                              , command=blackforest)
blackforestcake.grid(row=8, column=0, sticky=W)

# entry fields for cakes

textoreo = Entry(cakesFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=0, column=1)

textapple = Entry(cakesFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_apple)
textapple.grid(row=1, column=1)

textkitkat = Entry(cakesFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkat)
textkitkat.grid(row=2, column=1)

textvanilla = Entry(cakesFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vanilla)
textvanilla.grid(row=3, column=1)

textbanana = Entry(cakesFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_banana)
textbanana.grid(row=4, column=1)

textbrownie = Entry(cakesFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=5, column=1)

textpineapple = Entry(cakesFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pineapple)
textpineapple.grid(row=6, column=1)

textchocolate = Entry(cakesFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chocolate)
textchocolate.grid(row=7, column=1)

textblackforest = Entry(cakesFrame, font=('Script MT Bold', 18, 'bold'), bd=7, width=6, state=DISABLED,
                        textvariable=e_blackforest)
textblackforest.grid(row=8, column=1)



def Cart():
    Cart=Toplevel(root)
    Cart.title("CART")
    Cart.geometry("500x550")
    l1=Label(Cart,text="---CART---",font=("algerian",15,'bold')).pack()

    billarea=Frame(Cart,bd=10,highlightbackground='black',highlightthickness=4,relief=SUNKEN,bg="black")
    billarea.place(x=0,y=25,width=500,height=500)
    scrol_y=Scrollbar(billarea,orient=VERTICAL)
    txtarea=Text(billarea,yscrollcommand=scrol_y.set)
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH,expand=1)
    x=random.randint(1000,9999)
    def BILL():
        txtarea.delete(1.0,END)
        txtarea.insert(END,"\t\tWELCOME TO HOTEL\nPhone-No.7392754100")
        txtarea.insert(END,f"\t\n\nBill no. : {str(x)}")
        txtarea.insert(END,"\t\n==============================================\n")
        txtarea.insert(END,"\t\nProduct\t\t\tQty\t\tPrice\n")
        txtarea.insert(END,"\t\n==============================================\n")
    def billarea():
        BILL()
        s=[]
        if int(textroti.get())!=0:
            txtarea.insert(END,f"Roti\t\t\t {textroti.get()}\t\t{int(textroti.get())*20}\n")
            s.append(int(textroti.get())*20)
        if int(textdaal.get())!=0:
            txtarea.insert(END,f"Daal\t\t\t {textdaal.get()}\t\t{int(textdaal.get())*50}\n")
            s.append(int(textdaal.get())*50)
        if int(textfish.get())!=0:
            txtarea.insert(END,f"Fish\t\t\t {textfish.get()}\t\t{int(textfish.get())*120}\n")
            s.append(int(textfish.get())*120)
        if int(textsabji.get())!=0:
            txtarea.insert(END,f"Sabji\t\t\t {textsabji.get()}\t\t{int(textsabji.get())*80}\n")
            s.append(int(textsabji.get())*80)
        if int(textkebab.get())!=0:
            txtarea.insert(END, f"Kebab\t\t\t {textkebab.get()}\t\t{int(textkebab.get()) * 180}\n")
            s.append(int(textkebab.get()) * 180)
        if int(textchawal.get()) != 0:
            txtarea.insert(END, f"Chawal\t\t\t {textchawal.get()}\t\t{int(textchawal.get()) * 80}\n")
            s.append(int(textchawal.get()) * 80)
        if int(textmutton.get()) != 0:
            txtarea.insert(END, f"Mutton\t\t\t {textmutton.get()}\t\t{int(textmutton.get()) *165}\n")
            s.append(int(textmutton.get()) *165)
        if int(textpaneer.get()) != 0:
            txtarea.insert(END, f"Paneer\t\t\t {textpaneer.get()}\t\t{int(textpaneer.get()) *150}\n")
            s.append(int(textpaneer.get()) * 150)
        if int(textchicken.get()) != 0:
            txtarea.insert(END, f"chicken\t\t\t {textchicken.get()}\t\t{int(textchicken.get()) *140}\n")
            s.append(int(textchicken.get()) * 140)
        #Drinks
        if int(textlassi.get()) != 0:
            txtarea.insert(END, f"Lassi\t\t\t {textlassi.get()}\t\t{int(textlassi.get()) * 65}\n")
            s.append(int(textlassi.get()) * 65)
        if int(textcoffee.get()) != 0:
            txtarea.insert(END, f"Coffee\t\t\t {textcoffee.get()}\t\t{int(textcoffee.get()) * 40}\n")
            s.append(int(textcoffee.get())*40)
        if int(textfaluda.get()) != 0:
            txtarea.insert(END, f"Faluda\t\t\t {textfaluda.get()}\t\t{int(textfaluda.get()) * 75}\n")
            s.append(int(textfaluda.get())*75)
        if int(textshikanji.get()) != 0:
                txtarea.insert(END, f"Shikanji\t\t\t {textshikanji.get()}\t\t{int(textshikanji.get()) * 45}\n")
                s.append(int(textshikanji.get()) * 45)
        if int(textjaljeera.get()) != 0:
                txtarea.insert(END, f"Jaljeera\t\t\t {textjaljeera.get()}\t\t{int(textjaljeera.get()) * 35}\n")
                s.append(int(textjaljeera.get()) * 35)
        if int(textroohafza.get()) != 0:
                txtarea.insert(END, f"Roohafza\t\t\t {textroohafza.get()}\t\t{int(textroohafza.get()) * 60}\n")
                s.append(int(textroohafza.get()) * 60)
        if int(textmasalatea.get()) != 0:
                txtarea.insert(END, f"Masala Tea\t\t\t {textmasalatea.get()}\t\t{int(textmasalatea.get()) * 15}\n")
                s.append(int(textmasalatea.get()) * 15)
        if int(textbadammilk.get()) != 0:
                txtarea.insert(END, f"Badam Milk\t\t\t {textbadammilk.get()}\t\t{int(textbadammilk.get()) * 25}\n")
                s.append(int(textbadammilk.get()) * 25)
        if int(textcolddrinks.get()) != 0:
                txtarea.insert(END, f"Cold Drinks\t\t\t {textcolddrinks.get()}\t\t{int(textcolddrinks.get()) * 25}\n")
                s.append(int(textcolddrinks.get()) * 25)
        #Cakes
        if int(textoreo.get()) != 0:
                txtarea.insert(END, f"Oreo Cake\t\t\t {textoreo.get()}\t\t{int(textoreo.get()) * 220}\n")
                s.append(int(textoreo.get()) * 220)
        if int(textapple.get()) != 0:
                txtarea.insert(END, f"Apple Cake\t\t\t {textapple.get()}\t\t{int(textapple.get()) * 180}\n")
                s.append(int(textapple.get()) * 180)
        if int(textkitkat.get()) != 0:
                txtarea.insert(END, f"KitKat Cake\t\t\t {textkitkat.get()}\t\t{int(textkitkat.get()) * 225}\n")
                s.append(int(textkitkat.get()) * 225)
        if int(textvanilla.get()) != 0:
                txtarea.insert(END, f"Vanilla\t\t\t {textvanilla.get()}\t\t{int(textvanilla.get()) * 160}\n")
                s.append(int(textvanilla.get()) * 160)
        if int(textbanana.get()) != 0:
                txtarea.insert(END, f"Banana Cake\t\t\t {textbanana.get()}\t\t{int(textbanana.get()) * 160}\n")
                s.append(int(textbanana.get()) * 160)
        if int(textbrownie.get()) != 0:
                txtarea.insert(END, f"Brownie Cake\t\t\t {textbrownie.get()}\t\t{int(textbrownie.get()) * 250}\n")
                s.append(int(textbrownie.get()) * 250)
        if int(textpineapple.get()) != 0:
                txtarea.insert(END, f"Pineapple Cake\t\t\t {textpineapple.get()}\t\t{int(textpineapple.get()) * 190}\n")
                s.append(int(textpineapple.get()) * 190)
        if int(textchocolate.get()) != 0:
                txtarea.insert(END, f"Chocolate Cake\t\t\t {textchocolate.get()}\t\t{int(textchocolate.get()) * 220}\n")
                s.append(int(textchocolate.get()) * 220)
        if int(textblackforest.get()) != 0:
                txtarea.insert(END, f"Black Forest Cake\t\t\t {textblackforest.get()}\t\t{int(textblackforest.get()) * 300}\n")
                s.append(int(textblackforest.get()) * 300)
        def Billtab():
            Billtab=Toplevel(root)
            Billtab.title("CART")
            Billtab.geometry("500x550")
            l1=Label(Billtab,text="---BILL---",font=("algerian",15,'bold')).pack()

            billarea1=Frame(Billtab,bd=10,highlightbackground='black',highlightthickness=4,relief=SUNKEN,bg="black")
            billarea1.place(x=0,y=25,width=500,height=500)
            scrol_y=Scrollbar(billarea1,orient=VERTICAL)
            txtarea1=Text(billarea1,yscrollcommand=scrol_y.set)
            scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=txtarea1.yview)
            txtarea1.pack(fill=BOTH,expand=1)
            global X
            def BILL1():
                txtarea1.delete(1.0,END)
                txtarea1.insert(END,"\t\tWELCOME TO HOTEL\nPhone-No.7392754100")
                txtarea1.insert(END,f"\t\n\nBill no. : {str(x)}")
                txtarea1.insert(END,"\t\n==============================================\n")
                txtarea1.insert(END,"\t\nProduct\t\t\tQty\t\tPrice\n")
                txtarea1.insert(END,"\t\n==============================================\n")
            def billarea1():
                BILL1()
                s=[]
                if int(textroti.get())!=0:
                    txtarea1.insert(END,f"Roti\t\t\t {textroti.get()}\t\t{int(textroti.get())*20}\n")
                    s.append(int(textroti.get())*20)
                if int(textdaal.get())!=0:
                    txtarea1.insert(END,f"Daal\t\t\t {textdaal.get()}\t\t{int(textdaal.get())*50}\n")
                    s.append(int(textdaal.get())*50)
                if int(textfish.get())!=0:
                    txtarea1.insert(END,f"Fish\t\t\t {textfish.get()}\t\t{int(textfish.get())*120}\n")
                    s.append(int(textfish.get())*120)
                if int(textsabji.get())!=0:
                    txtarea1.insert(END,f"Sabji\t\t\t {textsabji.get()}\t\t{int(textsabji.get())*80}\n")
                    s.append(int(textsabji.get())*80)
                if int(textkebab.get())!=0:
                    txtarea1.insert(END, f"Kebab\t\t\t {textkebab.get()}\t\t{int(textkebab.get()) * 180}\n")
                    s.append(int(textkebab.get()) * 180)
                if int(textchawal.get()) != 0:
                    txtarea1.insert(END, f"Chawal\t\t\t {textchawal.get()}\t\t{int(textchawal.get()) * 80}\n")
                    s.append(int(textchawal.get()) * 80)
                if int(textmutton.get()) != 0:
                    txtarea1.insert(END, f"Mutton\t\t\t {textmutton.get()}\t\t{int(textmutton.get()) *165}\n")
                    s.append(int(textmutton.get()) *165)
                if int(textpaneer.get()) != 0:
                    txtarea1.insert(END, f"Paneer\t\t\t {textpaneer.get()}\t\t{int(textpaneer.get()) *150}\n")
                    s.append(int(textpaneer.get()) * 150)
                if int(textchicken.get()) != 0:
                    txtarea1.insert(END, f"chicken\t\t\t {textchicken.get()}\t\t{int(textchicken.get()) *140}\n")
                    s.append(int(textchicken.get()) * 140)
                #Drinks
                if int(textlassi.get()) != 0:
                    txtarea1.insert(END, f"Lassi\t\t\t {textlassi.get()}\t\t{int(textlassi.get()) * 65}\n")
                    s.append(int(textlassi.get()) * 65)
                if int(textcoffee.get()) != 0:
                    txtarea1.insert(END, f"Coffee\t\t\t {textcoffee.get()}\t\t{int(textcoffee.get()) * 40}\n")
                    s.append(int(textcoffee.get())*40)
                if int(textfaluda.get()) != 0:
                    txtarea1.insert(END, f"Faluda\t\t\t {textfaluda.get()}\t\t{int(textfaluda.get()) * 75}\n")
                    s.append(int(textfaluda.get())*75)
                if int(textshikanji.get()) != 0:
                    txtarea1.insert(END, f"Shikanji\t\t\t {textshikanji.get()}\t\t{int(textshikanji.get()) * 45}\n")
                    s.append(int(textshikanji.get()) * 45)
                if int(textjaljeera.get()) != 0:
                    txtarea1.insert(END, f"Jaljeera\t\t\t {textjaljeera.get()}\t\t{int(textjaljeera.get()) * 35}\n")
                    s.append(int(textjaljeera.get()) * 35)
                if int(textroohafza.get()) != 0:
                    txtarea1.insert(END, f"Roohafza\t\t\t {textroohafza.get()}\t\t{int(textroohafza.get()) * 60}\n")
                    s.append(int(textroohafza.get()) * 60)
                if int(textmasalatea.get()) != 0:
                    txtarea1.insert(END, f"Masala Tea\t\t\t {textmasalatea.get()}\t\t{int(textmasalatea.get()) * 15}\n")
                    s.append(int(textmasalatea.get()) * 15)
                if int(textbadammilk.get()) != 0:
                    txtarea1.insert(END, f"Badam Milk\t\t\t {textbadammilk.get()}\t\t{int(textbadammilk.get()) * 25}\n")
                    s.append(int(textbadammilk.get()) * 25)
                if int(textcolddrinks.get()) != 0:
                    txtarea1.insert(END, f"Cold Drinks\t\t\t {textcolddrinks.get()}\t\t{int(textcolddrinks.get()) * 25}\n")
                    s.append(int(textcolddrinks.get()) * 25)
                #Cakes
                if int(textoreo.get()) != 0:
                    txtarea1.insert(END, f"Oreo Cake\t\t\t {textoreo.get()}\t\t{int(textoreo.get()) * 220}\n")
                    s.append(int(textoreo.get()) * 220)
                if int(textapple.get()) != 0:
                    txtarea1.insert(END, f"Apple Cake\t\t\t {textapple.get()}\t\t{int(textapple.get()) * 180}\n")
                    s.append(int(textapple.get()) * 180)
                if int(textkitkat.get()) != 0:
                    txtarea1.insert(END, f"KitKat Cake\t\t\t {textkitkat.get()}\t\t{int(textkitkat.get()) * 225}\n")
                    s.append(int(textkitkat.get()) * 225)
                if int(textvanilla.get()) != 0:
                    txtarea1.insert(END, f"Vanilla\t\t\t {textvanilla.get()}\t\t{int(textvanilla.get()) * 160}\n")
                    s.append(int(textvanilla.get()) * 160)
                if int(textbanana.get()) != 0:
                    txtarea1.insert(END, f"Banana Cake\t\t\t {textbanana.get()}\t\t{int(textbanana.get()) * 160}\n")
                    s.append(int(textbanana.get()) * 160)
                if int(textbrownie.get()) != 0:
                    txtarea1.insert(END, f"Brownie Cake\t\t\t {textbrownie.get()}\t\t{int(textbrownie.get()) * 250}\n")
                    s.append(int(textbrownie.get()) * 250)
                if int(textpineapple.get()) != 0:
                    txtarea1.insert(END, f"Pineapple Cake\t\t\t {textpineapple.get()}\t\t{int(textpineapple.get()) * 190}\n")
                    s.append(int(textpineapple.get()) * 190)
                if int(textchocolate.get()) != 0:
                    txtarea1.insert(END, f"Chocolate Cake\t\t\t {textchocolate.get()}\t\t{int(textchocolate.get()) * 220}\n")
                    s.append(int(textchocolate.get()) * 220)
                if int(textblackforest.get()) != 0:
                    txtarea1.insert(END, f"Black Forest Cake\t\t\t {textblackforest.get()}\t\t{int(textblackforest.get()) * 300}\n")
                    s.append(int(textblackforest.get()) * 300)
                txtarea1.insert(END,"\t\n==============================================\n")
                txtarea1.insert(END,f"\nBill Amount :\t\t\t\t\t{sum(s)}\n")
                txtarea1.insert(END,f"\nDiscount :\t\t\t\t\t{sum(s)/10} \n")
                txtarea1.insert(END,f"\nTotal Bill Amount :\t\t\t\t\t{sum(s)-sum(s)/10}\n")

            billarea1()
            Cart.destroy()
        Q1=Button(Cart,text="Confirm Order",font=('algerian',15,'bold'),activebackground='black',command=Billtab)
        Q1.place(x=160,y=450)


    def total():
        billarea()
    total()






def clear():
    e_roti.set('0')
    e_daal.set('0')
    e_sabji.set('0')
    e_fish.set('0')

    e_kebab.set('0')
    e_chawal.set('0')
    e_mutton.set('0')
    e_chicken.set('0')
    e_paneer.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_roohafza.set('0')
    e_shikanji.set('0')
    e_jaljeera.set('0')
    e_masalatea.set('0')
    e_badammilk.set('0')
    e_coldrinks.set('0')

    e_kitkat.set('0')
    e_banana.set('0')
    e_pineapple.set('0')
    e_apple.set('0')
    e_chocolate.set('0')
    e_oreo.set('0')
    e_blackforest.set('0')
    e_brownie.set('0')
    e_vanilla.set('0')

    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')
    var6.set('0')
    var7.set('0')
    var8.set('0')
    var9.set('0')
    var10.set('0')
    var11.set('0')
    var12.set('0')
    var13.set('0')
    var14.set('0')
    var15.set('0')
    var16.set('0')
    var17.set('0')
    var18.set('0')
    var19.set('0')
    var20.set('0')
    var21.set('0')
    var22.set('0')
    var23.set('0')
    var24.set('0')
    var25.set('0')
    var26.set('0')
    var27.set('0')
    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textkebab.config(state=DISABLED)
    textchawal.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textmasalatea.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textcolddrinks.config(state=DISABLED)
    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)
def exit():
    root.destroy()

B1=Button(root,text="Cart",font=('algerian',15,'bold'),activebackground='black',command=Cart)
B1.place(x=1100,y=250)
B2=Button(root,text="Clear",font=('algerian',15,'bold'),activebackground='black',command=clear)
B2.place(x=1100,y=350)
B3=Button(root,text="Exit",font=('algerian',15,'bold'),activebackground='black',command=exit)
B3.place(x=1100,y=450)


root.mainloop()
