from peak_utility.number import Ordinal


class Rank(Ordinal):
    
    def __new__(cls, value, **kwargs):
        instance = super().__new__(cls, str(value).replace("=", ""))    
        instance.tied = kwargs.get('tied', "=" in str(value))
        return instance