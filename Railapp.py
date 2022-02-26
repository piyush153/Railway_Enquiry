from tkinter import *
from tkinter import messagebox
import requests

apikey = "fbc883cdff4385dd61d80b41c9a1bda3"


# pnr=6736154164
#######################################################for pnr status#######################################
def pnr_status():
    nw = Tk()
    nw.geometry("400x300")
    nw.title("CHECK PNR")
    lab1 = Label(nw, text="Please enter PNR number", fg="blue", bg="OliveDrab1")
    lab1.pack(fill=X)
    e1 = Entry(nw, relief=RAISED)
    e1.pack()
    bt = Button(nw, text="OK", command=lambda: dis(), bg="snow")
    bt.pack(fill=X)
    result = Label(nw, text="", justify=LEFT)
    result.pack(fill=X)

    def dis():
        url = "http://indianrailapi.com/api/v2/PNRCheck/apikey/{}/PNRNumber/{}/Route/1/".format(apikey, e1.get())
        print(url)
        response = requests.get(url)
        response = response.json()
        print(response)
        response_code = response['ResponseCode']
        if response_code == '201':
            if 'Message' in response:
                messagebox.showinfo('Something Went Wrong', response['Message'])
            else:
                messagebox.showinfo("SORRY!", "Something Went Wrong")
        else:
            result.configure(text="Passenger No.     Booking status    Current Status\n\n", fg="blue")
            for i in response['Passangers']:
                result_text = result['text'] + i['Passenger'] + "         " + i['BookingStatus'] + "        " + i[
                    'CurrentStatus'] + "\n\n"
                result.configure(text=result_text)


###################################################FOR LIVE STATION###################################################
def livestation():
    nw = Tk()
    nw.configure(bg="snow")
    nw.geometry("400x300")
    nw.title("Station_LiveStatus")
    lab1 = Label(nw, text="Station Code", fg="blue", bg="OliveDrab1")
    lab1.pack(fill=X)
    e1 = Entry(nw, relief=RAISED)
    e1.pack()
    lab2 = Label(nw, text="Hours", fg="black", bg="Deep sky blue")
    lab2.pack()
    e2 = Entry(nw, relief=RAISED)
    e2.pack()
    bt = Button(nw, text="Search", command=lambda: dis2())
    bt.pack(fill=X)

    def dis2():
        url = "http://indianrailapi.com/api/v2/LiveStation/apikey/{}/StationCode/{}/hours/{}/".format(apikey, e1.get(),
                                                                                                      e2.get())
        print(url)
        response = requests.get(url)
        response = response.json()
        print(response)
        response_code = response['ResponseCode']
        if response_code == '201':
            messagebox.showinfo('Something Went Wrong', response['Message'])

        else:
            result.configure(text="Train Name  \n", fg="blue")
            result1.configure(text="   Sch.Arr\n", fg="blue")
            result2.configure(text="Sch.Dep\n", fg="blue")
            result3.configure(text="   Exp.Arr\n", fg="blue")
            result4.configure(text="   Exp.Dep \n", fg="blue")
            result5.configure(text="   PF No.\n", fg="blue")
            for i in response['Trains']:
                print(i)
                result_text = result['text'] + i['Name'] + "\n "
                result.configure(text=result_text)
                result_text1 = result1['text'] + i['ScheduleArrival'] + "\n "
                result1.configure(text=result_text1)
                result_text2 = result2['text'] + "   " + i['ScheduleDeparture'] + "\n "
                result2.configure(text=result_text2)
                result_text3 = result3['text'] + "   " + i['ExpectedArrival'] + "\n "
                result3.configure(text=result_text3)
                result_text4 = result4['text'] + "   " + i['ExpectedDeparture'] + "\n "
                result4.configure(text=result_text4)
                result_text5 = result5['text'] + "   " + i['Platform'] + "\n "
                result5.configure(text=result_text5)


#########################################FOR TRAIN LIVE STATUS############################################
def livetrain():
    nw = Tk()
    nw.configure(bg="plum2")
    nw.geometry("400x300")
    nw.title("LIVE STATUS")
    lab1 = Label(nw, text="please enter the train number", fg="blue", bg="OliveDrab1")
    lab1.pack(fill=X)
    e1 = Entry(nw, relief=RAISED)
    e1.pack()
    lab4 = Label(nw, text="please enter the date in yyyymmdd format", fg="blue")
    lab4.pack(fill=X)
    e2 = Entry(nw, relief=RAISED)
    e2.pack()
    bt = Button(nw, text="Click Here", command=lambda: dis2(), bg="orange", fg="black")
    bt.pack(fill=X)

    def dis2():
        url = "http://indianrailapi.com/api/v2/livetrainstatus/apikey/{}/trainnumber/{}/date/{}/".format(apikey,
                                                                                                         e1.get(),
                                                                                                         e2.get())
        print(url)
        response = requests.get(url)
        response = response.json()
        print(response)
        response_code = response['ResponseCode']
        if response_code == '201':
            messagebox.showinfo('Something Went Wrong', response['Message'])
        else:
            result.configure(text="Train Name\n\n" + response['CurrentStation']['StationName'] + " **\n", fg="blue")
            result1.configure(text="   Sch.Arr\n\n" + "   " + response['CurrentStation']['ScheduleArrival'] + "\n ",
                              fg="blue")
            result2.configure(text="   Act.Arr\n\n" + "   " + response['CurrentStation']['ActualArrival'] + "\n ",
                              fg="blue")
            result3.configure(
                text="   Delay in .Arr\n\n" + "   " + response['CurrentStation']['DelayInArrival'] + "\n ",
                fg="blue")
            result4.configure(text="   Sch.Dep \n\n" + "   " + response['CurrentStation']['ScheduleDeparture'] + "\n ",
                              fg="blue")
            result5.configure(text="   Act.Dep\n\n" + "   " + response['CurrentStation']['ActualDeparture'] + "\n ",
                              fg="blue")
            result6.configure(
                text="   Delay in .Dep\n\n" + "   " + response['CurrentStation']['DelayInDeparture'] + "\n ", fg="blue")
            result7.configure(text="   Day\n\n" + "   " + response['CurrentStation']['Day'] + "\n ", fg="blue")

            for i in response['TrainRoute']:
                result_text = result['text'] + i['StationName'] + "\n "
                result.configure(text=result_text)
                result_text1 = result1['text'] + "   " + i['ScheduleArrival'] + "\n "
                result1.configure(text=result_text1)
                result_text2 = result2['text'] + "   " + i['ActualArrival'] + "\n "
                result2.configure(text=result_text2)
                result_text3 = result3['text'] + "   " + i['DelayInArrival'] + "\n "
                result3.configure(text=result_text3)
                result_text4 = result4['text'] + "   " + i['ScheduleDeparture'] + "\n "
                result4.configure(text=result_text4)
                result_text5 = result5['text'] + "   " + i['ActualDeparture'] + "\n "
                result5.configure(text=result_text5)
                result_text6 = result6['text'] + "   " + i['DelayInDeparture'] + "\n "
                result6.configure(text=result_text6)
                result_text7 = result7['text'] + "   " + i['Day'] + "\n "
                result7.configure(text=result_text7)


##################################################FOR SEAT AVAILABILITY######################################
def vacant():
    nw = Tk()
    nw.configure(bg="khaki1")
    nw.geometry("700x500")
    nw.title("Seat Availability")
    lab1 = Label(nw, text="Please Enter the Train Number", fg="blue4", bg="OliveDrab1")
    lab1.pack(fill=X)
    e1 = Entry(nw, relief=RAISED)
    e1.pack()
    lab2 = Label(nw, text="From ", bg="white", fg="blue4")
    lab2.pack()
    e2 = Entry(nw, relief=RAISED)
    e2.pack()
    lab9 = Label(nw, text="To", bg="white", fg="blue")
    lab9.pack()
    e3 = Entry(nw, relief=RAISED)
    e3.pack()
    lab4 = Label(nw, text="Please Enter the Date in yyyymmdd format", bg="white", fg="blue")
    lab4.pack()
    e4 = Entry(nw, relief=RAISED)
    e4.pack()
    lab5 = Label(nw, text="Enter the class 1A/2A/3A/SL", bg="white", fg="blue")
    lab5.pack()
    e5 = Entry(nw, relief=RAISED, bg="white", fg="blue")
    e5.pack()
    bt = Button(nw, text="Search", command=lambda: dis2(), bg="black", fg="white")
    bt.pack(fill=X)
    result = Label(nw, text="", fg="blue", justify=LEFT)
    result.pack(fill=X)

    def dis2():
        url = "https://indianrailapi.com/api/v2/SeatAvailability/apikey/{}/TrainNumber/{}/From/{}/To/{}/Date/{}/Quota/GN/Class/{}".format(
            apikey, e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
        print(url)
        response = requests.get(url)
        response = response.json()
        print(response)
        response_code = response['ResponseCode']
        if response_code == '201':
            messagebox.showinfo('Something Went Wrong', response['Message'])
        else:
            result.configure(text=" Date          Availability     Chance\n\n")
            for i in response['Availability']:
                result_text = result['text'] + i['JourneyDate'] + "    " + i['Availability'] + "    " + i[
                    'Confirm'] + "\n\n"
                result.configure(text=result_text)


#####################################TRAIN INFORMATION############################################
def train_info():
    nw = Tk()
    nw.geometry("400x300")
    nw.title("Train Information")
    lab1 = Label(nw, text="Please enter TRAIN number", fg="blue", bg="OliveDrab1")
    lab1.pack(fill=X)
    e1 = Entry(nw, relief=RAISED)
    e1.pack()
    bt = Button(nw, text="OK", command=lambda: dis(), bg="snow")
    bt.pack(fill=X)
    result = Label(nw, text="", justify=LEFT)
    result.pack(fill=X)

    def dis():
        url = "http://indianrailapi.com/api/v2/TrainInformation/apikey/{}/TrainNumber/{}/".format(apikey, e1.get())
        print(url)
        response = requests.get(url)
        response = response.json()
        print(response)
        response_code = response['ResponseCode']
        if response_code == '201':
            if 'Message' in response:
                messagebox.showinfo('Something Went Wrong', response['Message'])
            else:
                messagebox.showinfo("SORRY!", "Something Went Wrong")
        else:

            b = response['TrainName']

            result.configure(text="Train Name:" + b, fg="blue")


#####################################################MAIN PAGE#############################################
abc = Tk()
abc.configure(bg='SkyBlue1')

abc.geometry("800x400")
abc.title("Raiway_App")
label1 = Label(abc, text="Choose from the options Below ", fg="blue", bg="OliveDrab1", font=("arial", 16, "bold"))
label1.pack(fill=X)
pnr_status = Button(abc, text="PNR STATUS", command=pnr_status, fg="black", bg="mint cream")
pnr_status.pack(fill=X)
live_station = Button(abc, text="LIVE STATION", command=livestation, fg="black", bg="mint cream")
live_station.pack(fill=X)
live_status = Button(abc, text="TRAIN LIVE STATUS", command=livetrain, fg="black", bg="mint cream")
live_status.pack(fill=X)
seat_available = Button(abc, text="SEAT AVAILABILITY", command=vacant, fg="black", bg="mint cream")
seat_available.pack(fill=X)
train_info = Button(abc, text="TRAIN INFORMATION", command=train_info, fg="black", bg="mint cream")
train_info.pack(fill=X)

abc.mainloop()