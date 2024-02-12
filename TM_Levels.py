import pygame
import TM_Texts
import TM_Classes


# Level definitions
def level_list(player, door0, door1, door2, door3, door4, door5, door6, dungeon_screen, background, lava,
               block_1_level_1, block_2_level_1, block_3_level_1, block_4_level_1, block_5_level_1, block_6_level_1,
               block_7_level_1, block_8_level_1, block_9_level_1,
               block_1_level_2, block_2_level_2,
               block_1_level_3, block_2_level_3, block_3_level_3, block_4_level_3, block_5_level_3,
               block_1_level_4, block_2_level_4, block_3_level_4, block_4_level_4, block_5_level_4, block_6_level_4,
               block_7_level_4, block_8_level_4, block_9_level_4, block_10_level_4, block_11_level_4, block_12_level_4,
               block_13_level_4,
               enemy1, enemy2, bullet1, bullet2, enemy3, enemy4, bullet3, bullet4,
               coin1, coin2, coin3, coin4, coin5,
               min_portal):
    levels = [
        {"background": background, "sprites": [player], "doors": [door0], "texts": [0]},

        {"background": dungeon_screen, "sprites": [player], "doors": [door1],
         "blocks": [block_1_level_1, block_2_level_1, block_3_level_1, block_4_level_1, block_5_level_1,
                    block_6_level_1, block_7_level_1, block_8_level_1, block_9_level_1], "texts": [1],
         "coins": [coin1, coin2, coin3, coin4],
         "portal": [min_portal]},

        {"background": dungeon_screen, "sprites": [player], "doors": [door2],
         "blocks": [block_1_level_2, block_2_level_2],
         "lava": [lava], "texts": [2], "coins": [coin5]},

        {"background": dungeon_screen, "sprites": [player], "doors": [door3],
         "blocks": [block_1_level_3, block_2_level_3, block_3_level_3, block_4_level_3, block_5_level_3],
         "enemies": [enemy1, enemy2], "bullets": [bullet1, bullet2], "texts": [3]},

        {"background": dungeon_screen, "sprites": [player], "doors": [door4],
         "blocks": [block_1_level_4, block_2_level_4, block_3_level_4, block_4_level_4, block_5_level_4,
                    block_6_level_4, block_7_level_4, block_8_level_4, block_9_level_4, block_10_level_4,
                    block_11_level_4, block_12_level_4, block_13_level_4], "enemies": [enemy3, enemy4],
         "bullets": [bullet3, bullet4], "texts": [4]},

        {"background": dungeon_screen, "sprites": [player], "doors": [door5], "texts": [5]},

        {"background": background, "sprites": [player], "doors": [door6], "texts": [6]}
    ]

    return levels


def game_levels(screen, exit_sprite, blocks_sprite, enemy_group, bullet_group, lava_group, coin_group, portal_group,
                current_level, level_text, score_text, lives_text):
    # Common functionalities for each level
    screen.blit(current_level["background"], (0, 0))

    for sprite in current_level["sprites"]:
        sprite.appear(screen)

    if "doors" in current_level:
        exit_sprite.empty()
        for door in current_level["doors"]:
            exit_sprite.add(door)
            door.appear(screen)
    else:
        exit_sprite.empty()

    if "blocks" in current_level:
        blocks_sprite.empty()
        for block in current_level["blocks"]:
            blocks_sprite.add(block)
            block.appear(screen)
    else:
        blocks_sprite.empty()

    if "enemies" in current_level:
        enemy_group.empty()
        for enemy in current_level["enemies"]:
            enemy_group.add(enemy)
            enemy.appear(screen)
    else:
        enemy_group.empty()

    if "bullets" in current_level:
        bullet_group.empty()
        for bullet in current_level["bullets"]:
            bullet_group.add(bullet)
            bullet.animate()
            bullet.appear(screen)
    else:
        bullet_group.empty()

    if "lava" in current_level:
        lava_group.empty()
        for lava in current_level["lava"]:
            lava_group.add(lava)
            lava.appear(screen)
    else:
        lava_group.empty()

    if "coins" in current_level:
        coin_group.empty()
        for coin in current_level["coins"]:
            coin_group.add(coin)
            coin_group.draw(screen)

    for text_index in current_level["texts"]:
        TM_Texts.display_text(text_index)

    if "portal" in current_level:
        portal_group.empty()
        for portal in current_level["portal"]:
            portal_group.add(portal)
            portal.appear(screen)
    else:
        portal_group.empty()

    if 0 < current_level["texts"][0] < 7:
        screen.blit(level_text, (750, 20))
        screen.blit(score_text, (450, 20))
        screen.blit(lives_text, (150, 20))

    pygame.display.flip()
