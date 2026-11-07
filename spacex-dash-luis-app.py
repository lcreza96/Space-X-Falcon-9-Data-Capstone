# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)
dropdown_options= [{'label': 'All Sites', 'value': 'ALL'}]+ [{'label': site, 'value': site} for site in spacex_df['Launch Site'].dropna().unique()]

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',options= dropdown_options, placeholder= 'Select a Launch Site', searchable= True, value='ALL'),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                min= 0, 
                                max= 10000, 
                                marks= {0: '0', 10000:'10000'}, 
                                value= [0, 10000]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        data= spacex_df.groupby('Launch Site')['class'].sum().reset_index()
        fig = px.pie(data, values='class', 
        names='Launch Site', 
        title='Launching Sites')
        return fig
    else:
        filtered_df2= spacex_df[spacex_df['Launch Site'] == entered_site]
        filtered_df3=filtered_df2.groupby('class').size().reset_index(name = 'count')
        fig2= px.pie(filtered_df3, values='count', names= 'class', title= 'Launching Sites')
        return fig2
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'), 
Input(component_id='site-dropdown', component_property='value'), Input(component_id="payload-slider", component_property="value"))
def get_scatter_plot(entered_site, payloadrange):
    filtered_df= spacex_df
    filtered_df= filtered_df[(filtered_df['Payload Mass (kg)'] >=  payloadrange[0]) 
     & (filtered_df['Payload Mass (kg)'] <= payloadrange[1])] 
    if entered_site == 'ALL':
        fig4= px.scatter(filtered_df, x= 'Payload Mass (kg)', y= 'class')
        return fig4
    else:
        filtered_df4= filtered_df[filtered_df['Launch Site']== entered_site]
        fig5= px.scatter(filtered_df4, x= 'Payload Mass (kg)', y= 'class')
        return fig5 
        
# Run the app
if __name__ == '__main__':
    app.run()
