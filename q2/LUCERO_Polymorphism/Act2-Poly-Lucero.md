 1. Answer the following questions. 
 (a) What is duck typing, as explained in the video?
     --Duck typing is a concept where an object's suitability 
       is determined by the presence of certain methods and properties, 
       rather than its actual inheritance or type 
       ("If it walks like a duck and quacks like a duck, it's a duck").   
 (b) What did the Car class need to have so it could work inside the same loop 
 as Dog and Cat, even if it does not inherit from the Animal class?
 
      --It needed to have a move() method with the same name so Python 
        could invoke it dynamically. 

2.
                      class Car:
                          def move(self):
                              print("The car drives on the road.")
                        
                        class Boat:
                            def move(self):
                                print("The boat sails on water.")
                        
                        class Drone:
                            def move(self):
                                print("The drone flies in the sky.")
                        
                        def start_trip(vehicle):
                            vehicle.move()
                        
                        vehicles = [Car(), Boat(), Drone()]
                        
                        for v in vehicles:
                            start_trip(v)


 3. How does the code demonstrate polymorphism?
       --It allows different, unrelated classes (Car, Boat, Drone) 
         to be accessed using the exact same function call (start_trip()) 
         or method name (move()), letting Python automatically execute the 
         correct behavior at runtime based on the object.
