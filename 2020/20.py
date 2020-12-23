from aocd.models import Puzzle
import numpy as np
from utils import *

puzzle = Puzzle(year=2020, day=20)
raw = puzzle.input_data

def np_img(img):
    return np.array([[ 0 if (c =='.') else 1 for c in l] for l in img])

tiles_raw = raw.split('\n\n')
tiles = {}
for tile in tiles_raw:
    tid, img = tile.split(':')
    tid = pints(tid)[0]
    tiles[tid] = np_img(img.strip().split('\n'))

boundaries = {}
for tid, tile in tiles.items():
    top = tile[0]
    bot = tile[-1]
    lef = tile[:,0]
    rig = tile[:,-1]
    boundaries[tid] = [i.tolist() for i in (top,bot,lef,rig)]

def is_corner(tid):
    if len(get_matches(tid)) == 2:
        return True
    return False

match_cache = {}
def get_matches(tid):
    if tid in match_cache:
        return match_cache[tid]
    matches = set()
    for edge in boundaries[tid]:
        for tid2, edges in boundaries.items():
            if(tid2 != tid):
                if edge in edges or edge[::-1] in edges:
                    matches.add(tid2)
    match_cache[tid] = matches
    return matches

corners = []
for tid in tiles:
    if(is_corner(tid)):
        corners.append(tid)
print('Corners:', prod(corners))

def get_configs(tile):
    for i in range(4):
        tile = np.rot90(tile)
        yield tile
    tile = np.flipud(tile)
    for i in range(4):
        tile = np.rot90(tile)
        yield tile

def orient_lr(l, r):
    for config in get_configs(tiles[r]):
        if all(config[:,0] == tiles[l][:,-1]):
            tiles[r] = config
            return True
    return False

def orient_lrd(l,r,d,lfix = False):
    if lfix:
        for d_config in get_configs(tiles[d]):
            if all(tiles[l][-1] == d_config[0]):
                tiles[d] = d_config
                if orient_lr(l, r):
                    return True
    else:
        for l_config in get_configs(tiles[l]):
            tiles[l] = l_config
            if(orient_lrd(l,r,d,True)):
                return True
    return False

done = set()
d = corners[0]
nt = len(tiles[d]) - 2
n = int(len(tiles)**0.5)
full_image = -1*np.ones((n*nt,n*nt), dtype=int)
for i in range(n):
    l = d
    if i < n-1:
        r,d = (get_matches(l)-done)
        if( not orient_lrd(l,r,d, i != 0) ):
            d,r = (get_matches(l)-done)
            orient_lrd(l,r,d,i != 0 )
    for j in range(n-1):
        rcandidates = get_matches(l) - done
        for rc in rcandidates:
            if orient_lr(l, rc):
                full_image[i*nt:(i+1)*nt,j*nt:(j+1)*nt] = tiles[l][1:-1,1:-1]
                done.add(l)
                l = rc
                break
    j += 1
    full_image[i*nt:(i+1)*nt,j*nt:(j+1)*nt] = tiles[l][1:-1,1:-1]
    done.add(l)

mimg = """..................#.
#....##....##....###
.#..#..#..#..#..#...""".splitlines()
monster = np_img(mimg)

n_monsters = 0
nf = full_image.shape[0]
for config in get_configs(monster):
    i,j = 0,0
    minv = np.array(config == 0, dtype=int)
    my,mx = config.shape
    while i < nf-my+1:
        j = 0
        while j < nf-mx+1:
            if( np.all(full_image[i:i+my, j:j+mx]*config == config) ):
                n_monsters += 1
                full_image[i:i+my, j:j+mx] *= minv
                j = j+mx
            else:
                j += 1
        i += 1
    if( n_monsters ): break
print('Monsters:', n_monsters)
print('Part 2:', full_image.sum())
