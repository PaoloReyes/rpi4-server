# Server imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Subscripts imports
import sys
sys.path.insert(1, '/home/paolo/ssh')
sys.path.insert(1, '/home/paolo/stock-portfolio/python')
from ngrok_tunnels import Ngrok_Connection
from stock_portfolio import Stock_Portfolio

# App
app = FastAPI()

# CORS
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_methods=["*"],
	allow_headers=["*"],
)

# Subscripts
portfolio = Stock_Portfolio()

internet_access = False
while not internet_access:
	try:
		ngrok_connection = Ngrok_Connection('web-server', 'ssh')
		internet_access = True
	except:
		internet_access = False

# Stock Portfolio Stuff
@app.get('/stock-portfolio/register')
def stock_portfolio_register_data(hey: float = 0.0, bbva: float = 0.0, uala = 0.0, nu: float = 0.0, fibras: float = 0.0, etfs: float = 0.0, cetes: float = 0.0, finsus: float = 0.0, mercado_pago: float = 0.0, bitso: float = 0.0, cash: float = 0.0):
    return portfolio.register_data(hey, bbva, uala, nu, fibras, etfs, cetes, finsus, mercado_pago, bitso, cash)

@app.get('/stock-portfolio/request')
def stock_portfolio_request_data():
	return portfolio.request_data()

@app.get('/stock-portfolio/register_percentages')
def stock_portfolio_register_percentages(debt: int = 0, sofipos: int = 0, fibras: int = 0, stocks: int = 0, crypto: int = 0):
	return portfolio.register_percentages(debt, sofipos, fibras, stocks, crypto)

@app.get('/stock-portfolio/request_percentages')
def stock_portfolio_request_percentages():
	return portfolio.request_percentages()

@app.get('/stock-portfolio/register_prediction')
def stock_portfolio_register_prediction(rate: float = 0.0, years: int = 0, contributions : float = 0.0):
	return portfolio.register_prediction(rate, years, contributions)

@app.get('/stock-portfolio/request_prediction')
def stock_portfolio_request_prediction():
	return portfolio.request_prediction()

# Ngrok Stuff
@app.get('/ngrok/ssh')
def get_ngrok_process():
	return ngrok_connection.get_ngrok_tcp(22)