import os

from fileopt import FileOpt

class Command:
    #configuration options
    cmd_str = "youtube_dl/__main__.py -i --geo-bypass --yes-playlist -x --prefer-ffmpeg --audio-format {audio_format} -o '{artist_name}/{album_name}/%(title)s.%(ext)s' {URL}"

    audio_format = "mp3"
                
    def run(self, artist_name, album_name, URL):
        #format the command with audio format, album name, and URL
        runstr=self.cmd_str.format(audio_format=self.audio_format, 
                artist_name=artist_name, album_name=album_name, URL=URL)

        #prind the command and run it
        print(runstr)
        os.system(runstr)

        #get the path to the songs
        folder_path = os.path.join(artist_name, album_name)

        #once done downloading, get the sorted file names and stats
        file_paths = FileOpt.getSortedFilePaths(folder_path)

        #set the base mp3 tags (wait for confirmation on title tag)
        if(audio_format != "mp3"): return

        for i, file_path in enumerate(file_paths):
            print(file_path)
            FileOpt.setBaseTags(file_path, artist_name, album_name, str(i+1))

    def confirmTitles(self, artist_name, album_name):
        if(audio_format != "mp3"): return

        #get the path to the songs
        folder_path = os.path.join(artist_name, album_name)

        #list all songs
        if(not os.path.isdir(folder_path)): return
        file_names = os.listdir(folder_path)

        #set the title tag to be the file name
        for file_name in file_names:
            file_path = os.path.join(folder_path, file_name)
            FileOpt.setTitleTag(file_path, file_name.split(".")[0])
