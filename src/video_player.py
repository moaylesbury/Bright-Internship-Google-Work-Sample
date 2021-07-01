"""A video player class."""

from .video_library import VideoLibrary
from random import randint


def collate_tags(vid):
    tagstr = "["
    for tag in vid.tags:
        tagstr += tag + " "

    if tagstr[-1] == " ":
        tagstr = tagstr[:-1]

    tagstr += "]"

    return tagstr


def lower_tags(tag):
    return tag[0:1] + tag[1:].lower()


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.currently_playing = None
        self.paused = False
        self.playlists = {}
        self.flags = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def get_full_title(self, id):
        vid = self._video_library.get_video(id)
        tagstr = collate_tags(vid)
        return (vid.title + " (" + vid.video_id + ") " + tagstr)

    def title_from_id(self, id):
        if self._video_library.get_video(id) is None:
            return None
        else:
            return self._video_library.get_video(id).title

    def show_all_videos(self):
        """Returns all videos."""
        vids = self._video_library.get_all_videos()
        out = []

        print("Here's a list of all available videos:")

        for vid in vids:

            tagstr = collate_tags(vid)

            out.append(vid.title + " (" + vid.video_id + ") " + tagstr)

        out.sort()

        for o in out:
            print(o)

        # print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        vid = self._video_library.get_video(video_id)

        if vid is not None:
            if vid.video_id in self.flags.keys():
                print("Cannot play video: Video is currently flagged (reason: " + self.flags[vid.video_id] + ")")
            else:
                if self.currently_playing is not None:
                    print("Stopping video: " + self._video_library.get_video(self.currently_playing).title)
                print("Playing video: " + vid.title)
                self.paused = False
                self.currently_playing = vid.video_id
        else:
            print("Cannot play video: Video does not exist")
            self.currently_playing = None
        # print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""

        if self.currently_playing is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: " + self._video_library.get_video(self.currently_playing).title)
            self.currently_playing = None

        # print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""

        if self.currently_playing is not None:
            self.stop_video()

        vids = self._video_library.get_all_videos()
        ids = [vid.video_id for vid in vids]

        all_flagged = True
        for id in ids:
            if id not in self.flags.keys():
                all_flagged = False

        if all_flagged:
            print("No videos available")
        else:
            play = False
            while not play:
                rand_index = randint(0, len(self._video_library.get_all_videos()) - 1)
                rand_id = ids[rand_index]
                if rand_id not in self.flags.keys():
                    play = True
            self.play_video(rand_id)

        # print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        if self.paused:
            print("Video already paused: " + self._video_library.get_video(self.currently_playing).title)
        else:
            if self.currently_playing is None:
                print("Cannot pause video: No video is currently playing")
            else:
                print("Pausing video: " + self._video_library.get_video(self.currently_playing).title)
                self.paused = True

        # print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.currently_playing is None:
            print("Cannot continue video: No video is currently playing")
        else:
            if self.paused:
                print("Continuing video: " + self._video_library.get_video(self.currently_playing).title)
                self.paused = False
            else:
                print("Cannot continue video: Video is not paused")



        # print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        if self.currently_playing is None:
            print("No video is currently playing")
        else:

            vid = self._video_library.get_video(self.currently_playing)

            if self.paused:
                print("Currently playing: " + vid.title + " (" +
                      vid.video_id + ") " + collate_tags(vid) + " - PAUSED")
            else:
                print("Currently playing: " + vid.title + " (" +
                      vid.video_id + ") " + collate_tags(vid))


        # print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """




        name = playlist_name.lower()

        if name in self.lower_keys():
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            print("Successfully created new playlist: " + playlist_name)
            self.playlists[playlist_name] = []

        # print("create_playlist needs implementation")

    def get_key(self, name):
        keys = [*self.playlists]
        for key in keys:
            if key.lower() == name:
                return key

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        name = playlist_name.lower()
        vid = self._video_library.get_video(video_id)

        if name in self.lower_keys():
            if self.title_from_id(video_id) is None:
                print("Cannot add video to " + playlist_name + ": Video does not exist")
            else:
                if vid.video_id in self.flags.keys():
                    print("Cannot add video to " + playlist_name + ": Video is currently flagged (reason: " + self.flags[video_id] + ")")
                else:
                    key = self.get_key(name)
                    if video_id in self.playlists[key]:
                        print("Cannot add video to " + playlist_name +": Video already added")
                    else:
                        print("Added video to " + playlist_name + ": " + vid.title)
                        self.playlists[key].append(video_id)
        else:
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")




        # print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""
        # No
        # playlists
        # exist
        # yet
        if len(self.playlists.keys()) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            # print([self.playlists.keys()].sort())
            names = [*self.playlists]
            names.sort()
            # print("NAMES", names)

            for name in names:
                print(name)


        # print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        name = playlist_name.lower()
        key = self.get_key(name)

        if name in self.lower_keys():
            print("Showing playlist: " + playlist_name)
            if len(self.playlists[key]) == 0:
                print("No videos here yet.")
            else:
                ids = self.playlists[key]

                for id in ids:
                    print(self.get_full_title(id))
        else:
            print("Cannot show playlist another_playlist: Playlist does not exist")

        # print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        name = playlist_name.lower()
        vid = self._video_library.get_video(video_id)
        key = self.get_key(name)

        if name in self.lower_keys():
            if vid is None:
                print("Cannot remove video from " + playlist_name + ": Video does not exist")
            else:
                if video_id in self.playlists[key]:
                    print("Removed video from " + playlist_name + ": " + vid.title)
                    self.playlists[key].remove(video_id)
                else:
                    print("Cannot remove video from " + playlist_name + ": Video is not in playlist " + playlist_name)
        else:
            print("Cannot remove video from " + playlist_name + ": Playlist does not exist")


        # print("remove_from_playlist needs implementation")

    def lower_keys(self):
        return [key.lower() for key in [*self.playlists]]

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        name = playlist_name.lower()
        key = self.get_key(name)

        if name in self.lower_keys():
            self.playlists[key] = []
            print("Successfully removed all videos from " + playlist_name)
        else:
            print("Cannot clear playlist " + playlist_name + ": Playlist does not exist")






        # print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        name = playlist_name.lower()
        key = self.get_key(name)

        if name in self.lower_keys():
            print("Deleted playlist: " + playlist_name)
            del self.playlists[key]
        else:
            print("Cannot delete playlist " + playlist_name + ": Playlist does not exist")



        # print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        # print("search_videos needs implementation")
        term = search_term.lower()

        matches = []
        options = {}

        for vid in self._video_library.get_all_videos():
            if term in vid.title.lower():
                matches.append(vid)

        if len(matches) == 0:
            print("No search results for " + term)
        else:
            print("Here are the results for " + term + ":")
            for count, match in enumerate(matches):
                print(str(count+1) + ") " + self.get_full_title(match.video_id))
                options[count+1] = match.video_id
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            inp = input()
            if inp.isnumeric():
                if int(inp) in options.keys():
                    self.play_video(options[int(inp)])

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        # print("search_videos_tag needs implementation")
        term = lower_tags(video_tag)

        matches = []
        options = {}

        for vid in self._video_library.get_all_videos():
            if term in [lower_tags(tag) for tag in vid.tags]:
                matches.append(vid)

        if len(matches) == 0:
            print("No search results for " + term)
        else:
            print("Here are the results for " + term + ":")
            for count, match in enumerate(matches):
                print(str(count + 1) + ") " + self.get_full_title(match.video_id))
                options[count + 1] = match.video_id
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            inp = input()
            if inp.isnumeric():
                if int(inp) in options.keys():
                    self.play_video(options[int(inp)])

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        # print("flag_video needs implementation")

        if self._video_library.get_video(video_id) is not None:
            if video_id in self.flags.keys():
                print("Cannot flag video: Video is already flagged")
            else:
                if flag_reason == "":
                    print("Successfully flagged video: " + self._video_library.get_video(video_id).title + " (reason: Not supplied)")
                    self.flags[video_id] = "Not supplied"
                else:
                    print("Successfully flagged video: " + self._video_library.get_video(video_id).title + " (reason: dont_like_cats)")
                    self.flags[video_id] = flag_reason
        else:
            print("Cannot flag video: Video does not exist")



    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        # print("allow_video needs implementation")

        if self._video_library.get_video(video_id) is not None:
            if video_id in self.flags.keys():
                print("Successfully removed flag from video: " + self._video_library.get_video(video_id).title)
                del self.flags[video_id]
            else:
                print("Cannot remove flag from video: Video is not flagged")
        else:
            print("Cannot remove flag from video: Video does not exist")
