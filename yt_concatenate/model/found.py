

class Found:
    def __init__(self, yt, caption, time):
        self.yt = yt
        self.caption = caption
        self.time = time

    def __str__(self) -> str:
        return f'<Found yt={self.yt.id}>'

    def __repr__(self) -> str:
        return f'yt={self.yt} : caption={self.caption} : time={self.time}'
