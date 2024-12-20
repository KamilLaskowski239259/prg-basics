class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 10
        self.fare = 5

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
    # your program
        print('RECEIPT')
        print('=========')
        print(f'You traveled: {self.distance}')
        print(f'Your rate per km: {self.rate_per_km}')
        print(f'Your fare: {self.fare}')

def main():
    ride=TaxiRide(rate_per_km=2)
    ride.calculate_fare(distance=15)
    ride.print_receipt()

if __name__ == "__main__":
    main()
