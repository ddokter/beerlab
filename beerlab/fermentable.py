from .config import PPG_CONST, PKdL_CONST


class FermentableMixin:

    """Mixin that implements some typical fermentable calculations, and
    requires the 'extract' attribute on the actual class.

    """

    def get_extract(self):

        """Implement this method so that it returns the actual extract in
        fermentable sugars for a given material.

        """

        raise NotImplementedError

    @property
    def ppg(self):

        return self.get_extract() * PPG_CONST

    @property
    def pkdl(self):

        return self.get_extract() * PKdL_CONST


class Fermentable(FermentableMixin, object):

    """ Base fermentable, be it grain, sugar, etc. """

    def __init__(self, extract):

        self.extract = extract

    def get_extract(self):

        return self.extract
