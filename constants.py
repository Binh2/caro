QUIT = -1
SCENE_GAME = 0
SCENE_MENU = 1

SCREEN_WIDTH = 560
SCREEN_HEIGHT = 560

FPS_LIMIT = 10

MENU_OBJECT = {
    "buttons": [
        {
            "name": "play",
            "x": SCREEN_WIDTH / 2,
            "y": SCREEN_HEIGHT / 2,
            "width": 100,
            "height": 50,
            "border_radius": 5,
            "text": "Play",
            "text_size": 50,
            "color": {
                "background": [255,0,0],
                "text": [0,255,0]
            },
            "is_center": True
        }
    ],
    "color": {
        "background": (255,255,255)
    }
}

BOARD_OBJECT = {
    "square_width": 40,
    "x_offset": 100,
    "y_offset": 100,
    "row": 10,
    "col": 10,
    "color": {
        "square_border": (255,0,0)
    },
    "is_aspect_ratio_rescale": True
}

MARK_OBJECT = {
    "color": {
        "x": [255,0,0],
        "y": [0,255,0]
    },
    "is_aspect_ratio_rescale": True
}

CARO_OBJECT = {
    "color": {
        "background": (0,0,100),
        "winning_line": (0,100,0)
    },
    "buttons": [
        {
            "name": "move_backward",
            "x": 100,
            "y": 50,
            "width": 40,
            "height": 40,
            "border_radius": 5,
            "text": "<",
            "text_size": 50,
            "color": {
                "background": [255,0,0],
                "text": [0,255,0]
            },
            "is_center": True
        },
        {
            "name": "move_forward",
            "x": 150,
            "y": 50,
            "width": 40,
            "height": 40,
            "border_radius": 5,
            "text": ">",
            "text_size": 50,
            "color": {
                "background": [255,0,0],
                "text": [0,255,0]
            },
            "is_center": True
        }
    ]
}
