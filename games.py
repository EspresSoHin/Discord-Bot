import random
#bubblewrap, gems games, raffles...

async def start_games(message):

    content = message.content.lower()

    if message.content.lower().startswith("bubblewrap!"):
            bubbles = ["||pffft||", "||POP||"]
            secret_bubble1 = "||♡♡♡||"
            secret_bubble2 = "||CAW||"

            grid = [[random.choice(bubbles) for _ in range(10)] for _ in range(16)]

    
            row_caw, col_caw = random.randint(0, 15), random.randint(0, 9)
            row_heart, col_heart = random.randint(0, 15), random.randint(0, 9)

   
            while (row_caw, col_caw) == (row_heart, col_heart):
                row_heart, col_heart = random.randint(0, 15), random.randint(0, 9)

   
            grid[row_caw][col_caw] = secret_bubble2
            grid[row_heart][col_heart] = secret_bubble1

    
            bubble_wrap = "\n".join(" ".join(row) for row in grid)

            await message.channel.send(bubble_wrap)