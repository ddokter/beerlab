from .fermentable import FermentableMixin
from .ingredient import Ingredient


BREWHOUSE_EFF = 0.8


class RecipeMixin:

    """ The recipe is a collection of materials and a yield in volume. """

    @property
    def size_liters(self):

        """All calculations are done with metric units. So we always need to
        convert to liters.

        """

        return self.size

    def list_fermentables(self):

        return [ingredient for ingredient in self.ingredients if
                isinstance(ingredient.material, FermentableMixin)]

    @property
    def degrees_plato(self):

        """ Give the strength of the recipe in degrees Plato """

        _yield = sum([(ingredient.material.extract * BREWHOUSE_EFF
                      * ingredient.weight_kilos) for ingredient in
                      self.list_fermentables()])

        return _yield / self.mass * 100

    @property
    def mass(self):

        return self.size_liters * self.SG

    @property
    def specific_gravity(self):

        """ Calculate the gravity of the beer """

        sg_points = 0

        for ingredient in self.list_fermentables():
            sg_points += (ingredient.material.pkdl * ingredient.weight_kilos *
                          BREWHOUSE_EFF / (
                              self.size_liters / 10))

        return (1000 + sg_points) / 1000.0

    # Shortcut
    SG = specific_gravity


class Recipe(RecipeMixin, object):

    """ The recipe is a collection of materials and a yield in volume. """

    def __init__(self, size, unit, ingredients=[]):

        self.size = size
        self.unit = unit

        self.ingredients = ingredients[:]
