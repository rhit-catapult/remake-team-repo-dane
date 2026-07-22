import pygame
import math
import sys
import random

# Initialize Pygame
pygame.init()

pygame.mixer.init()

sound = pygame.mixer.Sound()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TILE_SIZE = 64

# Color Palette
CEILING_COLOR = (7, 7, 10)
FLOOR_COLOR = (15, 15, 18)
WHITE = (255, 255, 255)
GRAY = (90, 95, 100)
LIGHT_GRAY = (160, 165, 170)
DARK_GRAY = (35, 35, 40)
RED = (230, 0, 0)
BRIGHT_RED = (255, 50, 50)
BLUE = (0, 120, 255)
BRIGHT_BLUE = (50, 180, 255)
BLACK = (0, 0, 0)
GOLD = (245, 190, 0)
CYAN = (0, 240, 255)
GREEN = (0, 210, 60)
SNOW_WHITE = (235, 240, 250)
DARK_BLUE_GRAY = (20, 25, 38)
NEON_RED = (255, 60, 60)

# Raycasting Configuration
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 2000
DELTA_ANGLE = FOV / NUM_RAYS
SCALE = SCREEN_WIDTH // NUM_RAYS

LEVELS = {
    1: [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    2: [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 2, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
}

for i in range(3, 11):
    LEVELS[i] = LEVELS[2 if i % 2 == 0 else 1]

MAP_2D = [
    [1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 1],
    [1, 4, 1, 0, 1, 0, 1, 4, 1, 0, 1, 0, 1, 4, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 4, 1, 1, 0, 1, 1, 4, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 4, 0, 0, 1, 0, 0, 4, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 4, 1, 0, 1, 4, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Smiler:
    def __init__(self, x, y, speed, type_id='WHITE'):
        self.x = x
        self.y = y
        self.speed = speed
        self.type = type_id
        self.screen_rect = pygame.Rect(-1000, -1000, 0, 0)
        self.is_alive = True
        self.respawn_timer = 0
        self.stare_timer = 0

    def update(self, player_x, player_y, game_map, game_instance):
        if not self.is_alive:
            self.respawn_timer -= 1
            if self.respawn_timer <= 0:
                new_spot = game_instance.get_random_open_tiles(1)[0]
                self.x = (new_spot[0] + 0.5) * TILE_SIZE
                self.y = (new_spot[1] + 0.5) * TILE_SIZE
                self.is_alive = True
                self.stare_timer = 0
            return

        angle = math.atan2(player_y - self.y, player_x - self.x)
        dx = self.speed * math.cos(angle)
        dy = self.speed * math.sin(angle)

        if game_map[int(self.y // TILE_SIZE)][int((self.x + dx) // TILE_SIZE)] not in (1, 4):
            self.x += dx
        if game_map[int((self.y + dy) // TILE_SIZE)][int(self.x // TILE_SIZE)] not in (1, 4):
            self.y += dy


class PM606Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PM 6:06 - Clean Atmospheric Build")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Courier New", 22, bold=True)
        self.shop_small_font = pygame.font.SysFont("Courier New", 14, bold=True)
        self.title_font = pygame.font.SysFont("Courier New", 64, bold=True)

        self.state = 'MENU'
        self.current_sublevel = 1
        self.game_over = False
        self.victory = False

        self.max_hearts = 5
        self.hearts = self.max_hearts

        # Virtual currency balance for shop architecture
        self.player_tokens = 250

        # 10 Unique Survival Store Items Data Structure
        self.shop_items = [
            {"name": "Thermal Coat", "cost": 50, "desc": "+1 Max Heart"},
            {"name": "Ice Cleats", "cost": 30, "desc": "+10% Move Speed"},
            {"name": "Flashlight", "cost": 25, "desc": "Improves Vision"},
            {"name": "Blue Banish", "cost": 40, "desc": "Longer Blue Stun"},
            {"name": "Red Sensor", "cost": 60, "desc": "Faster Red Burnout"},
            {"name": "Energy Drink", "cost": 15, "desc": "Sprint Burst Mod"},
            {"name": "Hand Warmers", "cost": 20, "desc": "Bypass Frostbite"},
            {"name": "Station Key", "cost": 100, "desc": "Unlock Shortcuts"},
            {"name": "Coin Magnet", "cost": 75, "desc": "Auto-Harvest Coins"},
            {"name": "Medkit", "cost": 35, "desc": "Restore All Hearts"}
        ]

        self.jumpscare_active = False
        self.jumpscare_timer = 0
        self.jumpscare_killer_type = 'WHITE'

        self.intro_distance = 0.0
        self.blizzard_particles = [
            [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), random.randint(2, 5)] for _ in
            range(150)]
        self.menu_snow_particles = [
            [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), random.randint(1, 3),
             random.uniform(1.0, 2.5)] for _ in range(80)]

        self.load_sublevel()

        self.p2d_tile_x = 7
        self.p2d_tile_y = 13
        self.move_cooldown = 0
        self.collected_coins = 0
        self.total_required_coins = 10
        self.harvested_positions = set()

    def get_random_open_tiles(self, count):
        open_tiles = []
        for r in range(self.map_rows):
            for c in range(self.map_cols):
                if self.map[r][c] == 0:
                    open_tiles.append((c, r))
        random.shuffle(open_tiles)
        return open_tiles[:count]

    def load_sublevel(self):
        if self.current_sublevel > 10:
            self.state = 'PLAYING_2D'
            return

        self.map = LEVELS[self.current_sublevel]
        self.map_cols = len(self.map[0])
        self.map_rows = len(self.map)

        spawn_spots = self.get_random_open_tiles(5)

        player_tile = spawn_spots[0]
        self.player_x = (player_tile[0] + 0.5) * TILE_SIZE
        self.player_y = (player_tile[1] + 0.5) * TILE_SIZE
        self.player_angle = random.uniform(0, math.pi * 2)
        self.player_speed = 3.5
        self.rotation_speed = 0.05

        self.smilers = []
        white_speed = 1.0 + (self.current_sublevel * 0.15)
        blue_speed = 0.8 + (self.current_sublevel * 0.10)
        red_speed = 1.2 + (self.current_sublevel * 0.12)

        white_tile = spawn_spots[1]
        self.smilers.append(
            Smiler((white_tile[0] + 0.5) * TILE_SIZE, (white_tile[1] + 0.5) * TILE_SIZE, white_speed, 'WHITE'))

        if self.current_sublevel >= 2:
            blue_tile = spawn_spots[2]
            self.smilers.append(
                Smiler((blue_tile[0] + 0.5) * TILE_SIZE, (blue_tile[1] + 0.5) * TILE_SIZE, blue_speed, 'BLUE'))

        red_tile = spawn_spots[3]
        self.smilers.append(Smiler((red_tile[0] + 0.5) * TILE_SIZE, (red_tile[1] + 0.5) * TILE_SIZE, red_speed, 'RED'))

        self.depth_buffer = [MAX_DEPTH] * NUM_RAYS
        self.jumpscare_active = False
        self.jumpscare_timer = 0

    def reset_entire_game(self):
        self.current_sublevel = 1
        self.hearts = self.max_hearts
        self.game_over = False
        self.victory = False
        self.intro_distance = 0.0
        self.p2d_tile_x = 7
        self.p2d_tile_y = 13
        self.collected_coins = 0
        self.harvested_positions.clear()
        self.load_sublevel()
        self.state = 'MENU'

    def draw_button(self, text, x, y, w, h, target_state=None, action=None, disabled=False):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if disabled:
            pygame.draw.rect(self.screen, DARK_GRAY, (x, y, w, h))
            txt_surface = self.font.render(text, True, GRAY)
            self.screen.blit(txt_surface, (x + (w // 2 - txt_surface.get_width() // 2),
                                           y + (h // 2 - txt_surface.get_height() // 2)))
            return False

        hover = x + w > mouse[0] > x and y + h > mouse[1] > y
        if hover:
            pygame.draw.rect(self.screen, LIGHT_GRAY, (x, y, w, h))
            if click[0] == 1:
                pygame.time.delay(150)
                if action == 'RESET':
                    self.reset_entire_game()
                elif target_state:
                    self.state = target_state
                elif action == 'QUIT':
                    pygame.quit()
                    sys.exit()
                return True
        else:
            pygame.draw.rect(self.screen, GRAY, (x, y, w, h))

        txt_surface = self.font.render(text, True, BLACK)
        self.screen.blit(txt_surface,
                         (x + (w // 2 - txt_surface.get_width() // 2), y + (h // 2 - txt_surface.get_height() // 2)))
        return False

    def display_menu(self):
        self.screen.fill(DARK_BLUE_GRAY)

        for p in self.menu_snow_particles:
            p[1] += p[3]
            p[0] += math.sin(p[1] * 0.02) * 0.4
            if p[1] > SCREEN_HEIGHT:
                p[1] = -10
                p[0] = random.randint(0, SCREEN_WIDTH)
            pygame.draw.circle(self.screen, (220, 230, 255), (int(p[0]), int(p[1])), p[2])

        title = self.title_font.render("PM 6:06", True, RED)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 80))

        self.draw_button("START", SCREEN_WIDTH // 2 - 125, 220, 250, 50, target_state='INTRO')
        self.draw_button("SHOP", SCREEN_WIDTH // 2 - 125, 290, 250, 50, target_state='SHOP')
        self.draw_button("INSTRUCTIONS", SCREEN_WIDTH // 2 - 125, 360, 250, 50, target_state='INSTRUCTIONS')
        self.draw_button("QUIT", SCREEN_WIDTH // 2 - 125, 430, 250, 50, action='QUIT')

    def display_shop(self):
        self.screen.fill(DARK_BLUE_GRAY)

        # Render decorative storefront title panel
        header = self.title_font.render("STATION STORE", True, CYAN)
        self.screen.blit(header, (SCREEN_WIDTH // 2 - header.get_width() // 2, 25))

        # Virtual Currency Display Tracker
        tokens_lbl = self.font.render(f"TOKENS AVAILABLE: {self.player_tokens} T", True, GOLD)
        self.screen.blit(tokens_lbl, (SCREEN_WIDTH // 2 - tokens_lbl.get_width() // 2, 95))

        # Grid parameters for laying out the 10 shop elements cleanly (5 Columns x 2 Rows)
        start_x = 40
        start_y = 145
        box_w = 132
        box_h = 160
        gap_x = 15
        gap_y = 25

        for index, item in enumerate(self.shop_items):
            col = index % 5
            row = index // 5
            bx = start_x + col * (box_w + gap_x)
            by = start_y + row * (box_h + gap_y)

            # Item Display Box frame
            pygame.draw.rect(self.screen, FLOOR_COLOR, (bx, by, box_w, box_h))
            pygame.draw.rect(self.screen, GRAY, (bx, by, box_w, box_h), 2)

            # Render labels using smaller specialized dynamic font limits
            name_txt = self.shop_small_font.render(item["name"], True, WHITE)
            cost_txt = self.shop_small_font.render(f"{item['cost']} Tokens", True, GOLD)
            desc_txt = self.shop_small_font.render(item["desc"], True, LIGHT_GRAY)

            self.screen.blit(name_txt, (bx + (box_w // 2 - name_txt.get_width() // 2), by + 12))
            self.screen.blit(cost_txt, (bx + (box_w // 2 - cost_txt.get_width() // 2), by + 36))
            self.screen.blit(desc_txt, (bx + (box_w // 2 - desc_txt.get_width() // 2), by + 65))

            # Individual Item Purchase Action Call Button Check
            btn_text = "BUY" if self.player_tokens >= item["cost"] else "LOCKED"
            disabled_status = self.player_tokens < item["cost"]

            # Adjust individual font layout inside draw button logic
            if self.draw_button(btn_text, bx + 12, by + 110, box_w - 24, 32, disabled=disabled_status):
                self.player_tokens -= item["cost"]

        # Back Button navigation routing logic
        self.draw_button("BACK TO MENU", SCREEN_WIDTH // 2 - 125, 515, 250, 48, target_state='MENU')

    def display_instructions(self):
        self.screen.fill(CEILING_COLOR)
        header = self.title_font.render("INSTRUCTIONS", True, WHITE)
        self.screen.blit(header, (SCREEN_WIDTH // 2 - header.get_width() // 2, 60))

        lines = [
            "Use WASD / ARROWS to navigate corridors.",
            "Locate glowing GOLD walls to escape 3D mode.",
            "CLICK ON BLUE SMILERS to temporarily banish them.",
            "STARE AT THE RED SMILER for 2 seconds to banish it.",
            "Survive the entities! You have 5 hearts before failure."
        ]

        y_offset = 180
        for line in lines:
            rendered_line = self.font.render(line, True, LIGHT_GRAY)
            self.screen.blit(rendered_line, (SCREEN_WIDTH // 2 - rendered_line.get_width() // 2, y_offset))
            y_offset += 45

        self.draw_button("BACK TO MENU", SCREEN_WIDTH // 2 - 125, 480, 250, 50, target_state='MENU')

    def update_intro_mode(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.intro_distance += 1.2

        for p in self.blizzard_particles:
            p[0] -= random.randint(3, 7)
            p[1] += random.randint(2, 5)
            if p[0] < 0: p[0] = SCREEN_WIDTH
            if p[1] > SCREEN_HEIGHT: p[1] = 0

        if self.intro_distance >= 350:
            self.state = 'PLAYING'

    def render_intro_view(self):
        self.screen.fill(DARK_BLUE_GRAY)
        pygame.draw.rect(self.screen, SNOW_WHITE, (0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2))

        for side in [-1, 1]:
            poly_points = [
                (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                (SCREEN_WIDTH // 2 + side * 150, SCREEN_HEIGHT // 2),
                (SCREEN_WIDTH // 2 + side * 500, SCREEN_HEIGHT),
                (SCREEN_WIDTH // 2, SCREEN_HEIGHT)
            ]
            pygame.draw.polygon(self.screen, (200, 215, 235), poly_points)
            pygame.draw.line(self.screen, (140, 160, 190), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                             (SCREEN_WIDTH // 2 + side * 500, SCREEN_HEIGHT), 3)

        progression_ratio = min(1.0, self.intro_distance / 350.0)
        entrance_w = int(60 + (progression_ratio * 400))
        entrance_h = int(40 + (progression_ratio * 250))
        ent_x = SCREEN_WIDTH // 2 - entrance_w // 2
        ent_y = (SCREEN_HEIGHT // 2 - entrance_h) + int(progression_ratio * 60)

        pygame.draw.rect(self.screen, (40, 42, 48), (ent_x - 20, ent_y - 20, entrance_w + 40, entrance_h + 20))
        pygame.draw.rect(self.screen, (80, 85, 95), (ent_x - 20, ent_y - 20, entrance_w + 40, entrance_h + 20), 4)
        pygame.draw.rect(self.screen, BLACK, (ent_x, ent_y, entrance_w, entrance_h))

        if entrance_w > 100:
            pillar_w = max(4, entrance_w // 14)
            pygame.draw.rect(self.screen, (60, 65, 75), (ent_x - 20 - pillar_w, ent_y - 20, pillar_w, entrance_h + 20))
            pygame.draw.rect(self.screen, (60, 65, 75),
                             (ent_x + entrance_w + 20, ent_y - 20, pillar_w, entrance_h + 20))

        stair_count = 6
        for step in range(stair_count):
            stair_y = ent_y + entrance_h - int((entrance_h / 3) * (step / stair_count))
            stair_w = entrance_w - (step * 8)
            pygame.draw.rect(self.screen, (24, 24, 26), (SCREEN_WIDTH // 2 - stair_w // 2, stair_y, stair_w, 5))

        for p in self.blizzard_particles:
            pygame.draw.circle(self.screen, WHITE, (p[0], p[1]), p[2])

        haze = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        haze.fill((235, 240, 250, int(75 * (1.0 - progression_ratio))))
        self.screen.blit(haze, (0, 0))

        txt = self.font.render("HOLD 'W' TO WALK THROUGH THE FREEZING BLIZZARD", True, WHITE)
        self.screen.blit(txt, (SCREEN_WIDTH // 2 - txt.get_width() // 2, 40))
        subway_lbl = self.font.render("SUBWAY TRANSIT STATION AHEAD", True, CYAN)
        self.screen.blit(subway_lbl, (SCREEN_WIDTH // 2 - subway_lbl.get_width() // 2, 85))

    def move_player(self):
        if self.jumpscare_active or self.game_over:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player_angle -= self.rotation_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player_angle += self.rotation_speed

        self.player_angle %= math.pi * 2

        cos_a = math.cos(self.player_angle)
        sin_a = math.sin(self.player_angle)
        dx, dy = 0, 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dx += self.player_speed * cos_a
            dy += self.player_speed * sin_a
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dx -= self.player_speed * cos_a
            dy -= self.player_speed * sin_a

        if self.map[int(self.player_y // TILE_SIZE)][int((self.player_x + dx) // TILE_SIZE)] != 1:
            self.player_x += dx
        if self.map[int((self.player_y + dy) // TILE_SIZE)][int(self.player_x // TILE_SIZE)] != 1:
            self.player_y += dy

    def handle_clicking(self):
        if self.jumpscare_active or self.game_over:
            return
        mouse_pos = pygame.mouse.get_pos()
        for s in self.smilers:
            if s.is_alive and s.type == 'BLUE':
                if s.screen_rect.collidepoint(mouse_pos):
                    s.is_alive = False
                    s.respawn_timer = 15 * FPS

    def update_game(self):
        if self.game_over:
            return

        if self.jumpscare_active:
            self.jumpscare_timer -= 1
            if self.jumpscare_timer <= 0:
                self.jumpscare_active = False
                if self.hearts <= 0:
                    self.game_over = True
            return

        self.move_player()

        center_x = SCREEN_WIDTH // 2

        for smiler in self.smilers:
            smiler.update(self.player_x, self.player_y, self.map, self)

            if not smiler.is_alive:
                continue

            if smiler.type == 'RED':
                if smiler.screen_rect.collidepoint((center_x, SCREEN_HEIGHT // 2)):
                    smiler.stare_timer += 1
                    if smiler.stare_timer >= 2 * FPS:
                        smiler.is_alive = False
                        smiler.respawn_timer = 30 * FPS
                else:
                    if smiler.stare_timer > 0:
                        smiler.stare_timer -= 1

            distance = math.hypot(self.player_x - smiler.x, self.player_y - smiler.y)
            if distance < 30:
                self.hearts -= 1
                self.jumpscare_active = True
                self.jumpscare_timer = 45
                self.jumpscare_killer_type = smiler.type

                relocation_spot = self.get_random_open_tiles(1)[0]
                smiler.x = (relocation_spot[0] + 0.5) * TILE_SIZE
                smiler.y = (relocation_spot[1] + 0.5) * TILE_SIZE
                return

        gx = int(self.player_x // TILE_SIZE)
        gy = int(self.player_y // TILE_SIZE)
        if self.map[gy][gx] == 2:
            self.current_sublevel += 1
            self.load_sublevel()

    def update_2d_mode(self):
        if self.move_cooldown > 0:
            self.move_cooldown -= 1
            return

        keys = pygame.key.get_pressed()
        next_x, next_y = self.p2d_tile_x, self.p2d_tile_y

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            next_y -= 1
            self.move_cooldown = 10
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            next_y += 1
            self.move_cooldown = 10
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            next_x -= 1
            self.move_cooldown = 10
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            next_x += 1
            self.move_cooldown = 10

        if 0 <= next_y < len(MAP_2D) and 0 <= next_x < len(MAP_2D[0]):
            if MAP_2D[next_y][next_x] not in (1, 4):
                if MAP_2D[next_y][next_x] == 3 and self.collected_coins < self.total_required_coins:
                    pass
                else:
                    self.p2d_tile_x = next_x
                    self.p2d_tile_y = next_y

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                check_x = self.p2d_tile_x + dx
                check_y = self.p2d_tile_y + dy
                if 0 <= check_y < len(MAP_2D) and 0 <= check_x < len(MAP_2D[0]):
                    if MAP_2D[check_y][check_x] == 4:
                        pos_key = (check_x, check_y)
                        if pos_key not in self.harvested_positions:
                            self.harvested_positions.add(pos_key)
                            self.collected_coins += 1

        if MAP_2D[self.p2d_tile_y][self.p2d_tile_x] == 3 and self.collected_coins >= self.total_required_coins:
            self.victory = True

    def draw_walls(self):
        start_angle = self.player_angle - HALF_FOV

        for ray in range(NUM_RAYS):
            cur_angle = start_angle + ray * DELTA_ANGLE
            cos_a = math.cos(cur_angle)
            sin_a = math.sin(cur_angle)

            for depth in range(1, MAX_DEPTH, 4):
                tx = self.player_x + depth * cos_a
                ty = self.player_y + depth * sin_a

                gx, gy = int(tx // TILE_SIZE), int(ty // TILE_SIZE)
                if gx < 0 or gx >= self.map_cols or gy < 0 or gy >= self.map_rows:
                    break

                if self.map[gy][gx] in (1, 2):
                    tile_type = self.map[gy][gx]

                    corrected_depth = depth * math.cos(self.player_angle - cur_angle)
                    self.depth_buffer[ray] = corrected_depth

                    wall_height = min(int((TILE_SIZE * SCREEN_HEIGHT) / (corrected_depth + 0.0001)), SCREEN_HEIGHT)
                    shade_factor = max(0.08, min(1.0, 1.0 - (corrected_depth / 750.0)))

                    top_y = (SCREEN_HEIGHT // 2) - (wall_height // 2)

                    if tile_type == 1:
                        x_offset = tx % TILE_SIZE
                        y_offset = ty % TILE_SIZE
                        texture_coordinate = x_offset if abs(x_offset - TILE_SIZE / 2) > abs(
                            y_offset - TILE_SIZE / 2) else y_offset

                        segment_height = max(1, wall_height // 8)
                        for segment in range(8):
                            seg_top = top_y + segment * segment_height
                            seg_height = segment_height
                            if segment == 7:
                                seg_height = ((SCREEN_HEIGHT // 2) + (wall_height // 2)) - seg_top

                            col_check = int((texture_coordinate / TILE_SIZE) * 6) % 6
                            is_border = (int(texture_coordinate) % 10 == 0) or (
                                        segment % 2 == 0 and int(texture_coordinate) % 20 == 0)

                            if is_border:
                                base_color = (25, 25, 28)
                            else:
                                val = 130 if (col_check + segment) % 2 == 0 else 80
                                base_color = (int(val * shade_factor), int(val * shade_factor),
                                              int(val * (shade_factor * 1.05)))

                            pygame.draw.rect(self.screen, base_color, (ray * SCALE, seg_top, SCALE, seg_height))
                    else:
                        x_offset = int(tx % TILE_SIZE)
                        is_gold_pattern = (x_offset % 16 < 3)

                        g_factor = shade_factor if not is_gold_pattern else shade_factor * 0.4
                        gold_color = (int(GOLD[0] * g_factor), int(GOLD[1] * g_factor), int(30 * g_factor))

                        pygame.draw.rect(self.screen, gold_color, (
                            ray * SCALE, top_y, SCALE, wall_height
                        ))
                    break

    def draw_smilers(self):
        if self.jumpscare_active:
            return

        sprites = []
        for s in self.smilers:
            if not s.is_alive:
                continue
            sx = s.x - self.player_x
            sy = s.y - self.player_y
            dist = math.hypot(sx, sy)
            sprites.append((dist, sx, sy, s))
        sprites.sort(key=lambda x: x[0], reverse=True)

        for dist, sx, sy, s in sprites:
            theta = math.atan2(sy, sx)
            gamma = theta - self.player_angle
            gamma = (gamma + math.pi) % (math.pi * 2) - math.pi

            if not (-HALF_FOV - 0.4 <= gamma <= HALF_FOV + 0.4):
                s.screen_rect = pygame.Rect(-1000, -1000, 0, 0)
                continue

            proj_dist = dist * math.cos(gamma)
            if proj_dist > 5:
                s_height = min(int((TILE_SIZE * SCREEN_HEIGHT) / proj_dist), SCREEN_HEIGHT)
                s_width = s_height // 2

                screen_x = int((SCREEN_WIDTH // 2) + math.tan(gamma) * (SCREEN_WIDTH // 2))
                screen_y = (SCREEN_HEIGHT // 2) - (s_height // 2)

                ray_index = int(screen_x // SCALE)

                if 0 <= ray_index < NUM_RAYS and proj_dist < self.depth_buffer[ray_index] + 45:
                    s.screen_rect = pygame.Rect(screen_x - s_width // 2, screen_y, s_width, s_height)

                    if s.type == 'BLUE':
                        core_color = BLUE
                        glow_color = BRIGHT_BLUE
                    elif s.type == 'RED':
                        core_color = RED
                        glow_color = BRIGHT_RED
                    else:
                        core_color = GRAY
                        glow_color = WHITE

                    pygame.draw.ellipse(self.screen, (5, 5, 5), s.screen_rect)
                    pygame.draw.ellipse(self.screen, core_color, s.screen_rect, max(1, s_width // 20))

                    eye_y = screen_y + s_height // 3
                    left_eye_x = screen_x - s_width // 4
                    right_eye_x = screen_x + s_width // 4
                    eye_rad = max(2, s_width // 8)

                    pygame.draw.circle(self.screen, glow_color, (left_eye_x, eye_y), eye_rad)
                    pygame.draw.circle(self.screen, glow_color, (right_eye_x, eye_y), eye_rad)
                    pygame.draw.circle(self.screen, WHITE, (left_eye_x, eye_y), max(1, eye_rad // 2))
                    pygame.draw.circle(self.screen, WHITE, (right_eye_x, eye_y), max(1, eye_rad // 2))

                    mouth_rect = pygame.Rect(screen_x - s_width // 3, screen_y + s_height // 2, (s_width * 2) // 3,
                                             s_height // 4)
                    pygame.draw.arc(self.screen, glow_color, mouth_rect, math.pi, 0, max(2, s_width // 10))

                    pygame.draw.line(self.screen, core_color, (s.screen_rect.left, s.screen_rect.bottom),
                                     (s.screen_rect.right, s.screen_rect.bottom), max(1, s_width // 16))

    def render_hud_hearts(self):
        start_x = SCREEN_WIDTH - 200
        y_pos = 20
        for i in range(self.max_hearts):
            heart_rect = pygame.Rect(start_x + (i * 35), y_pos, 25, 25)
            if i < self.hearts:
                pygame.draw.circle(self.screen, RED, (heart_rect.x + 7, heart_rect.y + 8), 7)
                pygame.draw.circle(self.screen, RED, (heart_rect.x + 18, heart_rect.y + 8), 7)
                pygame.draw.polygon(self.screen, RED, [
                    (heart_rect.x, heart_rect.y + 11),
                    (heart_rect.x + 25, heart_rect.y + 11),
                    (heart_rect.x + 12, heart_rect.y + 25)
                ])
            else:
                pygame.draw.rect(self.screen, (40, 40, 40), heart_rect, 2)

    def render_jumpscare(self):
        if self.jumpscare_killer_type == 'RED':
            self.screen.fill(BLACK)
            win_rect = pygame.Rect(SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 180, 500, 320)
            pygame.draw.rect(self.screen, (35, 10, 10), win_rect)
            pygame.draw.rect(self.screen, NEON_RED, win_rect, 4)

            pygame.draw.rect(self.screen, NEON_RED, (win_rect.x, win_rect.y, win_rect.width, 35))
            head_txt = self.font.render("SYSTEM EXCEPTION: UNHANDLED_SMILE", True, BLACK)
            self.screen.blit(head_txt, (win_rect.x + 15, win_rect.y + 6))

            face_center_y = win_rect.centery + 10
            pygame.draw.rect(self.screen, NEON_RED, (win_rect.centerx - 80, face_center_y - 40, 25, 25))
            pygame.draw.rect(self.screen, NEON_RED, (win_rect.centerx + 55, face_center_y - 40, 25, 25))

            pygame.draw.rect(self.screen, NEON_RED, (win_rect.centerx - 90, face_center_y + 30, 180, 12))
            pygame.draw.rect(self.screen, NEON_RED, (win_rect.centerx - 90, face_center_y + 10, 12, 20))
            pygame.draw.rect(self.screen, NEON_RED, (win_rect.centerx + 78, face_center_y + 10, 12, 20))

            warn_txt = self.font.render("RED ENGINE FILE CORRUPTED.", True, WHITE)
            self.screen.blit(warn_txt, (SCREEN_WIDTH // 2 - warn_txt.get_width() // 2, win_rect.bottom - 45))
            return

        if self.jumpscare_killer_type == 'BLUE':
            self.screen.fill((0, 0, 40))
            face_w, face_h = 600, 750
            face_rect = pygame.Rect(SCREEN_WIDTH // 2 - face_w // 2, SCREEN_HEIGHT // 2 - face_h // 2, face_w, face_h)
            pygame.draw.ellipse(self.screen, (5, 5, 15), face_rect)
            pygame.draw.ellipse(self.screen, BLUE, face_rect, 6)

            eye_y = face_rect.top + face_h // 3
            pygame.draw.circle(self.screen, BRIGHT_BLUE, (face_rect.centerx - face_w // 4, eye_y), face_w // 7)
            pygame.draw.circle(self.screen, BRIGHT_BLUE, (face_rect.centerx + face_w // 4, eye_y), face_w // 7)
            pygame.draw.circle(self.screen, WHITE, (face_rect.centerx - face_w // 4, eye_y), face_w // 16)
            pygame.draw.circle(self.screen, WHITE, (face_rect.centerx + face_w // 4, eye_y), face_w // 16)

            mouth_rect = (face_rect.centerx - face_w // 3, face_rect.top + face_h // 2, (face_w * 2) // 3, face_h // 3)
            pygame.draw.arc(self.screen, BRIGHT_BLUE, mouth_rect, math.pi, 0, 16)
            return

        if self.jumpscare_timer % 2 == 0:
            self.screen.fill((120, 120, 120))
        else:
            self.screen.fill(BLACK)

        shake_x = random.randint(-25, 25)
        shake_y = random.randint(-25, 25)
        face_w = int(450 + (50 - self.jumpscare_timer) * 4)
        face_h = int(600 + (50 - self.jumpscare_timer) * 4)

        face_rect = pygame.Rect((SCREEN_WIDTH // 2 - face_w // 2) + shake_x,
                                (SCREEN_HEIGHT // 2 - face_h // 2) + shake_y, face_w, face_h)
        pygame.draw.ellipse(self.screen, (10, 10, 10), face_rect)
        pygame.draw.ellipse(self.screen, WHITE, face_rect, 8)

        eye_radius = max(8, face_w // 8)
        eye_y = face_rect.top + face_h // 3
        pygame.draw.circle(self.screen, LIGHT_GRAY, (face_rect.centerx - face_w // 4, eye_y), eye_radius)
        pygame.draw.circle(self.screen, LIGHT_GRAY, (face_rect.centerx + face_w // 4, eye_y), eye_radius)

        mouth_rect = (face_rect.centerx - face_w // 3, face_rect.top + face_h // 2, (face_w * 2) // 3, face_h // 3)
        pygame.draw.arc(self.screen, LIGHT_GRAY, mouth_rect, math.pi, 0, max(8, face_w // 12))

    def render_2d_view(self):
        self.screen.fill(BLACK)
        grid_scale = 32
        offset_x = (SCREEN_WIDTH - (len(MAP_2D[0]) * grid_scale)) // 2
        offset_y = (SCREEN_HEIGHT - (len(MAP_2D) * grid_scale)) // 2

        for r in range(len(MAP_2D)):
            for c in range(len(MAP_2D[0])):
                rect = pygame.Rect(offset_x + c * grid_scale, offset_y + r * grid_scale, grid_scale, grid_scale)
                if MAP_2D[r][c] == 1:
                    pygame.draw.rect(self.screen, GRAY, rect)
                elif MAP_2D[r][c] == 4:
                    pygame.draw.rect(self.screen, DARK_GRAY, rect)
                    if (c, r) not in self.harvested_positions:
                        pygame.draw.circle(self.screen, GOLD, (rect.centerx, rect.centery), 6)
                elif MAP_2D[r][c] == 3:
                    color = GREEN if self.collected_coins >= self.total_required_coins else RED
                    pygame.draw.rect(self.screen, color, rect)
                else:
                    pygame.draw.rect(self.screen, FLOOR_COLOR, rect, 1)

        p_rect = pygame.Rect(offset_x + self.p2d_tile_x * grid_scale + 4, offset_y + self.p2d_tile_y * grid_scale + 4,
                             grid_scale - 8, grid_scale - 8)
        pygame.draw.rect(self.screen, CYAN, p_rect)

        lbl = self.font.render("SUBLEVEL 11: ALTERNATE CORE", True, CYAN)
        self.screen.blit(lbl, (20, 20))
        coin_lbl = self.font.render(f"COINS EXTRACTED FROM WALLS: {self.collected_coins} / {self.total_required_coins}",
                                    True, GOLD)
        self.screen.blit(coin_lbl, (20, 50))

        if self.collected_coins < self.total_required_coins:
            status_lbl = self.font.render("EXIT GATE LOCKED: EXTRACT REMAINING COINS FROM THE WALL CORNERS", True, RED)
            self.screen.blit(status_lbl, (20, SCREEN_HEIGHT - 40))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.state == 'PLAYING':
                        if self.game_over:
                            mouse = pygame.mouse.get_pos()
                            rx, ry, rw, rh = SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 50
                            if rx + rw > mouse[0] > rx and ry + rh > mouse[1] > ry:
                                self.reset_entire_game()
                        elif not self.jumpscare_active and not self.victory:
                            self.handle_clicking()

            if self.state == 'MENU':
                self.display_menu()
            elif self.state == 'SHOP':
                self.display_shop()
            elif self.state == 'INSTRUCTIONS':
                self.display_instructions()
            elif self.state == 'INTRO':
                self.update_intro_mode()
                self.render_intro_view()
            elif self.state == 'PLAYING':
                self.update_game()

                if self.jumpscare_active:
                    self.render_jumpscare()
                else:
                    self.screen.fill(CEILING_COLOR)
                    pygame.draw.rect(self.screen, FLOOR_COLOR,
                                     (0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2))

                    self.draw_walls()
                    self.draw_smilers()

                    # Stylized Crosshair
                    pygame.draw.circle(self.screen, CYAN, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 6, 1)
                    pygame.draw.line(self.screen, CYAN, (SCREEN_WIDTH // 2 - 2, SCREEN_HEIGHT // 2),
                                     (SCREEN_WIDTH // 2 + 2, SCREEN_HEIGHT // 2), 1)
                    pygame.draw.line(self.screen, CYAN, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 2),
                                     (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 2), 1)

                    self.render_hud_hearts()

                    if self.game_over:
                        go_txt = self.font.render("YOU FAILED TO ESCAPE THE SMILE.", True, RED)
                        self.screen.blit(go_txt, (SCREEN_WIDTH // 2 - go_txt.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
                        self.draw_button("RESET", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 50,
                                         action='RESET')
                    else:
                        lbl = self.font.render(f"SUBLEVEL: {self.current_sublevel}", True, WHITE)
                        self.screen.blit(lbl, (20, 20))

                        for s in self.smilers:
                            if s.type == 'RED':
                                if s.is_alive and s.stare_timer > 0:
                                    pct = int((s.stare_timer / (2 * FPS)) * 100)
                                    meter = self.font.render(f"RED SMILE BURNOUT ANALYSIS: {pct}%", True, RED)
                                    self.screen.blit(meter, (20, 55))
                                elif not s.is_alive:
                                    rem = max(0, int(s.respawn_timer // FPS))
                                    meter = self.font.render(f"RED SMILE RE-MATERIALIZING IN: {rem}s", True, GRAY)
                                    self.screen.blit(meter, (20, 55))

            elif self.state == 'PLAYING_2D':
                if not self.victory:
                    self.update_2d_mode()
                self.render_2d_view()

                if self.victory:
                    vic_txt = self.font.render("CORE ARCHIVE PURGED. YOU WIN!", True, GOLD)
                    self.screen.blit(vic_txt, (SCREEN_WIDTH // 2 - vic_txt.get_width() // 2, SCREEN_HEIGHT // 2 - 180))
                    self.draw_button("MAIN MENU", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 100, 200, 50,
                                     action='RESET')

            pygame.display.flip()
            self.clock.tick(FPS)




if __name__ == "__main__":
    game = PM606Game()
    game.run()