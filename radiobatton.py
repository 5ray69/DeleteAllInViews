# -*- coding: utf-8 -*-

import clr

clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import Form, FormBorderStyle, GroupBox, RadioButton
clr.AddReference('System.Drawing')
from System.Drawing import ContentAlignment, Point, Size, SystemColors


class MyRadioButton(RadioButton):
    def __init__(self):
        super(MyRadioButton, self).__init__()
        self.Size = Size(80, 100)
        self.TextAlign = ContentAlignment.BottomCenter
        self.AutoCheck = False


class Window(Form):
    def __init__(self):
        self._initialize_components()

    def _initialize_components(self):

        self._gbx_opts = GroupBox()
        self._rb_opt1 = MyRadioButton()
        self._rb_opt2 = MyRadioButton()
        self._rb_opt3 = MyRadioButton()
        self._rb_opt4 = MyRadioButton()
        #
        # gbx_opts
        #
        self._gbx_opts.Location = Point(5, 5)
        self._gbx_opts.Size = Size(400, 175)
        self._gbx_opts.Controls.Add(self._rb_opt1)
        self._gbx_opts.Controls.Add(self._rb_opt2)
        self._gbx_opts.Controls.Add(self._rb_opt3)
        self._gbx_opts.Controls.Add(self._rb_opt4)
        #
        # rb_opt1
        #
        self._rb_opt1.Location = Point(10, 15)
        self._rb_opt1.Text = '1'
        self._rb_opt1.Checked = True
        self._rb_opt1.Click += self._on_checked_changed
        #
        # rb_opt2
        #
        self._rb_opt2.Location = Point(110, 15)
        self._rb_opt2.Text = '2'
        self._rb_opt2.Click += self._on_checked_changed
        #
        # rb_opt3
        #
        self._rb_opt3.Location = Point(210, 15)
        self._rb_opt3.Text = '3'
        self._rb_opt3.Click += self._on_checked_changed
        #
        # rb_opt4
        #
        self._rb_opt4.Location = Point(310, 15)
        self._rb_opt4.Text = '4'
        self._rb_opt4.Click += self._on_checked_changed
        #
        # Window
        #
        self.ClientSize = Size(594, 284)
        self.FormBorderStyle = FormBorderStyle.FixedToolWindow
        self.CenterToScreen()
        self.BackColor = SystemColors.Window

        self.Controls.Add(self._gbx_opts)

    def _on_checked_changed(self, sender, event_args):
        for rb in self._gbx_opts.Controls:
            if rb == sender:
                rb.Checked = True
                continue
            rb.Checked = False

w = Window()
w.ShowDialog()
