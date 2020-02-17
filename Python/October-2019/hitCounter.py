
class HitCounter:
    def __init__(self):
        self.hits = []

    def record(self, timestamp):
        self.hits.append(timestamp)

    def total(self):
        return len(self.hits)

    def range(self, lowerTime, higherTime):
        if lowerTime in self.hits and higherTime in self.hits:
            # find indexes
            indxLower = self.hits.index(lowerTime)
            indxHigher = self.hits.index(higherTime)
            return len(self.hits[indxLower + 1: indxHigher])
        else:
            return 0

    def showTimeStampError(self):
        print("Timestamp not registered")


# Create the counter
hitCounter = HitCounter()
# Add some hits by adding the timestamps
hitCounter.record("09130417TXUS")
hitCounter.record("09130786TXUS")
hitCounter.record("09140061TXUS")
hitCounter.record("09140526TXUS")
hitCounter.record("09150863TXUS")
hitCounter.record("09160124TXUS")
# Check range between some timestamps
print(hitCounter.range("09130786TXUS", "09150863TXUS"))
