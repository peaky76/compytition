from peak_utility.number import Ordinal


class Rank(Ordinal):
    
    def __new__(cls, value, **kwargs):
        instance = super().__new__(cls, str(value).replace("=", ""))    
        instance.tied = kwargs.get('tied', "=" in str(value))
        return instance

    def __repr__(self):
        return f"{super().__repr__()}{'=' if self.tied else ''}"

    def __str__(self):
        return f"{int(self)}{'=' if self.tied else ''}"