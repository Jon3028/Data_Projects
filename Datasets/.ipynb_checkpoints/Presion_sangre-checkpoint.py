import pandas as pd
import wget
import requests
from zipfile import ZipFile
import plotly.offline as pyo
import plotly.graph_objs as go


url = 'https://storage.googleapis.com/kagglesdsdata/datasets/2527538/4289678/diabetes.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221103%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221103T034252Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=323062f94e8302c1dae6399c36f7b5d8a93e227e8c1772d5047af7d2842dc32d2cfba16aec58f794d1cd88b3d11d29aeee004b6d286b2e534d6ba1359f373a1ae10658c422f5cf944abb5e80c6589cdc26c15b9ddb19b98740963ece103379f41c2f638070bc61aa75ddabb9b6ac779feec22ec312291f014f0657bebfe7a345a1da6985af5b734ab27391289722c34db8a3610cb667cc9b5cc8c5b1fa3b53af7a8a721f2a29283e726718b4ce4f15a42575032fd9f8755247fae0f28c6f504896140e96b1e5fcfda560a7fb996c2b22e5e5cbd41c6824aef6450261b5afc530ef5e7912abe5cbab79e10fce2c8886a304c56a9762c664d4d9dc1c85166d53e2'
data = pd.read_csv(url) # use sep="," for coma separation. 
data1=[go.Scatter(x=data["Age"],y=data["BloodPressure"],mode="markers",marker=dict(size=12,symbol="circle",line={"width":3}))]
layout1=go.Layout(title="Presion de sangre por edad",xaxis=dict(title="edad"),yaxis=dict(title="presion sanguinea"))
fig=go.Figure(data=data1,layout=layout1)
pyo.plot(fig,filename="Sangre.html") 