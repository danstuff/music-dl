import os

class Command:
    #configuration options
    cmd_str = "youtube_dl/__main__.py -i --geo-bypass --yes-playlist -x --prefer-ffmpeg --audio-format {audio_format} -o '{album_name}/%(playlist_index)s - %(title)s.%(ext)s' {URL}"

    audio_format = "best"

    def run(self, album_name, URL):
        #format the command with audio format, album name, and URL
        runstr=self.cmd_str.format(audio_format=self.audio_format, album_name=album_name, URL=URL)

        #prind the command and run it
        print(runstr)
        os.system(runstr)

        #once done downloading, remove commonalities in the file names
