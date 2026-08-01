import pygame

HEIGHT = 500
WIDTH = 500
pygame.init()
window = pygame.display.set_mode((HEIGHT,WIDTH))

start_state = [
    ['bR','bN','bB','bQ','bK','bB','bN','bR'],
    ['bP','bP','bP','bP','bP','bP','bP','bP'],
    ['_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_','_'],
    ['wP','wP','wP','wP','wP','wP','wP','wP'],
    ['wR','wN','wB','wQ','wK','wB','wN','wR']
]

piece_ref = {
    'bP': 'pieces/pawn-b.svg',
    'bR': 'pieces/rook-b.svg',
    'bN': 'pieces/knight-b.svg',
    'bB': 'pieces/bishop-b.svg',
    'bK': 'pieces/king-b.svg',
    'bQ': 'pieces/queen-b.svg',
    'wP': 'pieces/pawn-w.svg',
    'wR': 'pieces/rook-w.svg',
    'wN': 'pieces/knight-w.svg',
    'wB': 'pieces/bishop-w.svg',
    'wK': 'pieces/king-w.svg',
    'wQ': 'pieces/queen-w.svg'
}

background = pygame.Surface((400,400))

def board(background):
    light_square = (186,202,68)
    dark_square = (118,150,86)
    sq_type = True #dark_square is True
    sq_values = dark_square

    for i in range(0,8):
        for j in range(0,8):
            if sq_type:
                sq_values = dark_square
            else:
                sq_values = light_square
            square = (j*50,i*50,50,50)
            pygame.draw.rect(background,sq_values,square)
            sq_type = not sq_type
        sq_type = not sq_type
    window.blit(background,(50,50))
    pygame.display.flip()
    return

def display_piece(vis):
    for name, piece_link in piece_ref.items():
        piece = pygame.image.load(piece_link).convert_alpha()
        scaled = pygame.transform.scale_by(piece , 0.35)
        piece_x = 50
        piece_y = 50
        for x in range (0,8):
            for y in range (0,8):
                if (name==start_state[x][y] and vis[x][y]!=True):
                    piece_x = 50 + 50 * x
                    piece_y = 50 + 50 * y
                    window.blit(scaled,(piece_y,piece_x))
                    vis[x][y] = True
    pygame.display.flip()
    return

running=True
while running:
    for event in pygame.event.get():
        board(background)
        vis=[[False for _ in range(8)]for _ in range(8)]
        display_piece(vis)
        if event.type==pygame.QUIT:
            running=False

pygame.quit()