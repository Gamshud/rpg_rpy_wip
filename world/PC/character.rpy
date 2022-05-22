init python:
    pc0 = Player(race="elf", inventory=[["cookie", 5]], start_traits=[]) 
    pc_s_num = 0
    pc_s = ["pc0"]
    pc_dict = {
    "pc0": pc0
    }
    pc = pc_dict["pc"+str(pc_s_num)]

    
    def pc_ch(num):
        renpy.call_in_new_context("pc_num", num)

label pc_num(num):
    $ pc_s_num = num
    $ pc = pc_dict["pc"+str(pc_s_num)]
    return
    

init -2 python:
    class Player:
        def __init__(self, hp=100, base_hp=100, base_mp=100,  mp=100, max_intel=11, intel=3, max_strength=11, strength=3, max_agil=11, agil=3, xp=1, lvl=1, inventory=[], skill_points=0, race="elf", money=10, xp_rate=1, name=renpy.random.choice(["A", "B", "C"]), start_traits = []):
            self.name = name
            
            self.face = "neutral"
            self.max_strength = max_strength
            self.max_agil = max_agil
            self.max_intel = max_intel
            self.strength = strength
            self.agil = agil
            self.intel = intel
            self.base_hp = base_hp
            self.base_mp = base_mp
            self.max_hp = base_hp + self.strength*2
            self.max_mp = base_mp + self.intel*2
            self.hp = self.max_hp
            self.mp = self.max_mp
            self.atk = 1 + strength/2
            self.matk = 1 + intel/2
            self.defence = (self.strength/3)+(self.max_hp/6)
            self.mdef = (self.intel/3) + (self.max_hp/6)
            self.lvl = lvl
            self.skill_points = skill_points
            self.xp = xp
            self.xp_rate = xp_rate
            self.money = money
            self.race = race
            self.traits = []
            self.incompatibility = []
            self.inventory = inventory
            self.buffs_count = []
            self.buffs = []
            self.equip = {
                "neck":"None",
                "ring1":"None",
                "ring2":"None",
                "body":"None",
                "bracers":"None",
                "legs":"None",
                "bots":"None"
            }
            self.img_acc1 = {
            "pose":"1"
            }
            self.img_acc = {
                "body_race":str(self.race) + str(self.img_acc1["pose"]),
                "face_tat":"None",
                "neck":"None",
                "ring1":"None",
                "ring2":"None",
                "body":"None",
                "bracers":"None",
                "legs":"None",
                "bots":"None",
                "leg_tat":"None"
            }
            for i in start_traits:
                self.acc_trait(i)
            
        

        def all_charsstat(self):
            self.base_stat_up()
         
        def base_stat_up(self):
            if self.intel > self.max_intel:
                self.intel -= 1
            
            if self.strength > self.max_strength:
                self.strength -= 1
                
            if self.agil > self.max_agil:
                self.agil -= 1
            
            self.max_hp = self.base_hp + self.strength*2
            self.max_mp = self.base_mp + self.intel*2
            self.atk = self.strength/2
            self.matk = self.intel/2
            self.defence = (self.strength/3)+(self.max_hp/6)
            self.mdef = (self.intel/3) + (self.max_hp/6)

        def hp_damage(self, hp_dmg):
            self.hp -= hp_dmg
            deathname = "default"
            
            if self.hp <= 0:
                self.deafeat_set(deathname)
            else:
                pass
                
        def hp_regen(self, hp_add, noty="+"):
            if hp_add <= (self.max_hp - self.hp):
                self.hp += hp_add
                if noty == "+":
                    renpy.notify(str(hp_add) + ' здоровья восстановлено!')
                else:
                    pass
            elif hp_add > (self.max_hp - self.hp):
                self.hp = self.max_hp
                if noty == "+":
                    renpy.notify('Здоровье восполнено!')
                else:
                    pass
            else:
                if noty == "+":
                    renpy.notify('У тебя и так максимально здоровья!')
                else:
                    pass
        
        def mp_regen(self, mp_add, noty="+"):
            if mp_add <= (self.max_mp - self.mp):
                self.mp += mp_add
                if noty == "+":
                    renpy.notify(str(mp_add) + ' маны восстановлено!')
                else:
                    pass
            elif mp_add > (self.max_mp - self.mp):
                self.mp = self.max_mp
                if noty == "+":
                    renpy.notify('Мана восполнена!')
                else:
                    pass
            else:
                if noty == "+":
                    renpy.notify('У тебя и так максимально маны!')
                else:
                    pass
        
        def lvlup(self, lvl_add):
            while lvl_add > 0:
                lvl_add -= 1
                self.lvl += 1
                self.skill_points += 1
                self.max_hp += 5
                self.max_agil += 1
                self.max_intel += 1
                self.max_strength += 1
                renpy.notify('Уровень повышен!')
        
        def xp_rate_up(self, xp_r):
            if self.xp_rate > 0 and (self.xp_rate + xp_r) > 0:
                self.xp_rate += xp_r
            else:
                self.xp_rate = 0.1

        def xpup(self, xp_add):
            self.xp += (xp_add*self.xp_rate)
            while self.xp >= 1000 + self.lvl*10:
                self.xp -= (1000 + self.lvl*10)
                self.lvlup(1)
            if xp_add < (1000 + self.lvl*10) or (self.xp + xp_add) > (1000 + self.lvl*10):
                renpy.notify("Добавлено " + str(int(xp_add*self.xp_rate)) + " опыта!")
                
        def strengthup(self, strength_ch=0, noty="+", why="+"):
            if strength_ch == 0:
                noty = "-"
            if why == "+":
                if (self.strength + strength_ch) >= self.max_strength:
                    self.strength = self.max_strength
                else:
                    self.strength += strength_ch
                if noty == "+":
                    renpy.notify("Добавлено " + str(strength_ch) + " силы!")
            else:
                self.strength -= strength_ch
                if noty == "+":
                    renpy.notify("Сила снижена на " + str(strength_ch) + "!")
                
        def agilup(self, agi_ch=0, noty="+", why="+"):
            if agi_ch == 0:
                noty = "-"
            if why == "+":
                if (self.agil + agi_ch) >= self.max_agil:
                    self.agil = self.max_agil
                else:
                    self.agil += agi_ch
                if noty == "+":
                    renpy.notify("Добавлено " + str(agi_ch) + " ловкости!")
            else:
                self.agil -= agi_ch
                if noty == "+":
                    renpy.notify("Ловкость снижена на " + str(agi_ch) + "!")
                    
        def intelup(self, intel_ch=0, noty="+", why="+"):
            if intel_ch == 0:
                noty = "-"
            if why == "+":
                if (self.intel + intel_ch) >= self.max_intel:
                    self.intel = self.max_intel
                    if noty == "+":
                        renpy.notify("Интеллекта максимум!")
                else:
                    self.intel += intel_ch
                if noty == "+":
                    renpy.notify("Добавлено " + str(intel_ch) + " интеллекта!")
            else:
                self.intel -= intel_ch
                if noty == "+":
                    renpy.notify("Интеллект снижен на " + str(intel_ch) + " очков!")
                
        
        def statsup(self, str=0, agil=0, intel=0, why="+", noty="+"):
            self.strengthup(str, noty, why)
            self.agilup(agil, noty, why)
            self.intelup(intel, noty, why)
        
        def acc_trait(self, traitname):
            if traits[traitname]["traitn"] not in self.traits:
                if traits[traitname]["traitn"] not in self.incompatibility:
                    self.max_hp += traits[traitname].get("max_hp", 0)
                    self.max_mp += traits[traitname].get("max_mp", 0)
                    self.hp_regen(traits[traitname].get("hp_add", 0), noty="-")
                    self.mp_regen(traits[traitname].get("mp_add", 0), noty="-")
                    self.max_strength += traits[traitname].get("max_strength", 0)
                    self.max_intel += traits[traitname].get("max_intel", 0)
                    self.max_agil += traits[traitname].get("max_agil", 0)
                    self.strength += traits[traitname].get("strength", 0)
                    self.agil += traits[traitname].get("agil", 0)
                    self.intel += traits[traitname].get("intel", 0)
                    self.lvl += traits[traitname].get("lvl", 0)
                    self.skill_points += traits[traitname].get("skill_points", 0)
                    self.xp += traits[traitname].get("xp_add", 0)
                    self.xp_rate += traits[traitname].get("xp_rate", 0)
                    
                    if "incompatibility" in traits[traitname]:
                        self.incompatibility += traits[traitname].get("incompatibility")
                    if traits[traitname].get("visual_changes", "-") == "+":
                        for i in traits[traitname]["visual_add"]:
                            if i[2] == "high":
                                self.img_acc[i[1]] = i[0]
                            else:
                                if self.img_acc[i[1]] == "None":
                                    self.img_acc[i[1]] = i[0]
                                else:
                                    pass
                    self.traits.append(traits[traitname]["traitn"])
                    renpy.notify(traits[traitname].get("noty", ""))
                    if "upgrades" in traits[traitname]:
                        for i in traits[traitname]["upgrades"]:
                            result = list(set(i[0]) - set(self.traits))
                            if len(result) > 0:
                                pass
                            else:
                                for a in i[0]:
                                    self.del_trait(a)
                                self.acc_trait(i[1])
                    
                else:   
                    pass
            else:   
                pass
            
                

        def del_trait(self, traitname):
            if traits[traitname]["traitn"] in self.traits:
                self.max_hp -= traits[traitname].get("max_hp", 0)
                self.max_mp -= traits[traitname].get("max_mp", 0)
                self.max_strength -= traits[traitname].get("max_strength", 0)
                self.max_intel -= traits[traitname].get("max_intel", 0)
                self.max_agil -= traits[traitname].get("max_agil", 0)
                self.strength -= traits[traitname].get("strength", 0)
                self.intel -= traits[traitname].get("intel", 0)
                self.agil -= traits[traitname].get("agil", 0)
                self.xp_rate -= traits[traitname].get("xp_rate", 0)
                self.traits.remove(traits[traitname]['traitn'])
                if traits[traitname].get("visual_changes", "-") == "+":
                    for i in traits[traitname]["visual_add"]:
                        if self.img_acc[i[1]] == i[0]:
                            self.img_acc[i[1]] = "None"
                if "incompatibility" in traits[traitname]:
                    for i in traits[traitname]["incompatibility"]:
                        self.incompatibility.remove(i)
            else:   
                pass
        
        def additem(self, itemname="None", many=1):
            self.currentitems=[]
            for i in self.inventory:
                self.currentitems.append(i[0])
            if itemname == "None":
                print("Такого предмета нет!")
                pass
            elif itemname in self.currentitems:
                for i in self.inventory:
                    if i[0] == itemname:
                        i[1] += many
            elif itemname not in self.currentitems:
                self.inventory.append([itemname, many])
                
        def delitem(self, itemname="None", many=1):
            for i in self.inventory:
                if i[0] == itemname:
                    if i[1] > many:
                        i[1] -= many
                    elif i[1] == many:
                        self.inventory.remove(i)
                    elif i[1] < many:
                        print("Не хватает предметов, это странно...")
                        self.inventory.remove(i) 
        
        def use_item(self, itemname, how=1):
            if "consumable" in items[itemname]['type']:
                self.buff_add(itemname)
            elif "equippable" in items[itemname]['type']:
                if itemname != self.equip[items[itemname]["slot"]]:
                    if self.equip[items[itemname]["slot"]] != "None":
                        currentitem = self.equip[items[itemname]["slot"]]
                        self.unequip_item(currentitem)
                        self.equip_item(itemname)
                    else:
                        self.equip_item(itemname)   
                else:
                    self.unequip_item(itemname)
            else:
                print("Ошибка - Неизвестный тип!")
                
        def null(self):
            pass
        
        def equip_item(self, itemname):
            self.equip[items[itemname]["slot"]] = items[itemname]["itemn"]
            self.img_acc[items[itemname]["slot"]] = items[itemname]["model"]
            self.delitem(itemname, 1)
            
            self.max_hp += items[itemname].get("max_hp", 0)
            self.max_mp += items[itemname].get("max_mp", 0)
            self.hp_regen(items[itemname].get("hp_add", 0), "-")
            self.mp_regen(items[itemname].get("mp_add", 0), "-")
            self.max_strength += items[itemname].get("max_strength", 0)
            self.max_agil += items[itemname].get("max_agil", 0)
            self.max_intel += items[itemname].get("max_intel", 0)
            self.strength += items[itemname].get("strength", 0)
            self.agil += items[itemname].get("agil", 0)
            self.intel += items[itemname].get("intel", 0)

        def unequip_item(self, itemname):
            clearslot = items[itemname]["slot"]
            self.additem(self.equip[clearslot])
            self.equip[items[itemname]["slot"]] = "None"
            self.img_acc[items[itemname]["slot"]] = "None"
            
            self.max_hp -= items[itemname].get("max_hp", 0)
            self.max_mp -= items[itemname].get("max_mp", 0)
            self.strength -= items[itemname].get("strength", 0)
            self.max_strength -= items[itemname].get("max_strength", 0)
            self.max_intel -= items[itemname].get("max_intel", 0)
            self.max_agil -= items[itemname].get("max_agil", 0)
            self.agil -= items[itemname].get("agil", 0)
            self.intel -= items[itemname].get("intel", 0)



        def buff_add(self, itemname):
            timedur = time.globalminutes + items[itemname].get("timeact", 0)
            if timedur > 0:
                self.buffs.append([timedur, items[itemname]['itemn']])
            self.delitem(itemname, 1)
            
            self.max_hp += items[itemname].get("max_hp", 0)
            self.max_mp += items[itemname].get("max_mp", 0)
            self.hp_regen(items[itemname].get("hp_add", 0), "-")
            self.mp_regen(items[itemname].get("mp_add", 0), "-")
            self.max_strength += items[itemname].get("max_strength", 0)
            self.max_agil += items[itemname].get("max_agil", 0)
            self.max_intel += items[itemname].get("max_intel", 0)
            self.strength += items[itemname].get("strength", 0)
            self.agil += items[itemname].get("agil", 0)
            self.intel += items[itemname].get("intel", 0)
            
        def buff_del(self, itemname):
            self.max_hp -= items[itemname].get("max_hp", 0)
            self.max_mp -= items[itemname].get("max_mp", 0)
            self.strength -= items[itemname].get("strength", 0)
            self.max_strength -= items[itemname].get("max_strength", 0)
            self.max_intel -= items[itemname].get("max_intel", 0)
            self.max_agil -= items[itemname].get("max_agil", 0)
            self.agil -= items[itemname].get("agil", 0)
            self.intel -= items[itemname].get("intel", 0)