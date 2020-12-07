import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        #propriedades da janela (tamanho e título)
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        #caixa de texto
        self.txtUser = QLineEdit(self)
        self.txtUser.move(130,100)
        self.txtUser.resize(400, 30)
        self.txtUser.setStyleSheet('QLineEdit{font-size: 16px}')

        #caixa de senha
        self.txtPw = QLineEdit(self)
        self.txtPw.setEchoMode(QLineEdit.Password)
        self.txtPw.move(130,200)
        self.txtPw.resize(400, 30)

        #botão 1
        botao1 = QPushButton('Entrar', self)
        botao1.move(270,500)
        botao1.resize(100, 50)
        botao1.setStyleSheet('QPushButton{background-color: #10ff6f; font: bold; font-size: 20px}')
        botao1.clicked.connect(self.botao1_click)

        #botao 2
        botao2 = QPushButton('Sair', self)
        botao2.move(420,500)
        botao2.resize(100, 50)
        botao2.setStyleSheet('QPushButton{background-color: #ff1015; font: bold; font-size: 20px}')
        botao2.clicked.connect(self.botao2_click)

        #label usuário
        lbl_1 = QLabel(self)
        lbl_1.setText('Usuário: ')
        lbl_1.move(50,100)
        lbl_1.setStyleSheet('QLabel{font-size: 16px}')

        #label senha
        lbl_2 = QLabel(self)
        lbl_2.setText('Senha: ')
        lbl_2.move(50,200)
        lbl_2.setStyleSheet('QLabel{font-size: 16px}')

        #label que muda de texto (teste)
        self.lbl_3 = QLabel(self)
        self.lbl_3.setText('Teste')
        self.lbl_3.move(50,300)
        self.lbl_3.setStyleSheet('QLabel{font-size: 16px}')

        #imagem
        self.net = QLabel(self)
        self.net.move(370,30)
        self.net.resize(100, 50)
        self.net.setPixmap(QtGui.QPixmap('internet.png'))



        self.CarregarJanela()
        
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def botao1_click(self):
        print('Botão foi clicado')

    def botao2_click(self):
        self.lbl_3.setText('Hello World')

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())