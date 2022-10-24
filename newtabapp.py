import dash
from dash import dcc, Dash, html, Input, Output, State, callback_context, no_update

app = Dash(__name__, update_title=None, suppress_callback_exceptions=True)

websites = {
    'Youtube': {
        'url': 'youtube.com'
    },
    'Amazon': {
        'url': 'amazon.com'
    }
}

website_containers = []
for k, v in websites.items():
    website_containers.append(html.Div(k, className='website'))

app.layout = html.Div([
    html.Div([
        html.Div(html.Img(src='assets/youtube.png'), className='item'),
        html.Div('ayo2', className='item'),
        html.Div('ayo1', className='item'),
        html.Div('ayo1', className='item'),
        html.Div('ayo1', className='item'),
        html.Div('ayo1', className='item'),],
    className='center'),
    html.Div([
        html.Div('ayo1', className='item'),
        html.Div('ayo2', className='item'),
        html.Div('ayo1', className='item'),
        html.Div('ayo1', className='item'),
        html.Div('ayo1', className='item'),
        html.Div('ayo1', className='item'),],
    className='center'),],
className='background')

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050", debug=True)

