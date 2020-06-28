class Character:
    def __init__(self, name_, health_, mana_, position_, max_atk_cd_, atk_cd_, max_spell_cd_, spell_cd_, atk_, armor_,
                 team_=None, target_=None, alive_=True):
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
        self.team = team_
        self.armor = armor_
        self.alive = alive_

    @staticmethod
    def armor_reduction(armor):
        return armor / 10

    def update_heatlh(self, timestep):
        pass

    def update_mana(self, timestep):
        pass

    def update_atk_cd(self, timestep):
        if self.atk_cd <= 0:
            self.hit()
            self.atk_cd = self.max_atk_cd
        self.atk_cd -= timestep
        pass

    def update_position(self, timestep):
        pass

    def update_spell_cd(self, timestep):
        pass

    def update_dmg(self, timestep):
        pass

    def update_alive(self):
        if self.health <= 0:
            self.alive = False

    def hit(self):
        dmg_dealt = self.atk * (1 - Character.armor_reduction(self.target.armor))
        self.target.health -= dmg_dealt
        self.target.mana += dmg_dealt * 0.3
        print("\n", self.name, " hit ", self.target.name, " for ", dmg_dealt, ". Health: ", self.target.health)
