class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        
        # onbulbs = set()

        # for bulb in bulbs:
        #     if bulb in onbulbs:
        #         onbulbs.remove(bulb)
        #     else:
        #         onbulbs.add(bulb)

        # # onbulbs.sort()
        # onbulbs  = list(onbulbs)
        # onbulbs.sort()
        # return onbulbs


        on = set()

        for bulb in bulbs:
            if bulb in on:
                on.remove(bulb)
            else:
                on.add(bulb)

        return sorted(on)