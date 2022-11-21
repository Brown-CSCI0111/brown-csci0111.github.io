from dataclasses import dataclass

@dataclass
class Course:
    name: str
    enrollment: int
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

courses_dict_class = {"CSCI0111" : CSCI111,
                      "ENVS1552" : ENVS1552,
                      "LANG0800": LANG0800,
                      "SOC1260": SOC1260
                     }

courses_dict_dict = {"CSCI0111" : {"enrollment": 208, "prof": "Fisler", "location": "Metcalf"},
                      "ENVS1552" : {"enrollment": 9, "prof": "Egilman", "location": "Smith-Buonanno G18"},
                      "LANG0800": {"enrollment": 8, "prof": "Sokolosky", "location": "SciLi 604"},
                      "SOC1260": {"enrollment": 175, "prof": "Spearin", "location": "Metcalf"}
                    }

pass