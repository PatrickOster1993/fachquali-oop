from decimal import Decimal, ROUND_HALF_UP, getcontext
import random
from abc import ABC, abstractmethod

class MathUtils:
    @staticmethod
    def rund(number, decimals=0):
        getcontext().rounding = ROUND_HALF_UP
        number_decimal = Decimal(str(number))
        result = number_decimal.quantize(Decimal('1e-{}'.format(decimals)))
        return float(result) if decimals > 0 else int(result)

class StatCalculator:
    @staticmethod
    def calculate_hp(strength, vitality):
        return MathUtils.rund(80 + strength * 1.8 + vitality * 4.3, 0)

    @staticmethod
    def calculate_sp(strength, dexterity):
        return MathUtils.rund(30 + strength * 1.4 + dexterity * 2.8, 0)
    
    @staticmethod
    def calculate_mp(wisdom, intelligence):
        return MathUtils.rund(20 + wisdom * 3.4 + intelligence * 1.6, 0)
    
    @staticmethod
    def calculate_attack(strength):
        return MathUtils.rund(strength * 2.2, 0)
    
    @staticmethod
    def calculate_defense(vitality):
        return MathUtils.rund(vitality * 1.7, 0)
    
    @staticmethod
    def calculate_psiattack(intelligence, wisdom, dexterity):
        return MathUtils.rund(intelligence * 1.3 + wisdom * 1.5 + dexterity * 1.3, 0)
    
    @staticmethod
    def calculate_magicattack(intelligence):
        return MathUtils.rund(intelligence * 3.2, 0)
    
    @staticmethod
    def calculate_magicdefense(wisdom):
        return MathUtils.rund(wisdom * 2.7, 0)
    
    @staticmethod
    def calculate_accuracy(dexterity, agility, fortune):
        return MathUtils.rund(75 + dexterity * 2.4 + agility * 0.8 + fortune * 0.7, 0)
    
    @staticmethod
    def calculate_dodge(agility, fortune):
        return MathUtils.rund(10 + agility * 1.1 + fortune * 0.7, 0)
    
    @staticmethod
    def calculate_crit(fortune, dexterity):
        return MathUtils.rund(1 + fortune * 0.7 + dexterity * 0.3, 0)
    
    @staticmethod
    def calculate_speed(agility):    
        return MathUtils.rund(agility * 2.1, 0)
    
    @staticmethod
    def calculate_luck(fortune):
        return MathUtils.rund(fortune * 1, 0)

class Stats:
    def __init__(self, name, strength=None, vitality=None, dexterity=None, agility=None, intelligence=None, wisdom=None, fortune=None,
                hp=None, sp=None, mp=None, attack=None, defense=None, psiattack=None, magicattack=None, magicdefense=None, 
                accuracy=None, dodge=None, crit=None, speed=None, luck=None):
        
        # Basisattribute
        self.name = name
        self.strength = strength if strength is not None else 0
        self.vitality = vitality if vitality is not None else 0
        self.dexterity = dexterity if dexterity is not None else 0
        self.agility = agility if agility is not None else 0
        self.intelligence = intelligence if intelligence is not None else 0
        self.wisdom = wisdom if wisdom is not None else 0
        self.fortune = fortune if fortune is not None else 0
        
        # Backing Fields für Kampfattribute (werden nur gesetzt, wenn explizit angegeben)
        self._hp = hp
        self._sp = sp
        self._mp = mp
        self._attack = attack
        self._defense = defense
        self._psiattack = psiattack
        self._magicattack = magicattack
        self._magicdefense = magicdefense
        self._accuracy = accuracy
        self._dodge = dodge
        self._crit = crit
        self._speed = speed
        self._luck = luck

    # Properties für dynamische Berechnung
    @property
    def hp(self):
        return self._hp if self._hp is not None else StatCalculator.calculate_hp(self.strength, self.vitality)
    
    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def sp(self):
        return self._sp if self._sp is not None else StatCalculator.calculate_sp(self.strength, self.dexterity)
    
    @sp.setter
    def sp(self, value):
        self._sp = value

    @property
    def mp(self):
        return self._mp if self._mp is not None else StatCalculator.calculate_mp(self.wisdom, self.intelligence)
    
    @mp.setter
    def mp(self, value):
        self._mp = value

    @property
    def attack(self):
        return self._attack if self._attack is not None else StatCalculator.calculate_attack(self.strength)
    
    @attack.setter
    def attack(self, value):
        self._attack = value

    @property
    def defense(self):
        return self._defense if self._defense is not None else StatCalculator.calculate_defense(self.vitality)
    
    @defense.setter
    def defense(self, value):
        self._defense = value

    @property
    def psiattack(self):
        return self._psiattack if self._psiattack is not None else StatCalculator.calculate_psiattack(self.intelligence, self.wisdom, self.dexterity)
    
    @psiattack.setter
    def psiattack(self, value):
        self._psiattack = value

    @property
    def magicattack(self):
        return self._magicattack if self._magicattack is not None else StatCalculator.calculate_magicattack(self.intelligence)
    
    @magicattack.setter
    def magicattack(self, value):
        self._magicattack = value

    @property
    def magicdefense(self):
        return self._magicdefense if self._magicdefense is not None else StatCalculator.calculate_magicdefense(self.wisdom)
    
    @magicdefense.setter
    def magicdefense(self, value):
        self._magicdefense = value

    @property
    def accuracy(self):
        return self._accuracy if self._accuracy is not None else StatCalculator.calculate_accuracy(self.dexterity, self.agility, self.fortune)
    
    @accuracy.setter
    def accuracy(self, value):
        self._accuracy = value

    @property
    def dodge(self):
        return self._dodge if self._dodge is not None else StatCalculator.calculate_dodge(self.agility, self.fortune)
    
    @dodge.setter
    def dodge(self, value):
        self._dodge = value

    @property
    def crit(self):
        return self._crit if self._crit is not None else StatCalculator.calculate_crit(self.fortune, self.dexterity)
    
    @crit.setter
    def crit(self, value):
        self._crit = value

    @property
    def speed(self):
        return self._speed if self._speed is not None else StatCalculator.calculate_speed(self.agility)
    
    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def luck(self):
        return self._luck if self._luck is not None else StatCalculator.calculate_luck(self.fortune)
    
    @luck.setter
    def luck(self, value):
        self._luck = value



