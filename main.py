import os

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup

from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '200')

#URL input and download button
urlInput = TextInput(text='Enter a playlist or song URL', multiline=False)
downloadButton = Button(text='Download')

#configuration options
command = "youtube_dl/__main__.py -i --geo-bypass --yes-playlist -x --prefer-ffmpeg --audio-format {audio_format} -o '{album_name}/%(playlist_index)s - %(title)s.%(ext)s' {URL}"

audio_format = "best"
album_name = "No Name"

def stub(instance):
    return

def onDownload(instance):
    downloadButton.text = "Working..."
    downloadButton.bind(on_press=stub)

    global options, audio_format, album_name, urlInput, downloadButton

    #ask user for the album name
    layout = GridLayout(cols=1)
    AlbumInput = TextInput(text="No Name", multiline=False)
    ConfirmBtn = Button(text="Confirm")
    popup = Popup(title="Enter Album Name", 
            content=AlbumInput,sizehint=(None, None),
            size=(400, 200))
    popup.open()

def onAlbumSpecified(instance):
    album_name = AlbumInput.text

    runstr=command.format(audio_format=audio_format, album_name=album_name, URL=urlInput.text)


    print(runstr)
    os.system(runstr)

    downloadButton.text = "Download"
    downloadButton.bind(on_press=onDownload)

    

def onRadio(instance):
    global audio_format
    audio_format = instance.text
    print(audio_format)

class MusicDL(App):
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

        layout.add_widget(sub_layout)

        #download button
        downloadButton.bind(on_press=onDownload)

        layout.add_widget(downloadButton) 

        #bottom copyright label
        layout.add_widget(Label(text="Created by Daniel Yost - MIT License 2019",
            font_size="11sp", padding_y="0", markup=True))

        return layout

MusicDL().run()
