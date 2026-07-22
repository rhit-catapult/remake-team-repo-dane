import pygame
import math
import random
import sys
import array

# ==================== 1. 全局配置 ====================
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
TILE_SIZE = 40
FPS = 60
MAP_COLS = 60
MAP_ROWS = 45
TOTAL_KEYS = 8
ESCAPE_COIN_THRESHOLD = 12  # ★ 新增：金币逃离阈值

# --- 调色板 ---
C_BG = (6, 6, 10)
C_WALL_FACE = (52, 52, 62)
C_WALL_TOP = (95, 95, 110)
C_WALL_SIDE = (28, 28, 35)
C_WALL_SHADOW = (10, 10, 15, 140)
C_WALL_MORTAR = (35, 35, 42)
C_WALL_BRICK_LIGHT = (68, 68, 82)
C_WALL_BRICK_DARK = (42, 42, 52)
C_FLOOR_HALL = (175, 170, 160)
C_FLOOR_BED = (155, 165, 185)
C_FLOOR_KITCHEN = (185, 190, 195)
C_FLOOR_BATH = (165, 195, 205)
C_FLOOR_OUTDOOR = (195, 205, 215)
C_MONSTER_BODY = (135, 28, 28)
C_MONSTER_HEAD = (175, 38, 38)
C_MONSTER_EYE = (255, 215, 45)
C_DOOR_LOCKED = (75, 75, 85)
C_DOOR_OPEN = (35, 175, 55)
C_SNOW = (255, 255, 255)
C_FURNITURE = (95, 65, 35)
C_FURNITURE_TOP = (125, 90, 50)
C_FURNITURE_SEARCHED = (75, 55, 30)
C_P_COAT = (65, 85, 135)
C_P_COAT_SHADOW = (45, 60, 100)
C_P_HOOD = (55, 75, 125)
C_P_GOGGLE = (175, 215, 250)
C_P_GOGGLE_FRAME = (35, 35, 45)
C_P_BACKPACK = (115, 75, 35)
C_P_GLOVE = (55, 45, 35)
C_P_BOOT = (45, 35, 30)
C_P_SKIN = (225, 195, 165)
C_GATE_CLOSED = (155, 35, 35)
C_GATE_OPEN = (35, 135, 55)
C_SWITCH_OFF = (175, 115, 35)
C_SWITCH_ON = (55, 195, 75)
C_SWITCH_BASE = (55, 55, 65)
C_FLASH_CD_READY = (75, 195, 75)
C_FLASH_CD_COOLDOWN = (175, 55, 55)
C_MENU_BG = (10, 10, 15)
C_MENU_TITLE = (195, 215, 250)
C_MENU_ITEM = (155, 155, 165)
C_MENU_SELECTED = (250, 215, 95)
C_MENU_BORDER = (55, 55, 75)
C_TEXT_BODY = (185, 185, 195)
C_TEXT_HIGHLIGHT = (95, 215, 145)
C_TEXT_KEY = (250, 210, 0)
C_MINIMAP_BG = (0, 0, 0, 190)
C_MINIMAP_PLAYER = (95, 250, 95)
C_MINIMAP_ENEMY = (250, 55, 55)
C_MINIMAP_WALL = (75, 75, 95)
C_MINIMAP_GATE = (195, 55, 55)
C_GUN_METAL = (85, 85, 95)
C_GUN_BARREL = (55, 55, 65)
C_GUN_GRIP = (95, 55, 25)
C_AMMO_COLOR = (215, 175, 55)
C_ITEM_GLOW = (250, 215, 95, 70)
C_ITEM_GUN = (175, 135, 55)
C_MUTANT_SKIN = (65, 22, 22)
C_MUTANT_SKIN_HL = (85, 35, 35)
C_MUTANT_VEIN = (250, 35, 15)
C_MUTANT_EYE = (255, 195, 45)
C_MUTANT_GLOW = (255, 55, 25, 70)
C_MUTANT_TRAIL = (175, 25, 15, 50)
C_MUTANT_HAIR = (35, 12, 12)
C_MUTANT_JOINT = (50, 18, 18)
C_MUTANT_CLAW = (200, 180, 140)
C_BLOOD_TRAIL = (115, 12, 8, 90)
C_BLOOD_SPLATTER = (155, 18, 12, 130)
C_NOTE_PAPER = (220, 210, 180)
C_NOTE_TEXT = (40, 30, 20)
C_COMPASS_NEEDLE = (250, 80, 60)
C_COMPASS_BG = (20, 20, 30, 180)
C_BLIZZARD_TINT = (180, 190, 210)
C_TRAIL_CORE = (255, 240, 150)
C_TRAIL_EDGE = (255, 180, 50)
C_COIN_GOLD = (255, 215, 0)
C_COIN_SHINE = (255, 245, 150)
C_ESCAPE_READY = (95, 250, 95)

# --- 核心游戏参数 ---
SCARE_CHANCE = 0.15
SCARE_DURATION = 40
SCARE_SHAKE_INTENSITY = 6
KILL_HITS_REQUIRED = 2
STUN_DURATION_FRAMES = 180
FLASH_COOLDOWN_FRAMES = 600
FLASH_RANGE = 250
FLASH_VISUAL_DURATION = 12
GUN_MAG_SIZE = 3
GUN_FIRE_CD = 480
GUN_RANGE = 600
GUN_ALERT_DURATION = 480
GUN_ALERT_SPEED_MULT = 1.5
GUN_STATIONS_COUNT = 2
GUN_AIM_CONE_HALF_ANGLE = math.radians(60)
FLASHLIGHT_CONE_HALF_ANGLE = math.radians(100)
FLASHLIGHT_RANGE = 480
SNOW_COUNT_MENU = 80
SNOW_COUNT_GAME = 120
SNOW_MAX_SIZE = 1
BLIZZARD_EXTRA_SNOW_MAX = 60
BLIZZARD_TINT_ALPHA_MAX = 100
BLIZZARD_VISIBILITY_MIN = 0.65
PLAYER_MAX_HP = 3
DAMAGE_INVULN_FRAMES = 90
INTRO_TOTAL_FRAMES = 240
BLIZZARD_CYCLE_FRAMES = 1800
BLIZZARD_PEAK_FRAMES = 600
BLIZZARD_SPEED_PENALTY = 0.6
NOTE_COUNT = 5
TRAIL_LENGTH = 12
COIN_LOOT_CHANCE = 0.6
COINS_PER_LOOT = (1, 3)

INTRO_RADIO_LINES = [
    (0, "...SAR-3, do you copy?..."),
    (40, "Signal degrading... visib--..."),
    (90, "Target zone is DARK. No thermal sigs."),
    (140, "You are on your own. Good lu--..."),
]

RESEARCHER_NOTES = [
    "Day 12: The breathing sounds from the vents\nare NOT mechanical. Dr. Vasquez disagrees.",
    "Day 19: Found claw marks on the inside of\nthe freezer door. From the INSIDE.",
    "Day 24: Three more missing. Security footage\nshows them walking INTO the walls.",
    "Day 31: It mimics voices. Heard my daughter\ncalling from Lab B. She's in Boston.",
    "FINAL: DO NOT use the flare gun unless\nnecessary. The sound... it makes them ANGRY.",
]

ROOM_COLORS = {
    '.': C_FLOOR_BED, ',': C_FLOOR_KITCHEN,
    '~': C_FLOOR_BATH, '0': C_FLOOR_HALL,
    'O': C_FLOOR_OUTDOOR, 'G': C_FLOOR_HALL, 'S': C_FLOOR_HALL,
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snow Escape: Coin Escape Route")
clock = pygame.time.Clock()


# ==================== 音频合成器 ====================
class SynthAudio:
    def __init__(self):
        self.bgm_channel = None
        self.bgm_playing = False

    @staticmethod
    def _make_sound(freq, duration_ms, wave='sine', volume=0.3):
        sample_rate = 22050
        n_samples = int(sample_rate * duration_ms / 1000)
        buf = array.array('h')
        max_amp = int(32767 * volume)
        for i in range(n_samples):
            t = i / sample_rate
            envelope = max(0, 1.0 - (i / n_samples))
            if wave == 'sine':
                val = int(max_amp * envelope * math.sin(2 * math.pi * freq * t))
            elif wave == 'square':
                val = int(max_amp * envelope * (1 if math.sin(2 * math.pi * freq * t) > 0 else -1))
            elif wave == 'noise':
                val = int(max_amp * envelope * random.uniform(-1, 1))
            else:
                val = 0
            buf.append(val)
        return pygame.mixer.Sound(buffer=buf)

    def start_bgm(self):
        if self.bgm_playing:
            return
        sample_rate = 22050
        duration = 4.0
        n_samples = int(sample_rate * duration)
        buf = array.array('h')
        notes = [55, 55, 65.41, 55, 49, 49, 55, 65.41]
        note_dur = duration / len(notes)
        for i in range(n_samples):
            t = i / sample_rate
            note_idx = min(int(t / note_dur), len(notes) - 1)
            freq = notes[note_idx]
            local_t = t - note_idx * note_dur
            envelope = max(0, 1.0 - local_t / note_dur) * 0.15
            phase = (freq * local_t) % 1.0
            val = int(32767 * envelope * (2.0 * phase - 1.0))
            buf.append(val)
        bgm_sound = pygame.mixer.Sound(buffer=buf)
        self.bgm_channel = bgm_sound.play(loops=-1)
        self.bgm_playing = True

    def play_shoot(self):
        self._make_sound(600, 80, 'square', 0.15).play()

    def play_coin(self):
        self._make_sound(1400, 120, 'sine', 0.12).play()


synth_audio = SynthAudio()


def get_font(names, size, bold=False):
    for name in names:
        try:
            return pygame.font.SysFont(name, size, bold=bold)
        except Exception:
            continue
    return pygame.font.Font(None, size)


font_large = get_font(['Arial', 'Helvetica', 'sans-serif'], 70, bold=True)
font_medium = get_font(['Arial', 'Helvetica', 'sans-serif'], 36, bold=True)
font_small = get_font(['Arial', 'Helvetica', 'sans-serif'], 28)
font_hint = get_font(['Arial', 'Helvetica', 'sans-serif'], 22)
font_story = get_font(['Consolas', 'Courier New', 'monospace'], 22)
font_cd = get_font(['Arial', 'Helvetica', 'sans-serif'], 20, bold=True)
font_mini = get_font(['Arial', 'Helvetica', 'sans-serif'], 14, bold=True)
font_hp = get_font(['Arial', 'Helvetica', 'sans-serif'], 24, bold=True)
font_radio = get_font(['Consolas', 'Courier New', 'monospace'], 26, bold=True)
font_note = get_font(['Consolas', 'Courier New', 'monospace'], 18)
font_compass = get_font(['Arial', 'Helvetica', 'sans-serif'], 16, bold=True)
font_loot = get_font(['Arial', 'Helvetica', 'sans-serif'], 22, bold=True)

_wall_noise_surf = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
for _ny in range(TILE_SIZE):
    for _nx in range(TILE_SIZE):
        if random.random() < 0.3:
            c = (75, 75, 90, 30) if random.random() > 0.5 else (30, 30, 38, 40)
            _wall_noise_surf.set_at((_nx, _ny), c)


# ==================== 2. 天气系统 ====================
class WeatherSystem:
    def __init__(self):
        self.frame = 0
        self.intensity = 0.0
        self.blizzard_active = False

    def update(self):
        self.frame += 1
        cycle_pos = self.frame % BLIZZARD_CYCLE_FRAMES
        if cycle_pos < BLIZZARD_PEAK_FRAMES:
            self.intensity = cycle_pos / BLIZZARD_PEAK_FRAMES
        elif cycle_pos < BLIZZARD_PEAK_FRAMES * 2:
            self.intensity = 1.0 - (cycle_pos - BLIZZARD_PEAK_FRAMES) / BLIZZARD_PEAK_FRAMES
        else:
            self.intensity = 0.0
        self.blizzard_active = self.intensity > 0.3

    def get_speed_multiplier(self):
        return 1.0 - self.intensity * (1.0 - BLIZZARD_SPEED_PENALTY)

    def get_visibility(self):
        return 1.0 - self.intensity * (1.0 - BLIZZARD_VISIBILITY_MIN)

    def draw_overlay(self, surface):
        if self.intensity <= 0.01:
            return
        alpha_val = int(BLIZZARD_TINT_ALPHA_MAX * self.intensity)
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((*C_BLIZZARD_TINT, alpha_val))
        surface.blit(overlay, (0, 0))
        extra_count = int(self.intensity * BLIZZARD_EXTRA_SNOW_MAX)
        for _ in range(extra_count):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            a_val = int(150 * self.intensity)
            pygame.draw.circle(surface, (*C_SNOW[:3], a_val), (x, y), SNOW_MAX_SIZE)


# ==================== 3. 文本内容（★含金币逃离说明） ====================
STORY_LINES = [
    "[MISSION BRIEFING: FROSTWHISPER PERIMETER]", "",
    "DATE: Nov 14, 2087 | 03:00 UTC",
    "LOC:  Arctic Circle, Frostwhisper Deep Climate Lab", "",
    "All contact lost 72h ago. Last transmission contained",
    "non-natural biological breathing patterns.",
    "You are the third SAR operative deployed.",
    "First two teams went dark within 15 min of entry.", "",
    "The facility spans a large outdoor perimeter with",
    "multiple buildings connected by security gates.",
    "Gates require manual switch activation from one side",
    "then traversal from the other. Plan your route.", "",
    "8 mechanical keys hidden across the compound.",
    "Search crates & furniture to find coins and keys!",
    "Hostile density is HIGH.", "",
    "[COMBAT PROTOCOL A: THERMAL OVERLOAD]",
    "Strobe DESTROYS hostiles in exactly 2 flashes.",
    "First flash stuns + deals 1st hit.",
    "Second flash while stunned = KILL.", "",
    "[COMBAT PROTOCOL B: SENTRY FLARE GUN]",
    "2 fixed flare gun stations placed outdoors.",
    "Approach and press [E] to equip. Each has 3 rounds.",
    "GUARANTEED ONE-SHOT KILL. WARNING: Alerts ALL hostiles.", "",
    "[SYSTEM OVERRIDE: FULL VISIBILITY]",
    "Thermal optics online. Darkness penalty removed.",
    "Blizzards still reduce movement speed by 40%.", "",
    "OBJECTIVE: Collect all keys > Unlock main door > Evac.",
    "",
    "[ALTERNATE ESCAPE PROTOCOL]",
    f"Collect {ESCAPE_COIN_THRESHOLD} coins from searchable crates",
    "to trigger emergency extraction. No keys required.",
]

CONTROLS_LINES = [
    "[CONTROLS GUIDE]", "",
    "  W/S/A/D        Move",
    "  MOUSE          Aim flashlight & flare gun",
    "  E              Search crates / Equip / Read Note",
    "  SPACE          Strobe Flash (2 hits to kill)",
    "  F              Fire Flare Gun (ONE SHOT KILL)",
    "  R              Restart (after game over)",
    "  ESC            Return to Main Menu", "",
    "[FEATURES]",
    "  - Visible bullet trails on all projectiles",
    "  - Coins hidden inside searchable crates/furniture",
    f"  - Collect {ESCAPE_COIN_THRESHOLD} coins for alternate escape",
    "  - Synthesized BGM & SFX (no external files)",
    "  - Blood trails persist after flash hit",
    "  - Humanoid mutant form when alerted",
    "  - Dynamic blizzard weather cycle",
    "  - Clean minimap (no item clutter)",
]


# ==================== 实体类 ====================
class BulletTrail:
    def __init__(self):
        self.trails = []

    def add_trail(self, start_x, start_y, end_x, end_y):
        points = []
        dist = math.hypot(end_x - start_x, end_y - start_y)
        steps = max(int(dist / 8), 2)
        for i in range(steps + 1):
            t = i / steps
            px = start_x + (end_x - start_x) * t
            py = start_y + (end_y - start_y) * t
            points.append((px, py))
        self.trails.append([points, TRAIL_LENGTH])

    def update(self):
        for trail in self.trails:
            trail[1] -= 1
        self.trails = [t for t in self.trails if t[1] > 0]

    def draw(self, surface, cam_x, cam_y):
        for points, life in self.trails:
            alpha_ratio = life / TRAIL_LENGTH
            if len(points) < 2:
                continue
            for i in range(1, len(points)):
                seg_alpha = (i / len(points)) * alpha_ratio
                width = max(1, int(4 * seg_alpha))
                r = int(C_TRAIL_CORE[0] * seg_alpha + C_TRAIL_EDGE[0] * (1 - seg_alpha))
                g = int(C_TRAIL_CORE[1] * seg_alpha + C_TRAIL_EDGE[1] * (1 - seg_alpha))
                b = int(C_TRAIL_CORE[2] * seg_alpha + C_TRAIL_EDGE[2] * (1 - seg_alpha))
                sx = int(points[i - 1][0] - cam_x)
                sy = int(points[i - 1][1] - cam_y)
                ex = int(points[i][0] - cam_x)
                ey = int(points[i][1] - cam_y)
                pygame.draw.line(surface, (r, g, b), (sx, sy), (ex, ey), width)


class SnowSystem:
    def __init__(self, count=300):
        self.flakes = [
            [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT),
             random.uniform(0.8, 2.5), random.uniform(-0.3, 0.3)]
            for _ in range(count)
        ]

    def update_and_draw(self, surface):
        for f in self.flakes:
            f[1] += f[2]
            f[0] += f[3] + math.sin(f[1] * 0.008) * 0.5
            if f[1] > SCREEN_HEIGHT:
                f[1] = -5
                f[0] = random.randint(0, SCREEN_WIDTH)
            pygame.draw.circle(surface, C_SNOW, (int(f[0]), int(f[1])), SNOW_MAX_SIZE)


class BloodTrailSystem:
    def __init__(self):
        self.drops = []

    def add_drop(self, x, y, size=None, splatter=False):
        life = random.randint(900, 1200)
        s = size or random.randint(2, 5)
        color = C_BLOOD_SPLATTER if splatter else C_BLOOD_TRAIL
        self.drops.append([x + random.uniform(-3, 3), y + random.uniform(-3, 3), life, s, color])

    def add_trail_segment(self, x1, y1, x2, y2, count=3):
        for _ in range(count):
            t = random.random()
            self.add_drop(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)

    def update(self):
        for d in self.drops:
            d[2] -= 1
        self.drops = [d for d in self.drops if d[2] > 0]

    def draw(self, surface, cam_x, cam_y):
        for d in self.drops:
            alpha_val = min(d[4][3], int(d[4][3] * (d[2] / 1200)))
            if alpha_val <= 0:
                continue
            sx = int(d[0]) - cam_x - d[3]
            sy = int(d[1]) - cam_y - d[3]
            drop_surf = pygame.Surface((d[3] * 2 + 2, d[3] * 2 + 2), pygame.SRCALPHA)
            pygame.draw.circle(drop_surf, (*d[4][:3], alpha_val), (d[3] + 1, d[3] + 1), d[3])
            surface.blit(drop_surf, (sx, sy))


class LootPopup:
    def __init__(self, x, y, amount):
        self.x = x
        self.y = y
        self.amount = amount
        self.life = 60
        self.vy = -1.2

    def update(self):
        self.y += self.vy
        self.life -= 1

    def draw(self, surface, cam_x, cam_y):
        alpha = max(0, min(255, int(255 * (self.life / 60))))
        txt = font_loot.render(f"+{self.amount} COIN", True, C_COIN_GOLD)
        txt.set_alpha(alpha)
        surface.blit(txt, (int(self.x - cam_x) - txt.get_width() // 2, int(self.y - cam_y)))


class MainMenu:
    ITEMS = ["START GAME", "BACKGROUND STORY", "CONTROLS"]

    def __init__(self):
        self.selected = 0
        self.state = "menu"
        self.snow = SnowSystem(SNOW_COUNT_MENU)

    def run(self):
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if self.state == "menu":
                        if event.key in (pygame.K_UP, pygame.K_w):
                            self.selected = (self.selected - 1) % len(self.ITEMS)
                        elif event.key in (pygame.K_DOWN, pygame.K_s):
                            self.selected = (self.selected + 1) % len(self.ITEMS)
                        elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                            if self.selected == 0:
                                return True
                            elif self.selected == 1:
                                self.state = "story"
                            elif self.selected == 2:
                                self.state = "controls"
                        elif event.key == pygame.K_ESCAPE:
                            return False
                    elif self.state in ("story", "controls"):
                        if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE, pygame.K_RETURN):
                            self.state = "menu"
            screen.fill(C_MENU_BG)
            self.snow.update_and_draw(screen)
            if self.state == "menu":
                self._draw_menu()
            elif self.state == "story":
                self._draw_text_screen("BACKGROUND STORY", STORY_LINES)
            elif self.state == "controls":
                self._draw_text_screen("CONTROLS", CONTROLS_LINES)
            pygame.display.flip()
        return False

    def _draw_menu(self):
        title = font_large.render("SNOW ESCAPE", True, C_MENU_TITLE)
        subtitle = font_small.render("Frozen Perimeter", True, (120, 140, 180))
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 140))
        screen.blit(subtitle, (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 220))
        start_y, spacing = 340, 70
        for i, item in enumerate(self.ITEMS):
            is_sel = (i == self.selected)
            color = C_MENU_SELECTED if is_sel else C_MENU_ITEM
            text = font_medium.render(item, True, color)
            x = SCREEN_WIDTH // 2 - text.get_width() // 2
            y = start_y + i * spacing
            screen.blit(text, (x, y))
            if is_sel:
                ind = font_medium.render(">", True, C_MENU_SELECTED)
                screen.blit(ind, (x - 35, y))
        hint = font_hint.render("UP/DOWN Select | ENTER Confirm | ESC Quit", True, (100, 100, 120))
        screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, SCREEN_HEIGHT - 50))

    def _draw_text_screen(self, title, lines):
        pygame.draw.rect(screen, C_MENU_BORDER, (0, 0, SCREEN_WIDTH, 60))
        t = font_medium.render(title, True, C_MENU_TITLE)
        screen.blit(t, (40, 15))
        back = font_hint.render("[ESC / ENTER] Back to Menu", True, (120, 120, 140))
        screen.blit(back, (SCREEN_WIDTH - back.get_width() - 30, 20))
        content_x, content_y, line_h = 80, 90, 28
        max_lines = (SCREEN_HEIGHT - 120) // line_h
        keywords = [
            "W/", "S/", "A/", "D/", "E  ", "SPACE", "F  ", "MOUSE", "R  ", "ESC",
            "Cooldown", "SENTRY", "ALERT", "CONE", "flashlight",
            "3 HP", "MUTATE", "Blood", "SCARE", "Heartbeat", "Humanoid",
            "ONE SHOT", "Blizzard", "Note", "Compass", "VISIBILITY", "2 hits",
            "Search", "trail", "Synth", "BGM", "crates", "Clean",
            "coins", "escape", "ALTERNATE", "extraction"
        ]
        for i, line in enumerate(lines[:max_lines]):
            if line.startswith("["):
                color = C_TEXT_HIGHLIGHT
            elif any(kw.lower() in line.lower() for kw in keywords):
                color = C_TEXT_KEY
            elif line.strip().startswith("-"):
                color = C_TEXT_HIGHLIGHT
            else:
                color = C_TEXT_BODY
            rendered = font_story.render(line, True, color)
            screen.blit(rendered, (content_x, content_y + i * line_h))


class Furniture:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.searched = False
        self.has_key = False
        self.has_coins = False
        self.coin_amount = 0
        self.search_progress = 0
        self.search_time = 60

    def draw(self, surface, cam_x, cam_y):
        r = self.rect.move(-cam_x, -cam_y)
        color = C_FURNITURE_SEARCHED if self.searched else C_FURNITURE
        top_color = (100, 80, 50) if self.searched else C_FURNITURE_TOP
        pygame.draw.rect(surface, (20, 15, 10), r.move(3, 3))
        pygame.draw.rect(surface, color, r)
        pygame.draw.rect(surface, top_color, (r.x, r.y, TILE_SIZE, 10))
        if not self.searched:
            pygame.draw.circle(surface, (180, 160, 100), (r.centerx, r.centery + 5), 3)
            pygame.draw.rect(surface, (160, 140, 80), (r.centerx - 4, r.centery + 2, 8, 3))
        else:
            pygame.draw.line(surface, (60, 50, 30),
                             (r.x + 8, r.y + 15), (r.right - 8, r.y + 15), 2)


class GateSwitch:
    def __init__(self, gate_obj):
        self.gate = gate_obj
        self.rect = gate_obj['switch_rect']
        self.activated = False

    def activate(self):
        if not self.activated:
            self.activated = True
            self.gate['open'] = True
            return True
        return False

    def draw(self, surface, cam_x, cam_y):
        r = self.rect.move(-cam_x, -cam_y)
        pygame.draw.rect(surface, C_SWITCH_BASE, r.inflate(-10, -10))
        color = C_SWITCH_ON if self.activated else C_SWITCH_OFF
        cx, cy = r.centerx, r.centery
        if self.activated:
            pygame.draw.rect(surface, color, (cx - 3, cy - 10, 6, 14), border_radius=2)
            pygame.draw.circle(surface, (100, 255, 100), (cx, cy - 10), 4)
        else:
            pygame.draw.rect(surface, color, (cx - 3, cy - 4, 6, 14), border_radius=2)
            pygame.draw.circle(surface, (255, 180, 60), (cx, cy + 10), 4)


class ResearcherNote:
    def __init__(self, data):
        self.x = data['x']
        self.y = data['y']
        self.text = data['text']
        self.read = data['read']
        self.rect = pygame.Rect(self.x - 15, self.y - 15, 30, 30)

    def draw(self, surface, cam_x, cam_y):
        if self.read:
            return
        sx = self.x - cam_x
        sy = self.y - cam_y
        pulse = 0.6 + 0.4 * math.sin(pygame.time.get_ticks() * 0.004)
        glow = pygame.Surface((28, 28), pygame.SRCALPHA)
        pygame.draw.circle(glow, (220, 210, 180, int(60 * pulse)), (14, 14), 14)
        surface.blit(glow, (int(sx) - 14, int(sy) - 14))
        pygame.draw.rect(surface, C_NOTE_PAPER, (int(sx) - 6, int(sy) - 8, 12, 16))
        pygame.draw.line(surface, C_NOTE_TEXT, (int(sx) - 4, int(sy) - 4), (int(sx) + 4, int(sy) - 4), 1)
        pygame.draw.line(surface, C_NOTE_TEXT, (int(sx) - 4, int(sy) - 1), (int(sx) + 4, int(sy) - 1), 1)
        pygame.draw.line(surface, C_NOTE_TEXT, (int(sx) - 4, int(sy) + 2), (int(sx) + 2, int(sy) + 2), 1)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.base_speed = 3.5
        self.speed = self.base_speed
        self.keys_collected = 0
        self.coins_collected = 0
        self.searching = False
        self.search_target = None
        self.facing_right = True
        self.anim_frame = 0
        self.is_moving = False
        self.flash_cd_timer = 0
        self.flash_visual_timer = 0
        self.has_gun = False
        self.gun_ammo = 0
        self.gun_fire_cd = 0
        self.gun_muzzle_timer = 0
        self.hp = PLAYER_MAX_HP
        self.invn_timer = 0
        self.scare_timer = 0
        self.current_tile_type = 'O'

    def move(self, dx, dy, walls, furniture_list, gates, speed_mult=1.0):
        if self.searching:
            self.is_moving = False
            return
        self.is_moving = (dx != 0 or dy != 0)
        self.speed = self.base_speed * speed_mult
        if self.is_moving:
            self.anim_frame += 0.18
            if dx > 0.1:
                self.facing_right = True
            elif dx < -0.1:
                self.facing_right = False
        nx = self.x + dx * self.speed
        if not self._collides(nx, self.y, walls, furniture_list, gates):
            self.x = nx
        ny = self.y + dy * self.speed
        if not self._collides(self.x, ny, walls, furniture_list, gates):
            self.y = ny

    def _collides(self, x, y, walls, furniture_list, gates):
        r = 12
        tr = pygame.Rect(x - r, y - r, r * 2, r * 2)
        if any(tr.colliderect(w) for w in walls):
            return True
        if any(tr.colliderect(f.rect) for f in furniture_list):
            return True
        for g in gates:
            if not g['open'] and tr.colliderect(g['gate_rect']):
                return True
        return False

    def get_nearby_interactable(self, furniture_list, switches, gun_stations, notes):
        pr = pygame.Rect(self.x - 25, self.y - 25, 50, 50)
        for n in notes:
            if not n.read and pr.colliderect(n.rect):
                return ('note', n)
        if not self.has_gun:
            for gs in gun_stations:
                if not gs['taken'] and pr.colliderect(gs['rect']):
                    return ('gun_station', gs)
        for sw in switches:
            if not sw.activated and pr.colliderect(sw.rect):
                return ('switch', sw)
        for f in furniture_list:
            if not f.searched and pr.colliderect(f.rect):
                return ('furniture', f)
        return None

    def try_flash(self):
        if self.flash_cd_timer <= 0:
            self.flash_cd_timer = FLASH_COOLDOWN_FRAMES
            self.flash_visual_timer = FLASH_VISUAL_DURATION
            return True
        return False

    def try_fire(self):
        if self.has_gun and self.gun_ammo > 0 and self.gun_fire_cd <= 0:
            self.gun_ammo -= 1
            self.gun_fire_cd = GUN_FIRE_CD
            self.gun_muzzle_timer = 6
            if self.gun_ammo <= 0:
                self.has_gun = False
            return True
        return False

    def equip_gun(self, station):
        self.has_gun = True
        self.gun_ammo = station['ammo']
        self.gun_fire_cd = 0
        station['taken'] = True

    def take_damage(self):
        if self.invn_timer > 0:
            return False
        self.hp -= 1
        self.invn_timer = DAMAGE_INVULN_FRAMES
        return True

    def trigger_scare(self):
        self.scare_timer = SCARE_DURATION

    def update_timers(self):
        if self.flash_cd_timer > 0:
            self.flash_cd_timer -= 1
        if self.flash_visual_timer > 0:
            self.flash_visual_timer -= 1
        if self.gun_fire_cd > 0:
            self.gun_fire_cd -= 1
        if self.gun_muzzle_timer > 0:
            self.gun_muzzle_timer -= 1
        if self.invn_timer > 0:
            self.invn_timer -= 1
        if self.scare_timer > 0:
            self.scare_timer -= 1

    def update_tile_type(self, grid):
        tx = max(0, min(int(self.x // TILE_SIZE), MAP_COLS - 1))
        ty = max(0, min(int(self.y // TILE_SIZE), MAP_ROWS - 1))
        self.current_tile_type = grid[ty][tx]

    def draw(self, surface, cam_x, cam_y):
        px, py = int(self.x - cam_x), int(self.y - cam_y)
        flip = 1 if self.facing_right else -1
        so = 4 if self.searching else 0
        swing = 0 if self.searching else (math.sin(self.anim_frame) * 5 if self.is_moving else 0)
        if self.invn_timer > 0 and (self.invn_timer // 4) % 2 == 0:
            return
        pygame.draw.ellipse(surface, (0, 0, 0, 80), (px - 11, py + 10, 22, 7))
        ls = swing
        lx1, ly1 = px - 4 * flip, py + 4 + so
        lx2, ly2 = lx1 - ls * flip, py + 15
        pygame.draw.line(surface, C_P_COAT_SHADOW, (lx1, ly1), (lx2, ly2), 5)
        pygame.draw.ellipse(surface, C_P_BOOT, (lx2 - 3, ly2 - 2, 7, 5))
        rx1, ry1 = px + 4 * flip, py + 4 + so
        rx2, ry2 = rx1 + ls * flip, py + 15
        pygame.draw.line(surface, C_P_COAT, (rx1, ry1), (rx2, ry2), 5)
        pygame.draw.ellipse(surface, C_P_BOOT, (rx2 - 3, ry2 - 2, 7, 5))
        bpx, bpy = px - 8 * flip, py - 6 + so
        pygame.draw.rect(surface, C_P_BACKPACK, (bpx - 5, bpy, 10, 14), border_radius=3)
        pygame.draw.line(surface, (90, 60, 30), (bpx, bpy + 2), (bpx + 3 * flip, bpy + 12), 2)
        bt = py - 10 + so
        br = pygame.Rect(px - 7, bt, 14, 16)
        pygame.draw.rect(surface, C_P_COAT, br, border_radius=3)
        sx = px - 7 if self.facing_right else px + 3
        pygame.draw.rect(surface, C_P_COAT_SHADOW, (sx, bt + 2, 4, 12), border_radius=1)
        zx = px + 1 * flip
        pygame.draw.line(surface, (90, 110, 160), (zx, bt + 2), (zx, bt + 14), 1)
        asw = -swing
        baex, baey = px - 10 * flip + asw * flip, py + 2 + so
        pygame.draw.line(surface, C_P_COAT_SHADOW, (px - 6 * flip, py - 5 + so), (baex, baey), 4)
        pygame.draw.circle(surface, C_P_GLOVE, (int(baex), int(baey)), 3)
        faex, faey = px + 10 * flip - asw * flip, py + 2 + so
        pygame.draw.line(surface, C_P_COAT, (px + 6 * flip, py - 5 + so), (faex, faey), 4)
        pygame.draw.circle(surface, C_P_GLOVE, (int(faex), int(faey)), 3)
        if self.has_gun:
            gun_x = int(faex) + 2 * flip
            gun_y = int(faey) - 2
            pygame.draw.rect(surface, C_GUN_BARREL, (gun_x, gun_y - 2, 10 * flip, 4))
            pygame.draw.rect(surface, C_GUN_METAL, (gun_x - 2 * flip, gun_y - 3, 6 * flip, 6))
            pygame.draw.rect(surface, C_GUN_GRIP, (gun_x - 1 * flip, gun_y + 2, 4 * flip, 5))
            if self.gun_ammo > 0:
                pygame.draw.circle(surface, C_AMMO_COLOR, (gun_x + 3 * flip, gun_y - 1), 2)
            if self.gun_muzzle_timer > 0:
                mf_size = 12 + random.randint(0, 6)
                mf_surf = pygame.Surface((mf_size * 2, mf_size * 2), pygame.SRCALPHA)
                pygame.draw.circle(mf_surf, (255, 240, 150, 200), (mf_size, mf_size), mf_size)
                pygame.draw.circle(mf_surf, (255, 255, 255, 255), (mf_size, mf_size), mf_size // 2)
                tip_x = gun_x + 12 * flip
                surface.blit(mf_surf, (tip_x - mf_size, gun_y - mf_size - 2))
        hcy = py - 15 + so
        pygame.draw.circle(surface, C_P_HOOD, (px, hcy), 9)
        fx = px + 3 * flip
        pygame.draw.circle(surface, C_P_SKIN, (fx, hcy + 1), 5)
        gx = fx + 1 * flip
        pygame.draw.rect(surface, C_P_GOGGLE_FRAME, (gx - 4, hcy - 3, 8, 5), border_radius=2)
        pygame.draw.rect(surface, C_P_GOGGLE, (gx - 3, hcy - 2, 6, 3), border_radius=1)
        pygame.draw.circle(surface, (255, 255, 255), (gx - 1, hcy - 1), 1)


class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.base_speed = 2.4
        self.speed = self.base_speed
        self.state = "patrol"
        self.patrol_timer = 0
        self.move_dir = [0, 0]
        self.view_dist = 280
        self.radius = 14
        self.anim_frame = 0
        self.facing_right = True
        self.stun_timer = 0
        self.flash_hits = 0
        self.alive = True
        self.alert_timer = 0
        self.trail = []
        self.trail_timer = 0
        self.last_blood_pos = None
        self.breath_phase = random.uniform(0, math.pi * 2)
        self.hit_flash_timer = 0

    def update(self, player, walls, furniture_list, gates, blood_system):
        if not self.alive:
            return
        if self.hit_flash_timer > 0:
            self.hit_flash_timer -= 1
        if self.stun_timer > 0:
            self.stun_timer -= 1
            self.state = "stunned"
            if self.last_blood_pos:
                dist = math.hypot(self.x - self.last_blood_pos[0], self.y - self.last_blood_pos[1])
                if dist > 8:
                    blood_system.add_trail_segment(*self.last_blood_pos, self.x, self.y)
                    self.last_blood_pos = (self.x, self.y)
            elif self.last_blood_pos is None:
                self.last_blood_pos = (self.x, self.y)
                blood_system.add_drop(self.x, self.y, splatter=True)
            return
        if self.alert_timer > 0:
            self.alert_timer -= 1
            self.speed = self.base_speed * GUN_ALERT_SPEED_MULT
            self.state = "chase"
            self.trail_timer += 1
            if self.trail_timer >= 4:
                self.trail.append((self.x, self.y))
                if len(self.trail) > 6:
                    self.trail.pop(0)
                self.trail_timer = 0
        else:
            self.speed = self.base_speed
            self.trail.clear()
            dist = math.hypot(player.x - self.x, player.y - self.y)
            if dist < self.view_dist:
                self.state = "chase"
            elif self.state == "chase" and dist > self.view_dist * 1.8:
                self.state = "patrol"
        ddx, ddy = 0, 0
        if self.state == "chase":
            a_val = math.atan2(player.y - self.y, player.x - self.x)
            ddx, ddy = math.cos(a_val), math.sin(a_val)
        else:
            self.patrol_timer -= 1
            if self.patrol_timer <= 0:
                a_val = random.uniform(0, 2 * math.pi)
                self.move_dir = [math.cos(a_val), math.sin(a_val)]
                self.patrol_timer = random.randint(60, 180)
            ddx, ddy = self.move_dir
        vec_len = math.hypot(ddx, ddy)
        if vec_len > 0:
            ddx, ddy = ddx / vec_len, ddy / vec_len
            if ddx > 0.1:
                self.facing_right = True
            elif ddx < -0.1:
                self.facing_right = False
        moved = False
        nx = self.x + ddx * self.speed
        if not self._collides(nx, self.y, walls, furniture_list, gates):
            self.x = nx
            moved = True
        ny = self.y + ddy * self.speed
        if not self._collides(self.x, ny, walls, furniture_list, gates):
            self.y = ny
            moved = True
        if not moved and self.state == "patrol":
            self.patrol_timer = 0
        if moved:
            self.anim_frame += 0.15
        self.breath_phase += 0.06

    def receive_flash(self, blood_system):
        if not self.alive:
            return None
        self.flash_hits += 1
        if self.flash_hits >= KILL_HITS_REQUIRED:
            self.alive = False
            for _ in range(8):
                blood_system.add_drop(
                    self.x + random.uniform(-15, 15),
                    self.y + random.uniform(-15, 15),
                    size=random.randint(3, 7), splatter=True
                )
            return 'kill'
        else:
            self.stun_timer = STUN_DURATION_FRAMES
            self.state = "stunned"
            self.last_blood_pos = (self.x, self.y)
            for _ in range(5):
                blood_system.add_drop(
                    self.x + random.uniform(-12, 12),
                    self.y + random.uniform(-12, 12),
                    size=random.randint(2, 5), splatter=True
                )
            return 'stun'

    def receive_bullet(self, blood_system):
        if not self.alive:
            return False
        self.alive = False
        self.hit_flash_timer = 4
        for _ in range(15):
            blood_system.add_drop(
                self.x + random.uniform(-20, 20),
                self.y + random.uniform(-20, 20),
                size=random.randint(4, 9), splatter=True
            )
        return True

    def apply_alert(self):
        if self.alive and self.state != "stunned":
            self.alert_timer = GUN_ALERT_DURATION

    def _collides(self, x, y, walls, furniture_list, gates):
        tr = pygame.Rect(x - self.radius, y - self.radius, self.radius * 2, self.radius * 2)
        if any(tr.colliderect(w) for w in walls):
            return True
        if any(tr.colliderect(f.rect) for f in furniture_list):
            return True
        for g in gates:
            if not g['open'] and tr.colliderect(g['gate_rect']):
                return True
        return False

    def draw(self, surface, cam_x, cam_y):
        if not self.alive:
            return
        pos = (int(self.x - cam_x), int(self.y - cam_y))
        flip = -1 if self.facing_right else 1
        is_mutant = (self.alert_timer > 0 and self.state != "stunned")
        breath = math.sin(self.breath_phase) * 1.5
        override_color = (255, 255, 255) if self.hit_flash_timer > 0 else None

        if is_mutant:
            trail_len = max(len(self.trail), 1)
            for i, (tx, ty) in enumerate(self.trail):
                trail_alpha = int(50 * ((i + 1) / trail_len))
                trail_surf = pygame.Surface((24, 40), pygame.SRCALPHA)
                pygame.draw.ellipse(trail_surf, (*C_MUTANT_TRAIL[:3], trail_alpha), (4, 4, 16, 32))
                surface.blit(trail_surf, (int(tx - cam_x) - 12, int(ty - cam_y) - 20))
            glow_surf = pygame.Surface((60, 60), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, C_MUTANT_GLOW, (30, 30), 30)
            surface.blit(glow_surf, (pos[0] - 30, pos[1] - 30))
            sw = math.sin(self.anim_frame * 1.5) * 10
            asw = -sw
            lc = override_color or C_MUTANT_SKIN
            for side in (-1, 1):
                knee_x = pos[0] + side * 4 + sw * 0.5 * side
                knee_y = pos[1] + 8
                foot_x = pos[0] + side * 5 + sw * side
                foot_y = pos[1] + 22
                pygame.draw.line(surface, lc, (pos[0] + side * 4, pos[1] + 4), (knee_x, knee_y), 4)
                pygame.draw.circle(surface, override_color or C_MUTANT_JOINT, (int(knee_x), int(knee_y)), 2)
                pygame.draw.line(surface, lc, (knee_x, knee_y), (foot_x, foot_y), 3)
                pygame.draw.ellipse(surface, override_color or (30, 10, 10), (foot_x - 3, foot_y - 2, 7, 5))
            torso_w = 14 + breath * 0.5
            torso_h = 24 + breath
            torso_x = pos[0] - int(torso_w / 2)
            torso_y = pos[1] - 16
            pygame.draw.rect(surface, lc, (torso_x, torso_y, int(torso_w), int(torso_h)), border_radius=4)
            if not override_color:
                pygame.draw.line(surface, C_MUTANT_SKIN_HL,
                                 (torso_x + 1, torso_y + 2), (torso_x + 1, torso_y + int(torso_h) - 2), 1)
                vein_pulse = 0.5 + 0.5 * math.sin(pygame.time.get_ticks() * 0.012)
                vc = tuple(min(255, int(c * vein_pulse)) for c in C_MUTANT_VEIN)
                pygame.draw.line(surface, vc, (pos[0] - 4, torso_y + 4), (pos[0] + 2, torso_y + 14), 1)
                pygame.draw.line(surface, vc, (pos[0] + 4, torso_y + 6), (pos[0] - 1, torso_y + 18), 1)
            shoulder_y = torso_y + 2
            reach = 6 if self.state == "chase" else 0
            for side in (-1, 1):
                elbow_x = pos[0] + side * 12 + asw * 0.5 * side
                elbow_y = shoulder_y + 10
                hand_x = pos[0] + side * 14 + asw * side + reach * flip
                hand_y = shoulder_y + 17 + abs(asw) * 0.2
                pygame.draw.circle(surface, lc, (pos[0] + side * 8, shoulder_y), 4)
                pygame.draw.line(surface, lc, (pos[0] + side * 8, shoulder_y), (elbow_x, elbow_y), 3)
                pygame.draw.circle(surface, override_color or C_MUTANT_JOINT, (int(elbow_x), int(elbow_y)), 2)
                pygame.draw.line(surface, lc, (elbow_x, elbow_y), (hand_x, hand_y), 3)
                pygame.draw.circle(surface, override_color or C_MUTANT_VEIN, (int(hand_x), int(hand_y)), 3)
                for f_idx in range(3):
                    fa = -0.5 + f_idx * 0.5 + (0 if flip > 0 else math.pi)
                    pygame.draw.line(surface, override_color or C_MUTANT_CLAW, (hand_x, hand_y),
                                     (hand_x + math.cos(fa) * 5, hand_y + math.sin(fa) * 5), 1)
            pygame.draw.line(surface, lc, (pos[0], torso_y), (pos[0], torso_y - 4), 3)
            head_cy = torso_y - 10
            head_w = 12 + breath * 0.3
            head_h = 15
            pygame.draw.ellipse(surface, lc,
                                (pos[0] - int(head_w / 2), head_cy - int(head_h / 2), int(head_w), head_h))
            if not override_color:
                pygame.draw.arc(surface, C_MUTANT_JOINT,
                                (pos[0] - int(head_w / 2) + 1, head_cy, int(head_w) - 2, int(head_h // 2)),
                                math.pi, 2 * math.pi, 1)
            for s in range(5):
                sx = pos[0] - 5 + s * 3
                sy = head_cy - int(head_h / 2)
                pygame.draw.line(surface, override_color or C_MUTANT_HAIR, (sx, sy),
                                 (sx + random.choice([-2, 0, 2]), sy - 4), 1)
            ex = 3 * flip
            eye_pulse = 0.7 + 0.3 * math.sin(pygame.time.get_ticks() * 0.015)
            eb = override_color or tuple(min(255, int(c * eye_pulse)) for c in C_MUTANT_EYE)
            pygame.draw.circle(surface, eb, (pos[0] + ex - 3, head_cy - 1), 2)
            pygame.draw.circle(surface, eb, (pos[0] + ex + 3, head_cy), 3)
            if not override_color:
                eg = pygame.Surface((24, 24), pygame.SRCALPHA)
                pygame.draw.circle(eg, (*C_MUTANT_EYE[:3], int(70 * eye_pulse)), (12, 12), 12)
                surface.blit(eg, (pos[0] + ex - 12, head_cy - 12))
        else:
            pygame.draw.ellipse(surface, (0, 0, 0, 60), (pos[0] - 12, pos[1] + 8, 24, 8))
            sw = math.sin(self.anim_frame) * 4
            body_color = override_color or (C_MONSTER_BODY if self.state != "stunned" else (100, 100, 110))
            head_color = override_color or (C_MONSTER_HEAD if self.state != "stunned" else (130, 130, 140))
            pygame.draw.ellipse(surface, body_color, (pos[0] - 10 + sw, pos[1] - 8, 20, 18))
            pygame.draw.circle(surface, head_color, (pos[0] + sw * 0.5, pos[1] - 12), 8)
            eye_x = pos[0] + (4 if self.facing_right else -4) + sw * 0.5
            pygame.draw.circle(surface, override_color or C_MONSTER_EYE, (eye_x, pos[1] - 13), 3)
            if self.state == "stunned" and not override_color:
                for i in range(3):
                    angle = pygame.time.get_ticks() * 0.01 + i * 2.094
                    stx = pos[0] + math.cos(angle) * 12
                    sty = pos[1] - 18 + math.sin(angle) * 6
                    pygame.draw.circle(surface, (255, 255, 100), (int(stx), int(sty)), 2)


# ==================== 渲染辅助函数 ====================
def draw_gun_station(surface, gs, cam_x, cam_y):
    if gs['taken']:
        return
    cx = gs['x'] - cam_x
    cy = gs['y'] - cam_y
    pulse = 0.5 + 0.5 * math.sin(pygame.time.get_ticks() * 0.005)
    glow_size = int(20 + pulse * 8)
    glow_alpha = int(50 + pulse * 40)
    glow_surf = pygame.Surface((glow_size * 2, glow_size * 2), pygame.SRCALPHA)
    pygame.draw.circle(glow_surf, (*C_ITEM_GUN[:3], glow_alpha), (glow_size, glow_size), glow_size)
    surface.blit(glow_surf, (int(cx) - glow_size, int(cy) - glow_size))
    pygame.draw.rect(surface, (60, 50, 40), (int(cx) - 10, int(cy) - 8, 20, 16), border_radius=3)
    pygame.draw.rect(surface, C_GUN_BARREL, (int(cx) - 8, int(cy) - 3, 16, 6))
    pygame.draw.rect(surface, C_GUN_GRIP, (int(cx) - 3, int(cy) + 2, 6, 6))
    for i in range(gs['ammo']):
        pygame.draw.circle(surface, C_AMMO_COLOR, (int(cx) - 6 + i * 6, int(cy) - 10), 2)


def draw_textured_wall(surface, wall_rect):
    x, y, w, h = wall_rect.x, wall_rect.y, wall_rect.w, wall_rect.h
    top_h = 8
    side_w = 4
    shadow_off = 5
    shadow_surf = pygame.Surface((w + shadow_off * 2, h + shadow_off * 2), pygame.SRCALPHA)
    pygame.draw.rect(shadow_surf, C_WALL_SHADOW, (shadow_off, shadow_off, w, h), border_radius=2)
    surface.blit(shadow_surf, (x - shadow_off + 3, y - shadow_off + 3))
    pygame.draw.rect(surface, C_WALL_SIDE, (x + w - side_w, y + top_h, side_w, h - top_h))
    pygame.draw.rect(surface, C_WALL_FACE, (x, y + top_h, w - side_w, h - top_h))
    for ty in range(y + top_h, y + h, TILE_SIZE):
        for tx in range(x, x + w - side_w, TILE_SIZE):
            clip_w = min(TILE_SIZE, x + w - side_w - tx)
            clip_h = min(TILE_SIZE, y + h - ty)
            if clip_w > 0 and clip_h > 0:
                surface.blit(_wall_noise_surf, (tx, ty), area=(0, 0, clip_w, clip_h))
    brick_h = 10
    row_idx = 0
    by = y + top_h + 2
    while by < y + h - 2:
        offset = brick_h if (row_idx % 2 == 1) else 0
        bx = x + 2 + offset
        while bx < x + w - side_w - 2:
            bw = min(brick_h * 2, x + w - side_w - 2 - bx)
            if bw > 4:
                bc = C_WALL_BRICK_LIGHT if (row_idx + bx // 20) % 3 == 0 else C_WALL_BRICK_DARK
                pygame.draw.rect(surface, bc, (bx, by, bw - 2, min(brick_h - 2, y + h - 2 - by)))
            bx += brick_h * 2
        by += brick_h
        row_idx += 1
    for my in range(y + top_h + brick_h, y + h - 2, brick_h):
        pygame.draw.line(surface, C_WALL_MORTAR, (x + 1, my), (x + w - side_w - 1, my), 1)
    pygame.draw.rect(surface, C_WALL_TOP, (x, y, w, top_h), border_radius=1)
    pygame.draw.line(surface, (120, 120, 140), (x + 1, y + 1), (x + w - 2, y + 1), 1)


def draw_compass(surface, player, key_items):
    uncollected_keys = [k for k in key_items if not k['collected']]
    if not uncollected_keys:
        txt = font_compass.render("ALL KEYS COLLECTED - FIND EXIT", True, C_ESCAPE_READY)
        surface.blit(txt, (SCREEN_WIDTH // 2 - txt.get_width() // 2, 8))
        return
    nearest = min(uncollected_keys, key=lambda t: math.hypot(t['x'] - player.x, t['y'] - player.y))
    angle = math.atan2(nearest['y'] - player.y, nearest['x'] - player.x)
    dist = int(math.hypot(nearest['x'] - player.x, nearest['y'] - player.y) / TILE_SIZE)
    cx, cy = SCREEN_WIDTH // 2, 22
    compass_surf = pygame.Surface((160, 36), pygame.SRCALPHA)
    pygame.draw.rect(compass_surf, C_COMPASS_BG, (0, 0, 160, 36), border_radius=8)
    surface.blit(compass_surf, (cx - 80, 4))
    needle_len = 14
    nx = cx + math.cos(angle) * needle_len
    ny = cy + math.sin(angle) * needle_len
    pygame.draw.line(surface, C_COMPASS_NEEDLE, (cx, cy), (int(nx), int(ny)), 3)
    pygame.draw.circle(surface, C_COMPASS_NEEDLE, (int(nx), int(ny)), 3)
    dist_txt = font_compass.render(f"KEY {dist}m", True, (200, 200, 210))
    surface.blit(dist_txt, (cx + 20, cy - 8))


def draw_note_popup(surface, note_text):
    popup_w, popup_h = 420, 180
    px = SCREEN_WIDTH // 2 - popup_w // 2
    py = SCREEN_HEIGHT // 2 - popup_h // 2
    popup = pygame.Surface((popup_w, popup_h), pygame.SRCALPHA)
    popup.fill((20, 18, 15, 230))
    pygame.draw.rect(popup, C_NOTE_PAPER, (0, 0, popup_w, popup_h), border_radius=6)
    pygame.draw.rect(popup, (80, 70, 50), (0, 0, popup_w, popup_h), 3, border_radius=6)
    surface.blit(popup, (px, py))
    title = font_cd.render("RESEARCHER NOTE", True, (60, 40, 20))
    surface.blit(title, (px + 15, py + 10))
    lines = note_text.split('\n')
    for i, line in enumerate(lines):
        rendered = font_note.render(line, True, C_NOTE_TEXT)
        surface.blit(rendered, (px + 20, py + 40 + i * 24))
    hint = font_mini.render("[E] Close", True, (100, 80, 50))
    surface.blit(hint, (px + popup_w - hint.get_width() - 15, py + popup_h - 25))


# ==================== 地图生成 ====================
def generate_map():
    grid = [['O' for _ in range(MAP_COLS)] for _ in range(MAP_ROWS)]
    for x in range(MAP_COLS):
        grid[0][x] = '1'
        grid[MAP_ROWS - 1][x] = '1'
    for y in range(MAP_ROWS):
        grid[y][0] = '1'
        grid[y][MAP_COLS - 1] = '1'

    buildings = [
        {'x': 3, 'y': 3, 'w': 10, 'h': 8, 'type': '.', 'ds': 'right'},
        {'x': 20, 'y': 2, 'w': 12, 'h': 9, 'type': ',', 'ds': 'bottom'},
        {'x': 42, 'y': 3, 'w': 10, 'h': 8, 'type': '~', 'ds': 'left'},
        {'x': 3, 'y': 18, 'w': 9, 'h': 8, 'type': '.', 'ds': 'right'},
        {'x': 22, 'y': 18, 'w': 14, 'h': 10, 'type': ',', 'ds': 'top'},
        {'x': 44, 'y': 18, 'w': 10, 'h': 8, 'type': '~', 'ds': 'left'},
        {'x': 3, 'y': 33, 'w': 10, 'h': 8, 'type': '.', 'ds': 'right'},
        {'x': 20, 'y': 34, 'w': 12, 'h': 8, 'type': ',', 'ds': 'top'},
        {'x': 42, 'y': 33, 'w': 10, 'h': 8, 'type': '~', 'ds': 'left'},
    ]
    furniture_positions = []
    room_floor_tiles = []

    for b in buildings:
        bx, by, bw, bh = b['x'], b['y'], b['w'], b['h']
        for x in range(bx, bx + bw):
            grid[by][x] = '1'
            grid[by + bh - 1][x] = '1'
        for y in range(by, by + bh):
            grid[y][bx] = '1'
            grid[y][bx + bw - 1] = '1'
        for y in range(by + 1, by + bh - 1):
            for x in range(bx + 1, bx + bw - 1):
                grid[y][x] = b['type']
                room_floor_tiles.append((x, y))
        ds = b['ds']
        if ds == 'right':
            grid[by + bh // 2][bx + bw - 1] = '0'
        elif ds == 'left':
            grid[by + bh // 2][bx] = '0'
        elif ds == 'top':
            grid[by][bx + bw // 2] = '0'
        elif ds == 'bottom':
            grid[by + bh - 1][bx + bw // 2] = '0'
        num_f = random.randint(3, 5)
        cands = [(x, y) for y in range(by + 1, by + bh - 1)
                 for x in range(bx + 1, bx + bw - 1)]
        for fx, fy in random.sample(cands, min(num_f, len(cands))):
            furniture_positions.append((fx * TILE_SIZE, fy * TILE_SIZE))

    gates_data = [
        {'gx': 15, 'gy': 6, 'sx': 13, 'sy': 6},
        {'gx': 36, 'gy': 6, 'sx': 38, 'sy': 6},
        {'gx': 28, 'gy': 13, 'sx': 28, 'sy': 11},
        {'gx': 14, 'gy': 22, 'sx': 12, 'sy': 22},
        {'gx': 38, 'gy': 22, 'sx': 40, 'sy': 22},
        {'gx': 28, 'gy': 30, 'sx': 28, 'sy': 32},
        {'gx': 15, 'gy': 37, 'sx': 13, 'sy': 37},
        {'gx': 36, 'gy': 37, 'sx': 38, 'sy': 37},
    ]
    gate_objects = []
    for g in gates_data:
        grid[g['gy']][g['gx']] = 'G'
        grid[g['sy']][g['sx']] = 'S'
        gate_objects.append({
            'gate_rect': pygame.Rect(g['gx'] * TILE_SIZE, g['gy'] * TILE_SIZE, TILE_SIZE, TILE_SIZE),
            'switch_rect': pygame.Rect(g['sx'] * TILE_SIZE, g['sy'] * TILE_SIZE, TILE_SIZE, TILE_SIZE),
            'open': False
        })

    grid[5][5] = 'P'
    grid[MAP_ROWS - 2][MAP_COLS // 2] = 'D'

    monster_positions = []
    outdoor_tiles = [(x, y) for y in range(1, MAP_ROWS - 1)
                     for x in range(1, MAP_COLS - 1) if grid[y][x] == 'O']

    gun_stations = []
    available_outdoor = list(outdoor_tiles)
    random.shuffle(available_outdoor)
    chosen = []
    for tx, ty in available_outdoor:
        wx = tx * TILE_SIZE + TILE_SIZE // 2
        wy = ty * TILE_SIZE + TILE_SIZE // 2
        dist_to_start = math.hypot(wx - 5 * TILE_SIZE, wy - 5 * TILE_SIZE)
        too_close = any(math.hypot(wx - cx, wy - cy) < 400 for cx, cy in chosen)
        if dist_to_start > 300 and not too_close:
            chosen.append((wx, wy))
            gun_stations.append({
                'x': wx, 'y': wy,
                'rect': pygame.Rect(wx - 12, wy - 12, 24, 24),
                'ammo': GUN_MAG_SIZE, 'taken': False
            })
            if len(chosen) >= GUN_STATIONS_COUNT:
                break

    for mx, my in random.sample(outdoor_tiles, min(12, len(outdoor_tiles))):
        monster_positions.append((mx * TILE_SIZE + TILE_SIZE // 2,
                                  my * TILE_SIZE + TILE_SIZE // 2))

    note_positions = []
    all_floor_tiles = [(x, y) for y in range(1, MAP_ROWS - 1)
                       for x in range(1, MAP_COLS - 1) if grid[y][x] != '1']
    random.shuffle(all_floor_tiles)
    for i, (nx, ny) in enumerate(all_floor_tiles[:NOTE_COUNT]):
        note_positions.append({
            'x': nx * TILE_SIZE + TILE_SIZE // 2,
            'y': ny * TILE_SIZE + TILE_SIZE // 2,
            'text': RESEARCHER_NOTES[i % len(RESEARCHER_NOTES)],
            'read': False
        })

    key_tiles = random.sample(room_floor_tiles, min(TOTAL_KEYS, len(room_floor_tiles)))
    key_items = []
    for kx, ky in key_tiles:
        wx = kx * TILE_SIZE + TILE_SIZE // 2
        wy = ky * TILE_SIZE + TILE_SIZE // 2
        key_items.append({'x': wx, 'y': wy, 'collected': False})

    return grid, furniture_positions, gate_objects, monster_positions, gun_stations, note_positions, key_items


# ==================== 开场动画 ====================
class IntroAnimation:
    def __init__(self):
        self.frame = 0
        self.snow = SnowSystem(SNOW_COUNT_GAME)
        self.spotlight_x = -200
        self.spotlight_y = SCREEN_HEIGHT // 2
        self.spotlight_angle = 0.3
        self.finished = False

    def run(self):
        while not self.finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE, pygame.K_ESCAPE):
                        self.finished = True
                        return True
            self.frame += 1
            if self.frame >= INTRO_TOTAL_FRAMES:
                self.finished = True
                return True
            progress = self.frame / INTRO_TOTAL_FRAMES
            self.spotlight_x = int(-200 + progress * (SCREEN_WIDTH + 400))
            self.spotlight_y = SCREEN_HEIGHT // 2 + int(math.sin(self.frame * 0.05) * 30)
            self.spotlight_angle = 0.3 + math.sin(self.frame * 0.03) * 0.1
            screen.fill((2, 2, 5))
            self.snow.update_and_draw(screen)
            spot_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            cone_len, half_angle = 500, 0.25
            points = [(self.spotlight_x, self.spotlight_y)]
            for i in range(20):
                a_val = self.spotlight_angle - half_angle + (2 * half_angle) * (i / 19)
                points.append((
                    self.spotlight_x + int(math.cos(a_val) * cone_len),
                    self.spotlight_y + int(math.sin(a_val) * cone_len)
                ))
            for layer in range(8, 0, -1):
                alpha_val = int(40 * (layer / 8))
                scale = layer / 8
                cx, cy = self.spotlight_x, self.spotlight_y
                scaled_points = [
                    (cx + (px - cx) * scale, cy + (py - cy) * scale)
                    for px, py in points
                ]
                pygame.draw.polygon(spot_surf, (255, 255, 240, alpha_val), scaled_points)
            screen.blit(spot_surf, (0, 0))
            hx, hy = self.spotlight_x, self.spotlight_y - 20
            pygame.draw.ellipse(screen, (10, 10, 15), (hx - 25, hy - 10, 50, 20))
            pygame.draw.line(screen, (10, 10, 15), (hx - 35, hy - 12), (hx + 35, hy - 12), 3)
            pygame.draw.line(screen, (10, 10, 15), (hx + 20, hy), (hx + 50, hy + 5), 2)
            for idx, (start_frame, text) in enumerate(INTRO_RADIO_LINES):
                if self.frame >= start_frame:
                    char_count = min(len(text), (self.frame - start_frame) // 2)
                    visible_text = text[:char_count]
                    if random.random() < 0.05:
                        visible_text = ''.join(
                            c if random.random() > 0.3 else random.choice('#@!&%')
                            for c in visible_text
                        )
                    rendered = font_radio.render(visible_text, True, (180, 220, 180))
                    ty = SCREEN_HEIGHT - 120 + idx * 32
                    screen.blit(rendered, (60, ty))
            scanline = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            for sy in range(0, SCREEN_HEIGHT, 3):
                pygame.draw.line(scanline, (0, 0, 0, 40), (0, sy), (SCREEN_WIDTH, sy), 1)
            screen.blit(scanline, (0, 0))
            if self.frame > 60:
                skip = font_mini.render("[ENTER / SPACE] Skip", True, (100, 100, 120))
                screen.blit(skip, (SCREEN_WIDTH - skip.get_width() - 20, SCREEN_HEIGHT - 30))
            pygame.display.flip()
        return True


# ==================== ★ 主游戏循环（含金币逃离条件） ====================
def game_loop():
    grid, furniture_pos, gates, monster_pos, gun_stations, note_data, key_items = generate_map()
    walls = []
    wall_rects = []
    for y in range(MAP_ROWS):
        for x in range(MAP_COLS):
            if grid[y][x] == '1':
                r = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                walls.append(r)
                wall_rects.append(r)

    furniture_list = []
    for x, y in furniture_pos:
        f = Furniture(x, y)
        if random.random() < COIN_LOOT_CHANCE:
            f.has_coins = True
            f.coin_amount = random.randint(*COINS_PER_LOOT)
        furniture_list.append(f)

    switches = [GateSwitch(g) for g in gates]
    monsters = [Monster(x, y) for x, y in monster_pos]
    notes = [ResearcherNote(nd) for nd in note_data]
    blood_system = BloodTrailSystem()
    bullet_trail = BulletTrail()
    loot_popups = []
    snow = SnowSystem(SNOW_COUNT_GAME)
    weather = WeatherSystem()

    intro = IntroAnimation()
    if not intro.run():
        return False
    menu = MainMenu()
    if not menu.run():
        return False

    synth_audio.start_bgm()

    player_start = None
    door_rect = None
    for y in range(MAP_ROWS):
        for x in range(MAP_COLS):
            if grid[y][x] == 'P':
                player_start = (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2)
            elif grid[y][x] == 'D':
                door_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    player = Player(*player_start)
    camera_x, camera_y = 0, 0
    mouse_x, mouse_y = 0, 0
    running = True
    game_over = False
    victory = False
    reading_note = None

    while running:
        clock.tick(FPS)
        weather.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            if event.type == pygame.KEYDOWN:
                if game_over or victory:
                    if event.key == pygame.K_r:
                        return True
                    if event.key == pygame.K_ESCAPE:
                        return False
                    continue
                if reading_note is not None:
                    if event.key in (pygame.K_e, pygame.K_ESCAPE, pygame.K_RETURN):
                        reading_note = None
                    continue
                if event.key == pygame.K_SPACE:
                    player.try_flash()
                if event.key == pygame.K_f:
                    if player.try_fire():
                        synth_audio.play_shoot()
                        aim_angle = math.atan2(mouse_y + camera_y - player.y, mouse_x + camera_x - player.x)
                        muzzle_x = player.x + math.cos(aim_angle) * 28
                        muzzle_y = player.y + math.sin(aim_angle) * 28
                        end_x = player.x + math.cos(aim_angle) * GUN_RANGE
                        end_y = player.y + math.sin(aim_angle) * GUN_RANGE
                        bullet_trail.add_trail(muzzle_x, muzzle_y, end_x, end_y)
                if event.key == pygame.K_e:
                    interactable = player.get_nearby_interactable(
                        furniture_list, switches, gun_stations, notes
                    )
                    if interactable:
                        kind, obj = interactable
                        if kind == 'note':
                            obj.read = True
                            reading_note = obj.text
                        elif kind == 'furniture':
                            if not player.searching:
                                player.searching = True
                                player.search_target = obj
                        elif kind == 'switch':
                            obj.activate()
                        elif kind == 'gun_station':
                            player.equip_gun(obj)
                if event.key == pygame.K_ESCAPE:
                    return False

        # ★ 结算画面：区分金币逃离与钥匙逃离
        if game_over or victory:
            screen.fill(C_BG)
            if victory:
                if player.coins_collected >= ESCAPE_COIN_THRESHOLD:
                    msg = "RICH ESCAPE!"
                    color = C_COIN_GOLD
                else:
                    msg = "MISSION COMPLETE"
                    color = C_ESCAPE_READY
            else:
                msg = "YOU DIED"
                color = (250, 55, 35)
            txt = font_large.render(msg, True, color)
            screen.blit(txt, (SCREEN_WIDTH // 2 - txt.get_width() // 2, SCREEN_HEIGHT // 2 - 60))
            hint = font_small.render("[R] Restart  |  [ESC] Menu", True, (150, 150, 160))
            screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, SCREEN_HEIGHT // 2 + 30))
            pygame.display.flip()
            continue

        if reading_note is None:
            keys_pressed = pygame.key.get_pressed()
            dx = dy = 0
            if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
                dy = -1
            if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
                dy = 1
            if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
                dx = -1
            if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                dx = 1
            if dx != 0 and dy != 0:
                inv = 1 / math.sqrt(2)
                dx *= inv
                dy *= inv

            speed_mult = weather.get_speed_multiplier()
            player.move(dx, dy, walls, furniture_list, gates, speed_mult)
            player.update_timers()
            player.update_tile_type(grid)

            if player.searching and player.search_target:
                player.search_target.search_progress += 1
                if player.search_target.search_progress >= player.search_target.search_time:
                    target = player.search_target
                    target.searched = True
                    player.searching = False
                    player.search_target = None

                    if target.has_coins:
                        player.coins_collected += target.coin_amount
                        synth_audio.play_coin()
                        loot_popups.append(LootPopup(
                            target.rect.centerx, target.rect.top,
                            target.coin_amount
                        ))

                    if random.random() < SCARE_CHANCE:
                        player.trigger_scare()

            for m in monsters:
                m.update(player, walls, furniture_list, gates, blood_system)
                if m.alive and m.state != "stunned":
                    dist = math.hypot(player.x - m.x, player.y - m.y)
                    if dist < m.radius + 12:
                        if player.take_damage() and player.hp <= 0:
                            game_over = True

            blood_system.update()
            bullet_trail.update()

            for popup in loot_popups:
                popup.update()
            loot_popups = [p for p in loot_popups if p.life > 0]

            world_mouse_x = mouse_x + camera_x
            world_mouse_y = mouse_y + camera_y
            aim_angle = math.atan2(world_mouse_y - player.y, world_mouse_x - player.x)

            if player.flash_visual_timer > 0:
                for m in monsters:
                    if m.alive:
                        dist = math.hypot(m.x - player.x, m.y - player.y)
                        if dist < FLASH_RANGE:
                            angle_to = math.atan2(m.y - player.y, m.x - player.x)
                            diff = abs(math.atan2(
                                math.sin(angle_to - aim_angle),
                                math.cos(angle_to - aim_angle)
                            ))
                            if diff < FLASHLIGHT_CONE_HALF_ANGLE:
                                m.receive_flash(blood_system)

            if player.has_gun and player.gun_muzzle_timer == 5:
                best_target = None
                best_dist = GUN_RANGE
                for m in monsters:
                    if m.alive:
                        dist = math.hypot(m.x - player.x, m.y - player.y)
                        if dist < GUN_RANGE:
                            angle_to = math.atan2(m.y - player.y, m.x - player.x)
                            diff = abs(math.atan2(
                                math.sin(angle_to - aim_angle),
                                math.cos(angle_to - aim_angle)
                            ))
                            if diff < GUN_AIM_CONE_HALF_ANGLE and dist < best_dist:
                                best_target = m
                                best_dist = dist
                if best_target:
                    best_target.receive_bullet(blood_system)
                    for m in monsters:
                        m.apply_alert()

            for ki in key_items:
                if not ki['collected']:
                    if math.hypot(player.x - ki['x'], player.y - ki['y']) < 25:
                        ki['collected'] = True
                        player.keys_collected += 1
                        synth_audio.play_coin()

            # ★ 核心修改：双胜利条件判定
            coin_escape = player.coins_collected >= ESCAPE_COIN_THRESHOLD
            key_escape = False
            if player.keys_collected >= TOTAL_KEYS and door_rect:
                pr = pygame.Rect(player.x - 15, player.y - 15, 30, 30)
                if pr.colliderect(door_rect):
                    key_escape = True

            if coin_escape or key_escape:
                victory = True

        camera_x = max(0, min(player.x - SCREEN_WIDTH // 2, MAP_COLS * TILE_SIZE - SCREEN_WIDTH))
        camera_y = max(0, min(player.y - SCREEN_HEIGHT // 2, MAP_ROWS * TILE_SIZE - SCREEN_HEIGHT))

        shake_x = shake_y = 0
        if player.scare_timer > 0:
            intensity = SCARE_SHAKE_INTENSITY * (player.scare_timer / SCARE_DURATION)
            shake_x = random.uniform(-intensity, intensity)
            shake_y = random.uniform(-intensity, intensity)

        render_x = camera_x + shake_x
        render_y = camera_y + shake_y

        screen.fill(C_BG)
        snow.update_and_draw(screen)

        visible_cols = SCREEN_WIDTH // TILE_SIZE + 2
        visible_rows = SCREEN_HEIGHT // TILE_SIZE + 2
        start_col = max(0, int(render_x // TILE_SIZE))
        end_col = min(MAP_COLS, start_col + visible_cols)
        start_row = max(0, int(render_y // TILE_SIZE))
        end_row = min(MAP_ROWS, start_row + visible_rows)

        for y in range(start_row, end_row):
            for x in range(start_col, end_col):
                tile = grid[y][x]
                if tile in ROOM_COLORS:
                    pygame.draw.rect(screen, ROOM_COLORS[tile],
                                     (x * TILE_SIZE - render_x, y * TILE_SIZE - render_y,
                                      TILE_SIZE, TILE_SIZE))

        for wr in wall_rects:
            if (wr.right > render_x and wr.left < render_x + SCREEN_WIDTH and
                    wr.bottom > render_y and wr.top < render_y + SCREEN_HEIGHT):
                draw_textured_wall(screen, wr.move(-render_x, -render_y))

        for f in furniture_list:
            if (f.rect.right > render_x and f.rect.left < render_x + SCREEN_WIDTH and
                    f.rect.bottom > render_y and f.rect.top < render_y + SCREEN_HEIGHT):
                f.draw(screen, render_x, render_y)

        for g in gates:
            gr = g['gate_rect']
            if gr.right > render_x and gr.left < render_x + SCREEN_WIDTH:
                color = C_GATE_OPEN if g['open'] else C_GATE_CLOSED
                pygame.draw.rect(screen, color, gr.move(-render_x, -render_y))
                if not g['open']:
                    pygame.draw.line(screen, (200, 50, 50),
                                     (gr.x - render_x + 5, gr.y - render_y + 5),
                                     (gr.right - render_x - 5, gr.bottom - render_y - 5), 2)

        for sw in switches:
            if sw.rect.right > render_x and sw.rect.left < render_x + SCREEN_WIDTH:
                sw.draw(screen, render_x, render_y)

        for gs in gun_stations:
            draw_gun_station(screen, gs, render_x, render_y)

        for n in notes:
            nr = pygame.Rect(n.x - 15 - render_x, n.y - 15 - render_y, 30, 30)
            if nr.right > 0 and nr.left < SCREEN_WIDTH and nr.bottom > 0 and nr.top < SCREEN_HEIGHT:
                n.draw(screen, render_x, render_y)

        for ki in key_items:
            if not ki['collected']:
                kx = ki['x'] - render_x
                ky = ki['y'] - render_y
                if 0 < kx < SCREEN_WIDTH and 0 < ky < SCREEN_HEIGHT:
                    pulse = 0.5 + 0.5 * math.sin(pygame.time.get_ticks() * 0.006)
                    glow = pygame.Surface((30, 30), pygame.SRCALPHA)
                    pygame.draw.circle(glow, (*C_ITEM_GLOW[:3], int(C_ITEM_GLOW[3] * pulse)), (15, 15), 15)
                    screen.blit(glow, (int(kx) - 15, int(ky) - 15))
                    pygame.draw.circle(screen, (255, 215, 0), (int(kx), int(ky)), 5)
                    pygame.draw.rect(screen, (200, 170, 0), (int(kx) - 2, int(ky) - 8, 4, 6))

        if door_rect:
            dr = door_rect.move(-render_x, -render_y)
            locked = player.keys_collected < TOTAL_KEYS
            color = C_DOOR_LOCKED if locked else C_DOOR_OPEN
            pygame.draw.rect(screen, color, dr)
            if locked:
                pygame.draw.circle(screen, (200, 200, 50), (dr.centerx, dr.centery), 4)
            else:
                pygame.draw.line(screen, (100, 255, 100), (dr.x + 5, dr.y + 5),
                                 (dr.right - 5, dr.bottom - 5), 2)

        blood_system.draw(screen, render_x, render_y)
        bullet_trail.draw(screen, render_x, render_y)

        for m in monsters:
            if m.alive:
                mx = m.x - render_x
                my = m.y - render_y
                if -30 < mx < SCREEN_WIDTH + 30 and -30 < my < SCREEN_HEIGHT + 30:
                    m.draw(screen, render_x, render_y)

        player.draw(screen, render_x, render_y)

        for popup in loot_popups:
            popup.draw(screen, render_x, render_y)

        if player.flash_visual_timer > 0:
            flash_alpha = int(200 * (player.flash_visual_timer / FLASH_VISUAL_DURATION))
            flash_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            flash_surf.fill((255, 255, 240, flash_alpha))
            screen.blit(flash_surf, (0, 0))

        if player.scare_timer > 0:
            scare_alpha = int(120 * (player.scare_timer / SCARE_DURATION))
            scare_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            scare_surf.fill((180, 20, 20, scare_alpha))
            screen.blit(scare_surf, (0, 0))

        if player.hp <= 1 and player.hp > 0:
            hb_pulse = 0.5 + 0.5 * math.sin(pygame.time.get_ticks() * 0.008)
            hb_alpha = int(60 * hb_pulse)
            hb_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            pygame.draw.rect(hb_surf, (180, 20, 20, hb_alpha), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 8)
            screen.blit(hb_surf, (0, 0))

        weather.draw_overlay(screen)

        vis = weather.get_visibility()
        if vis < 1.0:
            dim = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            dim.fill((0, 0, 0, int(120 * (1.0 - vis))))
            screen.blit(dim, (0, 0))

        hp_text = font_hp.render(f"HP: {'♥' * player.hp}{'♡' * (PLAYER_MAX_HP - player.hp)}", True, (250, 80, 80))
        screen.blit(hp_text, (20, 20))
        key_text = font_hp.render(f"KEYS: {player.keys_collected}/{TOTAL_KEYS}", True, (250, 215, 0))
        screen.blit(key_text, (20, 50))

        # ★ HUD金币显示：达标时变绿高亮
        if player.coins_collected >= ESCAPE_COIN_THRESHOLD:
            coin_color = C_ESCAPE_READY
            coin_label = f"COINS: {player.coins_collected}/{ESCAPE_COIN_THRESHOLD} ESCAPE READY"
        else:
            coin_color = C_COIN_GOLD
            coin_label = f"COINS: {player.coins_collected}/{ESCAPE_COIN_THRESHOLD}"
        coin_text = font_hp.render(coin_label, True, coin_color)
        screen.blit(coin_text, (20, 80))

        cd_ratio = max(0, player.flash_cd_timer / FLASH_COOLDOWN_FRAMES)
        cd_color = C_FLASH_CD_COOLDOWN if cd_ratio > 0 else C_FLASH_CD_READY
        cd_bar_w = 120
        pygame.draw.rect(screen, (30, 30, 40), (20, 110, cd_bar_w, 12), border_radius=3)
        pygame.draw.rect(screen, cd_color, (20, 110, int(cd_bar_w * (1 - cd_ratio)), 12), border_radius=3)
        cd_label = font_cd.render("FLASH", True, (180, 180, 190))
        screen.blit(cd_label, (20 + cd_bar_w + 8, 108))

        if player.has_gun:
            ammo_text = font_cd.render(f"FLARE GUN: {player.gun_ammo}/3", True, C_AMMO_COLOR)
            screen.blit(ammo_text, (20, 130))
            gun_cd_ratio = max(0, player.gun_fire_cd / GUN_FIRE_CD)
            if gun_cd_ratio > 0:
                gcd_w = 100
                pygame.draw.rect(screen, (30, 30, 40), (20, 152, gcd_w, 8), border_radius=2)
                pygame.draw.rect(screen, (200, 150, 50),
                                 (20, 152, int(gcd_w * (1 - gun_cd_ratio)), 8), border_radius=2)

        draw_compass(screen, player, key_items)

        if weather.blizzard_active:
            warn = font_mini.render("BLIZZARD", True, (200, 200, 250))
            screen.blit(warn, (SCREEN_WIDTH // 2 - warn.get_width() // 2, 44))

        interactable = player.get_nearby_interactable(furniture_list, switches, gun_stations, notes)
        if interactable and not game_over and not victory and reading_note is None:
            kind, obj = interactable
            if kind == 'note':
                label = "[E] Read Note"
            elif kind == 'furniture':
                label = "[E] Search Crate"
            elif kind == 'switch':
                label = "[E] Activate Switch"
            elif kind == 'gun_station':
                label = f"[E] Equip Flare Gun ({obj['ammo']} rounds)"
            else:
                label = ""
            if label:
                lbl = font_hint.render(label, True, (255, 255, 200))
                screen.blit(lbl, (SCREEN_WIDTH // 2 - lbl.get_width() // 2, SCREEN_HEIGHT - 60))

        if player.searching and player.search_target:
            prog = player.search_target.search_progress / player.search_target.search_time
            bar_w = 100
            bx = SCREEN_WIDTH // 2 - bar_w // 2
            by = SCREEN_HEIGHT // 2 + 30
            pygame.draw.rect(screen, (30, 30, 40), (bx, by, bar_w, 10), border_radius=3)
            pygame.draw.rect(screen, (100, 200, 100), (bx, by, int(bar_w * prog), 10), border_radius=3)
            st = font_mini.render("SEARCHING...", True, (200, 200, 210))
            screen.blit(st, (SCREEN_WIDTH // 2 - st.get_width() // 2, by - 18))

        mm_size = 140
        mm_surf = pygame.Surface((mm_size, mm_size), pygame.SRCALPHA)
        mm_surf.fill(C_MINIMAP_BG)
        scale = mm_size / max(MAP_COLS, MAP_ROWS)
        for wr in wall_rects:
            mx = int(wr.x / TILE_SIZE * scale)
            my = int(wr.y / TILE_SIZE * scale)
            ms = max(1, int(scale))
            pygame.draw.rect(mm_surf, C_MINIMAP_WALL, (mx, my, ms, ms))
        for g in gates:
            if not g['open']:
                gx = int(g['gate_rect'].x / TILE_SIZE * scale)
                gy = int(g['gate_rect'].y / TILE_SIZE * scale)
                pygame.draw.rect(mm_surf, C_MINIMAP_GATE,
                                 (gx, gy, max(2, int(scale * 1.5)), max(2, int(scale * 1.5))))
        px_mm = int(player.x / TILE_SIZE * scale)
        py_mm = int(player.y / TILE_SIZE * scale)
        pygame.draw.circle(mm_surf, C_MINIMAP_PLAYER, (px_mm, py_mm), 3)
        for m in monsters:
            if m.alive:
                ex = int(m.x / TILE_SIZE * scale)
                ey = int(m.y / TILE_SIZE * scale)
                pygame.draw.circle(mm_surf, C_MINIMAP_ENEMY, (ex, ey), 2)
        screen.blit(mm_surf, (SCREEN_WIDTH - mm_size - 15, 15))
        pygame.draw.rect(screen, (80, 80, 100), (SCREEN_WIDTH - mm_size - 15, 15, mm_size, mm_size), 2)

        if reading_note is not None:
            draw_note_popup(screen, reading_note)

        pygame.display.flip()

    return False


# ==================== 入口 ====================
if __name__ == "__main__":
    while True:
        result = game_loop()
        if not result:
            break
    pygame.quit()
    sys.exit()