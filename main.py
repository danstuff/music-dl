import os

from kivy.app import App
from kivy.config import Config

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup

from command import Command

#set window width and height
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '200')

#create instance of the command object
command = Command()

#URL input, album input
urlInput = TextInput(text='Enter a playlist or song URL', multiline=False)
albumInput = TextInput(text="No Name", multiline=False)

#album popup
albumPopup = Popup(title="Enter Album Name", sizehint=(None, None), size=(400, 100))

def stub(instance):
    return

def onDownload(instance):
    global albumPopup 
    albumPopup.open()

def onAlbumSpecified(instance):
    global albumPopup, command
    global albumInput, urlInput

    albumPopup.dismiss()
    command.run(albumInput.text, urlInput.text)

def onRadio(instance):
    global command

    command.audio_format = instance.text
    print(">>>Switched to {af} format".format(af=command.audio_format))

class MusicDLApp(App):
    def build(self):
        layout = GridLayout(cols=1, row_force_default=True, row_default_height=40)

        #title label
        layout.add_widget(Label(text="[color=#ffffff]music[/color][color=#ff3300]-dl[/color]",
            font_size="20sp", markup=True))

        #add URL input
        layout.add_widget(urlInput)

        #type select is in a sub layout
        sub_layout = GridLayout(cols=5)

        #type select radio buttons
        labels = ( "best", "mp3", "m4a", "wav", "ogg" )

        for i in range(5):
            btn = ToggleButton(text=labels[i], group="format")
            btn.bind(on_press=onRadio)
            if(i == 0): btn.state = "down"
            
            sub_layout.add_widget(btn)

        #add type select sub layout to main layout 
        layout.add_widget(sub_layout)

        #download button
        downloadButton = Button(text="Download")
        downloadButton.bind(on_press=onDownload)

        layout.add_widget(downloadButton) 

        #bottom copyright label
        layout.add_widget(Label(text="Created by Daniel Yost - MIT License 2019",
            font_size="11sp", padding_y="0", markup=True))
        
        #create layout for the popup
        global albumPopup

        popupLayout = GridLayout(cols=1)

        confirmBtn = Button(text="Confirm")
        confirmBtn.bind(on_press=onAlbumSpecified)

        popupLayout.add_widget(albumInput)
        popupLayout.add_widget(confirmBtn)

        albumPopup.content = popupLayout

        return layout

MusicDLApp().run()
