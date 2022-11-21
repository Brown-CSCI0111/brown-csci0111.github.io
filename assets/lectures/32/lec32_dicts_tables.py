from dataclasses import dataclass

@dataclass
class Course:
    name: str
    enrollment: num
    prof: str
    location: str


"""
course     enrollment     prof           location
---------------------------------------------------
"CSCI0111"   208       "Fisler"          "Metcalf"
"ENVS1552"    9        "Egilman"     "Smith-Buonanno G18"
"LANG0800"    8       "Sokolosky"       "SciLi 604"
"SOC1260"    175       "Spearin"         "Metcalf"
"""

CSCI111 = Course("CSCI0111", 208, "Fisler", "Metcalf")
ENVS1552 = Course("ENVS1552", 9, "Egilman", "Smith-Buonanno G18")
LANG0800 = Course("LANG0800", 8, "Sokolosky", "SciLi 604")
SOC1260 = Course("SOC1260", 175, "Spearin", "Metcalf")

courses_list = [CSCI111, ENVS1552, LANG0800, SOC1260]

courses_dict = {"CSCI0111" : CSCI111,
                "ENVS1552" : ENVS1552,
                "LANG0800": LANG0800,
                "SOC1260": SOC1260
               }
