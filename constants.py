QUIT = -1
SCENE_GAME = 0
SCENE_MENU = 1

SCREEN_SIZE = (560, 560)
SCREEN_WIDTH, SCREEN_HEIGHT= SCREEN_SIZE

FPS_LIMIT = 10

TEXT_BOX_OBJECT = [
    {
        "name": "play",
        "center_x": SCREEN_WIDTH / 2,
        "center_y": SCREEN_HEIGHT / 2,
        "width": 100,
        "height": 50,
        "border_radius": 5,
        "text": "Play",
        "text_font": None,
        "text_size": 50,
        "text_limit": 100,
        "color": {
            "background": [255,0,0],
            "text": [0,255,0],
            "cursor": [0,100,0]
        },
        "is_center": True,
        "padding_left": 60,
        "padding_right": 20
    },
    {
        "name": "play",
        "x": SCREEN_WIDTH / 2,
        "y": SCREEN_HEIGHT / 2,
        "width": 100,
        "height": 50,
        "border_radius": 5,
        "text": "Play",
        "text_font": None,
        "text_size": 50,
        "text_limit": 6,
        "color": {
            "background": [255,0,0],
            "text": [0,255,0],
            "cursor": [0,100,0]
        },
        "is_center": False,
        "padding_left": 60,
        "padding_right": 20
    }
]

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
            "is_center": True,
            "is_visible": True
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
            "is_center": True,
            "is_visible": True
        },
        {
            "name": "restart",
            "x": SCREEN_WIDTH // 2,
            "y": SCREEN_HEIGHT // 2,
            "width": 100,
            "height": 40,
            "border_radius": 5,
            "text": "Restart",
            "text_size": 50,
            "color": {
                "background": [255,0,0],
                "text": [0,255,0]
            },
            "is_center": True,
            "is_visible": False
        }
    ]
}
