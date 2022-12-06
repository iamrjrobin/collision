from superwires import games
import pygame

games.init(screen_width = 512, screen_height = 512, fps = 60)
wall_image = games.load_image("road.jpg", transparent = False)
games.screen.background = wall_image
car_incoming = games.load_image("car_in.jpg")
car_outgoing = games.load_image("car_out.png")


class my_car(games.Sprite):
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()

    def check_collide(self):
        for incoming_car in self.overlapping_sprites:
            exit()


# resize sprite
car_incoming = pygame.transform.scale(car_incoming, (150, 150))
# car_incoming_sprite = games.Sprite(image = car_incoming, x = 50, y = 100)


car_outgoing = pygame.transform.scale(car_outgoing, (75, 150))
car_outgoing_sprite = games.Sprite(image = car_outgoing, x = 200, y = 400)

# add random movement to car_incoming_sprite
incoming_car_obj = games.Sprite(image=car_incoming,
             x=games.screen.width/2.6,
             y=games.screen.height/100,
             dx=0,
             dy=1)

my_car_obj = my_car(car_outgoing)
my_car_obj.check_collide

games.screen.add(incoming_car_obj)
games.screen.add(my_car_obj)
# check for collision
games.screen.mainloop()
