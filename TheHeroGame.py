#ceva
import random

class Character(object):

    def __init__(self,health, strengh, defence, speed, Luck):
        self.health = random.randrange(health[0], health[1])
        self.strengh = random.randrange(strengh[0], strengh[1])
        self.defence = random.randrange(defence[0], defence[1])
        self.speed = random.randrange(speed[0], speed[1])
        self.Luck = random.randrange(Luck[0], Luck[1])

    def display(self):
        print("character name:{}, health:{}, strengh:{}, defence:{}, speed:{}, Luck:{}".format(self.name, self.health, self.strengh ,self.defence, self.speed, self.Luck))


    def attack(self, victim):
        raw_damage = self.strengh - victim.defence
        victim.receive_damage(raw_damage)

    def receive_damage(self, raw_damage):
        self.health -= raw_damage



    def random_chance(self, procent):
        """ Return True if have a x% """
        if random.randrange(0,100) <= procent:
            return True
        else:
            return False



class Hero(Character):
    def __init__(self):
        super().__init__([70,100],[70,80],[45,55],[40,50],[10,30])
        self.name = "hero"

    def attack(self, victim):
        if self.random_chance(victim.Luck):
            print ("The {} is not attacked,the attacker is miss, health remain : {}".format( victim.name, victim.health))
        else:
            if self.random_chance(10):
                raw_damage = self.strengh - victim.defence
                victim.receive_damage(2*raw_damage)
                print ("The {} was attacked, is used skill Rapid Strike health remain : {}".format( victim.name, victim.health))
            else:
                raw_damage = self.strengh - victim.defence
                victim.receive_damage(raw_damage)
                print ("The {} was attacked, health remain : {}".format( victim.name, victim.health))


    def receive_damage(self, raw_damage):
        if self.random_chance(20):
            self.health -= raw_damage/2
            print("The {} was attacked, was used magic_shield skill, health remain:{}".format(self.name, self.health))
        else:
            self.health -= raw_damage
            print("The {} was attacked, health remain:{}".format(self.name, self.health))


class Beast(Character):
    def __init__(self):
        super().__init__([60,90],[60,90],[40,60],[40,60],[25,40])
        self.name = 'beast'
    def attack(self, victim):
        if self.random_chance(victim.Luck):
            print ("The {} is not attacked,the attacker is miss, health remain : {}".format( victim.name, victim.health))
        else:
            raw_damage = self.strengh - victim.defence
            victim.receive_damage(raw_damage)





class Main():
    def __init__(self):
        """ Create the objects of all subclasses of Character """
        characters = [cls.__name__ for cls in Character.__subclasses__() ]
        self.first_ch = input("tell the name of first character:  ")
        self.first_ch_type = input("Write the type of the first character from the list {}:  ".format(characters))
        self.second_ch = input("tell the name of second character:  ")
        self.second_ch_type = input("Write the type of the second character from the list {}:  ".format(characters))
        # print(self.first_ch,self.first_ch_type,"-----",self.second_ch,self.second_ch_type)

        if self.first_ch_type.title() in characters:
            for cls in Character.__subclasses__():
                if cls.__name__ == self.first_ch_type.title():
                    self.first_ch = cls()
                elif cls.__name__ == self.second_ch_type.title():
                    self.second_ch = cls()
        else:
            print("the type of character is wrong")



    def while_func(self,attacker, victim):
        attacker.display()
        victim.display()
        n = 0
        while n<20:
            attacker.attack(victim)
            victim.attack(attacker)
            if attacker.health <= 0:
                print("the Winner is {} with health:{}".format(victim.name,victim.health))
                break
            elif victim.health <= 0:
                print("the Winner is {} with health:{}".format(attacker.name,attacker.health))
                break
            n += 1

    def atack_order(self):
        if self.first_ch.speed > self.second_ch.speed:
            self.while_func(self.first_ch,  self.second_ch)
        elif  self.first_ch.speed < self.second_ch.speed:
            self.while_func( self.second_ch, self.first_ch,)
        else:
            if self.first_ch.Luck > self.second_ch.Luck:
                self.while_func(self.first_ch,  self.second_ch)
            else:
                self.while_func( self.second_ch, self.first_ch,)



if __name__ == "__main__":
    Main().atack_order()
