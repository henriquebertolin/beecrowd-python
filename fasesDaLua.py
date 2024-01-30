lua_prim, lua_seg = map(int, input(). split())

if 0 <= lua_prim and lua_seg <= 2:
    print("nova")
elif lua_prim >= lua_seg and lua_seg <= 96:
    print("minguante")
elif lua_seg > lua_prim and lua_seg <= 96:
    print("crescente")
else:
    print("cheia")