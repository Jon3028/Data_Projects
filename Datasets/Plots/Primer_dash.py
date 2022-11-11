import dash
#import dash_core_components as dcc
from dash import dcc
#import dash_html_components as html
from dash import html

#Inicializamos el layout
app=dash.Dash()

#Definimos los objetos dentro del layout
app.layout =html.Div([
                html.H1(children="Primer dashboard con Dash"),
                html.Div(children="Dash es un framework para aplicaciones web"),
                dcc.Graph(id="figura_inicial",
                      figure={"data":[
                                      {"x":[1,2,3,4],"y":[1,1,2,2],"type":"bar","name":"Madrid"},
                                      {"x":[1,2,3,4],"y":[3,6,8,15],"type":"bar","name":"Barcelona"},
                                      ],
                              "layout":{"title":"Comparativa Madrid-Barcelona"}
                             }           
                        )
                ])

if __name__=="__main__":
        app.run_server(debug=True,host='192.168.1.117')