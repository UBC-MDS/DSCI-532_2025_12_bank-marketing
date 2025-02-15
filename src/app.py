from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H2("Bank Marketing Analytics", style={'textAlign': 'center', 'color': 'white', 'fontWeight': 'bold', 'fontSize': '50px'}),
        html.Hr(style={'color': 'gray', 'borderWidth': '5px'}),
        html.Div([
            html.H4("Filters", style={'textAlign': 'center', 'fontSize': '35px', 'marginTop': '20px'}),
            html.Div([
                html.P("Year", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px'}),
                dcc.Checklist(
                    options=[
                        {'label': '2008', 'value': '2008'},
                        {'label': '2009', 'value': '2009'},
                        {'label': '2010', 'value': '2010'}
                    ],
                    inline=True,  
                    labelStyle={
                        'backgroundColor': '#e08136', 
                        'color': 'black',
                        'padding': '10px 15px', 
                        'marginRight': '11px',
                        'marginLeft': '11px', 
                        'borderRadius': '5px',
                        'fontSize': '18px'
                    }
                )
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'}),
            html.Div([
                html.P("Age", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px'}),
                dcc.RangeSlider(min=18, max=100, value=[25, 60], marks={18: '18', 100: '100'}),
            ], style = {'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),
            html.Div([
                html.P("Marital Status", style={'textAlign': 'center', 'fontSize': '25px', 'color': 'black', 'marginTop': '5px', 'marginBottom': '5px'}),
                dcc.Checklist(
                    options=[
                        {'label': 'Married', 'value': 'Married'},
                        {'label': 'Divorced', 'value': 'Divorced'},
                        {'label': 'Single', 'value': 'Single'}
                    ],
                    inline=True,  
                    labelStyle={
                        'backgroundColor': '#e08136', 
                        'color': 'black',
                        'padding': '10px 15px', 
                        'marginRight': '20px',
                        'marginLeft': '20px',
                        'marginTop': '10px', 
                        'borderRadius': '5px',
                        'fontSize': '18px'
                    }
                )
            ], style={'backgroundColor': 'white', 'padding': '15px', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginTop': '20px'}),
            html.P("Job Type ...", style={'textAlign': 'center'}),
        ], style={'color': 'white'})
    ], style={'width': '20%', 'backgroundColor': '#232242', 'padding': '20px', 'height': '100vh'}),

    html.Div([
        html.Div([
            html.Div([
                html.Div("Proportion Subscribed", style={'fontWeight': 'bold', 'textAlign': 'center', 'fontSize': '25px'}), html.H3("0.5", style={'textAlign': 'center', 'fontSize': '35px', 'marginTop': '10px', 'marginBottom': '10px'})
            ], style={'backgroundColor': 'white', 'padding': '10px', 'margin': '5px', 'width': '15%'}),
            html.Div([
                html.Div("Average Number of Contacts during the Campaign", style={'fontWeight': 'bold', 'textAlign': 'center', 'fontSize': '20px'}), html.H3("2.75", style={'textAlign': 'center', 'fontSize': '35px', 'marginTop': '20px', 'marginBottom': '10px'})
            ], style={'backgroundColor': 'white', 'padding': '10px', 'margin': '5px', 'width': '20%'}),
            html.Div([
                html.Div("Average Number of Contacts before the Campaign", style={'fontWeight': 'bold', 'textAlign': 'center', 'fontSize': '20px'}), html.H3("0.58", style={'textAlign': 'center', 'fontSize': '35px', 'marginTop': '20px', 'marginBottom': '10px'})
            ], style={'backgroundColor': 'white', 'padding': '10px', 'margin': '5px', 'width': '20%'}),
            html.Div([
                html.Div("Average Last Contact Duration in minutes", style={'fontWeight': 'bold', 'textAlign': 'center', 'fontSize': '20px'}), html.H3("4.2", style={'textAlign': 'center', 'fontSize': '35px', 'marginTop': '20px', 'marginBottom': '10px'})
            ], style={'backgroundColor': 'white', 'padding': '10px', 'margin': '5px', 'width': '20%'}),
            html.Div([
                html.P("Subscribed?", style={'textAlign': 'center', 'fontWeight': 'bold', 'fontSize': '25px', 'marginTop': '0px', 'marginBottom': '10px'}),
                html.Div([
                    html.Div(style={'width': '20px', 'height': '20px', 'backgroundColor': '#6dbb6f', 'display': 'inline-block', 'marginRight': '5px'}),
                    html.Div("Yes", style={'display': 'inline-block', 'verticalAlign': 'middle', 'color': 'black', 'marginBottom': '8px'})
                ], style={'margin': '5px'}),
                html.Div([
                    html.Div(style={'width': '20px', 'height': '20px', 'backgroundColor': '#ee7171', 'display': 'inline-block', 'marginRight': '5px'}),
                    html.Div("No", style={'display': 'inline-block', 'verticalAlign': 'middle', 'color': 'black', 'marginBottom': '8px'})
                ], style={'margin': '5px'})
            ], style={'padding': '10px', 'margin': '5px', 'backgroundColor': 'white', 'width': '10%'})
        ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '15px', 'height': '15%'}),

        html.Div([
            html.Div([
                html.Div("Education", style={'height': '15%', 'padding': '10px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '30px', 'fontWeight': 'bold'}),
                html.Div(style={'height': '85%', 'backgroundColor': 'white'})
            ], style={'width': '45%', 'margin': '1%'}),
            html.Div([
                html.Div("Number of Contacts", style={'height': '15%', 'padding': '10px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '30px', 'fontWeight': 'bold'}),
                html.Div(style={'height': '85%', 'backgroundColor': 'white'})
            ], style={'width': '45%', 'margin': '1%'}),
            html.Div([
                html.Div("Balance", style={'height': '15%', 'padding': '10px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '30px', 'fontWeight': 'bold'}),
                html.Div(style={'height': '85%', 'backgroundColor': 'white'})
            ], style={'width': '45%', 'margin': '1%', 'marginTop':'30px'}),
            html.Div([
                html.Div("Loan", style={'height': '15%', 'padding': '10px', 'backgroundColor': '#232242', 'textAlign': 'center', 'color': 'white', 'fontSize': '30px', 'fontWeight': 'bold'}),
                html.Div(style={'height': '85%', 'backgroundColor': 'white'})
            ], style={'width': '45%', 'margin': '1%', 'marginTop':'30px'})
        ], style={'display': 'flex', 'flexWrap': 'wrap', 'height': '700px'})
    ], style={'width': '80%', 'backgroundColor': '#d3d3d3', 'padding': '20px', 'height': '100vh'})
], style={'display': 'flex'})

if __name__ == '__main__':
    app.run_server(debug=True)




