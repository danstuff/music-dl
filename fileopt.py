import os
import mutagen.mp3

class FileOpt:
    @staticmethod
    def getSortedFilePaths(directory):
        if(not os.path.isdir(directory)): return list()

        file_names = os.listdir(directory)
        file_paths = list()
        file_times = list()

        #get modification time all files
        for file_name in file_names:
            file_path = os.path.join(directory, file_name)

            file_paths.append(file_path)
            file_times.append(os.stat(file_path).st_mtime)

        #sort files based on mod time using a simple bubble sort
        unsorted = True

        while(unsorted):
            unsorted = False

            for i in range(len(file_times)):
                if(i > 0 and file_times[i] < file_times[i-1]):
                    file_times[i], file_times[i-1] = file_times[i-1], file_times[i]
                    file_paths[i], file_paths[i-1] = file_paths[i-1], file_paths[i]
                    unsorted = True
        
        #return sorted list
        return file_paths

    @staticmethod
    def getID3(file_path):
        tags = None

        #add an ID3 header if none already exists
        try:
            tags = ID3(file_path)
        except ID3NoHeaderError:
            print("Adding ID3 header to {fn}".format(fn=file_path))
            tags = ID3()

        return tags

    @staticmethod
    def setBaseTags(file_path, artist_name, album_name, track_number):
        tags = mutagen.mp3.EasyMP3(file_path) 

        #set album name, artist name, album artist, and track number
        tags["artist"] = artist_name
        tags["albumartist"] = artist_name
        tags["album"] = album_name
        tags["tracknumber"] = track_number

        print(artist_name, album_name, track_number)

        tags.save(file_path)

    @staticmethod
    def setTitleTag(file_path, title):
        tags = mutagen.mp3.EasyMP3(file_path) 

        #set the title
        tags["title"] = title

        print(title)

        tags.save(file_path)
