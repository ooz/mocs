# Lego Designs

My own Lego creations ("MOCs") with background information and instructions.

## Spaceships

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
[![Good Industries Personal Pod](thumbnails/personal_pod.png)](spaceships/personal-pod/)

* Triple Enforcer BT
* The Shiv

## Other Vehicles

[![Hover Scooter](thumbnails/hover_scooter.png)](vehicles/hover-scooter/)

## Structures

* Biwak Pod

## 60th Anniversary Models

[![Modular Rockets](thumbnails/modular_rockets.png)](60th-anniversary/modular-rockets/)
[![Crafty Miniboat](thumbnails/crafty_miniboat.png)](60th-anniversary/crafty-miniboat/)
[![Cloud Raider](thumbnails/cloud_raider.png)](60th-anniversary/cloud-raider/)
[![Pirate Ship](thumbnails/pirate_ship.png)](60th-anniversary/pirate-ship/)
[![El Presidente](thumbnails/el_pres.png)](60th-anniversary/el-presidente/)
[![Orange Mech](thumbnails/orange_mech.jpg)](60th-anniversary/orange-mech/)
[![Cannon Boat](thumbnails/cannon_boat.jpg)](60th-anniversary/cannon-boat/)

## Alternative Builds and Modifications

[![Minecraft Ivory Ship](thumbnails/ivory_ship.jpg)](alts-mods/minecraft-ivory-ship/)
[![Minecart Deluxe](thumbnails/minecart_deluxe.jpg)](alts-mods/minecart-deluxe/)
[![Lava Sails](thumbnails/lava_sails.jpg)](alts-mods/lava-sails/)
[![Dragon Rider](thumbnails/dragon_rider.png)](alts-mods/dragon-rider/)
[![Extended Satellite Service Mission](thumbnails/essm.jpg)](alts-mods/extended-ssm/)
[![Space Van](thumbnails/space_van.jpg)](alts-mods/space-van/)

## Legacy

Models built only from old bricks:

* [Propeller Pirate Bike](legacy/pirate-bike/)
* [Cloud Gunner](legacy/cloud-gunner/)
* [Space Capsule](legacy/space-capsule/)

<!-- * [Junk Propeller Plane](legacy/junk-propeller/) -->

## Philosophy

*Fictive abstraction over realism*

* Playable, functional, robust and can be moved conveniently
* All designs are open for modification
* Greeble is an afterthought and does not compromise the above in favor of more visual appeal or detail
* Models for children, lore for adults

Design approach:

* Focus on core idea or moving, functional parts first (e.g. cockpit, hatches, engine, trapdoors)!
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

* Thumbnails are in 4:3 format, 256x192 px

Rendering settings:

* 1024x768 size, "High" quality
* "Transparent" background, "Floor shadow" enabled
* Light: "Asteroid" (spaceships), "Dawn" (ship, atmospheric vehicles)
* Material effects:
    * "UV Degradation" on, Min. `0.15`, Max. `0.5`
    * other effects off
