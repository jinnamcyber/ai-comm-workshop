# Codex image jobs for the workshop tools. run_all.py draws each into raw/<name>.png
STYLE = ("Style: premium children's picture-book illustration, soft gouache with subtle coloured-pencil texture, "
         "warm friendly palette (cream, soft sky blue, leaf green, coral pink, sunny yellow), clean rounded shapes, "
         "gentle soft lighting, polished and professional. Absolutely no text, no letters, no numbers, no signage words, no watermark, no border.")
CUTOUT = ("Single subject centred, full body visible with generous margin, on a plain pure white (#FFFFFF) background, "
          "no ground shadow, no background scenery. ")
SCENE = "Wide landscape composition (3:2). "
KIDS = "Children are East Asian primary-school kids from Macau, cheerful, simple clothes. "

JOBS = {
  # presentation
  "deck_hero": SCENE + "A friendly young teacher sitting at a classroom desk, chatting happily with a small cute round robot assistant on the desk; a laptop shows a colourful learning game; warm classroom with plants and a whiteboard. Mood: clever, warm, inviting.",
  "deck_blind": SCENE + "Two teachers sitting back to back on chairs: one holds a card and describes it with expressive hands, the other draws on a sketchpad with a puzzled-but-amused face. Playful, communication theme, simple cream background.",
  # 01 plant
  "01_garden": SCENE + "Garden background for an educational plant diagram: soft sky with a few clouds in the top 60%, a gentle grass line, and the bottom 30% is a clean cross-section of brown soil with small pebbles and roots of distant grass. IMPORTANT: leave the centre of the picture completely empty (no plants, no flowers, no trees in the middle third) because a plant will be drawn there.",
  # 02 read aloud
  "02_reader": CUTOUT + KIDS + "A girl reading aloud proudly from an open book, a little yellow chick standing next to her cheering, small musical/sound wave marks near her mouth.",
  # 03 weather (same street, different weather, no people)
  "03_sunny": SCENE + "A cosy small neighbourhood corner in Macau: pastel colonial-style low building, a tree, a bench, a lamp post, Portuguese wave-pattern pavement. Bright sunny day, blue sky, sun top-right. No people.",
  "03_rainy": SCENE + "Same cosy Macau neighbourhood corner (pastel colonial low building, tree, bench, lamp post, wave-pattern pavement), but a rainy day: grey clouds, puddles, wet reflections. No people.",
  "03_cold": SCENE + "Same cosy Macau neighbourhood corner (pastel colonial low building, tree, bench, lamp post, wave-pattern pavement), a very cold winter day: pale sky, cold wind lines, bare tree, frosty light. No people.",
  "03_hot": SCENE + "Same cosy Macau neighbourhood corner (pastel colonial low building, tree, bench, lamp post, wave-pattern pavement), a very hot summer day: blazing sun, heat shimmer, bright light. No people.",
  "03_windy": SCENE + "Same cosy Macau neighbourhood corner (pastel colonial low building, tree, bench, lamp post, wave-pattern pavement), a very windy day: tree bending, leaves flying, clouds streaking. No people.",
  # 04 times-table actions
  "04_raise": CUTOUT + KIDS + "A child in PE clothes stretching both arms straight up high above the head, big smile, energetic.",
  "04_squat": CUTOUT + KIDS + "A child in PE clothes squatting down low with hands on knees, big smile.",
  "04_jump": CUTOUT + KIDS + "A child in PE clothes jumping in the air on the spot, feet off the ground, joyful.",
  # 05 music animals
  "05_bird": CUTOUT + "A small cute bluebird singing with its beak open, wings slightly raised.",
  "05_elephant": CUTOUT + "A big gentle cute grey elephant raising its trunk and trumpeting.",
  "05_rabbit": CUTOUT + "A cute white rabbit running fast mid-hop, speed feeling.",
  "05_tortoise": CUTOUT + "A cute green tortoise walking very slowly, calm sleepy smile.",
  "05_lion": CUTOUT + "A cute friendly lion roaring loudly with mouth wide open, mane flowing.",
  "05_mouse": CUTOUT + "A tiny cute grey mouse whispering quietly with a paw near its mouth, shy.",
  # 06 tenses
  "06_sam": SCENE + KIDS + "A boy (Sam) in his bright bedroom-study: a big wall calendar, a clock, a football, a school bag, a guitar and a plant; he is busy writing in a notebook at his desk. Cheerful busy-week feeling.",
  # 07 water cycle backgrounds (no characters)
  "07_sea": SCENE + "Calm sparkling blue sea under a warm sun in the upper-right, soft sky, a distant green island. No characters. Leave the middle area calm and open.",
  "07_sky": SCENE + "High in the sky above the sea: soft blue sky, fluffy white clouds forming, the sea far below, gentle sunlight. No characters.",
  "07_rain": SCENE + "Grey-blue rain clouds over green hills, rain falling softly onto the hills and a small village. No characters.",
  "07_river": SCENE + "Green mountains on the left, a winding river flowing down through fields into the blue sea on the right. No characters.",
  # 08 reading
  "08_garden": SCENE + KIDS + "A kind grandmother and her grandchild in a small sunny vegetable garden on a rooftop in Macau: tomatoes, green vegetables, a watering can, warm afternoon light.",
  "08_owl": CUTOUT + "A wise friendly owl teacher wearing round glasses, holding a small book, one wing raised as if asking a question.",
  # 09 Portuguese scenes (backgrounds; characters are drawn separately)
  "09_pastelaria": SCENE + "Interior of a cosy Portuguese pastry shop (pastelaria): glass counter with pastéis de nata, croissants, coffee machine, azulejo blue-and-white tiles on the wall. No people. Keep the lower-middle area of the floor clear.",
  "09_escola": SCENE + "A bright school corridor/courtyard in Macau with lockers, a notice board (no readable text), plants and windows. No people. Keep the lower-middle area clear.",
  "09_rua": SCENE + "A charming Macau street with Portuguese colonial buildings in pastel colours, black-and-white wave-pattern calçada pavement, a street sign post without readable text, trees. No people. Keep the lower-middle area clear.",
}

def style_for(name):
    return STYLE
