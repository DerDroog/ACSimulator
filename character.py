import numpy as np


class Character:
    def __init__(self, name_, health_, mana_, position_, max_atk_cd_, atk_cd_, max_spell_cd_, spell_cd_, atk_, armor_,
                 mv_speed_, mv_dir_, atk_range_, team_=None, target_=None, alive_=True):
        self.name = name_
        self.health = health_
        self.mana = mana_
        self.position = position_
        self.max_atk_cd = max_atk_cd_
        self.atk_cd = atk_cd_
        self.max_spell_cd = max_spell_cd_
        self.spell_cd = spell_cd_
        self.atk = atk_
        self.target = target_
        self.mv_speed = mv_speed_
        self.mv_dir = mv_dir_
        self.atk_range = atk_range_
        self.team = team_
        self.armor = armor_
        self.alive = alive_

    def __repr__(self):
        print("*******************************************************************************************")
        if self.target is not None:
            return f"Name: {self.name} \nHealth: {self.health} \nMana: {self.mana}\nPosition: {self.position} \nTarget: {self.target.name} \nAlive: {self.alive} \nTarget State: {self.target.alive}"
        else:
            return f"Name: {self.name} \nHealth: {self.health} \nMana: {self.mana}\nPosition: {self.position} \nTarget: None. \nAlive: {self.alive} \nTarget STate: None"
        print("*******************************************************************************************")

    @staticmethod
    def armor_reduction(armor):
        alpha = -np.log(0.8)/5
        return 1 - np.exp(-alpha*armor)

    def update_heatlh(self, timestep):
        pass

    def update_mana(self, timestep):
        pass

    def update_atk_cd(self, timestep):
        if self.atk_cd <= 0 and self.target is not None:
            self.hit()
            self.atk_cd = self.max_atk_cd
        self.atk_cd -= timestep
        pass

    def update_mv_dir(self, target):
        # default target is usually center of battle field
        self.mv_dir = (target - self.position)
        self.mv_dir = self.mv_dir / np.linalg.norm(self.mv_dir)

    def update_position(self, timestep):
        self.position = self.position + self.mv_speed * self.mv_dir * timestep
        return

    def update_spell_cd(self, timestep):
        pass

    def update_dmg(self, timestep):
        pass

    def hit(self):
        dmg_dealt = self.atk * (1 - Character.armor_reduction(self.target.armor))
        self.target.health -= dmg_dealt
        self.target.alive = (self.target.health > 0)
        self.target.mana += dmg_dealt * 0.3
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("\n", self.name, " hit ", self.target.name, " for ", dmg_dealt, ". Health: ", self.target.health, "\n")
        if self.target.alive == False:
            print("\n", self.target.name, " has died.")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
