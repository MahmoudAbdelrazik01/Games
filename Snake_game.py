import random
import curses
# هنا انا بظهر الشاشة
screen = curses.initscr()
#هنا شلت الماوس من الشاشة
curses.curs_set(0)
#هنا بحدد مساحة اللعب بتاعت اللاعب 
screen_height , screen_width = screen.getmax()
Window = curses.newin(screen_height , screen_width , 0 , 0)
#عاوز اخلي الكمب يتقبل مني مدخلات اسهم
Window.keypad(1)
Window.timeout (100)
#هبدا احدد شكل الثعبان ومكان ظهوره وحركته الافتراضية
snake_x = screen_width // 4
snake_y = screen_height // 3
snake = [
    [snake_x , snake_y], #head
    [snake_x , snake_y-1], #body
    [snake_x , snake_y-2] #tail
]
#تعريف الاكل
food = [screen_width // 5 , screen_height // 3.5]
Window.addch[food [0] , food [1] , curses.ASC_PI]
#حركة اللاعب
key = curses.KEY_RIGHT #الحركة الافتراضية للثعبان
while True:
    next_key = Window.getch()
    key = key if next_key == -1 else next_key #بقوله هنا لو المتسخدم مدخلش  اي سهم جديد يبقا الحرجة تفضل كما هي
    if snake[0][0] in [0 , screen_width] or snake[0][1] in [0 , screen_height] or snake[0] in snake[1:]:
        curses.endwin()
        print ('u lost') 
        quit()     
    new_head = [snake[0][0] , snake[0][1]]
    if key == curses.KEY_UP:
        new_head = [new_head[0] , new_head [1]+1]
    if key == curses.KEY_DOWN:
        new_head = [new_head[0] , new_head [1]-1]
    if key == curses.KEY_RIGHT:
        new_head = [new_head[0]+1 , new_head [1]]
    if key == curses.KEY_LEFT:
        new_head = [new_head[0]-1 , new_head [1]]

    snake.insert (0 , new_head)
    if snake [0] == food:
        food = None
        while food is None:
            new_food = [random.randint(1 , screen_height -1 ) , random.randint(1 , screen_width -1 )]
            food = new_food if new_food not in snake else None # 23كعناه انه هينزل اكل عشوئي في اي مكان ولو جه على لالتعبان هياخد مكان االلي اخترناه في الاوا في سطر 
            Window.addch(food [0] , food [1] , curses.ASC_PI)

    else:
        tail = snake.pop()
        Window.addch (tail[0], tail[1],"  ")