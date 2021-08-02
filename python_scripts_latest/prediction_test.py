# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git

from bigml.ensemble import Ensemble

# Downloads and generates a local version of the ensemble, if it
# hasn't been downloaded previously.
from bigml.api import BigML

ensemble = Ensemble('ensemble/61085e0f5e269e0554018f9f',
                    api=BigML("bgidataproject2021",
                              "e8dd610fb20cacb4420d55a4d7d4630dc5e8024a",
                              domain="bigml.io"))

# To make predictions fill the desired input_data in next line.
input_data = {"vehicle_type":'van',"special_day":'YES',"day":5,"hour":4,"entering_section":1}
prediction = ensemble.predict(input_data, full=True)
print('entering_section = 1 and preticted: ')
print(prediction)
print()
input_data = {"vehicle_type":'van',"special_day":'YES',"day":5,"hour":4,"entering_section":2}
prediction = ensemble.predict(input_data, full=True)
print('entering_section = 2 and preticted: ')
print(prediction)
print()
input_data = {"vehicle_type":'van',"special_day":'YES',"day":5,"hour":4,"entering_section":3}
prediction = ensemble.predict(input_data, full=True)
print('entering_section = 3 and preticted: ')
print(prediction)
print()
input_data = {"vehicle_type":'van',"special_day":'YES',"day":5,"hour":4,"entering_section":4}
prediction = ensemble.predict(input_data, full=True)
print('entering_section = 4 and preticted: ')
print(prediction)
print()
input_data = {"vehicle_type":'van',"special_day":'YES',"day":5,"hour":4,"entering_section":5}
prediction = ensemble.predict(input_data, full=True)
print('entering_section = 5 and preticted: ')
print(prediction)
print()
#
# input_data: dict for the input values
# (e.g. {"petal length": 1, "sepal length": 3})
# full: if set to True, the output will be a dictionary that includes all the
# available information in the predicted node. The attributes vary depending
# on the ensemble type. Please check:
# https://bigml.readthedocs.io/en/latest/#local-ensemble-s-predictions
