<!-- Output copied to clipboard! -->

<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 3

Conversion time: 4.247 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Sun Apr 09 2023 07:33:43 GMT-0700 (PDT)
* Source doc: Крестики-нолики
* Tables are currently converted to HTML tables.
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!


WARNING:
You have 3 H1 headings. You may want to use the "H1 -> H2" option to demote all headings by one level.

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 1; ALERTS: 3.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



# Крестики нолики



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")



# План урока для вводного курса по созданию игры "Крестики-нолики" с использованием Pygame



1. Введение в Pygame
    * Объяснить основы Pygame
    * Установка Pygame: `pip install pygame`
    * Показать простой пример инициализации Pygame и создания окна
2. Настройка окна игры
    * Создать окно игры "Крестики-нолики" с фиксированным размером (300x300 пикселей)
    * Установить название окна "Крестики-нолики"
    * Представить функцию `pygame.display.set_mode()`
3. Рисование сетки
    * Представить функцию `pygame.draw.line()`
    * Объяснить, как нарисовать сетку "Крестики-нолики" с помощью вертикальных и горизонтальных линий
4. Обработка ввода мыши
    * Объяснить основы обработки событий в Pygame
    * Представить событие `pygame.MOUSEBUTTONUP`
    * Показать, как получить позицию мыши с помощью `pygame.mouse.get_pos()`
    * Рассчитать строку и столбец нажатой ячейки
5. Обновление игрового поля
    * Представить игровое поле в виде списка списков 3x3
    * Обновить нажатую ячейку текущим символом игрока ('X' или 'O')
6. Проверка на победителя
    * Реализовать функцию `check_winner()`
    * Объяснить, как проверить победителя (ряды, столбцы, диагонали)
7. Рисование иконок X и O
    * Загрузить и масштабировать изображения значков с помощью `pygame.image.load()` и `pygame.transform.scale()`
    * Представить функцию `screen.blit()`
    * Показать, как рисовать иконки X и O на игровом поле
8. Выделение выигрышных ячеек
    * Изменить функцию `check_winner()`, чтобы она возвращала выигрышные ячейки
    * Реализовать функцию `highlight_cells()`
    * Объяснить, как рисовать прямоугольники с помощью `pygame.draw.rect()` для выделения выигрышных ячеек
9. Основной игровой цикл
    * Обсудить структуру основного игрового цикла
    * Объяснить процесс обработки событий, обновления доски и отображения экрана
10. Заключение
    * Повтор


## Введение

Для того чтобы понимать и писать такой код на языке Python, ученик должен быть знаком с основными конструкциями и понятиями языка, такими как:



1. Основы Python: переменные, типы данных (строки, числа, логические значения), операторы, ввод и вывод данных.
2. Управляющие конструкции: условные операторы (`if`, `elif`, `else`) и циклы (`for`, `while`).
3. Функции: определение функций, передача аргументов, возвращение значений.
4. Списки: создание списков, индексация, срезы, методы работы со списками (`.append()`, `.remove()`, и т.д.)
5. Вложенные списки: использование двумерных списков для представления игрового поля.
6. Модули и пакеты: импортирование модулей (`import`) и использование функций и классов из сторонних библиотек, таких как Pygame.
7. Обработка событий: работа с событиями ввода, такими как нажатия клавиш и клики мыши.
8. ООП (объектно-ориентированное программирование): классы, объекты, методы и атрибуты. В данном случае не обязательно для понимания кода, но полезно знать, так как Pygame активно использует ООП.
9. Работа с графическими интерфейсами: создание и настройка окон, отрисовка графических примитивов и изображений с использованием библиотеки Pygame.

Овладев этими понятиями и конструкциями, ученик сможет понимать и писать код для разработки простой игры "Крестики-нолики" на языке Python с использованием библиотеки Pygame.


# Реализация:


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code>import pygame</code></strong>
<strong><code>import sys</code></strong>
<strong><code>pygame.init()</code></strong>
<strong><code># Constants</code></strong>
<strong><code>SCREEN_WIDTH = 300</code></strong>
<strong><code>SCREEN_HEIGHT = 300</code></strong>
<strong><code>LINE_WIDTH = 5</code></strong>
<strong><code>ICON_SIZE = 80</code></strong>
<strong><code>HIGHLIGHT_WIDTH = 5</code></strong>
<strong><code># Colors</code></strong>
<strong><code>WHITE = (255, 255, 255)</code></strong>
<strong><code>BLACK = (0, 0, 0)</code></strong>
<strong><code>GREEN = (0, 255, 0)</code></strong>
<strong><code># Load assets</code></strong>
<strong><code>x_icon = pygame.image.load('x_icon.png')</code></strong>
<strong><code>o_icon = pygame.image.load('o_icon.png')</code></strong>
<strong><code># Scale icons</code></strong>
<strong><code>x_icon = pygame.transform.scale(x_icon, (ICON_SIZE, ICON_SIZE))</code></strong>
<strong><code>o_icon = pygame.transform.scale(o_icon, (ICON_SIZE, ICON_SIZE))</code></strong>
<strong><code># Initialize screen</code></strong>
<strong><code>screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))</code></strong>
<strong><code>pygame.display.set_caption('Tic Tac Toe')</code></strong>
<strong><code># Draw the grid</code></strong>
<strong><code>def draw_grid():</code></strong>
<strong><code>    for i in range(1, 3):</code></strong>
<strong><code>        pygame.draw.line(screen, BLACK, (i * SCREEN_WIDTH // 3, 0), (i * SCREEN_WIDTH // 3, SCREEN_HEIGHT), LINE_WIDTH)</code></strong>
<strong><code>        pygame.draw.line(screen, BLACK, (0, i * SCREEN_HEIGHT // 3), (SCREEN_WIDTH, i * SCREEN_HEIGHT // 3), LINE_WIDTH)</code></strong>
<strong><code>def check_winner(board):</code></strong>
<strong><code>    for i, row in enumerate(board):</code></strong>
<strong><code>        if row[0] == row[1] == row[2] != None:</code></strong>
<strong><code>            return row[0], [(i, 0), (i, 1), (i, 2)]</code></strong>
<strong><code>    for j in range(3):</code></strong>
<strong><code>        if board[0][j] == board[1][j] == board[2][j] != None:</code></strong>
<strong><code>            return board[0][j], [(0, j), (1, j), (2, j)]</code></strong>
<strong><code>    if board[0][0] == board[1][1] == board[2][2] != None:</code></strong>
<strong><code>        return board[0][0], [(0, 0), (1, 1), (2, 2)]</code></strong>
<strong><code>    if board[0][2] == board[1][1] == board[2][0] != None:</code></strong>
<strong><code>        return board[0][2], [(0, 2), (1, 1), (2, 0)]</code></strong>
<strong><code>    return None, []</code></strong>
<strong><code>def highlight_cells(cells):</code></strong>
<strong><code>    for i, j in cells:</code></strong>
<strong><code>        x = j * (SCREEN_WIDTH // 3) + (SCREEN_WIDTH // 6) - (ICON_SIZE // 2)</code></strong>
<strong><code>        y = i * (SCREEN_HEIGHT // 3) + (SCREEN_HEIGHT // 6) - (ICON_SIZE // 2)</code></strong>
<strong><code>        pygame.draw.rect(screen, GREEN, (x - HIGHLIGHT_WIDTH // 2, y - HIGHLIGHT_WIDTH // 2, ICON_SIZE + HIGHLIGHT_WIDTH, ICON_SIZE + HIGHLIGHT_WIDTH), HIGHLIGHT_WIDTH)</code></strong>
<strong><code>def main():</code></strong>
<strong><code>    board = [[None for _ in range(3)] for _ in range(3)]</code></strong>
<strong><code>    player = 'X'</code></strong>
<strong><code>    winning_cells = []</code></strong>
<strong><code>    running = True</code></strong>
<strong><code>    game_over = False</code></strong>
<strong><code>    while running:</code></strong>
<strong><code>        screen.fill(WHITE)</code></strong>
<strong><code>        draw_grid()</code></strong>
<strong><code>        for event in pygame.event.get():</code></strong>
<strong><code>            if event.type == pygame.QUIT:</code></strong>
<strong><code>                running = False</code></strong>
<strong><code>            if not game_over and event.type == pygame.MOUSEBUTTONUP:</code></strong>
<strong><code>                x, y = pygame.mouse.get_pos()</code></strong>
<strong><code>                row, col = y // (SCREEN_HEIGHT // 3), x // (SCREEN_WIDTH // 3)</code></strong>
<strong><code>                if board[row][col] is None:</code></strong>
<strong><code>                    board[row][col] = player</code></strong>
<strong><code>                    winner, winning_cells</code></strong>
<strong><code>                   winner, winning_cells = check_winner(board)</code></strong>
<strong><code>                    if winner:</code></strong>
<strong><code>                        print(f"Player {winner} wins!")</code></strong>
<strong><code>                        game_over = True</code></strong>
<strong><code>                    else:</code></strong>
<strong><code>                        player = 'O' if player == 'X' else 'X'</code></strong>
<strong><code>        # Draw icons</code></strong>
<strong><code>        for i in range(3):</code></strong>
<strong><code>            for j in range(3):</code></strong>
<strong><code>                x = j * (SCREEN_WIDTH // 3) + (SCREEN_WIDTH // 6) - (ICON_SIZE // 2)</code></strong>
<strong><code>                y = i * (SCREEN_HEIGHT // 3) + (SCREEN_HEIGHT // 6) - (ICON_SIZE // 2)</code></strong>
<strong><code>                if board[i][j] == 'X':</code></strong>
<strong><code>                    screen.blit(x_icon, (x, y))</code></strong>
<strong><code>                elif board[i][j] == 'O':</code></strong>
<strong><code>                    screen.blit(o_icon, (x, y))</code></strong>
<strong><code>        if game_over:</code></strong>
<strong><code>            highlight_cells(winning_cells)</code></strong>
<strong><code>        pygame.display.flip()</code></strong>
<strong><code>    pygame.quit()</code></strong>
<strong><code>    sys.exit()</code></strong>
<strong><code>if __name__ == "__main__":</code></strong>
<strong><code>    main()</code></strong>
   </td>
  </tr>
</table>



# А теперь, подробнее:



1. Введение в Pygame

Pygame - это популярная библиотека для разработки видеоигр на языке Python. Pygame предоставляет набор инструментов и функций, которые позволяют легко создавать игры и мультимедийные приложения. В этом разделе мы познакомимся с основами работы с Pygame и научимся создавать простое окно.



* Объяснить основы Pygame

Pygame использует модульный подход, поэтому вы можете импортировать только те модули, которые вам нужны. Чтобы начать работу с Pygame, вам сначала нужно установить библиотеку. Если у вас еще не установлен Pygame, вы можете установить его с помощью следующей команды:



* Установка Pygame: `pip install pygame`

Теперь, когда Pygame установлен, давайте создадим простое окно. Вам нужно импортировать библиотеку Pygame и инициализировать ее перед использованием. Это делается с помощью функции `pygame.init()`.



* Показать простой пример инициализации Pygame и создания окна

Сниппет кода для создания простого окна с использованием Pygame:


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code>import pygame</code></strong>
<strong><code># Инициализация Pygame</code></strong>
<strong><code>pygame.init()</code></strong>
<strong><code># Задаем размеры окна</code></strong>
<strong><code>screen_width = 300</code></strong>
<strong><code>screen_height = 300</code></strong>
<strong><code># Создание окна</code></strong>
<strong><code>screen = pygame.display.set_mode((screen_width, screen_height))</code></strong>
<strong><code>pygame.display.set_caption("Простое окно")</code></strong>
<strong><code># Основной цикл</code></strong>
<strong><code>running = True</code></strong>
<strong><code>while running:</code></strong>
<strong><code>    for event in pygame.event.get():</code></strong>
<strong><code>        if event.type == pygame.QUIT:</code></strong>
<strong><code>            running = False</code></strong>
<strong><code>    # Обновление экрана</code></strong>
<strong><code>    pygame.display.flip()</code></strong>
<strong><code># Завершение работы с Pygame</code></strong>
<strong><code>pygame.quit()</code></strong>
   </td>
  </tr>
</table>




1. Настройка окна игры

Теперь, когда мы знакомы с основами работы с Pygame, давайте создадим окно для игры "Крестики-нолики". В этом разделе мы настроим окно игры, зададим его размер и установим подходящий заголовок.



* Создать окно игры "Крестики-нолики" с фиксированным размером (300x300 пикселей)

Для создания окна игры нам нужно определить его размеры. Мы будем использовать размер 300x300 пикселей, что достаточно для размещения сетки 3x3 и отображения иконок крестиков и ноликов.



* Установить название окна "Крестики-нолики"

Чтобы установить заголовок окна, мы воспользуемся функцией `pygame.display.set_caption()`. В качестве аргумента передадим строку с названием игры.



* Представить функцию `pygame.display.set_mode()`

Функция `pygame.display.set_mode()` используется для создания окна с указанными размерами. Она принимает кортеж с шириной и высотой окна в пикселях.

Сниппет кода для настройки окна игры "Крестики-нолики":


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code>import pygame</code></strong>
<strong><code># Инициализация Pygame</code></strong>
<strong><code>pygame.init()</code></strong>
<strong><code># Задаем размеры окна</code></strong>
<strong><code>screen_width = 300</code></strong>
<strong><code>screen_height = 300</code></strong>
<strong><code># Создание окна игры</code></strong>
<strong><code>screen = pygame.display.set_mode((screen_width, screen_height))</code></strong>
<strong><code>pygame.display.set_caption("Крестики-нолики")</code></strong>
<strong><code># Основной цикл игры</code></strong>
<strong><code>running = True</code></strong>
<strong><code>while running:</code></strong>
<strong><code>    for event in pygame.event.get():</code></strong>
<strong><code>        if event.type == pygame.QUIT:</code></strong>
<strong><code>            running = False</code></strong>
<strong><code>    # Обновление экрана</code></strong>
<strong><code>    pygame.display.flip()</code></strong>
<strong><code># Завершение работы с Pygame</code></strong>
<strong><code>pygame.quit()</code></strong>
   </td>
  </tr>
</table>


В результате выполнения этого кода мы получим окно размером 300x300 пикселей с заголовком "Крестики-нолики". Окно будет отображаться до тех пор, пока пользователь не закроет его. В следующем разделе мы добавим сетку для игры "Крестики-нолики".



1. Рисование сетки

Теперь, когда у нас есть окно игры, давайте добавим сетку для игры "Крестики-нолики". Мы нарисуем сетку 3x3, используя вертикальные и горизонтальные линии, и разделим окно на 9 равных ячеек.



* Представить функцию `pygame.draw.line()`

Для рисования линий в Pygame используется функция `pygame.draw.line()`. Она принимает следующие аргументы: экран (surface), цвет линии, начальную и конечную точки линии, и толщину линии. Цвет задается в формате RGB.



* Объяснить, как нарисовать сетку "Крестики-нолики" с помощью вертикальных и горизонтальных линий

Чтобы нарисовать сетку, нам нужно нарисовать две горизонтальные линии и две вертикальные линии. Мы определим функцию `draw_grid()`, которая будет отвечать за рисование сетки на экране.

Сниппет кода для рисования сетки "Крестики-нолики":


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code>import pygame</code></strong>
<strong><code>def draw_grid(screen, width, height):</code></strong>
<strong><code>    grid_color = (255, 255, 255)  # Белый цвет</code></strong>
<strong><code>    grid_thickness = 2  # Толщина линии</code></strong>
<strong><code>    # Рисование вертикальных линий</code></strong>
<strong><code>    for x in range(1, 3):</code></strong>
<strong><code>        pygame.draw.line(screen, grid_color, (x * width // 3, 0), (x * width // 3, height), grid_thickness)</code></strong>
<strong><code>    # Рисование горизонтальных линий</code></strong>
<strong><code>    for y in range(1, 3):</code></strong>
<strong><code>        pygame.draw.line(screen, grid_color, (0, y * height // 3), (width, y * height // 3), grid_thickness)</code></strong>
<strong><code># Инициализация Pygame</code></strong>
<strong><code>pygame.init()</code></strong>
<strong><code># Задаем размеры окна</code></strong>
<strong><code>screen_width = 300</code></strong>
<strong><code>screen_height = 300</code></strong>
<strong><code># Создание окна игры</code></strong>
<strong><code>screen = pygame.display.set_mode((screen_width, screen_height))</code></strong>
<strong><code>pygame.display.set_caption("Крестики-нолики")</code></strong>
<strong><code># Основной цикл игры</code></strong>
<strong><code>running = True</code></strong>
<strong><code>while running:</code></strong>
<strong><code>    for event in pygame.event.get():</code></strong>
<strong><code>        if event.type == pygame.QUIT:</code></strong>
<strong><code>            running = False</code></strong>
<strong><code>    # Рисование сетки</code></strong>
<strong><code>    draw_grid(screen, screen_width, screen_height)</code></strong>
<strong><code>    # Обновление экрана</code></strong>
<strong><code>    pygame.display.flip()</code></strong>
<strong><code># Завершение работы с Pygame</code></strong>
<strong><code>pygame.quit()</code></strong>
   </td>
  </tr>
</table>


Этот код добавляет сетку на игровое поле, разделяя его на 9 равных ячеек. Сетка будет отображаться на экране до тех пор, пока пользователь не закроет окно. В следующем разделе мы обработаем ввод пользователя с помощью мыши.



1. Обработка ввода мыши

Теперь, когда у нас есть сетка для игры "Крестики-нолики", давайте добавим обработку ввода пользователя с помощью мыши. Мы хотим отслеживать клики левой кнопкой мыши и определять, в какой ячейке сетки произошел клик.



* Представить события `pygame.MOUSEBUTTONDOWN` и `pygame.MOUSEBUTTONUP`

Pygame предоставляет события для отслеживания нажатия и отпускания кнопок мыши. В данном случае нам нужно обработать событие `pygame.MOUSEBUTTONDOWN`, которое возникает при нажатии кнопки мыши.



* Объяснить, как определить ячейку сетки, в которой произошел клик

Чтобы определить ячейку сетки, в которой произошел клик, мы можем использовать координаты курсора мыши и делить их на размер ячейки. Это позволит нам получить индексы строки и столбца ячейки.

Сниппет кода для обработки ввода мыши и определения ячейки сетки:


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code>import pygame</code></strong>
<strong><code>def get_grid_cell(screen_width, screen_height, mouse_x, mouse_y):</code></strong>
<strong><code>    cell_width = screen_width // 3</code></strong>
<strong><code>    cell_height = screen_height // 3</code></strong>
<strong><code>    row = mouse_y // cell_height</code></strong>
<strong><code>    col = mouse_x // cell_width</code></strong>
<strong><code>    return row, col</code></strong>
<strong><code># Инициализация Pygame</code></strong>
<strong><code>pygame.init()</code></strong>
<strong><code># Задаем размеры окна</code></strong>
<strong><code>screen_width = 300</code></strong>
<strong><code>screen_height = 300</code></strong>
<strong><code># Создание окна игры</code></strong>
<strong><code>screen = pygame.display.set_mode((screen_width, screen_height))</code></strong>
<strong><code>pygame.display.set_caption("Крестики-нолики")</code></strong>
<strong><code># Основной цикл игры</code></strong>
<strong><code>running = True</code></strong>
<strong><code>while running:</code></strong>
<strong><code>    for event in pygame.event.get():</code></strong>
<strong><code>        if event.type == pygame.QUIT:</code></strong>
<strong><code>            running = False</code></strong>
<strong><code>        elif event.type == pygame.MOUSEBUTTONDOWN:</code></strong>
<strong><code>            # Левая кнопка мыши нажата</code></strong>
<strong><code>            if event.button == 1:</code></strong>
<strong><code>                mouse_x, mouse_y = event.pos</code></strong>
<strong><code>                row, col = get_grid_cell(screen_width, screen_height, mouse_x, mouse_y)</code></strong>
<strong><code>                print(f"Клик в ячейке ({row}, {col})")</code></strong>
<strong><code>    # Рисование сетки</code></strong>
<strong><code>    draw_grid(screen, screen_width, screen_height)</code></strong>
<strong><code>    # Обновление экрана</code></strong>
<strong><code>    pygame.display.flip()</code></strong>
<strong><code># Завершение работы с Pygame</code></strong>
<strong><code>pygame.quit()</code></strong>
   </td>
  </tr>
</table>


Этот код обрабатывает ввод пользователя с помощью мыши и выводит координаты ячейки сетки, в которой произошел клик. В следующем разделе мы добавим функциональность для отображения крестиков и ноликов в выбранных ячейках.



1. Обновление игрового поля

Теперь, когда мы можем определить ячейку сетки, в которой произошел клик, давайте добавим функциональность для отображения крестиков и ноликов в выбранных ячейках. Для этого нам понадобится хранить состояние игрового поля и обновлять его при каждом ходе.



* Создать двумерный массив для хранения состояния игрового поля

Мы будем использовать двумерный массив размером 3x3 для хранения состояния игрового поля. Значения в массиве будут соответствовать крестикам, ноликам и пустым ячейкам.



* Отобразить крестик или нолик в выбранной ячейке

Чтобы отобразить крестик или нолик в выбранной ячейке, нам нужно загрузить соответствующие изображения и отрисовать их на экране с использованием функции `screen.blit()`.



* Обновлять состояние игрового поля при каждом ходе

При каждом ходе мы будем обновлять состояние игрового поля, заменяя значение в выбранной ячейке на текущий символ (крестик или нолик).

Сниппет кода для обновления игрового поля:


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code>import pygame</code></strong>
<strong><code># Загрузка изображений крестика и нолика</code></strong>
<strong><code>X_img = pygame.image.load("X.png")</code></strong>
<strong><code>O_img = pygame.image.load("O.png")</code></strong>
<strong><code># Инициализация игрового поля</code></strong>
<strong><code>game_board = [[None for _ in range(3)] for _ in range(3)]</code></strong>
<strong><code># Функция для отрисовки символов на игровом поле</code></strong>
<strong><code>def draw_board(screen, board, screen_width, screen_height):</code></strong>
<strong><code>    for row in range(3):</code></strong>
<strong><code>        for col in range(3):</code></strong>
<strong><code>            x = col * screen_width // 3</code></strong>
<strong><code>            y = row * screen_height // 3</code></strong>
<strong><code>            if board[row][col] == "X":</code></strong>
<strong><code>                screen.blit(X_img, (x, y))</code></strong>
<strong><code>            elif board[row][col] == "O":</code></strong>
<strong><code>                screen.blit(O_img, (x, y))</code></strong>
<strong><code># Определение текущего игрока</code></strong>
<strong><code>current_player = "X"</code></strong>
<strong><code># Основной цикл игры</code></strong>
<strong><code>running = True</code></strong>
<strong><code>while running:</code></strong>
<strong><code>    for event in pygame.event.get():</code></strong>
<strong><code>        if event.type == pygame.QUIT:</code></strong>
<strong><code>            running = False</code></strong>
<strong><code>        elif event.type == pygame.MOUSEBUTTONDOWN:</code></strong>
<strong><code>            # Левая кнопка мыши нажата</code></strong>
<strong><code>            if event.button == 1:</code></strong>
<strong><code>                mouse_x, mouse_y = event.pos</code></strong>
<strong><code>                row, col = get_grid_cell(screen_width, screen_height, mouse_x, mouse_y)</code></strong>
<strong><code>                if game_board[row][col] is None:</code></strong>
<strong><code>                    game_board[row][col] = current_player</code></strong>
<strong><code>                    current_player = "O" if current_player == "X" else "X"</code></strong>
<strong><code>    # Рисование сетки и символов на игровом поле</code></strong>
<strong><code>    draw_grid(screen, screen_width, screen_height)</code></strong>
<strong><code>    draw_board(screen, game_board, screen_width, screen_height)</code></strong>
<strong><code># Обновление Экрана</code></strong>
<strong><code>pygame.display.flip()</code></strong>
   </td>
  </tr>
</table>


Этот код добавляет функциональность для отображения крестиков и ноликов на игровом поле. Теперь при каждом клике мыши в ячейке сетки будет отображаться соответствующий символ, и текущий игрок будет меняться после каждого хода.

В следующем разделе мы добавим определение победителя и завершение игры, когда один из игроков выиграет или когда закончатся доступные ходы.



1. Проверка на победителя

Теперь, когда у нас есть функциональность для отображения крестиков и ноликов на игровом поле, давайте добавим определение победителя. В "Крестики-нолики" победитель определяется, если один из игроков смог заполнить одну из горизонтальных, вертикальных или диагональных линий.



* Создать функцию для проверки победителя

Мы создадим функцию `check_winner()`, которая примет текущее состояние игрового поля и вернет символ победителя (если он есть) и координаты выигрышной комбинации.

Сниппет кода для проверки победителя:


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code>def check_winner(board):</code></strong>
<strong><code>    for row in range(3):</code></strong>
<strong><code>        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:</code></strong>
<strong><code>            return board[row][0], [(row, 0), (row, 1), (row, 2)]</code></strong>
<strong><code>    for col in range(3):</code></strong>
<strong><code>        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:</code></strong>
<strong><code>            return board[0][col], [(0, col), (1, col), (2, col)]</code></strong>
<strong><code>    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:</code></strong>
<strong><code>        return board[0][0], [(0, 0), (1, 1), (2, 2)]</code></strong>
<strong><code>    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:</code></strong>
<strong><code>        return board[0][2], [(0, 2), (1, 1), (2, 0)]</code></strong>
<strong><code>    return None, []</code></strong>
<strong><code># ... (остальной код)</code></strong>
<strong><code># Основной цикл игры</code></strong>
<strong><code>running = True</code></strong>
<strong><code>while running:</code></strong>
<strong><code>    for event in pygame.event.get():</code></strong>
<strong><code>        if event.type == pygame.QUIT:</code></strong>
<strong><code>            running = False</code></strong>
<strong><code>        elif event.type == pygame.MOUSEBUTTONDOWN:</code></strong>
<strong><code>            # Левая кнопка мыши нажата</code></strong>
<strong><code>            if event.button == 1:</code></strong>
<strong><code>                mouse_x, mouse_y = event.pos</code></strong>
<strong><code>                row, col = get_grid_cell(screen_width, screen_height, mouse_x, mouse_y)</code></strong>
<strong><code>                if game_board[row][col] is None:</code></strong>
<strong><code>                    game_board[row][col] = current_player</code></strong>
<strong><code>                    winner, winning_cells = check_winner(game_board)</code></strong>
<strong><code>                    if winner is not None:</code></strong>
<strong><code>                        print(f"Победитель: {winner}")</code></strong>
<strong><code>                        running = False</code></strong>
<strong><code>                    else:</code></strong>
<strong><code>                        current_player = "O" if current_player == "X" else "X"</code></strong>
<strong><code>    # Рисование сетки и символов на игровом поле</code></strong>
<strong><code>    draw_grid(screen, screen_width, screen_height)</code></strong>
<strong><code>    draw_board(screen, game_board, screen_width, screen_height)</code></strong>
<strong><code>    # Обновление экрана</code></strong>
<strong><code>    pygame.display.flip()</code></strong>
<strong><code># Завершение работы с Pygame</code></strong>
<strong><code>pygame.quit()</code></strong>
   </td>
  </tr>
</table>


Теперь при каждом ходе будет проверяться победитель, и если победитель определен, игра завершится


## 7. Рисование иконок X и O

В этом разделе мы обсудим, как загрузить и нарисовать иконки X и O, используя изображения, созданные с помощью GIMP. Для этого мы воспользуемся библиотекой Pygame.



* Создание иконок

Для создания иконок можно использовать графический редактор. В данном случае мы используем GIMP. 

Нам нужно будет загружать файлы с расширением png, размер 80х80

'x_icon.png'

'o_icon.png'

Вот так выглядит наша версия:



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")




* Загрузка и масштабирование иконок X и O

Мы уже загрузили иконки X и O из файлов 'x_icon.png' и 'o_icon.png' и масштабировали их до нужного размера. Теперь мы можем использовать эти иконки для отображения на игровом поле.

Сниппет кода для загрузки и масштабирования иконок:


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code>import pygame</code></strong>
<strong><code># Load assets</code></strong>
<strong><code>x_icon = pygame.image.load('x_icon.png')</code></strong>
<strong><code>o_icon = pygame.image.load('o_icon.png')</code></strong>
<strong><code># Scale icons</code></strong>
<strong><code>ICON_SIZE = 80</code></strong>
<strong><code>x_icon = pygame.transform.scale(x_icon, (ICON_SIZE, ICON_SIZE))</code></strong>
<strong><code>o_icon = pygame.transform.scale(o_icon, (ICON_SIZE, ICON_SIZE))</code></strong>
   </td>
  </tr>
</table>




* Отображение иконок X и O на игровом поле

Для отображения иконок X и O на игровом поле мы используем функцию `screen.blit()`, которая копирует содержимое одного изображения на другое.

Сниппет кода для отрисовки иконок X и O на игровом поле:


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code># Draw icons</code></strong>
<strong><code>for i in range(3):</code></strong>
<strong><code>    for j in range(3):</code></strong>
<strong><code>        x = j * (SCREEN_WIDTH // 3) + (SCREEN_WIDTH // 6) - (ICON_SIZE // 2)</code></strong>
<strong><code>        y = i * (SCREEN_HEIGHT // 3) + (SCREEN_HEIGHT // 6) - (ICON_SIZE // 2)</code></strong>
<strong><code>        if board[i][j] == 'X':</code></strong>
<strong><code>            screen.blit(x_icon, (x, y))</code></strong>
<strong><code>        elif board[i][j] == 'O':</code></strong>
<strong><code>            screen.blit(o_icon, (x, y))</code></strong>
   </td>
  </tr>
</table>


Теперь, когда вы запустите игру, на игровом поле будут отображаться ваши иконки крестика и нолика, созданные с помощью GIMP.


## 8. Выделение выигрышных ячеек

В этом разделе мы рассмотрим, как выделить выигрышные ячейки после завершения игры. Для этого мы нарисуем прямоугольник вокруг иконок X или O, когда один из игроков выигрывает.



* Функция для выделения выигрышных ячеек

Создадим функцию `highlight_cells()`, которая принимает список координат выигрышных ячеек и рисует прямоугольники вокруг соответствующих иконок X или O.

Сниппет кода для функции выделения выигрышных ячеек:


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code>def highlight_cells(cells):</code></strong>
<strong><code>    for i, j in cells:</code></strong>
<strong><code>        x = j * (SCREEN_WIDTH // 3) + (SCREEN_WIDTH // 6) - (ICON_SIZE // 2)</code></strong>
<strong><code>        y = i * (SCREEN_HEIGHT // 3) + (SCREEN_HEIGHT // 6) - (ICON_SIZE // 2)</code></strong>
<strong><code>        pygame.draw.rect(screen, GREEN, (x - HIGHLIGHT_WIDTH // 2, y - HIGHLIGHT_WIDTH // 2, ICON_SIZE + HIGHLIGHT_WIDTH, ICON_SIZE + HIGHLIGHT_WIDTH), HIGHLIGHT_WIDTH)</code></strong>
   </td>
  </tr>
</table>




* Выделение выигрышных ячеек в основном цикле игры

В основном цикле игры, после завершения игры, вызовите функцию `highlight_cells()` с координатами выигрышных ячеек.

Сниппет кода для выделения выигрышных ячеек в основном цикле игры:

**if game_over:**

**    highlight_cells(winning_cells)**


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code>if game_over:</code></strong>
<strong><code>    highlight_cells(winning_cells)</code></strong>
   </td>
  </tr>
</table>


Теперь при завершении игры выигрышные ячейки будут выделены зелеными прямоугольниками вокруг иконок X или O.


## 9. Основной игровой цикл

В этом разделе мы рассмотрим основной игровой цикл, который управляет логикой игры и отображением на экране. Основной игровой цикл будет выполняться до тех пор, пока игрок не закроет окно игры. Во время игрового цикла программа будет обрабатывать события, обновлять состояние игры и рисовать элементы на экране.



* Цикл while для основного игрового цикла

Основной игровой цикл выполняется внутри цикла `while`, который продолжает работать до тех пор, пока переменная `running` не станет равной `False`.

Сниппет кода для основного игрового цикла:


<table>
  <tr>
   <td>
   </td>
  </tr>
  <tr>
   <td><strong><code>running = True</code></strong>
<strong><code>game_over = False</code></strong>
<strong><code>while running:</code></strong>
<strong><code>    # Обработка событий</code></strong>
<strong><code>    for event in pygame.event.get():</code></strong>
<strong><code>        # Выход из игры</code></strong>
<strong><code>        if event.type == pygame.QUIT:</code></strong>
<strong><code>            running = False</code></strong>
<strong><code>    # Очистка экрана</code></strong>
<strong><code>    screen.fill(WHITE)</code></strong>
<strong><code>    # Рисование сетки</code></strong>
<strong><code>    draw_grid()</code></strong>
<strong><code>    # Обработка ввода мыши</code></strong>
<strong><code>    if not game_over:</code></strong>
<strong><code>        # ... (код для обработки ввода мыши)</code></strong>
<strong><code>    # Обновление игрового поля</code></strong>
<strong><code>    # ... (код для обновления игрового поля)</code></strong>
<strong><code>    # Рисование иконок X и O</code></strong>
<strong><code>    # ... (код для рисования иконок X и O)</code></strong>
<strong><code>    # Выделение выигрышных ячеек</code></strong>
<strong><code>    if game_over:</code></strong>
<strong><code>        highlight_cells(winning_cells)</code></strong>
<strong><code>    # Обновление дисплея</code></strong>
<strong><code>    pygame.display.flip()</code></strong>
   </td>
  </tr>
</table>


Теперь у вас есть полноценная игра "Крестики-нолики" с графическим интерфейсом на Python с использованием библиотеки Pygame. Вы можете продолжать улучшать игру, добавляя новые функции, такие как подсчет очков или режим для двух игроков.
