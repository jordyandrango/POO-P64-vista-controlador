# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:20:29 2024

@author: User
"""

class RobotModel:
    def __init__(self):
        
        self.elevation = 0
        self.rotation = 0
        self.length = 0
        self.is_moving = False
    
    def move_elevation(self, elevation):
        
        self.elevation = elevation
    
    def move_rotation(self, rotation):
        
        self.rotation = rotation
    
    def move_length(self, length):
        
        self.length = length
    
    def stop_movement(self):
        
        self.is_moving = False 
        
        
class RobotView:
    def show_message(self, message):
        
        print(message)
    
    def get_user_input(self, prompt):
        
        return input(prompt)         
        
from robot_model import RobotModel
from robot_view import RobotView

class RobotController:
    def __init__(self):
        self.model = RobotModel()
        self.view = RobotView()
    
    def run(self):
        while True:
            
            self.view.show_message("1. Mover elevación")
            self.view.show_message("2. Mover giro")
            self.view.show_message("3. Mover longitud")
            self.view.show_message("4. Detener movimiento")
            self.view.show_message("5. Salir")
            
           
            choice = self.view.get_user_input("Seleccione una opción: ")
            
            if choice == "1":
                elevation = float(self.view.get_user_input("Ingrese el valor de elevación: "))
                self.model.move_elevation(elevation)
            elif choice == "2":
                rotation = float(self.view.get_user_input("Ingrese el valor de giro: "))
                self.model.move_rotation(rotation)
            elif choice == "3":
                length = float(self.view.get_user_input("Ingrese el valor de longitud: "))
                self.model.move_length(length)
            elif choice == "4":
                self.model.stop_movement()
            elif choice == "5":
                break
            else:
                self.view.show_message("Opción no válida. Por favor, seleccione una opción válida.")

def main():
    controller = RobotController()
    controller.run()

if __name__ == "__main__":
    main()

from robot_controller import RobotController

def main():
    controller = RobotController()
    controller.run()

if __name__ == "__main__":
    main()        