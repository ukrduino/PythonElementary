# Write classes of the following heroes: Warrior, Mage, and Archer.
# All classes have health points (HP) and magic energy (mana).
# There are three different types of magic: Fire, Ice and Arcane;
# Fire magic has the spell fireball, Ice magic has the spell freeze and
# Arcane magic has the spell black hole.
# The Warrior is furious and can use Fire magic as well as his hammer;
# The Archer is calm and can use Ice magic in addition to his arrows;
# The Mag can use all types of magic.
# Each magic spell costs an arbitrary amount of magic energy and can be
# cast only if there is enough mana. Use magic mixins to reduce repetitive code.


class ArcaneMagicMixin(object):
    arcane_magic_word = "black hole"
    arcane_magic_cost = 5


class FireMagicMixin(object):
    fire_magic_word = "fireball"
    fire_magic_cost = 10


class IceMagicMixin(object):
    ice_magic_word = "freeze"
    ice_magic_cost = 15


class Hero(object):
    """
    Base Hero class
    """
    def __init__(self, weapon=None):
        self.mana = 100
        self.health = 200
        self.weapon = weapon

    def use_magic(self, magic_word, magic_cost):
        if self.mana > magic_cost:
            print self.__class__.__name__ + " said '" + magic_word + "'"
            self.mana -= magic_cost
        else:
            print "NOT ENOUGH MANA!!! YOU HAVE {} but required {}".format(self.mana, magic_cost)

    def attack(self):
        print self.__class__.__name__ + " used '" + self.weapon + "'"


class Warrior(FireMagicMixin, Hero):
    """
    >>> w = Warrior();
    >>> w.health
    200
    >>> w.mana
    100
    >>> w.fire_magic_word
    'fireball'
    >>> w.fire_magic_cost
    10
    >>> w.use_magic(w.fire_magic_word, w.fire_magic_cost)
    Warrior said 'fireball'
    >>> w.mana
    90
    >>> w.attack()
    Warrior used 'hammer'
    """
    def __init__(self):
        super(Warrior, self).__init__("hammer")


class Mag(IceMagicMixin, ArcaneMagicMixin, FireMagicMixin, Hero):
    """
    >>> m = Mag();
    >>> m.health
    200
    >>> m.mana
    100
    >>> m.fire_magic_word
    'fireball'
    >>> m.fire_magic_cost
    10
    >>> m.ice_magic_word
    'freeze'
    >>> m.ice_magic_cost
    15
    >>> m.arcane_magic_word
    'black hole'
    >>> m.arcane_magic_cost
    5
    >>> m.use_magic(m.arcane_magic_word, m.arcane_magic_cost)
    Mag said 'black hole'
    >>> m.mana
    95
    >>> m.use_magic(m.fire_magic_word, m.fire_magic_cost)
    Mag said 'fireball'
    >>> m.mana
    85
    >>> m.use_magic(m.ice_magic_word, m.ice_magic_cost)
    Mag said 'freeze'
    >>> m.mana
    70
    >>> m.use_magic(m.ice_magic_word, m.ice_magic_cost)
    Mag said 'freeze'
    >>> m.use_magic(m.ice_magic_word, m.ice_magic_cost)
    Mag said 'freeze'
    >>> m.use_magic(m.ice_magic_word, m.ice_magic_cost)
    Mag said 'freeze'
    >>> m.use_magic(m.ice_magic_word, m.ice_magic_cost)
    Mag said 'freeze'
    >>> m.use_magic(m.ice_magic_word, m.ice_magic_cost)
    NOT ENOUGH MANA!!! YOU HAVE 10 but required 15
    """
    def __init__(self):
        super(Mag, self).__init__()


class Archer(IceMagicMixin, Hero):
    """
    >>> a = Archer()
    >>> a.use_magic(a.ice_magic_word, a.ice_magic_cost)
    Archer said 'freeze'
    >>> a.mana
    85
    >>> a.attack()
    Archer used 'arrows'
    """
    def __init__(self):
        super(Archer, self).__init__("arrows")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
