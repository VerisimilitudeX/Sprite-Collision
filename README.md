# Sprite-Collision
  # Define: Collision
  * Collision is when two objects overlap on the screen
  * If two objects share any of the same pixels, they are colliding
  # How to tell if two sprites collide
  * Sprite collision works by comparing the rectangles around two sprites
  * Rect: the rectangle that contains all the pixels of a sprite
  * The rect bounds the whole image file of a Sprite, including any blank space
  * The rects of two sprites can overlap even if the sprite's pixels don't appear to touch
  * pygame.sprite.collide_rect(s1, s2) returns whether two sprites are colliding * s1 and s2 are two Sprite objects
  * This returns true every frame that two sprites are overlapping
  # How to tell if a point collides with a sprite
  * Point collision tells whether a point is within a Sprite's rect
  * sprite.rect.collidepoint(x, y) returns whether the point and sprite collide * sprite is a Sprite object * x and y are the coordinates of the point
  * Point collision is commonly used with the mouse position
  # Why is collision so useful?
  * All onscreen buttons work via collision * Any website where you click something uses point collision to checked what you clicked * Any app that uses touch input uses point collision to see what you tapped
  * Many games rely on sprite collision
  * Example: Super Mario * Sprite collision lets Mario land on the floor * Mario gets hurt when he collides with an enemy * The player wins the level when Mario collides with the flagpole
