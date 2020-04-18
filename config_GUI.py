#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.5 on Sun Apr 19 00:18:24 2020
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.spin_ctrl_9 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_10 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_11 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_12 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_13 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_20 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_19 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_14 = wx.SpinCtrl(self, wx.ID_ANY, "1", min=1, max=100)
        self.spin_ctrl_15 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=-100, max=100)
        self.spin_ctrl_16 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_17 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_18 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.checkbox_7 = wx.CheckBox(self, wx.ID_ANY, "Death from hunger")
        self.spin_ctrl_2 = wx.SpinCtrl(self, wx.ID_ANY, "1", min=1, max=100)
        self.spin_ctrl_4 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_5 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_6 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_7 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_8 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.checkbox_3 = wx.CheckBox(self, wx.ID_ANY, "PyGame preview\n")
        self.checkbox_4 = wx.CheckBox(self, wx.ID_ANY, "Save JSON")
        self.checkbox_5 = wx.CheckBox(self, wx.ID_ANY, "Gene data is numerical\n(only in summary mode)")
        self.radio_box_1 = wx.RadioBox(self, wx.ID_ANY, "CSV output mode", choices=["Summary", "Detail", "OFF"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.spin_ctrl_3 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.text_ctrl_7 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_ctrl_8 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.check_list_box_1 = wx.CheckListBox(self, wx.ID_ANY, choices=["ID", "Gender", "Parents", "Position", "Energy", "Breeding need", "Speed gene", "Attention threshold gene", "Breeding threshold gene", "Interest in eating gene", "Mutation resistance"])
        self.button_1 = wx.Button(self, wx.ID_ANY, "Revert to default")
        self.button_2 = wx.Button(self, wx.ID_ANY, "Save")
        self.button_3 = wx.Button(self, wx.ID_ANY, "Start\n")
        self.text_ctrl_9 = wx.TextCtrl(self, wx.ID_ANY, "Error bar", style=wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Simulation configuration")
        self.spin_ctrl_13.SetToolTip("0 disables the condition")
        self.spin_ctrl_20.SetToolTip("0 disables the condition")
        self.spin_ctrl_19.SetToolTip("Isn't used when 0; if higher consumed energy is multiplied by its logarithm of this value")
        self.spin_ctrl_15.SetToolTip("If lower than 0 animal will be guaranteed to wait this amount of turns")
        self.radio_box_1.SetSelection(2)
        self.button_1.SetMinSize((108, 26))
        self.button_2.SetMinSize((88, 26))
        self.button_3.SetMinSize((88, 26))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Data export settings"), wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.VERTICAL)
        sizer_15 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.GridSizer(3, 2, 0, 0)
        sizer_26 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_27 = wx.BoxSizer(wx.VERTICAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Gene settings"), wx.VERTICAL)
        sizer_20 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Starting mean values"), wx.VERTICAL)
        sizer_25 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_24 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_23 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_22 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_21 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_28 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Simulation settings"), wx.VERTICAL)
        sizer_34 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_33 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_32 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_31 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_30 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_29 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Finish conditions"), wx.VERTICAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Start conditions"), wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Map side length")
        label_4.SetToolTip("1 = 20 field positions")
        sizer_7.Add(label_4, 1, wx.ALIGN_CENTER | wx.ALL, 1)
        sizer_7.Add(self.spin_ctrl_9, 0, 0, 0)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Animal starting amount")
        sizer_8.Add(label_5, 1, wx.ALIGN_CENTER | wx.ALL, 1)
        sizer_8.Add(self.spin_ctrl_10, 0, 0, 0)
        sizer_6.Add(sizer_8, 1, wx.EXPAND, 0)
        label_6 = wx.StaticText(self, wx.ID_ANY, "Plant starting amount")
        sizer_9.Add(label_6, 1, wx.ALIGN_CENTER | wx.ALL, 1)
        sizer_9.Add(self.spin_ctrl_11, 0, 0, 0)
        sizer_6.Add(sizer_9, 1, wx.EXPAND, 0)
        label_14 = wx.StaticText(self, wx.ID_ANY, "Starting energy level")
        sizer_10.Add(label_14, 1, wx.ALIGN_CENTER | wx.ALL, 1)
        sizer_10.Add(self.spin_ctrl_12, 0, 0, 0)
        sizer_6.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_6, 1, wx.ALL | wx.EXPAND, 2)
        label_7 = wx.StaticText(self, wx.ID_ANY, "Max turns")
        sizer_11.Add(label_7, 1, wx.ALIGN_CENTER | wx.ALL, 1)
        sizer_11.Add(self.spin_ctrl_13, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(sizer_11, 1, wx.EXPAND, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, "Max animals")
        sizer_12.Add(label_8, 1, wx.ALIGN_CENTER | wx.ALL, 1)
        sizer_12.Add(self.spin_ctrl_20, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_2.Add(grid_sizer_1, 1, wx.ALL | wx.EXPAND, 2)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        label_20 = wx.StaticText(self, wx.ID_ANY, "Moving modificator")
        sizer_29.Add(label_20, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_29.Add(self.spin_ctrl_19, 0, 0, 0)
        sizer_28.Add(sizer_29, 1, wx.EXPAND, 0)
        label_21 = wx.StaticText(self, wx.ID_ANY, "Sight")
        sizer_30.Add(label_21, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_30.Add(self.spin_ctrl_14, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_28.Add(sizer_30, 1, wx.EXPAND, 0)
        label_22 = wx.StaticText(self, wx.ID_ANY, "Starting breeding need")
        label_22.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_31.Add(label_22, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_31.Add(self.spin_ctrl_15, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_28.Add(sizer_31, 1, wx.EXPAND, 0)
        label_23 = wx.StaticText(self, wx.ID_ANY, "Energy loss per turn")
        sizer_32.Add(label_23, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_32.Add(self.spin_ctrl_16, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_28.Add(sizer_32, 1, wx.EXPAND, 0)
        label_24 = wx.StaticText(self, wx.ID_ANY, "Nutritional value")
        sizer_33.Add(label_24, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_33.Add(self.spin_ctrl_17, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_28.Add(sizer_33, 1, wx.EXPAND, 0)
        label_25 = wx.StaticText(self, wx.ID_ANY, "Plant spawn rate")
        sizer_34.Add(label_25, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_34.Add(self.spin_ctrl_18, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_28.Add(sizer_34, 1, wx.EXPAND, 0)
        sizer_28.Add(self.checkbox_7, 1, wx.ALL, 2)
        sizer_16.Add(sizer_28, 1, wx.ALL | wx.EXPAND, 2)
        label_13 = wx.StaticText(self, wx.ID_ANY, "Gene length")
        sizer_18.Add(label_13, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_18.Add(self.spin_ctrl_2, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 2)
        sizer_17.Add(sizer_18, 0, wx.EXPAND, 0)
        label_15 = wx.StaticText(self, wx.ID_ANY, "Speed")
        sizer_21.Add(label_15, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_21.Add(self.spin_ctrl_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_20.Add(sizer_21, 1, wx.EXPAND, 0)
        label_16 = wx.StaticText(self, wx.ID_ANY, "Attention threshold")
        sizer_22.Add(label_16, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_22.Add(self.spin_ctrl_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_20.Add(sizer_22, 1, wx.EXPAND, 0)
        label_17 = wx.StaticText(self, wx.ID_ANY, "Breeding threshold")
        sizer_23.Add(label_17, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_23.Add(self.spin_ctrl_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_20.Add(sizer_23, 1, wx.EXPAND, 0)
        label_18 = wx.StaticText(self, wx.ID_ANY, "Interest in eating")
        sizer_24.Add(label_18, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_24.Add(self.spin_ctrl_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_20.Add(sizer_24, 1, wx.EXPAND, 0)
        label_19 = wx.StaticText(self, wx.ID_ANY, "Mutation resistance")
        sizer_25.Add(label_19, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_25.Add(self.spin_ctrl_8, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_20.Add(sizer_25, 1, wx.ALL | wx.EXPAND, 0)
        sizer_17.Add(sizer_20, 1, wx.EXPAND, 0)
        sizer_16.Add(sizer_17, 1, wx.ALL | wx.EXPAND, 2)
        sizer_1.Add(sizer_16, 1, wx.EXPAND, 0)
        sizer_27.Add(self.checkbox_3, 1, wx.ALL, 2)
        sizer_27.Add(self.checkbox_4, 1, wx.ALL, 2)
        sizer_27.Add(self.checkbox_5, 1, wx.ALL, 2)
        sizer_26.Add(sizer_27, 1, wx.EXPAND, 0)
        sizer_26.Add(self.radio_box_1, 0, wx.ALIGN_CENTER | wx.ALL, 2)
        sizer_15.Add(sizer_26, 1, wx.EXPAND, 0)
        label_12 = wx.StaticText(self, wx.ID_ANY, "Turns between saves")
        grid_sizer_2.Add(label_12, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        grid_sizer_2.Add(self.spin_ctrl_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        label_11 = wx.StaticText(self, wx.ID_ANY, "CSV output")
        grid_sizer_2.Add(label_11, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        grid_sizer_2.Add(self.text_ctrl_7, 2, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        label_10 = wx.StaticText(self, wx.ID_ANY, "JSON output")
        grid_sizer_2.Add(label_10, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        grid_sizer_2.Add(self.text_ctrl_8, 3, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 2)
        sizer_15.Add(grid_sizer_2, 1, wx.ALL | wx.EXPAND, 0)
        sizer_13.Add(sizer_15, 1, wx.EXPAND, 0)
        label_9 = wx.StaticText(self, wx.ID_ANY, "Information to export\n(only in detail mode)")
        sizer_14.Add(label_9, 0, wx.ALL, 2)
        sizer_14.Add(self.check_list_box_1, 0, wx.ALL | wx.EXPAND, 2)
        sizer_13.Add(sizer_14, 1, wx.EXPAND, 0)
        sizer_5.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_5, 1, wx.ALL | wx.EXPAND, 2)
        sizer_4.Add(self.button_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 8)
        sizer_4.Add(self.button_2, 1, wx.ALIGN_CENTER | wx.ALL, 8)
        sizer_4.Add(self.button_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 8)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_1.Add(self.text_ctrl_9, 0, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
