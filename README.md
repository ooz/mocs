# Lego Creations

My own Lego creations ("MOCs") with instructions and background information.

## Index

### Spaceships

[![The Mosquito](thumbnails/mosquito_front.png)](spaceships/the-mosquito/)
[![The Wedge](thumbnails/the_wedge_front.png)](spaceships/the-wedge/)
[![Good Industries Universal Pod](thumbnails/universal_pod.png)](spaceships/universal-pod/)
[![The Needle](thumbnails/the_needle.png)](spaceships/the-needle/)
[![The Square Falcon](thumbnails/the_square_falcon.png)](spaceships/the-square-falcon/)
[![Good Industries Saucer](thumbnails/saucer.png)](spaceships/saucer/)
[![The Dagger](thumbnails/the_dagger.png)](spaceships/the-dagger/)
[![The Swallow](thumbnails/the-swallow.png)](spaceships/the-swallow/)
[![Good Industries Commuter](thumbnails/commuter.png)](spaceships/commuter/)
[![Combat Needle](thumbnails/combat_needle.png)](spaceships/combat-needle/)

### Other Vehicles

[![Hover Scooter](thumbnails/hover_scooter.png)](vehicles/hover-scooter/)

### 60th Anniversary Models

[![Modular Rockets](thumbnails/modular_rockets.png)](60th-anniversary/modular-rockets/)
[![Crafty Miniboat](thumbnails/crafty_miniboat.png)](60th-anniversary/crafty-miniboat/)
[![Cloud Raider](thumbnails/cloud_raider.png)](60th-anniversary/cloud-raider/)
[![Pirate Ship](thumbnails/pirate_ship.png)](60th-anniversary/pirate-ship/)

### Alternative Builds and Modifications

* [Minecraft Ivory Ship](alts-mods/minecraft-ivory-ship/)
* [Minecart Deluxe](alts-mods/minecart-deluxe/)

### Backlog

TODO list of designs I still want to digitalize:

* Personal Pod
* Space Van
* Lava Sails (alt build)
* Satellite maintenance mission (mod build, just photos)

## Philosophy

* I prefer models that are playable, functional, sturdy and at a scale that can conveniently be moved.
* I only use legal connections.
* I prefer minifigure scale.
* My designs should be open for modification.
* I treat greeble as an afterthought and do not compromise on the above in favor of more visual appeal or realism.

Design approach:

* Focus on core idea or moving, functional parts first (e.g. cockpit, hatches, engine)!
* Flesh out raw form!
* Improve sturdiness!
* Iterate!

## Tools

All models are digitalized using [BrickLink Studio](https://studio.bricklink.com/v2/build/studio.page).

**Make sure to save regularly, since the software sometimes crashes under wine when making instructions!**

Resize model photos:

```
mogrify -resize 1600 *.jpg
```

Resize thumbnails:

```
mogrify -resize 256 *.png
```

Rendering settings:

* 1024x768 size, "High" quality
* "Transparent" background, "Floor shadow" enabled
* Light: "Asteroid" (spaceships), "Dawn" (ship, atmospheric vehicles)
* Material effects:
    * "UV Degradation" on, Min. `0.15`, Max. `0.5`
    * other effects off
