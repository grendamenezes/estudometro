import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq

exerc = [4,1,15,3,5,1]

def generate_message(avg_temp):
    if avg_temp <= 25:
        return ""
    elif 25 < avg_temp <= 50:
        return "Gostosa e inteligente?? Ah para né"
    elif 50 < avg_temp <= 75:
        return "Craque do jogo!!!"
    elif 75 < avg_temp <= 99:
        return "AGORA!! Nelson foi visto chorando no banheiro do poli"
    else:
        return "UM MONSTRO ENJAULADO!!"

app = dash.Dash(__name__)
server=app.server

app.layout = html.Div([
    html.H1("Dani macetando velho calvo",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div(id='message-box', style={'textAlign': 'center','color': 'red'}), html.Br(), html.Br(), html.Br(),
    
    # Div para centralizar o termômetro e a imagem
    html.Div([
        # Termômetro graduado
        daq.Thermometer(
            id='thermometer',
            min=0,
            max=100,
            scale={'start': 0, 'interval': 10, 'labelInterval': 10},
            label='Estudômetro',
        ),
        
        html.Img(id='sun-img', src='https://raw.githubusercontent.com/grendamenezes/estudometro/main/dani_docinho2.png', style={'height': '100px', 'width': '100px', 'margin-left': '10px'}),
    ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    
    html.Br(), html.Br(), html.Br(), html.Br(),

    html.Div([html.H2("Assuntos",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        dcc.Checklist(
            id='ass',
            options=[
                {'label': '18.1: Introdução ao método das características', 'value': 'Assunto1'},
                {'label': '18.2: Características e classificação de EDPs', 'value': 'Assunto2'},
                {'label': '18.3: O método de separação de variáveis para problemas parabólicos', 'value': 'Assunto3'},
                {'label': '18.4: O método de separação de variáveis para problemas elíticos', 'value': 'Assunto4'},
                {'label': '18.5: O método de separação de variáveis para problemas hiperbólicos', 'value': 'Assunto5'},
                {'label': '18.6: A solução de d’Alembert', 'value': 'Assunto6'},
                {'label': '18.7: Problemas difusivos com transformações de similaridade', 'value': 'Assunto7'}
            ],
            value=[],  # Inicialmente nenhum valor está selecionado
            style={'textAlign': 'left','flex-direction': 'column', 'display': 'flex'}, persistence=True
        ),
    ], style={'textAlign': 'left', 'display': 'inline-block', 'vertical-align': 'middle', 'width': '50%'}),
    html.Div([html.H2("Exercícios",style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
		html.H4("Cap. 18.1: 4 exercícios",style={'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
		dcc.Input(id='exer1', type='text', placeholder='Quantidade de exercícios feitos',
		          style={'width': '200px','textAlign': 'center','flex-direction': 'column', 'display': 'flex'}, persistence=True),
		html.H4("Cap. 18.2: 1 exercício",style={'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
		dcc.Input(id='exer2', type='text', placeholder='Quantidade de exercícios feitos',
		          style={'width': '200px','textAlign': 'center','flex-direction': 'column', 'display': 'flex'}, persistence=True),
		html.H4("Cap. 18.3: 15 exercícios",style={'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
		dcc.Input(id='exer3', type='text', placeholder='Quantidade de exercícios feitos',
		          style={'width': '200px','textAlign': 'center','flex-direction': 'column', 'display': 'flex'}, persistence=True),
		html.H4("Cap. 18.4: 3 exercícios",style={'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
		dcc.Input(id='exer4', type='text', placeholder='Quantidade de exercícios feitos',
		          style={'width': '200px','textAlign': 'center','flex-direction': 'column', 'display': 'flex'}, persistence=True),
		html.H4("Cap. 18.5: 5 exercícios",style={'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
		dcc.Input(id='exer5', type='text', placeholder='Quantidade de exercícios feitos',
		          style={'width': '200px','textAlign': 'center','flex-direction': 'column', 'display': 'flex'}, persistence=True),
		html.H4("Cap. 18.7: 1 exercício",style={'display': 'flex', 'align-items': 'left', 'justify-content': 'left'}),
		dcc.Input(id='exer6', type='text', placeholder='Quantidade de exercícios feitos',
		          style={'width': '200px','textAlign': 'center','flex-direction': 'column', 'display': 'flex'}, persistence=True),
    ], style={'textAlign': 'right', 'display': 'inline-block', 'vertical-align': 'middle', 'width': '30%'}),
    html.Br(),html.Br(),
    
    
])

@app.callback(
	Output('message-box', 'children'),
    Output('thermometer', 'value'),
    Output('thermometer', 'color'),
    Output('sun-img', 'style'),
    Input('ass', 'value'),
    Input('exer1', 'value'),
    Input('exer2', 'value'),
    Input('exer3', 'value'),
    Input('exer4', 'value'),
    Input('exer5', 'value'),
    Input('exer6', 'value')
)
def update_thermometer(assun,exer1,exer2,exer3,exer4,exer5,exer6):
	if not exer1: exer1=0 
	if not exer2: exer2=0 
	if not exer3: exer3=0 
	if not exer4: exer4=0 
	if not exer5: exer5=0 
	if not exer6: exer6=0 
	avg_temp = (len(assun)/7)*50 + (int(exer1)/exerc[0])*(100/12)+(int(exer2)/exerc[1])*(100/12)+(int(exer3)/exerc[2])*(100/12)+(int(exer4)/exerc[3])*(100/12)+(int(exer5)/exerc[4])*(100/12)+(int(exer6)/exerc[5])*(100/12)
	thermometer_value = avg_temp
	img_style = {
        'height': '150px',
        'width': '100px',
        'position': 'relative',
        'top': f'{2 * (60 - thermometer_value)}px'
    }
	color = f'rgb({255 - int(2.55 * thermometer_value)}, {int(2.55 * thermometer_value)}, 0)'
	message = generate_message(avg_temp)
	return html.H3(message),thermometer_value, color, img_style

if __name__ == '__main__':
    app.run_server(debug=True)
