class IngredientMixin:

    @property
    def weight_kilos(self):

        """ Internally, all weights are converted to kilos """

        raise NotImplementedError


class Ingredient(IngredientMixin, object):

    """ Combination of material with size and unit """

    def __init__(self, material, weight, unit):

        self.material = material
        self.weight = weight
        self.unit = unit

    @property
    def weight_kilos(self):

        """ Internally, all weights are converted to kilos """

        return self.weight
