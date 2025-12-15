import wx
from datetime import datetime, date

# ----------- Functions -----------

def is_valid_date(d):
    parts = d.split("-")
    if len(parts) != 3:
        return False

    day, month, year = parts

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    day = int(day)
    month = int(month)
    year = int(year)

    if year < 1 or month < 1 or month > 12 or day < 1:
        return False

    # Days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Leap year check
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29

    if day > days_in_month[month - 1]:
        return False

    return True

def get_date():
    d = txt_date.GetValue()
    if is_valid_date(d):
        day, month, year = map(int, d.split("-"))
        return date(year, month, day)
    else:
        wx.MessageBox("Enter valid date in DD-MM-YYYY format", "Error")
        return None
    
    
def day_of_week(event):
    d = get_date()
    if d:
        days = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
        lbl_result.SetLabel("Day : " + days[d.weekday()])


def calculate_age(event):
    dob = get_date()
    if dob:
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        lbl_result.SetLabel(f"Age : {age} years")

def countdown(event):
    future = get_date()
    if future:
        today = date.today()
        days = (future - today).days
        if days >= 0:
            lbl_result.SetLabel(f"{days} days remaining")
        else:
            lbl_result.SetLabel("Date already passed")

# ----------- GUI -----------

app = wx.App()

frame = wx.Frame(None, title="Date & Time Applications", size=(400, 320))
panel = wx.Panel(frame)

vbox = wx.BoxSizer(wx.VERTICAL)

lbl = wx.StaticText(panel, label="Enter Date (DD-MM-YYYY)")
vbox.Add(lbl, 0, wx.ALL, 5)

txt_date = wx.TextCtrl(panel)
vbox.Add(txt_date, 0, wx.EXPAND | wx.ALL, 5)

btn_day = wx.Button(panel, label="Day of the Week")
btn_age = wx.Button(panel, label="Calculate Age")
btn_count = wx.Button(panel, label="Countdown")

vbox.Add(btn_day, 0, wx.EXPAND | wx.ALL, 5)
vbox.Add(btn_age, 0, wx.EXPAND | wx.ALL, 5)
vbox.Add(btn_count, 0, wx.EXPAND | wx.ALL, 5)

lbl_result = wx.StaticText(panel, label="")
vbox.Add(lbl_result, 0, wx.ALL, 10)

panel.SetSizer(vbox)

# ----------- Event Binding -----------

btn_day.Bind(wx.EVT_BUTTON, day_of_week)
btn_age.Bind(wx.EVT_BUTTON, calculate_age)
btn_count.Bind(wx.EVT_BUTTON, countdown)

frame.Show()
app.MainLoop()
