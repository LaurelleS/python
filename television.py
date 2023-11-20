class Television:
    """
    A class that represents a television
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self):
        """
        A function that switches the status of a television object
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        """
        A function that switches the muted value of a television object
        """
        if self.__status:
            if self.__muted:
                self.__status = False
            else:
                self.__muted = True

    def channel_up(self):
        """
        A function that increases the channel by one
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        A function that decreases the channel by one
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        A function that increases the volume by one
        """
        self.__muted = False
        if self.__status:
            if self.__volume == self.MAX_VOLUME:
                return
            else:
                self.__volume += 1

    def volume_down(self):
        """
        A function that decreases the volume by one
        """
        self.__muted = False
        if self.__status:
            if self.__volume == self.MIN_VOLUME:
                return
            else:
                self.__volume -= 1

    def __str__(self):
        if not self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'
