import pygame
import random
from functools import partial
import os

class App:
	def __init__(self):
		pygame.font.init()
		self.alto = 506
		self.ancho = 506
		self.titulo = "Juego del 15"
		self.fondo = (181,115,66)
		self.color_marco = (59, 31, 0)
		self.fuente = pygame.font.SysFont('Arial', 30)
		self.color_fuente = pygame.Color('white')
		self.fichas = []
		self.num_pos_array = []

	def identificar(self, ficha):
		print(ficha.rect)

	def completado(self):
		print("GANASTE")

	def moverFicha(self, direccion, ficha_rect):
		os.system("cls")
		self.identificar(ficha_rect)
		if direccion == "DERECHA":
			ficha_rect.rect.left += 120
			print("ACTUAL: " + str(self.num_pos_array[self.indice]))
			print("ATRÁS: " +str(self.num_pos_array[self.indice-1]))
			print("ADELANTE: " + str(self.num_pos_array[self.indice+1]))
			self.num_pos_array[self.indice], self.num_pos_array[self.indice+1] = self.num_pos_array[self.indice+1], self.num_pos_array[self.indice]
			print("ACTUAL2: " + str(self.num_pos_array[self.indice]))
			print("ATRÁS2: " +str(self.num_pos_array[self.indice-1]))
			print("ADELANTE2: " + str(self.num_pos_array[self.indice+1]))
			
		elif direccion == "IZQUIERDA":
			print("ACTUAL: " + str(self.num_pos_array[self.indice]))
			print("ATRÁS: " +str(self.num_pos_array[self.indice-1]))
			print("ADELANTE: " + str(self.num_pos_array[self.indice+1]))
			ficha_rect.rect.left -= 120
			self.num_pos_array[self.indice-1], self.num_pos_array[self.indice] = self.num_pos_array[self.indice], self.num_pos_array[self.indice-1]
			print("ACTUAL2: " + str(self.num_pos_array[self.indice]))
			print("ATRÁS2: " +str(self.num_pos_array[self.indice-1]))
			print("ADELANTE2: " + str(self.num_pos_array[self.indice+1]))

		elif direccion == "ARRIBA":
			print("ACTUAL: " + str(self.num_pos_array[self.indice]))
			print("ATRÁS: " +str(self.num_pos_array[self.indice-1]))
			print("ADELANTE: " + str(self.num_pos_array[self.indice+1]))
			ficha_rect.rect.top -= 120
			self.num_pos_array[self.indice], self.num_pos_array[self.indice-4] = self.num_pos_array[self.indice-4], self.num_pos_array[self.indice]
			print("ACTUAL2: " + str(self.num_pos_array[self.indice]))
			print("ATRÁS2: " +str(self.num_pos_array[self.indice-1]))
			print("ADELANTE2: " + str(self.num_pos_array[self.indice+1]))

		elif direccion == "ABAJO":
			print("ACTUAL: " + str(self.num_pos_array[self.indice]))
			print("ATRÁS: " +str(self.num_pos_array[self.indice-1]))
			print("ADELANTE: " + str(self.num_pos_array[self.indice+1]))
			ficha_rect.rect.top += 120
			try:
				self.num_pos_array[self.indice], self.num_pos_array[self.indice+4] = self.num_pos_array[self.indice+4], self.num_pos_array[self.indice]
				print("ACTUAL2: " + str(self.num_pos_array[self.indice]))
				print("ATRÁS2: " +str(self.num_pos_array[self.indice-1]))
				print("ADELANTE2: " + str(self.num_pos_array[self.indice+1]))
			except IndexError:
				print("Fuera de rango: ficha inmovible")

		if self.num_pos_array[0] == 1:#, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, '':
			self.completado()
		print(self.num_pos_array)
		print("Indice ficha: " + str(self.indice))

	def movimientos(self, ficha):
		# PROBAR POR AQUÍ POR ALLÁ, EN TODAS CON UN elif MOVIENDO LA FICHA Y QUE SE QUEDE EN DONDE NO CHOQUE
		mover_derecha = True
		mover_izquierda = False
		mover_abajo = False
		mover_arriba = False
		conteo = len(self.fichas)-1
		numchoques = 0

		# DERECHA #
		if mover_derecha:
			conteoD = conteo
			numchoquesD = numchoques
			self.moverFicha(direccion="DERECHA", ficha_rect=ficha)
			#self.num_pos_array[indice], self.num_pos_array[indice+1] = self.num_pos_array[indice+1], self.num_pos_array[indice]

			print("Posicion X: " + str(ficha.rect.left))
			if ficha.rect.left < 495:
				# PARA QUE LAS ORILLERAS DE LA IZQUIERDA NO SE SALGAN DEL CUADRO #
				print("DERECHA")
				if ficha.rect.left <= 15:
					print("fuera izquierda")
					self.moverFicha(direccion="DERECHA", ficha_rect=ficha)

				# Más de 2 choques, es que choca con otro #
				# Ese único choque es el de esa ficha con esa misma ficha #	
				while conteoD > -1:
					if pygame.sprite.collide_rect(ficha, self.fichas[conteoD]):
						numchoquesD += 1
					conteoD -= 1
					#print("choques: " + str(numchoquesD))
				if numchoquesD >= 2:
					self.moverFicha(direccion="IZQUIERDA", ficha_rect=ficha) # Regresa #
					#self.num_pos_array[indice], self.num_pos_array[indice+1] = self.num_pos_array[indice-1], self.num_pos_array[indice-1]
					mover_izquierda = True # Se habilita moverse hacia la izquierda #

			else:
				self.moverFicha(direccion="IZQUIERDA", ficha_rect=ficha) # Regresa #
				#self.num_pos_array[indice], self.num_pos_array[indice+1] = self.num_pos_array[indice-1], self.num_pos_array[indice-1]
				mover_izquierda = True

		# INTENTO A LA IZQUIERDA #
		if mover_izquierda:
			mover_derecha = False
			conteoI = conteo
			numchoquesI = numchoques
			print("\nIZQUIERDA")
			print("Posicion X IZ: " + str(ficha.rect.left))
			self.moverFicha(direccion="IZQUIERDA", ficha_rect=ficha)
			#self.num_pos_array[indice], self.num_pos_array[indice-1] = self.num_pos_array[indice-1], self.num_pos_array[indice]
			if ficha.rect.left < 15:
				self.moverFicha(direccion="DERECHA", ficha_rect=ficha) # Regresa #
				mover_abajo = True

			# Más de 2 choques, es que choca con otro #
			# Ese único choque es el de esa ficha con esa misma ficha #	
			while conteoI > -1:
				if pygame.sprite.collide_rect(ficha, self.fichas[conteoI]):
					numchoquesI += 1
				conteoI -= 1
				#print("choques: " + str(numchoquesI))
			if numchoquesI >= 2:
				self.moverFicha(direccion="DERECHA", ficha_rect=ficha) # Regresa #
				mover_abajo = True # Se habilita moverse hacia abajo # 


		# INTENTO HACIA ABAJO #
		if mover_abajo:
			mover_izquierda = False
			conteoA = conteo
			numchoquesA = numchoques
			print("\nABAJO")
			self.moverFicha(direccion="ABAJO", ficha_rect=ficha)
			print("Posicion Y: " + str(ficha.rect.top) + " | Posicion X: " + str(ficha.rect.left))
			if ficha.rect.top > 375:
				self.moverFicha(direccion="ARRIBA", ficha_rect=ficha) # Regresa #
				mover_arriba = True

			# Más de 2 choques, es que choca con otro #
			# Ese único choque es el de esa ficha con esa misma ficha #
			while conteoA > -1:
				if pygame.sprite.collide_rect(ficha, self.fichas[conteoA]):
					numchoquesA += 1
				conteoA -= 1
				#print("choques: " + str(numchoquesA))
			if numchoquesA >= 2:
				self.moverFicha(direccion="ARRIBA", ficha_rect=ficha) # Regresa #
				mover_arriba = True # Se habilita moverse hacia arriba #


		# INTENTO HACIA ARRIBA #
		if mover_arriba:
			mover_abajo = False
			conteoAR = conteo
			numchoquesAR = numchoques
			print("\nARRIBA")
			self.moverFicha(direccion="ARRIBA", ficha_rect=ficha)
			print("Posicion Y: " + str(ficha.rect.top) + " | Posicion X: " + str(ficha.rect.left))
			if ficha.rect.top < 15:
				print("Límite de altura")
				self.moverFicha(direccion="ABAJO", ficha_rect=ficha)

			# Más de 2 choques, es que choca con otro #
			# Ese único choque es el de esa ficha con esa misma ficha #
			while conteoAR > -1:
				if pygame.sprite.collide_rect(ficha, self.fichas[conteoAR]):
					numchoquesAR += 1
				conteoAR -= 1
				#print("choques: " + str(numchoquesAR))
			if numchoquesAR >= 2:
				self.moverFicha(direccion="ABAJO", ficha_rect=ficha) # Regresa #

	def interfaz(self):
		pygame.init()
		pantalla = pygame.display.set_mode([self.ancho, self.alto])
		pygame.display.set_caption(self.titulo)

		corriendo = True
		fps = pygame.time.Clock()

		# Imagenes y texto #
		fondo_img = pygame.transform.scale(pygame.image.load("img/fondo.jpg"), (506,506))
		madera = pygame.transform.scale(pygame.image.load("img/madera.jpg"), (117,117))

		# Recursos #
		cursor = pygame.Rect(0,0,1,1)
		marco = [pygame.Rect(3,3,496,10), pygame.Rect(3,10,10,486), pygame.Rect(494, 3, 10, 500), pygame.Rect(3, 494, 496, 10)]
		numeros = []
		numrandom = []

		while len(numrandom) < 15:
			x = random.randint(1,15)
			if x not in numrandom:
				numrandom.append(x)

		xpos = 15
		ypos = 15
		conteo = 0
		numero_ficha = 15

		for ficha in range(15):
			numero_ficha -= 1
			ficha = pygame.sprite.Sprite()
			ficha.image = madera
			ficha.rect = madera.get_rect()
			if conteo == 4:
				ypos += 120 # 3 PIXELES DE ESPACIO ENTRE CADA FILA, EN REALIDAD SERÍA 117 LA CANTIDAD PEGADA ENTRE ELLOS
				xpos = 15
				conteo = 0
			ficha.rect.left = xpos
			ficha.rect.top = ypos
			xpos += 120

			conteo += 1
			txt = self.fuente.render(str(numrandom[numero_ficha]), 5, self.color_fuente)
			#print(numero_ficha)
			numeros.append(txt)
			self.fichas.append(ficha)

		self.num_pos_array = numrandom
		self.num_pos_array.append("espacio")
		
		#print(len(numrandom))
		#print(numrandom)

		while corriendo:
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					corriendo = False
					exit()
				if evento.type == pygame.MOUSEBUTTONDOWN:
					for x in self.fichas:
						if cursor.colliderect(x.rect):
							self.indice = self.fichas.index(x)
							#print(numrandom)
							#print("indice: " + str(indice))

							self.movimientos(x)

			fps.tick(60)
			pantalla.fill(self.fondo)
			pantalla.blit(fondo_img, [0,0])
			numrandom_pos = 14

			# Creando las fichas #
			for i in marco:
				pygame.draw.rect(pantalla, self.color_marco, i)

			for i in self.fichas:
				pantalla.blit(i.image, i.rect)
				# Poner los números #
				pantalla.blit(numeros[numrandom_pos], [i.rect.left+45,i.rect.top+30])
				numrandom_pos -= 1
				#pantalla.blit(numeros[num_pos-1], [i.rect.left+45,i.rect.top+30])
							
			pygame.draw.rect(pantalla, (0,0,0), cursor)
			(cursor.left, cursor.top) = pygame.mouse.get_pos()
			pygame.display.update()

		pygame.quit()

if __name__ == "__main__":
	App().interfaz()

