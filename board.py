import pygame

HEIGHT = 500
WIDTH = 500
pygame.init()
window = pygame.display.set_mode((HEIGHT,WIDTH))

state = [
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
    return

def display_piece(vis):
    piece_images = []
    for name, piece_link in piece_ref.items():
        piece = pygame.image.load(piece_link).convert_alpha()
        scaled = pygame.transform.scale_by(piece , 0.35)
        piece_x = 50
        piece_y = 50
        for row in range (0,8):
            for col in range (0,8):
                if (name==state[row][col] and vis[row][col]!=True):
                    piece_x = 50 + 50 * col
                    piece_y = 50 + 50 * row
                    piece_images.append([row,col,scaled])
                    window.blit(scaled,(piece_x,piece_y))
                    vis[row][col] = True
    return piece_images

running=True
dragging = False
active_piece = None
src_row = -1
src_col = -1

while running:
    board(background)
    vis=[[False for _ in range(8)]for _ in range(8)]
    images = display_piece(vis)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            col = mouse_x//50 - 1
            row = mouse_y//50 - 1
            if(state[row][col] != '_'):
                for iter in images:
                    if (iter[0] == row and iter[1] == col):
                        active_piece = iter[2].get_rect()
                        src_row = row
                        src_col = col
                        dragging = True
                        break
            print(dragging)
            #print(active_piece)
            
        if event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x//50 -1
                row = mouse_y//50 -1
                if (col>=0 and col<=7 and row>=0 and row<=7):
                    piece_name = state[src_row][src_col]
                    state[row][col] = piece_name
                    state[src_row][src_col] = '_'
                pass
            dragging = False
            active_piece = None
            src_row=-1
            src_col=-1

        if event.type == pygame.MOUSEMOTION:
            if dragging and active_piece != None:
                mouse_x,mouse_y = event.pos
                active_piece.move_ip(event.rel) 
                pass
    
    pygame.display.flip()

pygame.quit()