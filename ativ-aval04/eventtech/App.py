from dao import EventoDAO, ConnectionFactory
from entity import Evento
from enums import CategoriasEvento, StatusEvento
from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)
dao = EventoDAO.EventoDAO()