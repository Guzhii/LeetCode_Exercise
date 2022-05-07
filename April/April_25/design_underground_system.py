class UndergroundSystem:

    def __init__(self):
        self.check = {}
        self.time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.check[id][0]
        startTime = self.check[id][1]
        
        self.check.pop(id)
        
        key = startStation + "," + stationName
        if key not in self.time:
            self.time[key] = [[], 0]
            
        self.time[key][0].append(t - startTime)
        self.time[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + "," + endStation
        return sum(self.time[key][0]) / self.time[key][1]
