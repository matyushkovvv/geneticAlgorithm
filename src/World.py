from enum import Enum


class WorldType(Enum):
    WATER_WORLD = 1

    def get_settings(self):
        settings_map = {
            WorldType.WATER_WORLD: {
                'entity': {
                    'HERBIVORES': 1,
                    'PREDATOR': 1,
                    'HYBRID': 1,
                    'MINERAL': 200,
                },
                'rules': {
                    'depth_factor': 10,
                    'gravity': {
                        'HERBIVORES': False,
                        'PREDATOR': False,
                        'HYBRID': False,
                        'MINERAL': True,
                    },
                    'energy_reproduction': 40,
                    'cannibalism': True
                }
            }
        }

        return settings_map[self]
