#
# how many days does the flights table cover ?
import pandas
def calculate_days(days):

   data = pandas.read_csv("flights.csv")
   days = data["day"]
   print(sum(days))
#how many departure cities the flight database covers
def calculate_cities(cities):
       data = pandas.read_csv("flights.csv")
       cities =data["dest"].tolist()

       print(len(cities))
# what is the relationship between flights and planes tables ?
def calculate_relation():
      data2 = pandas.read_csv("planes.csv")
      data = pandas.read_csv("flights.csv")

      relation = data2.apply(tuple,1).isin(data.apply(tuple,1))
      print(relation) #true shows the relation


#which airplane manufacturer incurred the most delays in the analysis period ?
def show_flight_of_max_delay():
   data = pandas.read_csv("flights.csv")
   max_delay = data["dep_delay"].max()
   airplane = (data[data.dep_delay==max_delay])
   print(airplane.flight)  #the flight of this airplane incurred most delays










