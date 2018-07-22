# -*- coding:Latin-1 -*-io import *

from Tkinter import *
from random import randrange

#pour détertminer les identifiant pouvant être déplacé voir la fonction :
#.find_enclosed(x1, y1, x2, y2)
	
class Application(Tk):
	def __init__(self):
		Tk.__init__(self)	#Constructeur de la classe parente
		self.can=Canvas(self,width=300,height=350,bg="grey")
		self.can.pack(side=TOP,padx=5,pady=5)	
		self.xPiece=[10,110,210,10,110,210,10,110,210]	
		self.yPiece=[10,10,10,110,110,110,210,210,210]
		self.compteur=0
		
		self.p1=Piece(self.can,self.xPiece[0],self.yPiece[0],80,"1",'white',3)	#pièce 1
		self.p2=Piece(self.can,self.xPiece[1],self.yPiece[1],80,"2",'white',3)	#pièce 2
		self.p3=Piece(self.can,self.xPiece[2],self.yPiece[2],80,"3",'white',3)	#...
		self.p4=Piece(self.can,self.xPiece[3],self.yPiece[3],80,"4",'white',3)
		self.p5=Piece(self.can,self.xPiece[4],self.yPiece[4],80,"5",'white',3)
		self.p6=Piece(self.can,self.xPiece[5],self.yPiece[5],80,"6",'white',3)
		self.p7=Piece(self.can,self.xPiece[6],self.yPiece[6],80,"7",'white',3)
		self.p8=Piece(self.can,self.xPiece[7],self.yPiece[7],80,"8",'white',3)	#pièce 8
		self.p9=Piece(self.can,self.xPiece[8],self.yPiece[8],80,"",'grey',0)	#Espace libre
		self.p=(self.p1,self.p2,self.p3,self.p4,self.p5,self.p6,self.p7,self.p8,self.p9)
		
		self.can.create_rectangle(0,305,300,350,fill='#F3EFC2',width=0)
		#Bouton mélanger :
		self.bt1=self.can.create_rectangle(10,310,110,345,fill='white',width=1)
		self.can.create_text((60,327),text='Mélanger',font=('Helvetica',12,'bold'),fill='#FFA500')
		self.can.bind("<Button-1>",self.mouseDown)
		
		#Texte compte point :
		self.ComptPoint=self.can.create_text((120,327),text='Nombre de coups : 0',font=('Helvetica',12,'bold'),fill='#000000',anchor='w')
			
	def mouseDown(self,event):
		"Opé à effectuér lors de l'appui sur le bouton de la souris :"
		self.currObject=None	#Dessin sélectionné
		#find_closet renvoie la référence vers le dessin le plus proche :
		objet=self.can.find_closest(event.x,event.y,10)
		for a in objet:
			if a >= self.bt1 and a < self.ComptPoint :
				self.melanger()
		
	def melanger(self):
		for i in range (2500):
			val=randrange(4)
			if val ==0 :				
				app.droit('')
			elif val ==1 :				
				app.gauche('')
			elif val ==2 :				
				app.haut('')
			elif val ==3 :				
				app.bas('')
		self.compteur=0
		text='Nombre de coups : ' + str(self.compteur)
		self.can.dchars(self.ComptPoint,0,'end')
		self.can.insert(self.ComptPoint,0,text)
	
	def afficherPoint(self):		
		self.compteur+=1
		text='Nombre de coups : ' + str(self.compteur)
		self.can.dchars(self.ComptPoint,0,'end')
		self.can.insert(self.ComptPoint,0,text)
		
	def droit(self,evt):
		#~ Canvas.insert(tagOrId, beforeThis, text)
		if(app.p[8].x>=110):
			app.p[8].changeX(-100)
			val=app.p[8].x
			
			for i in range(0,8):
				if (app.p[i].y == app.p[8].y) and (app.p[i].x == app.p[8].x):
					app.p[i].changeX(100)	
			self.afficherPoint()
					
	def haut(self,evt):
		if(app.p[8].y<=110):
			app.p[8].changeY(100)
			val=app.p[8].y
			
			for i in range(0,8):
				if (app.p[i].y == app.p[8].y) and (app.p[i].x == app.p[8].x):
					app.p[i].changeY(-100)	
			self.afficherPoint()
	
	def bas(self,evt):
		if(app.p[8].y>=110):
			app.p[8].changeY(-100)
			val=app.p[8].y
			
			for i in range(0,8):
				if (app.p[i].y == app.p[8].y) and (app.p[i].x == app.p[8].x):
					app.p[i].changeY(100)	
			self.afficherPoint()
		
	def gauche(self,evt):
		if(app.p[8].x<=110):
			app.p[8].changeX(100)
			val=app.p[8].x
			
			for i in range(0,8):
				if (app.p[i].y == app.p[8].y) and (app.p[i].x == app.p[8].x):
					app.p[i].changeX(-100)	
			self.afficherPoint()
						
class Piece:
	def __init__(self,canev,x,y,c,numero,color,bordure):
		#Dessine une pièce en x,y dans le canevas canev 
		#Mémorise les paramètres :
		self.canev=canev
		self.x=x
		self.y=y
		self.num=numero
		self.Rect=canev.create_rectangle(x,y,x+c,y+c,fill=color,width=bordure)
		self.Text=canev.create_text((x+c/2, y+c/2),text=numero,font=('Helvetica',36,'bold'),fill='#BF66D8')
			
				
	def changeX(self,pos):
		self.x+=pos
		self.canev.move(self.Rect,pos,0)
		self.canev.move(self.Text,pos,0)
		
	def changeY(self,pos):
			self.y+=pos
			self.canev.move(self.Rect,0,pos)
			self.canev.move(self.Text,0,pos)
		

	
app = Application()
app.bind("<Up>",app.haut)
app.bind("<Down>",app.bas)
app.bind("<Right>",app.droit)
app.bind("<Left>",app.gauche)
app.mainloop()
