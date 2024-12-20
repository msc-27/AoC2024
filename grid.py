import itertools
def plot_line(p, q):
    px,py = p
    qx,qy = q
    if px == qx:
        direction = 1 if qy >= py else -1
        yield from ((px,y) for y in range(py, qy+direction, direction))
    else:
        direction = 1 if qx >= px else -1
        yield from ((x,py) for x in range(px, qx+direction, direction))

def inrange(point, dist, include_point = False):
    dim = len(point)
    ranges = [range(-dist,dist+1)] * dim
    origin = tuple([0] * dim)
    for delta in itertools.product(*ranges):
        if include_point or delta != origin:
            yield tuple((x+y for x,y in zip(point, delta)))

def atrange(point, dist):
    dim = len(point)
    if dim == 1:
        yield (point[0]-dist,)
        if dist != 0: yield (point[0]+dist,)
    else:
        for p in ((point[0]-dist,) + q for q in inrange(point[1:], dist, True)):
            yield p
        for x in range(-dist+1, dist):
            for p in ((point[0]+x,) + q for q in atrange(point[1:], dist)):
                yield p
        if dist!= 0:
            for p in ((point[0]+dist,) + q for q in inrange(point[1:], dist, True)):
                yield p

def inmanhat(point, dist, include_point = False):
    dim = len(point)
    if dim == 1:
        p = point[0]
        for dp in range(-dist, dist+1):
            if dp or include_point: yield (p+dp,)
    elif dim == 2: # special case for performance
        if dist == 0:
            if include_point: yield point
        else:
            x,y = point
            for dx in range(-dist, 0):
                yield from ((x+dx, yy) for yy in range(y-dist-dx, y+dist+1+dx))
            if include_point:
                yield from ((x, yy) for yy in range(y-dist, y+dist+1))
            else:
                yield from ((x, yy) for yy in range(y-dist, y))
                yield from ((x, yy) for yy in range(y+1, y+dist+1))
            for dx in range(1, dist+1):
                yield from ((x+dx, yy) for yy in range(y-dist+dx, y+dist+1-dx))
    else: # general >= 3 dimensional case
        for d in range(-dist, dist+1):
            for p in ((point[0]+d,) + q for q in inmanhat(point[1:], dist-abs(d), True)):
                if include_point or p != point: yield p

def atmanhat(point, dist):
    dim = len(point)
    if dim == 1:
        yield (point[0]-dist,)
        if dist != 0: yield (point[0]+dist,)
    else:
        for x in range(-dist, dist+1):
            yield from ((point[0]+x,) + q for q in atmanhat(point[1:], dist - abs(x)))
