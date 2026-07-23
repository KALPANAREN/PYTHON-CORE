def demo_gen(x):
    print("Generator started")
    y = x + 10
    yield y
    print("Resumed after first yield")
    z = y * 2
    yield z
    print("Generator ending")

# creation phase
g = demo_gen(5)
print(g.gi_code,"\n")
print(g.gi_frame)
print(g.gi_frame.f_lasti)
print(g.gi_frame.f_locals,"\n")
print(g.gi_running)

# activation phase
print("********************************")
next(g)
print(g.gi_frame.f_lasti)
print(g.gi_frame.f_locals)
print(g.gi_running)
print("********************************")
next(g)
print(g.gi_frame.f_lasti)
print(g.gi_frame.f_locals)
print(g.gi_running)